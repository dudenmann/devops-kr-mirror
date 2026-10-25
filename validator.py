# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
def validate_phone(phone: str) -> bool:
    """Валидация российских номеров (v1.0)."""
    digits = "".join(c for c in phone if c.isdigit())
    return len(digits) == 11 and digits[0] in ("7", "8")