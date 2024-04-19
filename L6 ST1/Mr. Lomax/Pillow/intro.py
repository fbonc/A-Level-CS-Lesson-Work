from PIL import Image

image = Image.open("L6 ST1\Mr. Lomax\Pillow\landscape.png")
image_pixels = image.load()


red_version = Image.new('RGB', image.size)
red_pixels = red_version.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        red_pixels[x, y] = (image_pixels[x,y][0], 0, 0)



gray_version = Image.new('RGB', image.size)
gray_pixels = gray_version.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        av = (image_pixels[x,y][0] + image_pixels[x,y][1] + image_pixels[x,y][2])//3
        gray_pixels[x, y] = (av,av,av)



gray_version2 = Image.new('RGB', image.size)
gray_pixels2 = gray_version2.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        av = int(0.3*image_pixels[x,y][0]) + int(0.6*image_pixels[x,y][1]) + int(0.11*image_pixels[x,y][2])
        gray_pixels2[x, y] = (av,av,av)



reversed_version = Image.new('RGB', image.size)
reversed_pixels = reversed_version.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        reversed_pixels[x, y] = image_pixels[image.size[0]-1-x,y]


# image.show()
# red_version.show()
#gray_version.show()
gray_version2.show()
# reversed_version.show()

