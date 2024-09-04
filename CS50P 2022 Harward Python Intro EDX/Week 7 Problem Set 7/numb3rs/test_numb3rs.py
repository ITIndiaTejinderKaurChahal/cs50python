from numb3rs import validate

def test_validate():
    """
    Tests the validate function from the numb3rs module to ensure it correctly
    validates IPv4 addresses.
    """
    # Test with a valid IPv4 address
    assert validate("127.0.0.1") == True  # Loopback address
    assert validate("255.255.255.255") == True  # Maximum value for each octet

    # Test with invalid IPv4 addresses
    assert validate("512.512.512.512") == False  # Octets exceed maximum value of 255
    assert validate("1.2.3.1000") == False  # Last octet exceeds maximum value of 255
    assert validate("cat") == False  # Not an IPv4 address

    # Test with other valid IPv4 addresses
    assert validate("1.2.3.4") == True  # Standard valid address
    assert validate("11.99.22.88") == True  # Another valid address

    # Test with more invalid IPv4 addresses
    assert validate("199.911.288.882") == False  # Octets exceed maximum value of 255
    assert validate("249.249.249.249") == True  # Valid address

