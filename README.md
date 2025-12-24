# Positive Integer Addition Application

A simple Python application that takes two positive integers as input and adds them together.

## Features

- Takes two positive integer inputs from the user
- Validates that inputs are positive integers (greater than 0)
- Adds the two numbers together and displays the result
- Error handling for invalid inputs
- User-friendly prompts and output

## Requirements

- Python 3.6 or higher

## How to Run

1. Make sure you have Python 3 installed on your system:
   ```bash
   python3 --version
   ```

2. Navigate to the project directory:
   ```bash
   cd path/to/project
   ```

3. Run the application:
   ```bash
   python3 main.py
   ```

   Or make the file executable and run it directly:
   ```bash
   chmod +x main.py
   ./main.py
   ```

## Usage Example

```
=== Positive Integer Addition ===
This program adds two positive integers together.

Enter the first positive integer: 25
Enter the second positive integer: 17

Result: 25 + 17 = 42
```

## Input Validation

The application validates user input and will:
- Reject non-integer values
- Reject zero or negative numbers
- Continue prompting until valid positive integers are provided

## Code Structure

- `add_numbers(a, b)`: Function that adds two positive integers
- `get_positive_integer(prompt)`: Function that gets and validates user input
- `main()`: Main function that orchestrates the application flow

## Error Handling

The application handles the following error cases:
- Non-numeric input
- Zero or negative values
- Non-integer values

## License

This project is open source and available for educational purposes.
