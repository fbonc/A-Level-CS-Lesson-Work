from PIL import Image, ImageDraw

image = Image.open(r"L6 ST1\Mr. Lomax\Pillow\landscape.png")
draw = ImageDraw.Draw(image)


radius = min(image.size) // 2 - 1
centerx, centery = image.size[0] // 2, image.size[1] // 2

draw.line([(0, 0), (100, 100)], width=10, fill=(100, 125, 100))

draw.ellipse([(100, 50), (150, 100)], fill=(100, 200, 50))

draw.regular_polygon((centerx, centery, radius), 4, rotation=0, fill=None, outline=None)


image.show()