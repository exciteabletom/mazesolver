from PIL import Image
import os

def main(solution_path, input_path, output_path=None):
	"""
	Void function that marks the solution path into the image with green and saves the image

	:param solution_path: list of coordinates to the cells in the solution
	:param input_path: User-supplied path to input maze image
	:param output_path: User-supplied path to a directory where the image will be saved
	"""
	breakpoint()
	solution_image = Image.open(input_path)

	for i in solution_path:
		solution_image.putpixel((i[1], i[0]), (0,255,0))
	breakpoint()
	image_name = input_path.split("/")[-1]
	image_name = image_name.split(".")[0]
		
	out_path = f"{output_path}/{image_name}_out.jpg"

	solution_image.save(out_path, subsampling=0, quality=100)

	print("Your image was saved at out_path")


