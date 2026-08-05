from app.book import Book, validate_isbn

def test_validate_isbn_valid_13digit():
    assert validate_isbn("978-3-16-148410-0") == True

def test_validate_isbn_valid_10digit():
    assert validate_isbn("1234567890") == True

def test_validate_isbn_valid_hyphens():
    assert validate_isbn("123-456-789-0123") == True

def test_validate_isbn_withspaces():
    assert validate_isbn("123 456 789 1243") == True

def test_invalidate_isbn_too_short():
    assert validate_isbn("123") == False

def test_invalidate_isbn_too_long():
    assert validate_isbn("12345678901234567890") == False

def test_invalidate_isbn_contains_characters():
    assert validate_isbn("123456789X") == False

def test_invalidate_isbn_nonstring():
    assert validate_isbn(1234567890) == False
