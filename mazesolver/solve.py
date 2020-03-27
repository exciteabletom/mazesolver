## solve.py - Tommy Dougiamas
# This file contains all functions that interpret a maze matrix and provide a solution

from . import g  # global variables


def get_cell_value(coords: tuple):
	"""
	Gets the value of the cell at the specified coordinates

	:param coords: tuple containing x and y values
	:return: value of the cell at the specifed coordinates
	"""
	try:
		return g.maze[coords[0]][coords[1]]
	# Sometimes we get an IndexError if the maze doesn't have borders
	# This solution is not perfect however, so it is still best practice to use borders
	except IndexError:
		return False


def get_cell_neighbours(coords: tuple, mode="normal"):
	"""
	Gets the values of all cells that neighbour the cell at the specified coordinates

	:param coords: Tuple containing the x and y values of the cell to check the neighbours of
	:param mode: specifies whether we are doing our first pass or backtracking from
				 the exit. Is either "normal" (default) or "backtrack"
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
	Get cell coordinates based on the value of the cell.

	:param value: The value to search cells for
	:return: list of all coordinates that contain the specified value
	"""
	all_matching_cells = []  # the list containing all the coordinates of cells
	for row_index, row in enumerate(g.maze):
		for column_index, cell in enumerate(row):
			if cell == value:
				all_matching_cells.append((row_index, column_index))

	return all_matching_cells


def get_cell_by_value(value):
	"""
	The same as get_cells_by_value, except raises a ValueError if there is more than one cell with that value

	:param value: The value to search cells for
	:raises ValueError: If more then one of the value is found in the maze.
	:return: the cell coordinate that contains the value
	"""
	values = get_cells_by_value(value)
	if len(values) > 1:
		raise ValueError(f"Expected only one cell to have value '{value}'. {len(values)} cells contained the value.")

	return values[0]


def set_cell_value(coords: tuple, value: str or int):
	"""
	Sets the value of a cell at the specified coordinates.

	:param coords: The coordinates of the cell to be changed
	:param value: The value we want the cell to be set to
	"""
	g.maze[coords[0]][coords[1]] = value


def get_final_path(end_pos: tuple):
	"""
	Starts at the exit of the maze and works backwards to the entrance.

	:return: a list of all the cell coordinates that make up the path from the exit to the entrance
	"""
	reverse_final_path = []  # stores a path from the exit to the entrance

	current_cell = end_pos  # stores the cell we are currently at

	reverse_final_path.append(current_cell)

	dist_from_start = get_cell_value(end_pos)  # the distance from the entrance

	while dist_from_start >= 0:
		neighbours = get_cell_neighbours(current_cell, mode="backtrack")
		for coords in neighbours:
			if g.maze[coords[0]][coords[1]] == dist_from_start - 1:
				current_cell = (coords[0], coords[1])
				reverse_final_path.append(coords)
				break

		dist_from_start = dist_from_start - 1

	return reverse_final_path


def solve():
	"""
	Main entrypoint that solves the maze and outputs a list of cells representing a solution
	
	:return: A list of tuples (x, y) representing the cells in the solution path
	"""
	start_pos: tuple = get_cell_by_value("s")  # coords of entrance
	end_pos: tuple = get_cell_by_value("e")  # coords of exit of maze

	set_cell_value(start_pos, 0)  # mark the entrance as visited

	start_dist = 0  # the distance from the entrance

	# main program loop
	# exits when all cells have been searched
	while True:
		open_coordinates = []  # a list containing all coordinates that can be travelled to

		# for cells that contain a value equal to the furthest distance from the start
		for cell in get_cells_by_value(start_dist):
			neighbours = get_cell_neighbours(cell)  # get all open neighbouring cells
			for neighbour in neighbours:
				open_coordinates.append(neighbour)  # append all neighbours to our master open coords list

		if not open_coordinates:  # if there were no more open coordinates
			set_cell_value(end_pos, start_dist + 1)
			break  # then we must have parsed every cell in the maze

		for pos in open_coordinates:
			set_cell_value(pos, start_dist + 1)

		start_dist += 1

	final_path = get_final_path(end_pos)

	return final_path
