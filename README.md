# Integer Difference Calculator

A simple Python application that calculates the difference between two integers.

## Project Structure

- `main.py` - Main entry point that takes two integers as input and displays the difference
- `calculator.py` - Module containing the function to calculate the difference between two integers
- `test_calculator.py` - Unit tests for the calculator module
- `README.md` - Project documentation

## Requirements

- Python 3.6 or higher

## Usage

### Running the Application

To run the calculator application:

```bash
python main.py
```

You will be prompted to enter two integers, and the application will display their difference.

### Example

```
Integer Difference Calculator
==============================
Enter the first integer: 15
Enter the second integer: 7

The difference between 15 and 7 is: 8
```

### Using the Calculator Module

You can also import and use the `calculate_difference` function directly:

```python
from calculator import calculate_difference

result = calculate_difference(10, 5)
print(result)  # Output: 5
```

## Running Tests

To run the unit tests:

```bash
python test_calculator.py
```

Or using unittest discovery:

```bash
python -m unittest test_calculator.py
```

For verbose output:

```bash
python -m unittest test_calculator.py -v
```

## Features

- Calculate the difference between two integers
- Input validation and error handling
- Comprehensive unit tests
- Support for positive, negative, and zero values
- Support for floating-point numbers

## Function Documentation

### `calculate_difference(a, b)`

Calculates the difference between two numbers (a - b).

**Parameters:**
- `a` (int/float): The first number
- `b` (int/float): The second number

**Returns:**
- (int/float): The difference between a and b

**Raises:**
- `TypeError`: If inputs are not numeric types

## License

This project is open source and available for educational purposes.
