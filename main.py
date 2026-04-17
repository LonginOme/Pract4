import re
import sys


# -------------------------------------------------------------------
# Вспомогательные функции (будут реализованы на следующих этапах)
# -------------------------------------------------------------------

def fix_name(raw: str) -> str:
    """Разделяет слитно написанное ИмяФамилия пробелом."""
    if not raw or not raw.strip():
        return ""
    raw = raw.strip()
    # Если уже есть пробел и формат правильный — возвращаем как есть
    if re.match(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$', raw):
        return raw
    # Разделяем там, где строчная буква переходит в заглавную
    fixed = re.sub(r'([а-яё])([А-ЯЁ])', r'\1 \2', raw)
    # Проверяем что получилось "Слово Слово"
    if re.match(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$', fixed):
        return fixed
    return ""


def fix_age(raw: str) -> str:
    """Оставляет только цифры, проверяет диапазон 0–130."""
    if not raw or not raw.strip():
        return ""
    digits = re.sub(r'[^0-9]', '', raw.strip())
    if not digits:
        return ""
    age = int(digits)
    if 0 <= age <= 130:
        return str(age)
    return ""


def fix_phone(raw: str) -> str:
    """Приводит телефон к формату +7 (XXX) XXX-XX-XX."""
    if not raw or not raw.strip():
        return ""
    digits = re.sub(r'[^0-9]', '', raw.strip())
    # Убираем ведущую 7 или 8
    if digits.startswith('7') or digits.startswith('8'):
        digits = digits[1:]
    # После кода страны должно быть ровно 10 цифр
    if len(digits) != 10:
        return ""
    return f"+7 ({digits[0:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:10]}"


def fix_email(raw: str) -> str:
    """Убирает лишние @ и ., проверяет корректность email."""
    if not raw or not raw.strip():
        return ""
    
    raw = raw.strip()
    # Убираем дублирование знака @ (например, @@ -> @) [cite: 11, 37]
    raw = re.sub(r'@{2,}', '@', raw)
    # Убираем дублирование точек (например, .. -> .) [cite: 11, 37]
    raw = re.sub(r'\.{2,}', '.', raw)
    
    # Регулярное выражение для проверки структуры email 
    # Начинается с букв/цифр, содержит @, домен и зону (минимум 2 символа)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, raw):
        return raw
    return ""


# -------------------------------------------------------------------
# Главная логика: чтение файла → обработка строк → запись результата
# -------------------------------------------------------------------

def process_file(input_path: str, output_path: str) -> None:
    count = 0
    with open(input_path, encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 4:
                continue
            
            name  = fix_name(parts[0])
            age   = fix_age(parts[1])
            phone = fix_phone(parts[2])
            email = fix_email(parts[3])
            
            result = f"{name}|{age}|{phone}|{email}"
            fout.write(result + "\n")
            count += 1
            
            print(f"Вход:  {line}")
            print(f"Выход: {result}\n")
            
    print(f"Обработка завершена. Успешно сохранено строк: {count}")
    print(f"Результат записан в {output_path}")


# -------------------------------------------------------------------
# Точка входа
# -------------------------------------------------------------------

if __name__ == "__main__":
    input_file  = "input.txt"
    output_file = "output.txt"
    process_file(input_file, output_file)