from project import has_good_length, has_number, has_upper, has_special, check_password

def test_has_good_length():
    """Test the length check (must be >= 8)"""
    assert has_good_length("12345678") == True
    assert has_good_length("LongEnoughPassword") == True
    assert has_good_length("short") == False
    assert has_good_length("") == False


def test_has_number():
    """Test if digits are detected"""
    assert has_number("password123") == True
    assert has_number("123") == True
    assert has_number("password") == False
    assert has_number("!@#$") == False


def test_has_upper():
    """Test if uppercase letters are detected"""
    assert has_upper("Password") == True
    assert has_upper("PASSWORD") == True
    assert has_upper("password") == False
    assert has_upper("12345!") == False


def test_has_special():
    """Test if special characters are detected"""
    assert has_special("password!") == True
    assert has_special("#Secret") == True
    assert has_special("user@email") == True
    assert has_special("password123") == False
    assert has_special("HelloWorld") == False


def test_check_password():
    """Test the final score calculation and feedback logic"""

    # CASE 1: Perfect Password (Score: 4)
    # Length(ok), Number(ok), Upper(ok), Special(ok)
    score, feedback = check_password("StrongP@ss1")
    assert score == 4
    assert len(feedback) == 0  # No negative feedback for a perfect score

    # CASE 2: Weak Password (Score: 1)
    # Length(fail), Number(fail), Upper(ok), Special(fail)
    score, feedback = check_password("Weak")
    assert score == 1
    assert "Too short (needs 8+ characters)" in feedback
    assert "Missing a number" in feedback
    assert "Missing a special character (@, #, $, etc.)" in feedback

    # CASE 3: Medium Password (Score: 3)
    # Length(ok), Number(ok), Upper(ok), Special(fail)
    score, feedback = check_password("Password123")
    assert score == 3
    assert "Missing a special character (@, #, $, etc.)" in feedback
