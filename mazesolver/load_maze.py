## load_maze.py - Tommy Dougiamas
# This file holds functions that interpret an image as a matrix
from PIL import Image  # Pillow >=6.0


def load(input_path):
	"""
	Converts the input image into a matrix where:
	'#' == walls
	'.' == paths
	's' == start
	'e' == end

	:param input_path: A string containing a relative or absolute path to the image
	:return: A matrix representing the maze
	"""
	input_img = Image.open(input_path)  # open the image

	pixels = input_img.load()  # load the pixels from the image

	width, height = input_img.size  # get width and height of image

	maze: list = []  # this will contain our matrix

	for y in range(height):  # For each row
		maze.append([])  # append row
		for x in range(width):  # for each column
			current_pixel = pixels[x, y]  # get current pixel from coords
			pixel_color = current_pixel[0] + current_pixel[1] + current_pixel[2]  # get the sum of all RGB values

			# The way colours are matched is very broad. So you could use any two colours where one of
			# them exceeds an RGB sum of 600 and one of them doesn't.
			# E.g. Red for walls and white for paths. However this is not recommended

			if pixel_color < 600:  # if pixel is black
				maze[-1].append("#")  # append wall to most recent row

			elif pixel_color >= 600:  # if pixel is white
				maze[-1].append(".")  # append path to most recent row

	for index, cell in enumerate(maze[0]):
		if cell == ".":
			maze[0][index] = "s"  # The only path in the top row must be the start

	for index, cell in enumerate(maze[-1]):
		if cell == ".":
			maze[-1][index] = "e"  # The only path in the bottom row must be the exit

	return maze

