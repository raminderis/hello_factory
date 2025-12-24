"""Module containing the function to calculate the difference between two integers."""


def calculate_difference(a, b):
    """Calculate the difference between two integers.
    
    Args:
        a (int): The first integer
        b (int): The second integer
    
    Returns:
        int: The difference (a - b)
    
    Raises:
        TypeError: If inputs are not integers or numeric types
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric types")
    
    return a - b
