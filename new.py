#!/usr/bin/env python3
from PIL import Image
img_path = "./pics/loops.jpg"
input_img = Image.open(img_path)
pixels = input_img.load()

width, height = input_img.size

maze: list = []

for y in range(height):
	maze.append([])
	for x in range(width):
		pixel_colors = pixels[x, y]
		pixel_colors = pixel_colors[0] + pixel_colors[1] + pixel_colors[2]
		if pixel_colors < 600:
			maze[-1].append(1)

		elif pixel_colors >= 600:
			maze[-1].append(0)

		else:
			raise ValueError("An error occured when determining the color of some pixels")

for i in maze:
	print(i)

solution = []
for row in maze:
	solution.append([])
	for i in row:
		solution[-1].append(0)

start = None
for i in range(len(maze[0])):
	if maze[0][i] == 0:
		start = (0, i)

end = None
for i in range(len(maze[-1])):
	if maze[-1][i] == 0:
		end = (len(maze) - 1, i)

print(end, start)

if not end or not start:
	raise ValueError("End or start of maze couldn't be defined")

length = len(maze)


def solve_maze(row: int, col: int):
	if (row, col) == end:
		solution[row][col] = 1
		return True

	if row >= 0 and row < length and col >= 0 and col < length and solution[row][col] == 0 and maze[row][col] == 0:
		solution[row][col] = 1  # set this tile to visited

		# RIGHT
		if solve_maze(row, col + 1):
			print("RIGHT")
			return True
		# LEFT
		if solve_maze(row, col - 1):
			print("LEFT")
			return True
		# DOWN
		if solve_maze(row + 1, col):
			print("DOWN")
			return True
		# UP
		if solve_maze(row - 1, col):
			print("UP")
			return True

		solution[row][col] = 0
		return False

	return 0


if solve_maze(start[0], start[1]):
	solution_image = input_img.copy()
	counter = 0
	for y in range(height):
		for x in range(width):
			counter += 1
			if solution[x][y] == 1:
				solution_image.putpixel((y, x), (255, 0, 0))

	solution_image.save("./pics/out.jpg", quality=100, subsampling=0)
	for i in solution:
		print(i)
else:
	print("There is no solution for this maze")

