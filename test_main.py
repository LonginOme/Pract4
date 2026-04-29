import pytest
from main import fix_name, fix_age, fix_phone, fix_email


# ─── fix_name ────────────────────────────────────────────────────────────────

def test_fix_name_already_correct():
    assert fix_name("Иван Петров") == "Иван Петров"

def test_fix_name_merge_split():
    assert fix_name("ИванПетров") == "Иван Петров"

def test_fix_name_empty():
    assert fix_name("") == ""

def test_fix_name_whitespace_only():
    assert fix_name("   ") == ""

def test_fix_name_invalid_format():
    assert fix_name("ivan petrov") == ""

def test_fix_name_single_word():
    assert fix_name("Иван") == ""


# ─── fix_age ─────────────────────────────────────────────────────────────────

def test_fix_age_normal():
    assert fix_age("25") == "25"

def test_fix_age_with_noise():
    assert fix_age("25 лет") == "25"

def test_fix_age_zero():
    assert fix_age("0") == "0"

def test_fix_age_max():
    assert fix_age("130") == "130"

def test_fix_age_over_limit():
    assert fix_age("200") == ""

def test_fix_age_empty():
    assert fix_age("") == ""

def test_fix_age_no_digits():
    assert fix_age("abc") == ""


# ─── fix_phone ───────────────────────────────────────────────────────────────

def test_fix_phone_plus7():
    assert fix_phone("+79161234567") == "+7 (916) 123-45-67"

def test_fix_phone_8_prefix():
    assert fix_phone("89161234567") == "+7 (916) 123-45-67"

def test_fix_phone_formatted():
    assert fix_phone("+7 (916) 123-45-67") == "+7 (916) 123-45-67"

def test_fix_phone_too_short():
    assert fix_phone("12345") == ""

def test_fix_phone_empty():
    assert fix_phone("") == ""

def test_fix_phone_7_prefix():
    assert fix_phone("79161234567") == "+7 (916) 123-45-67"


# ─── fix_email ───────────────────────────────────────────────────────────────

def test_fix_email_valid():
    assert fix_email("user@example.com") == "user@example.com"

def test_fix_email_double_at():
    assert fix_email("user@@example.com") == "user@example.com"

def test_fix_email_double_dot():
    assert fix_email("user@example..com") == "user@example.com"

def test_fix_email_invalid_no_at():
    assert fix_email("userexample.com") == ""

def test_fix_email_invalid_no_domain():
    assert fix_email("user@") == ""

def test_fix_email_empty():
    assert fix_email("") == ""

def test_fix_email_whitespace():
    assert fix_email("  ") == ""
