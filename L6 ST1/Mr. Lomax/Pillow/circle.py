from PIL import Image
from math import cos
from math import sin
from math import pi
import math

image = Image.new('HSV', (1920, 1080))

pixels = image.load()

radius = min(image.size) // 2 - 1
centerx, centery = image.size[0] // 2, image.size[1] // 2

# angle = 0
# while angle < 2 * pi:
#     pixels[centerx + radius * sin(angle), centery + radius * cos(angle)] = (255,255,255)
#     angle += 0.005




for y in range(image.size[1]):
    for x in range(image.size[0]):

        dist = math.sqrt((centerx - x)**2 + (centery - y)**2)

        if dist < radius:
            pixels[x, y] = (int(255 % (x + y)), 255, 255)

image.show()    