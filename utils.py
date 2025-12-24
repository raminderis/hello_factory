"""Utility functions for input validation and handling."""


def validate_positive_integer(value, name="Value"):
    """Validate that a value is a positive integer.
    
    Args:
        value: The value to validate
        name (str): Name of the value for error messages
    
    Raises:
        ValueError: If value is not a positive integer
        TypeError: If value is not an integer
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} must be an integer, got {type(value).__name__}")
    
    if value <= 0:
        raise ValueError(f"{name} must be a positive integer, got {value}")


def get_positive_integer_input(prompt):
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
            validate_positive_integer(value, "Input")
            return value
        except ValueError as e:
            if "invalid literal" in str(e):
                print(f"Error: Please enter a valid integer.")
            else:
                print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            exit(0)
