from PIL import Image
import numpy

image = Image.new('HSV', (1920, 1080))

pixels = image.load()




image.show()    