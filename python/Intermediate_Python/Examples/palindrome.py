# Function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Unit Test using unittest
import unittest

class TestPalindrome(unittest.TestCase):
    
    def test_palindrome(self):
        # Test positive cases
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        
        # Test negative cases
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        
        # Test edge cases
        self.assertTrue(is_palindrome(""))  # Empty string
        self.assertTrue(is_palindrome("a"))  # Single character
        
if __name__ == '__main__':
    unittest.main()
