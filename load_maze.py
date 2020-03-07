from PIL import Image
from time import sleep


def main(input_path):
	def load_maze(input_path):
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

		for y in range(height):
			maze.append([])  # append row
			for x in range(width):
				current_pixel = pixels[x, y]  # get current pixel from coords
				pixel_color = current_pixel[0] + current_pixel[1] + current_pixel[2]  # get the sum of all RGB values

				if pixel_color < 600:  # if pixel is white
					maze[-1].append("#")  # append path to most recent row

				elif pixel_color >= 600:  # if pixel is black
					maze[-1].append(".")  # append wall to most recent row

				else:
					raise ValueError("An error occured when determining the color of some pixels")

		for index, cell in enumerate(maze[0]):
			if cell == ".":
				maze[0][index] = "s"

		for index, cell in enumerate(maze[-1]):
			if cell == ".":
				maze[-1][index] = "e"

		return maze

	try:
		maze = load_maze(input_path)

	except Exception as e:
		print(e)
		sleep(1)
		print("#####\n\nAn error occured, using default image instead!\n\n#####")

		maze = load_maze("./pics/maze.jpg")

	return maze
