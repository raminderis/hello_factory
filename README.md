# Simple Calculator Application

A simple Python application that takes two positive integers as input and displays their sum.

## Features

- Addition of two positive integers
- Input validation to ensure only positive integers are accepted
- User-friendly error messages
- Interactive command-line interface

## Requirements

- Python 3.6 or higher

## Project Structure

```
.
├── main.py          # Main entry point of the application
├── calculator.py    # Module containing arithmetic operations
├── utils.py         # Utility functions for input validation
└── README.md        # This file
```

## How to Run

1. Make sure you have Python 3.6+ installed on your system:
   ```bash
   python --version
   ```

2. Navigate to the project directory:
   ```bash
   cd /path/to/project
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Follow the prompts to enter two positive integers

## Usage Example

```
$ python main.py
Simple Calculator - Addition of Two Positive Integers
==================================================
Enter the first positive integer: 42
Enter the second positive integer: 58

Result: 42 + 58 = 100
```

## Input Validation

The application validates that:
- Both inputs are integers (not strings, floats, or other types)
- Both integers are positive (greater than 0)
- Invalid inputs will prompt the user to try again

## Module Documentation

### calculator.py

Contains the `add(a, b)` function that:
- Takes two positive integers as parameters
- Validates the inputs
- Returns their sum

### utils.py

Contains utility functions:
- `validate_positive_integer(value, name)`: Validates that a value is a positive integer
- `get_positive_integer_input(prompt)`: Gets validated positive integer input from the user

### main.py

The main entry point that:
- Prompts the user for two positive integers
- Calls the add function from calculator module
- Displays the result

## Error Handling

The application handles various error scenarios:
- Non-numeric input
- Negative numbers
- Zero
- Keyboard interrupts (Ctrl+C)

## License

This project is provided as-is for educational purposes.
