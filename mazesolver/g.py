## g.py - Tommy Dougiamas
# This file contains global variables and helper functions used by multiple files in the project

# Matrix representing the maze image
# Set in __main__.py
# Used in solve.py
maze = []


def change_string_length(string, length):
	"""
	Append spaces to a string until it reaches 'length'
	"""
	diff = length - len(string)
	return string + (" " * diff)
