"""Unit tests for the calculator module."""

import unittest
from calculator import calculate_difference


class TestCalculator(unittest.TestCase):
    """Test cases for the calculate_difference function."""
    
    def test_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(calculate_difference(10, 5), 5)
        self.assertEqual(calculate_difference(100, 50), 50)
    
    def test_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(calculate_difference(-10, -5), -5)
        self.assertEqual(calculate_difference(-5, -10), 5)
    
    def test_mixed_signs(self):
        """Test subtraction with mixed positive and negative numbers."""
        self.assertEqual(calculate_difference(10, -5), 15)
        self.assertEqual(calculate_difference(-10, 5), -15)
    
    def test_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(calculate_difference(0, 0), 0)
        self.assertEqual(calculate_difference(10, 0), 10)
        self.assertEqual(calculate_difference(0, 10), -10)
    
    def test_same_numbers(self):
        """Test subtraction of identical numbers."""
        self.assertEqual(calculate_difference(5, 5), 0)
        self.assertEqual(calculate_difference(-5, -5), 0)
    
    def test_large_numbers(self):
        """Test subtraction with large numbers."""
        self.assertEqual(calculate_difference(1000000, 500000), 500000)
        self.assertEqual(calculate_difference(-1000000, -500000), -500000)
    
    def test_float_numbers(self):
        """Test subtraction with float numbers."""
        self.assertAlmostEqual(calculate_difference(10.5, 5.2), 5.3, places=1)
        self.assertAlmostEqual(calculate_difference(3.7, 1.2), 2.5, places=1)
    
    def test_invalid_input(self):
        """Test that invalid inputs raise TypeError."""
        with self.assertRaises(TypeError):
            calculate_difference("10", 5)
        with self.assertRaises(TypeError):
            calculate_difference(10, "5")
        with self.assertRaises(TypeError):
            calculate_difference(None, 5)


if __name__ == "__main__":
    unittest.main()
