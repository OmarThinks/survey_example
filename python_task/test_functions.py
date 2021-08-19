import unittest
from app import count_words

"""
Here we test the function "count_words"
"""

"""
To run the tests
pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""

class count_words_TestCase(unittest.TestCase):
    def test_001_simple(self):
        text = "You are given a string of words"
        return_value = count_words(text)
        correct_return_value = [6,1, 31]
        self.assertEqual(return_value,correct_return_value)
        print("test_001: simple")
    
    def test_002_repeated_lower(self):
        text = "Please write some Some unit unit tests"
        return_value = count_words(text)
        correct_return_value = [4, 2, 38]
        self.assertEqual(return_value,correct_return_value)
        print("test_002: test_repeated_lower")

    def test_003_repeated_upper(self):
        text = "This This This is repeated upper"
        return_value = count_words(text)
        correct_return_value = [3, 1, 32]
        self.assertEqual(return_value,correct_return_value)
        print("test_003: test_repeated_upper")

    def test_004_repeated_upper_and_lower(self):
        text = "This this This this"
        return_value = count_words(text)
        correct_return_value = [1, 1, 19]
        self.assertEqual(return_value,correct_return_value)
        print("test_004: test_repeated_upper_and_lower")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()