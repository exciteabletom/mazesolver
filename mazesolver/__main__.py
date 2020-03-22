## __main__.py - Tommy Dougiamas
# This file interprets all command line arguments.
# It passes off the actual processing to other functions.

# Local imports
from . import load_maze
from . import solve
from . import create_final_image
from . import strings
from . import g  # globals

# Standard library imports
import sys
import os

# Check if we are running on windows
# If so we need to use different file path delimiters "\\" vs "/"
if os.name == "nt":  # If we are on windows
	g.is_windows = True
	g.file_delimiter = "\\"


def cmd_error(message=""):
	if message:
		print(f"ERROR: {message}\n")

	print("See --help for more info.")
	exit(1)


def cmd_info(mode):
	if mode == "help":
		print(strings.help_message)

	elif mode == "version":
		print(strings.version_long)

	elif mode == "maze_rules":
		print(strings.maze_rules)

	else:
		raise ValueError(f"DEV_ERROR: Option {mode} is not valid for cmd_info ")

	exit(0)


def main():
	input_path = ""  # Where the unsolved maze is
	output_dir = ""  # The directory for the picture to be outputted to

	cmd_args = sys.argv[1:]  # List storing all command line arguments passed to the program
	if len(cmd_args) == 0:  # if no arguments were given
		cmd_error("No arguments provided.")

	# Help command
	if "--help" in cmd_args or "-h" in cmd_args:
		cmd_info("help")

	elif "-v" in cmd_args or "--version" in cmd_args:
		cmd_info("version")

	elif "--maze-rules" in cmd_args:
		cmd_info("maze_rules")

	skip_next_arg = False  # Boolean indicating whether the current iteration should be skipped

	# Loop handling arguments that have params like "-i" and "-o"
	for index, arg in enumerate(cmd_args):
		if skip_next_arg:
			skip_next_arg = False
			continue
		try:
			if arg == "-i" or arg == "--input":
				input_path = cmd_args[index + 1]  # the argument after '-i' is the input path
				skip_next_arg = True  # We don't need to parse the next arg as it is a file-path

			elif arg == "-o" or arg == "--output":
				output_dir = cmd_args[index + 1]  # the argument after '-o' is the output path
				skip_next_arg = True  # We don't need to parse the next arg as it is a file-path

			else:
				cmd_error(f"Option {arg} not recognised.")

		except IndexError:  # If no parameter is passed to the argument
			cmd_error(f"Option {arg} requires an parameter.")

	if not os.path.exists(input_path):  # if dir doesn't exist
		cmd_error(f"Image {input_path} does not exist")

	if input_path:
		try:
			g.maze = load_maze.load(input_path)
		except FileNotFoundError:
			cmd_error(f"File {input_path} doesn't exist.")

	else:  # Make sure that an image path is defined
		cmd_error("No input path defined.")

	if not output_dir:
		output_dir_lst = input_path.split(g.file_delimiter)[0:-1]
		output_dir = g.file_delimiter.join(output_dir_lst)

		print(f"No output directory supplied. Using default directory: {output_dir}")
	
	if os.path.isdir(output_dir):
		cmd_error(f"Output directory {output_dir} doesn't exist or is not a directory")

	# maze_solution will be a list of cells representing the solution path
	maze_solution = []
	try:
		maze_solution = solve.solve()  # Try to solve the maze
	except IndexError or ValueError as e:  # Errors that occur when the maze image is not valid
		# print(e, e.message)  # Debugging calls
		cmd_error("Your maze was not valid! Make sure that it complies with the maze rules.")

	# call void function that outputs and image with the solution marked
	create_final_image.create(maze_solution, input_path, output_dir)

	exit(0)  # Success!
