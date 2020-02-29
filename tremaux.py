from pprint import pprint

from PIL import Image

maze: list = []

img_path = "pics/maze.jpg"
input_img = Image.open(img_path)
width, height = input_img.size

def populate_maze(empty_maze):
	pixels = input_img.load()

	for y in range(height):
		empty_maze.append([])
		for x in range(width):
			pixel_colors = pixels[x, y]
			pixel_colors = pixel_colors[0] + pixel_colors[1] + pixel_colors[2]
			if pixel_colors < 600:
				empty_maze[-1].append(1)

			elif pixel_colors >= 600:
				empty_maze[-1].append(0)

			else:
				raise ValueError("An error occured when determining the color of some pixels")

	for i in empty_maze:
		print(i)


populate_maze(maze)

markers: list = maze

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

last_direction = ""  # either r l u d

current_position = start


# -1 = visited once
# -2 = visited twice
def solve_maze(row: int, col: int):
	global counter
	global current_position
	global last_direction
	# Directional positions on actual maze
	left = maze[row][col - 1]
	right = maze[row][col + 1]
	down = maze[row + 1][col]
	up = maze[row - 1][col]
	# Directional positions on marker maze
	leftm = maze[row][col - 1]
	rightm = maze[row][col + 1]
	downm = maze[row + 1][col]
	upm = maze[row - 1][col]

	positions = {
		"left": [left, leftm, (row, col - 1)],
		"right": [right, rightm, (row, col + 1)],
		"down": [down, downm, (row + 1, col)],
		"up": [up, upm, (row + 1, col)]
	}

	for key in positions:
		curr = positions[key]
		if curr[0] == 0 and curr[1] > -2:
			print("here")
			current_position = curr[2]
			markers[curr[2][0]][curr[2][1]] += -1
			return False

	for key in positions:
		curr = positions[key]
		if curr[0] == 0 and curr[1] == -1:
			current_position = curr[2]
			markers[curr[2][0]][curr[2][1]] += -1

	if (row, col) == end:
		return True


counter = 0
while counter < 100:
	print(current_position)
	pprint(markers)
	if solve_maze(current_position[0], current_position[1]):
		break

	counter += 1

solution_image = input_img.copy()
counter = 0
for y in range(height):
	for x in range(width):
		if markers[x][y] < 0:
			solution_image.putpixel((y, x), (255, 0, 0))

solution_image.save("./pics/out.jpg", quality=100, subsampling=0)
