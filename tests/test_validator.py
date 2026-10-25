from validator import validate_phone

def test_phone_valid():
    assert validate_phone("+79001234567") is True
    assert validate_phone("89001234567") is True

def test_phone_invalid():
    assert validate_phone("123") is False
    assert validate_phone("abc") is False