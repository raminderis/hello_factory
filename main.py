#!/usr/bin/env python3
"""Main entry point for the calculator application."""

from calculator import subtract


def diff_numbers(a, b):
    """Calculate the difference between two numbers.
    
    Args:
        a: The first number (minuend)
        b: The second number (subtrahend)
    
    Returns:
        The difference (a - b)
    
    Raises:
        ValueError: If inputs are not valid numbers
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise ValueError("First argument must be a number")
    if not isinstance(b, (int, float)) or isinstance(b, bool) or b is None:
        raise ValueError("Second argument must be a number")
    if a is None:
        raise ValueError("First argument must be a number")
    
    return a - b


def main():
    """Main function to take two integers as input and calculate their difference."""
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        
        result = diff_numbers(num1, num2)
        
        print(f"{num1} - {num2} = {result}")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter valid integers.")
        else:
            raise
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()