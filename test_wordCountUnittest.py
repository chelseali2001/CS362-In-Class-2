import unittest
import wordCount

class SimpleTest(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(wordCount.count("Python"), 1)

    def test_calculator0(self):
        self.assertEqual(wordCount.count("a a a a "), 4)

    def test_calculator1(self):
        self.assertEqual(wordCount.count(111), "Strings only")