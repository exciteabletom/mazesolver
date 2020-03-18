from PIL import Image


def main(solution_path, input_path):
	"""
	Void function that marks the solution path into the image with green and saves the image

	:param solution_path: list of coordinates to the cells in the solution
	:param input_path: User-supplied path to input maze image
	"""
	solution_image = Image.open(input_path)

	for i in solution_path:
		solution_image.putpixel((i[1], i[0]), (0,255,0))

	image_name = input_path.split("/")[-1]
	image_name = image_name.split(".")[0]

	solution_image.save(f"./pics/{image_name}_out.jpg", subsampling=0, quality=100)


