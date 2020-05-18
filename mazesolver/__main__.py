## __main__.py - Tommy Dougiamas
# This file interprets all command line arguments.
# It passes off the actual processing to other functions.

# Local imports
from . import load_maze  # Image --> matrix
from . import solve  # Matrix --> solution path
from . import create_final_image  # Image + solution path --> output image
from . import strings  # Static strings
from . import g  # global variables

# Stdlib imports
import sys
import os
from pathlib import Path  # Used to fix incompatibilities between windows and unix-based file paths "/" vs "\\"

def cmd_error(message=""):  # Display error message and exit the program with exit code 1
	if message:
		print(f"ERROR: {message}\n", file=sys.stderr)

	print("See --help for more info.", file=sys.stderr)
	exit(1)


def cmd_info(mode):  # Display information and exit the program with exit code 0
	if mode == "help":
		print(strings.help_message)

	elif mode == "version":
		print(strings.version)

	elif mode == "maze_rules":
		print(strings.maze_rules)

	else:
		raise ValueError(f"DEV_ERROR: Option '{mode}' is not valid for cmd_info ", file=sys.stderr)  # If the mode was not valid warn, so then it doesn't get into prod
		exit(1)

	exit(0)


def main():
	input_path = ""  # Where the unsolved maze is
	output_dir = ""  # The directory for the picture to be outputted to

	cmd_args = sys.argv[1:]  # List storing all command line arguments passed to the program
	if len(cmd_args) == 0:  # if no arguments were given
		cmd_error("No arguments provided.")

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
				cmd_error(f"Option '{arg}' not recognised.")

		except IndexError:  # If no parameter is passed to the argument
			cmd_error(f"Option '{arg}' requires an parameter.")

	if not input_path:  # Image paths are required
		cmd_error("No input path defined.")

	if os.path.isdir(input_path):  # If the image path is a directory
		cmd_error(f"Path '{input_path}' is a directory")

	if not os.path.isfile(input_path):  # if image doesn't exist or is not a file
		cmd_error(f"Image '{input_path}' does not exist")

	else:
		try:
			g.maze = load_maze.load(input_path)
		except IsADirectoryError:
			cmd_error(f"'{input_path}' is a directory, not an image")
		except FileNotFoundError:
			cmd_error(f"File '{input_path}' doesn't exist.")
		except ValueError:
			cmd_error("Something went wrong when loading the image.")


	if not output_dir:
		output_dir_lst = input_path.split(str(Path("/")))[0:-1]
		if output_dir_lst:
			output_dir = str(Path("/")).join(output_dir_lst)
		else:
			output_dir = str(Path("./"))  # ./ or .\\

		print(f"No output directory supplied. Using default directory: '{output_dir}'")
	
	if not os.path.isdir(output_dir):
		cmd_error(f"Output directory '{output_dir}' doesn't exist or is not a directory")

	# maze_solution will be a list of cells representing the solution path
	maze_solution = []
	try:
		maze_solution = solve.solve()  # Try to solve the maze
	except (IndexError, ValueError) as e:  # Errors that occur when the maze image is not valid
		# print(e, e.message)  # Debugging calls
		cmd_error("Your maze was not valid! Make sure that it complies with the maze rules.")

	# call void function that outputs and image with the solution marked
	create_final_image.create(maze_solution, input_path, output_dir)

	exit(0)  # Success!
