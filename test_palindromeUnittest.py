import unittest
import palindrome

class SimpleTest(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(palindrome.palin("racecar"), True)

    def test_calculator0(self):
        self.assertEqual(palindrome.palin("Racecar"), True)
    
    def test_calculator1(self):
        self.assertEqual(palindrome.palin("something"), False)

    def test_calculator1(self):
        self.assertEqual(palindrome.palin(111), "Strings only")