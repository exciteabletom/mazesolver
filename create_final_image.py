from PIL import Image


def create_final_image(solution_path, input_path):
	solution_image = Image.open(input_path)
	width, height = solution_image.size

	for i in solution_path:
		solution_image.putpixel((i[1], i[0]), (255,0,0))

	solution_image.save("./pics/out.jpg", subsampling=0, quality=100)

