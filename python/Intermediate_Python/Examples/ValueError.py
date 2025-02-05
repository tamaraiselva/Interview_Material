# Function to divide two numbers
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Unit Test using unittest
import unittest

class TestDivision(unittest.TestCase):
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
    
    def test_divide_by_zero(self):
        # Check for ValueError when dividing by zero
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
