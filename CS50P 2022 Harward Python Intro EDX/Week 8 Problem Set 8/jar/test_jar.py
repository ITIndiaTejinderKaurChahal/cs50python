import pytest
from jar import Jar


def test_init():
    """
    Test the initialization of the Jar class.
    """
    jar = Jar()
    # Test that a new jar is created with default capacity and size
    assert jar.capacity == 12  # Default capacity
    assert jar.size == 0  # New jar should be empty


def test_str():
    """
    Test the string representation of the Jar class.
    """
    jar = Jar()
    # Test that the string representation of an empty jar is an empty string
    assert str(jar) == ""

    # Deposit 1 cookie and test the string representation
    jar.deposit(1)
    assert str(jar) == "🍪"

    # Deposit 11 more cookies and test the string representation
    jar.deposit(11)
    # Should be 12 cookies total, represented by 12 '🍪' characters
    assert str(jar) == "🍪" * 12


def test_deposit():
    """
    Test the deposit method of the Jar class.
    """
    jar = Jar()

    # Deposit 1 cookie and verify the size
    jar.deposit(1)
    assert jar.size == 1

    # Try to deposit more cookies than the capacity allows
    # Expect a ValueError to be raised
    with pytest.raises(ValueError):
        jar.deposit(20)  # This should exceed the default capacity of 12


def test_withdraw():
    """
    Test the withdraw method of the Jar class.
    """
    jar = Jar()

    # Deposit 4 cookies
    jar.deposit(4)

    # Withdraw 1 cookie and verify the size
    jar.withdraw(1)
    assert jar.size == 3

    # Try to withdraw more cookies than present in the jar
    # Expect a ValueError to be raised
    with pytest.raises(ValueError):
        jar.withdraw(100)  # There are only 3 cookies, so this should raise an error
