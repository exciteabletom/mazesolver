import load_maze
from create_final_image import create_final_image
from pprint import pprint

input_path = input("Where is your maze image?  ")

maze = load_maze.main(input_path)


def get_cell_value(coords: tuple):
	"""

	:param coords: tuple containing x and y values
	:return: value of the cell at the specifed coordinates
	"""
	try:
		return maze[coords[0]][coords[1]]
	except IndexError:  # sometimes we get an IndexError when at the edge of the maze
		return False


def get_cell_neighbours(coords: tuple, mode="normal"):
	"""

	:param coords: Tuple containing the x and y values of the tuple we
					want to check the neighbours of
	:return: coordinates of all neighbours that have not been visited in
				a list of tuples. Example: [(x,y), (x,y), (x,y)]

	"""
	# different tuples that contain the coords of all positions
	# relative to our input tuple
	left = (coords[0] - 1, coords[1])
	right = (coords[0] + 1, coords[1])
	up = (coords[0], coords[1] - 1)
	down = (coords[0], coords[1] + 1)

	# list containing all directional tuples
	all_dirs = [left, right, up, down]
	visitable_coordinates = []

	if mode == "normal":
		for dir in all_dirs:
			cell_value = get_cell_value(dir)

			if cell_value == ".":  # if unvisited path
				visitable_coordinates.append(dir)

	elif mode == "backtrack":  # if we are backtracking
		for dir in all_dirs:
			cell_value = get_cell_value(dir)

			if type(cell_value) == int:  # if path has been visited
				visitable_coordinates.append(dir)

	return visitable_coordinates


def get_cells_by_value(value):
	"""
	Gets cells based on their value.
	:param value: The value to look for
	:return: list of all coordinates that match the specified value
	"""
	all_matching_cells = []  # the list containing all the coordinates of cells
	for row_index, row in enumerate(maze):
		for column_index, cell in enumerate(row):
			if cell == value:
				all_matching_cells.append((row_index, column_index))

	return all_matching_cells


def set_cell_value(coords: tuple, value: str or int):
	"""
	:param coords: The coordinates of the cell to be changed
	:param value: The value we want the cell to be set to
	"""
	maze[coords[0]][coords[1]] = value


def get_final_path():
	final_path = []
	reverse_final_path = []

	end = get_cells_by_value('e')
	if len(end) > 1:
		raise ValueError("More than one exit")

	end = end[0]

	current_cell = (end[0] - 1, end[1])

	dist_from_start = maze[end[0] - 1][end[1]]

	reverse_final_path.append(end)
	reverse_final_path.append(current_cell)
	while dist_from_start >= 0:
		neighbours = get_cell_neighbours(current_cell, mode="backtrack")
		for coords in neighbours:
			if maze[coords[0]][coords[1]] == dist_from_start - 1:
				current_cell = (coords[0], coords[1])
				reverse_final_path.append(coords)
				break

		dist_from_start = dist_from_start - 1

	return reverse_final_path


def main():
	start_pos = (None, None)  # variable that stores the entrance coords
	for index, value in enumerate(maze[0]):  # loop through first row
		if value == "s":  # since there is only one path in first row, this must be the entrance
			start_pos = (0, index)  # save the coordinates of the entrance
			maze[0][index] = 0  # mark the entrance as visited

	# main program loop
	# exits only when all cells have been searched
	start_dist = 0  # the distance from the entrance

	while True:
		open_coordinates = []  # a list containing all coordinates that can be travelled to

		if start_dist == 0:  # if we are at the entrance
			open_coordinates = get_cell_neighbours(start_pos)

		else:
			for cell in get_cells_by_value(start_dist):
				neighbours = get_cell_neighbours(cell)
				for neighbour in neighbours:
					open_coordinates.append(neighbour)

		if not open_coordinates:
			break

		for pos in open_coordinates:
			set_cell_value(pos, start_dist + 1)

		start_dist += 1
	final_path = get_final_path()
	create_final_image(final_path, input_path)


main()