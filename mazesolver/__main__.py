#!/usr/bin/env python3
# Production imports
from . import load_maze
from . import solve
from . import create_final_image
from . import strings
from . import g  # globals
## Environment Agnostic imports
import sys

def cmd_error(message=""):
	if message:
		print(message,"\n")

	print(strings.help_message)
	exit(1)

def cmd_info(mode):
	if mode == "help":
		print(strings.help_message)

	elif mode == "version":
		print(strings.version_long)
	
	exit(0)
	

def main():
	input_path = ""  # Where the unsolved maze is
	output_path = ""  # The directory for the picture to be outputted to
	cmd_args = []  # List storing all command line arguments

	# Command line argument interpreter
	cmd_args = sys.argv[1:]
	if len(cmd_args) == 0:  # if no arguments were given
		cmd_error("No arguments provided.")

	# Help command
	if "--help" in cmd_args or "-h" in cmd_args:
		cmd_info("help")
	
	elif "-v" in cmd_args or "--version" in cmd_args:
		cmd_info("version")


	skip_next_arg = False  # Boolean indicating whether the current interation should be skipped

	# Loop handling arguments that have params like "-i" and "-o"
	for index, arg in enumerate(cmd_args):
		if skip_next_arg == True:
			skip_next_arg = False
			continue
		try:
			if arg == "-i" or arg == "--input":
				input_path = cmd_args[index + 1]  # the argument after '-i' is the input path
				skip_next_arg = True  # We don't need to parse the next arg as it is a file-path

			elif arg == "-o" or arg == "--output":
				output_path = cmd_args[index + 1]  # the argument after '-o' is the output path
				skip_next_arg = True  # We don't need to parse the next arg as it is a file-path


			else:
				cmd_error(f"Option {arg} not recognised.")

		except IndexError:  # If no parameter is passed to the argument
			cmd_error(f"Option {arg} requires an parameter.")
	
	if input_path:
		g.maze = load_maze.load(input_path)

	else:
		cmd_error("No input path defined.")

	if not output_path:
		print("No output path defined. Using default directory.\n")

	# maze_solution will be a list of cells representing the solution path
	maze_solution = solve.solve()

	# call void function that outputs and image with the solution marked
	create_final_image.create(maze_solution, input_path, output_path)

	return 0
