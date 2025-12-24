#!/usr/bin/env python3
"""Main entry point for the calculator application."""

import builtins


def add_numbers(a, b):
    """Add two positive integers together.
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        int: Sum of a and b
    
    Raises:
        ValueError: If either argument is not a positive integer or invalid type
    """
    # Validate types and values
    if not isinstance(a, int) or isinstance(a, bool):
        raise ValueError(f"First argument must be a positive integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise ValueError(f"Second argument must be a positive integer")
    
    if a <= 0:
        raise ValueError(f"First argument must be a positive integer")
    if b <= 0:
        raise ValueError(f"Second argument must be a positive integer")
    
    return a + b


def get_positive_integer(prompt):
    """Get a positive integer from user input with validation.
    
    Args:
        prompt (str): The prompt message to display to the user
    
    Returns:
        int: A valid positive integer from user input
    """
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            
            if value <= 0:
                print("Error: Please enter a positive integer.")
                continue
            
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            exit(0)


def main():
    """Main function that takes two positive integers as input and displays their sum."""
    print("Positive Integer Addition")
    print("=" * 50)
    
    # Get first positive integer
    num1 = get_positive_integer("Enter the first positive integer: ")
    
    # Get second positive integer
    num2 = get_positive_integer("Enter the second positive integer: ")
    
    # Calculate sum
    result = add_numbers(num1, num2)
    
    # Display result
    print(f"\n{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()
