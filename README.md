# Calculator Application

A simple Python application that calculates the difference between two integers.

## Features

- Takes two integers as input from the user
- Computes the difference (first number - second number)
- Includes error handling for invalid inputs
- Comprehensive unit tests

## Project Structure

```
.
├── main.py              # Main entry point
├── calculator.py        # Calculator module with subtract function
├── test_calculator.py   # Unit tests
└── README.md           # This file
```

## Installation

No external dependencies are required. This application uses only Python standard library.

## Usage

### Running the Application

```bash
python main.py
```

You will be prompted to enter two integers:

```
Enter the first integer: 10
Enter the second integer: 5
The difference between 10 and 5 is: 5
```

### Running Tests

To run the unit tests:

```bash
python test_calculator.py
```

Or using unittest discovery:

```bash
python -m unittest test_calculator.py
```

## Module Documentation

### calculator.py

#### `subtract(a, b)`

Computes the difference between two integers.

**Parameters:**
- `a` (int): The first integer (minuend)
- `b` (int): The second integer (subtrahend)

**Returns:**
- `int`: The difference (a - b)

**Example:**
```python
from calculator import subtract

result = subtract(10, 3)
print(result)  # Output: 7
```

## Requirements

- Python 3.6 or higher

## License

This project is provided as-is for educational purposes.