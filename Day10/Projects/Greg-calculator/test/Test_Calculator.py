import sys
sys.path.append('../Calculator')
import unittest
import Calculator

class TestCalculator(unittest.TestCase):
    def test_calculate_addition(self):
        result = Calculator.calculate(3.0, 5.2, 1)
        self.assertEqual(result, 8.2)
        self.assertIsInstance(result, float)
    
    def test_calculate_multiplication(self):
        result = Calculator.calculate(3.0, 5.0, 3)
        self.assertEqual(result, 15)
        self.assertIsInstance(result, int)

    def test_calculate_exponentiation(self):
        result = Calculator.calculate(2.0, 5.0, 5)
        self.assertEqual(result, 32)
        self.assertIsInstance(result, int)