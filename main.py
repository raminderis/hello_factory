#!/usr/bin/env python3
"""Main entry point for the positive integer addition application."""


def add_numbers(a, b):
    """Add two positive integers.
    
    Args:
        a: First number (must be positive integer)
        b: Second number (must be positive integer)
    
    Returns:
        int: The sum of a and b
    
    Raises:
        ValueError: If inputs are not positive integers
    """
    # Check if inputs are valid integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    
    # Check if inputs are positive
    if a <= 0 or b <= 0:
        raise ValueError("Both arguments must be positive integers")
    
    return a + b


def get_positive_integer(prompt):
    """Get a positive integer from user input.
    
    Args:
        prompt (str): The prompt to display to the user
    
    Returns:
        int: A positive integer entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main function that takes two positive integers as input and displays their sum."""
    print("Positive Integer Addition")
    print("=" * 30)
    
    num1 = get_positive_integer("Enter the first positive integer: ")
    num2 = get_positive_integer("Enter the second positive integer: ")
    
    result = add_numbers(num1, num2)
    
    print(f"\n{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()
