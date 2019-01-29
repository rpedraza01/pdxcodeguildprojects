#image_manipulation_lab_16.py
from PIL import Image
img = Image.open("lenna.png")
# PIL opens the image
width, height = img.size
# width and height create a grid of the pixels
pixels = img.load()
# pixels loads the image and stores it as variable pixels

for i in range(width):
	for j in range(height):
		r, g, b = pixels[i, j]
		y = 0.299*r + 0.587*g + 0.114*b
		y = round(y)
		r, g, b = y, y, y

		pixels[i, j] = (r, g, b)

img.show()