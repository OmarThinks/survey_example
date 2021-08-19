# Please note that you can solve these problems using any programming language but Python is preferred.

def count_words(words):
	"""You are given a string words.
	Count the number of unique words that starts with lower letter.
	Count the number of unique words that starts with Upper letter.
	And return a list contains the two counts and the length of the string words.

	If two words are same, count them as one.
	If two words are different, count them as two.
	Example:

	count_words("You are given a string of words") == [6,1, 31]
	count_words("Please write some Some unit unit tests") == [4, 2, 38]
	"""
	words = str(words)
	splitted_words = words.split()
	print(splitted_words)
	
	number_of_words = len(words) # The Third Requirement

	lower_letters_words = []
	upper_letters_words = []

	lower_letters_counter = 0 # The first Requirement
	upper_letters_counter = 0 # The second Requirement

	for word in splitted_words:
		first_letter = word[0]
		if first_letter.isupper():
			if word in upper_letters_words:
				continue
			upper_letters_counter += 1
			upper_letters_words.append(word)
		elif first_letter.islower():
			if word in lower_letters_words:
				continue
			lower_letters_counter += 1
			lower_letters_words.append(word)
	final_answer = [lower_letters_counter, 
	upper_letters_counter, number_of_words]
	print(final_answer)
	return final_answer



#----------------------------------------------------------------------------------------------------------#

def make_inverted(m, n):
	"""
	Given two integers m and n, write a function that returns a reversed list of integers between m and n.
	If the difference between m and n is even, include m and n, otherwise don't include.

	If m == n, return empty list
	If m < n, swap between m and n and continue.

	Example 1:

		Input: m = 2, n = 7
		Output: [6, 5,4,3]

	Example 2:
		Input: m = 6, n = 10
		Output: [10,9,8,7,6]
	"""
	if m == n:
		pass
		


#----------------------------------------------------------------------------------------------------------#

def count_matched_numbers(a, b):
	"""
	Write a function that takes two lists as parameters and returns a list
	containing the number of elements that occur in the same index in both
	lists. If there is not common elements in the same indices in both lists, return False
	Example:
	>>> count_matched_numbers([1, 2, 3], [1, 2, 3])
	3
	>>> count_matched_numbers([1, 2, 3], [1, 5, 3, 4, 5])
	2
	>>> count_matched_numbers([1, 2, 3], [4,5,6])
	False
	"""

#----------------------------------------------------------------------------------------------------------#

def check_subset(list_one, list_two):
	"""
	You are given two lists of integers list_one and list_two.  If list_two is a subset of list_one, return
	true, otherwise return list of items that are in list_two but NOT in list_one.

	Note: subset can be empty, if so return False

	Example 1:

		Input: list_one = [1,2,3,4,5], list_two = [1,2,3]
		Output: True

	Example 2:

		Input: list_one = [1,2,3,4,5], list_two = []
		Output: False

	Example 3:

		Input: list_one = [1,2,3,4,5], list_two = [1,3,6]
		Output: [6]

	Example 4:

		Input: list_one = [1,2,3,4,5], list_two = [5,10]
		Output: [10]
	"""

#----------------------------------------------------------------------------------------------------------#
