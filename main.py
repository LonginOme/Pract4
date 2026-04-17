import re
import sys


# -------------------------------------------------------------------
# Вспомогательные функции (будут реализованы на следующих этапах)
# -------------------------------------------------------------------

def fix_name(raw: str) -> str:
    """Разделяет слитно написанное ИмяФамилия пробелом."""
    pass  # TODO


def fix_age(raw: str) -> str:
    """Оставляет только цифры, проверяет диапазон 0–130."""
    pass  # TODO


def fix_phone(raw: str) -> str:
    """Приводит телефон к формату +7 (XXX) XXX-XX-XX."""
    pass  # TODO


def fix_email(raw: str) -> str:
    """Убирает лишние @ и ., проверяет корректность email."""
    pass  # TODO


# -------------------------------------------------------------------
# Главная логика: чтение файла → обработка строк → запись результата
# -------------------------------------------------------------------

def process_file(input_path: str, output_path: str) -> None:
    with open(input_path, encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:

        for line in fin:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) != 4:
                continue  # некорректная строка — пропускаем

            name  = fix_name(parts[0])
            age   = fix_age(parts[1])
            phone = fix_phone(parts[2])
            email = fix_email(parts[3])

            result = f"{name}|{age}|{phone}|{email}"
            print(f"Вход:  {line}")
            print(f"Выход: {result}\n")
            fout.write(result + "\n")

    print(f"Готово! Результат записан в {output_path}")


# -------------------------------------------------------------------
# Точка входа
# -------------------------------------------------------------------

if __name__ == "__main__":
    input_file  = "input.txt"
    output_file = "output.txt"
    process_file(input_file, output_file)