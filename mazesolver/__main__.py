#!/usr/bin/env python3
# Production imports
from . import load_maze
from . import solve
from . import create_final_image
from . import strings
from . import g  # globals
## Environment Agnostic imports
import sys


def main():
	input_path = ""  # Where the unsolved maze is
	output_path = ""  # The directory for the picture to be outputted to
	cmd_args = []  # List storing all command line arguments

	# Command line argument interpreter
	cmd_args = sys.argv[1:]
	if len(cmd_args) == 0:  # if no arguments were given
		print("No arguments provided.")
		print(strings.help_message)
		return 1

	# Help command
	if "--help" in cmd_args or "-h" in cmd_args:
		print(strings.help_message)
		return 0
	
	elif "-v" in cmd_args or "--version" in cmd_args:
		print(strings.version_long)
		return 0 

	# Main solve commands
	skip_next_arg = False  # Boolean indicating whether the current interation should be skipped

	for index, arg in enumerate(cmd_args):
		breakpoint()
		if skip_next_arg == True:
			skip_next_arg = False
			continue

		if arg == "-i" or arg == "--input":
			input_path = cmd_args[index + 1]  # the argument after '-i' is the input path
			skip_next_arg = True  # We don't need to parse the next arg as it is a path

		elif arg == "-o" or arg == "--output":
			output_path = cmd_args[index + 1]  # the argument after '-o' is the output path
			skip_next_arg = True  # We don't need to parse the next arg as it is a path


		else:
			print(f"Option {arg} not recognised.\n")
			print(strings.help_message)
			return 1
	
	if input_path:
		g.maze = load_maze.load(input_path)
	else:
		print("No input path defined.")
		print(strings.help_message)
		exit(1)

	if not output_path:
		print("No output path defined. Using default directory.")

	# maze_solution will be a list of cells representing the solution path
	maze_solution = solve.solve()

	# call void function that outputs and image with the solution marked
	create_final_image.create(maze_solution, input_path, output_path)

	return 0
