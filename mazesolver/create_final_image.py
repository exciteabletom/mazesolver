## create_final_image.py - Tommy Dougiamas
# This file holds functions that convert a list of coordinates and an image
# into an image where those coords are marked in green

from PIL import Image  # Pillow >=6.0
from pathlib import Path  # OS agnostic filesystem paths
import progress.bar

from . import g  # globals


def create(solution_path, input_path, output_dir=None):
	"""
	Void function that marks the solution path into the image with green and saves the image

	:param solution_path: list of coordinates to the cells in the solution
	:param input_path: String with User-supplied path to input maze image
	:param output_dir: String with User-supplied path to a directory where the image will be saved
	"""
	solution_image = Image.open(input_path)  # open the image that was inputted
	progress_bar = progress.bar.PixelBar(g.change_string_length("Drawing solution path", 30), max=len(solution_path))
	for i in solution_path:  # for every pixel in the solution path
		progress_bar.next()
		solution_image.putpixel((i[1], i[0]), (0, 255, 0))  # change the pixel to solid green

	progress_bar.finish()

	full_image_name = input_path.split(str(Path("/")))[-1]  # eg path/to/maze.jpg --> maze.jpg
	image_name, image_ext = [i for i in full_image_name.split(".")]  # eg maze.jpg --> maze, .jpg

	out_path = Path(f"{output_dir}/{image_name}_out.{image_ext}")  # Where the image will be saved to

	solution_image.save(out_path, subsampling=0, quality=100)  # Save the image with no aliasing or down-sampling

	print(f"The solution to {input_path} was saved at {out_path}")  # Make sure the user knows where the image was saved

