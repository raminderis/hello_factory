#!/usr/bin/env python3
"""Main application file that takes two positive integers as input and adds them together."""


def add_numbers(a, b):
    """Add two positive integers together.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
        
    Returns:
        int: Sum of a and b
        
    Raises:
        ValueError: If inputs are not positive integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive integers")
    return a + b


def get_positive_integer(prompt):
    """Get a positive integer from user input.
    
    Args:
        prompt (str): Prompt message to display
        
    Returns:
        int: Valid positive integer from user
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer (greater than 0).")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main function to run the application."""
    print("=== Positive Integer Addition ===")
    print("This program adds two positive integers together.\n")
    
    # Get two positive integers from user
    num1 = get_positive_integer("Enter the first positive integer: ")
    num2 = get_positive_integer("Enter the second positive integer: ")
    
    # Calculate and display result
    result = add_numbers(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")


if __name__ == "__main__":
    main()
