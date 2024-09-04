import pytest
from um import count

def test_input():
    """
    Test cases for the count function to ensure it correctly identifies
    occurrences of "um" as specified in the problem statement.
    """
    # Test case: "Um" at the beginning of the string, with a non-alphanumeric character following
    assert count("Um, thanks for the album.") == 1
    # Test case: Single occurrence of "um" with no surrounding characters
    assert count("um") == 1
    # Test case: "um" appears twice, with various punctuation in between
    assert count("Um, thanks, um...") == 2
    # Test case: "Um" at the end of the string, with a punctuation mark following
    assert count("Um?") == 1
