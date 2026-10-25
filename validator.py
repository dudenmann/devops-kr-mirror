def validate_email(email: str) -> bool:
    """Простая валидация email."""
    return "@" in email and "." in email.split("@")[-1]

def validate_phone(phone: str) -> bool:
    """Валидация российских номеров (v1.0)."""
    digits = "".join(c for c in phone if c.isdigit())
    return len(digits) == 11 and digits[0] in ("7", "8")

def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС (преподаватель)."""
    digits = "".join(c for c in snils if c.isdigit())
    return len(digits) == 11