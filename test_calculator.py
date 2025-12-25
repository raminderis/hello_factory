"""Unit tests for the calculator module."""

import unittest
from calculator import subtract


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(100, 50), 50)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, -20), 10)
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction of positive and negative numbers."""
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-10, 5), -15)
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)
    
    def test_subtract_same_numbers(self):
        """Test subtraction of identical numbers."""
        self.assertEqual(subtract(7, 7), 0)
        self.assertEqual(subtract(-5, -5), 0)


if __name__ == "__main__":
    unittest.main()