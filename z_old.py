#! /usr/bin/env python3
from PIL import Image
from pprint import pprint


def maze_from_image():
	img = Image.open("./pics/maze2.jpg")
	pixels = img.load()

	width, height = img.size

	path_pixels: list = []
	wall_pixels: list = []

	path_found: bool = False
	maze: list = []
	for y in range(height):
		maze.append([])
		for x in range(width):
			pixel_colors = pixels[x, y]
			pixel_colors = pixel_colors[0] + pixel_colors[1] + pixel_colors[2]
			if pixel_colors < 600:
				maze[y].append(0)

			elif pixel_colors >= 600:
				maze[y].append(1)

			else:
				raise TypeError("Image contains pixels that are out of colour range")

