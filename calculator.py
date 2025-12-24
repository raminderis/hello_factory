"""Calculator module containing arithmetic operations."""

from utils import validate_positive_integer


def add(a, b):
    """Add two positive integers together.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: Sum of a and b
    
    Raises:
        ValueError: If either argument is not a positive integer
    """
    # Validate inputs
    validate_positive_integer(a, "First argument")
    validate_positive_integer(b, "Second argument")
    
    # Return sum
    return a + b
