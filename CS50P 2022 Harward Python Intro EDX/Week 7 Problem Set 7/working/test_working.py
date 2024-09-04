import pytest
from working import convert

def test_convert():
    """
    Tests the convert function for various valid 12-hour to 24-hour format conversions.
    """
    # Test case: No minutes specified
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    # Test case: With minutes specified
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

    # Test case: Crossing from PM to AM
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

    # Test case: With minutes specified, crossing from PM to AM
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error():
    """
    Tests the convert function to ensure it raises ValueError for invalid input formats.
    """
    # Test case: Invalid separator
    with pytest.raises(ValueError):
        convert("9AM - 5PM")

    # Test case: Invalid time format, already in 24-hour format
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

    # Test case: Invalid hour range (15:00 is valid but 25:00 is not)
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")

    # Test case: Invalid minutes range (60 is out of range)
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
