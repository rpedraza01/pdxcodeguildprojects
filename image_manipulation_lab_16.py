#image_manipulation_lab_16.py
from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
	for j in range(height):
		r, g, b = pixels[i, j]


		pixels[i, j] = (r, g, b)

img.show()