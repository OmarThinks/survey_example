import unittest
from app import (count_words, make_inverted,
	count_matched_numbers, check_subset)

"""
Here we test the function "count_words"
"""

"""
To run the tests
pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""

class _1_count_words_TestCase(unittest.TestCase):
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
		print("test_002: repeated_lower")

	def test_003_repeated_upper(self):
		text = "This This This is repeated upper"
		return_value = count_words(text)
		correct_return_value = [3, 1, 32]
		self.assertEqual(return_value,correct_return_value)
		print("test_003: repeated_upper")

	def test_004_repeated_upper_and_lower(self):
		text = "This this This this"
		return_value = count_words(text)
		correct_return_value = [1, 1, 19]
		self.assertEqual(return_value,correct_return_value)
		print("test_004: repeated_upper_and_lower")

	def test_005_numbers(self):
		text = "123 4 6 87 24"
		return_value = count_words(text)
		correct_return_value = [0, 0, 13]
		self.assertEqual(return_value,correct_return_value)
		print("test_005: numbers")

	def test_006_empty_string(self):
		text = ""
		return_value = count_words(text)
		correct_return_value = [0, 0, 0]
		self.assertEqual(return_value,correct_return_value)
		print("test_006: empty_string")

	def test_007_arabic_letters(self):
		text = "فيس بوك"
		return_value = count_words(text)
		correct_return_value = [0, 0, 7]
		self.assertEqual(return_value,correct_return_value)
		print("test_007: arabic_letters")

	def test_008_converted_to_string(self):
		text = 123 # passing an interger
		return_value = count_words(text)
		correct_return_value = [0, 0, 3]
		self.assertEqual(return_value,correct_return_value)
		print("test_008: converted_to_string")






class _2_make_inverted_TestCase(unittest.TestCase):
	def test_001_positive_odd(self):
		return_value_1 = make_inverted(2,7)
		return_value_2 = make_inverted(7,2)
		correct_return_value = [6, 5,4,3]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_001: positive_odd")
	
	def test_002_positive_even(self):
		return_value_1 = make_inverted(6,10)
		return_value_2 = make_inverted(10,6)
		correct_return_value = [10,9,8,7,6]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_002: positive_even")

	def test_003_negative_odd(self):
		return_value_1 = make_inverted(-2,-7)
		return_value_2 = make_inverted(-7,-2)
		correct_return_value = [-3,-4,-5,-6]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_003: negative_odd")
	
	def test_004_negative_even(self):
		return_value_1 = make_inverted(-6,-10)
		return_value_2 = make_inverted(-10,-6)
		correct_return_value = [-6,-7,-8,-9,-10]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_004: negative_even")

	def test_005_positive_negative_odd(self):
		return_value_1 = make_inverted(-3,2)
		return_value_2 = make_inverted(2,-3)
		correct_return_value = [1,0,-1,-2]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_005: positive_negative_odd")
	
	def test_006_positive_negative_even(self):
		return_value_1 = make_inverted(-3,3)
		return_value_2 = make_inverted(3,-3)
		correct_return_value = [3,2,1,0,-1,-2,-3]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_006: positive_negative_even")

	def test_007_equal_positive(self):
		return_value_1 = make_inverted(3,3)
		correct_return_value = []
		self.assertEqual(type(return_value_1), list)
		self.assertEqual(return_value_1, correct_return_value)
		print("test_007: equal_positive")

	def test_008_equal_zero(self):
		return_value_1 = make_inverted(0,0)
		correct_return_value = []
		self.assertEqual(type(return_value_1), list)
		self.assertEqual(return_value_1, correct_return_value)
		print("test_008: equal_zero")

	def test_009_equal_negative(self):
		return_value_1 = make_inverted(-5,-5)
		correct_return_value = []
		self.assertEqual(type(return_value_1), list)
		self.assertEqual(return_value_1, correct_return_value)
		print("test_009: equal_negative")

	def test_010_string_integer(self):
		return_value_1 = make_inverted("2","7")
		return_value_2 = make_inverted("7","2")
		correct_return_value = [6,5,4,3]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_010: string_integer")

	def test_011_string_float(self):
		return_value_1 = make_inverted("2.5","7.6")
		return_value_2 = make_inverted("7.9","2.99")
		correct_return_value = [6, 5,4,3]
		self.assertEqual(return_value_1, correct_return_value)
		self.assertEqual(return_value_2, correct_return_value)
		print("test_011: string_float")






class _3_count_matched_numbers_TestCase(unittest.TestCase):
	def test_001_exact_match(self):
		return_value = count_matched_numbers([1, 2, 3], [1, 2, 3])
		correct_return_value = 3
		self.assertEqual(return_value, correct_return_value)
		print("test_001: exact_match")

	def test_002_partial_match(self):
		return_value = count_matched_numbers([1, 2, 3], [1, 5, 3, 4, 5])
		correct_return_value = 2
		self.assertEqual(return_value, correct_return_value)
		print("test_002: partial_match")

	def test_003_no_match(self):
		return_value = count_matched_numbers([1, 2, 3], [4,5,6])
		correct_return_value = False
		self.assertEqual(return_value, correct_return_value)
		print("test_003: no_match")

	def test_004_first_is_empty(self):
		return_value = count_matched_numbers([], [4,5,6])
		correct_return_value = False
		self.assertEqual(return_value, correct_return_value)
		print("test_004: first_is_empty")

	def test_005_second_is_empty(self):
		return_value = count_matched_numbers([4,5,6],[])
		correct_return_value = False
		self.assertEqual(return_value, correct_return_value)
		print("test_005: second_is_empty")

	def test_006_both_empty(self):
		return_value = count_matched_numbers([],[])
		correct_return_value = False
		self.assertEqual(return_value, correct_return_value)
		print("test_006: both_empty")

	def test_007_first_not_list(self):
		try:
			count_matched_numbers(1,[])
			raise Exception("First is not list")
		except Exception as e:
			pass
		print("test_007: first_not_list")

	def test_008_second_not_list(self):
		try:
			count_matched_numbers([],1)
			raise Exception("Second is not list")
		except Exception as e:
			pass
		print("test_008: second_not_list")

	def test_009_casted_types(self):
		return_value = count_matched_numbers([1,2], ["1",2.3])
		correct_return_value = 2
		self.assertEqual(return_value, correct_return_value)
		print("test_009: casted_types")
















class _4_check_subset_TestCase(unittest.TestCase):
	def test_001_is_subset(self):
		return_value = check_subset([1,2,3,4,5],[1,2,3])
		correct_return_value = True
		self.assertEqual(return_value, correct_return_value)
		print("test_001: is_subset")

	def test_002_empty_list_two(self):
		return_value = check_subset([1,2,3,4,5],[])
		correct_return_value = False
		self.assertEqual(return_value, correct_return_value)
		print("test_002: empty_list_two")

	def test_003_mismatching_indeces(self):
		return_value = check_subset([1,2,3,4,5],[1,3,6])
		correct_return_value = [6]
		self.assertEqual(return_value, correct_return_value)
		print("test_003: mismatching_indeces")

	def test_004_mismatching(self):
		return_value = check_subset([1,2,3,4,5],[5,10])
		correct_return_value = [10]
		self.assertEqual(return_value, correct_return_value)
		print("test_004: mismatching")

	def test_005_repeated(self):
		return_value = check_subset([1],[1,1,1,1])
		correct_return_value = [1,1,1]
		self.assertEqual(return_value, correct_return_value)
		print("test_005: repeated")

	def test_006_repeated(self):
		return_value = check_subset([1,2,"3"],["1",2,3])
		correct_return_value = True
		self.assertEqual(return_value, correct_return_value)
		print("test_006: casted")

	def test_007_both_empty(self):
		return_value = check_subset([],[])
		correct_return_value = True
		self.assertEqual(return_value, correct_return_value)
		print("test_007: both_empty")

	def test_008_not_list(self):
		try:
			return_value = check_subset(1,[])
			raise Exception("This is not list")
		except Exception as e:
			pass
		print("test_008: not_list")










# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()