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

class CircleCITestCase(unittest.TestCase):
    def test_given_test_1(self):
        text = "You are given a string of words"
        return_value = count_words(text)
        correct_return_value = [6,1, 31]
        self.assertEqual(return_value,correct_return_value)
        print("test_001: testing CircleCI")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()