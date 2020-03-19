from PIL import Image  # Pillow >=6.0
from pathlib import Path  # Needed to find user's home dir


def create(solution_path, input_path, output_path=None):
	"""
	Void function that marks the solution path into the image with green and saves the image

	:param solution_path: list of coordinates to the cells in the solution
	:param input_path: String with User-supplied path to input maze image
	:param output_path: String with User-supplied path to a directory where the image will be saved
	"""
	if not output_path:
		# OS agnostic home path
		# On *nix systems, will be ~/Pictures
		# On Windows will be /Users/{user}/Pictures
		output_path = str(Path.home()) + "/Pictures"

	solution_image = Image.open(input_path)  # open the image that was inputted

	for i in solution_path:  # for every pixel in the solution path
		solution_image.putpixel((i[1], i[0]), (0, 255, 0))  # change the pixel to solid green

	full_image_name = input_path.split("/")[-1]  # eg "path/to/maze.jpg --> maze.jpg
	image_name = full_image_name.split(".")[0]  # eg maze.jpg --> maze
		
	out_path = f"{output_path}/{image_name}_out.jpg"  # Where the image will be saved to

	solution_image.save(out_path, subsampling=0, quality=100)  # No aliasing or down-sampling

	print(f"The solution to {input_path} was saved at {out_path}")  # Make sure the user knows where the image was saved

