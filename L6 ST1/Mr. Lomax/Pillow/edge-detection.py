
from PIL import Image
import numpy


## Open the images in grayscale mode (i.e.black and white)

# original_image = Image.open("landscape.png").convert('L')
# original_image = Image.open("Spongebob.png").convert('L')
original_image = Image.open(r"L6 ST1\Mr. Lomax\Pillow\car.jpg").convert('L')

print(original_image.format, original_image.size, original_image.mode)

# width, height = original_image.size
# modified_image = Image.new('L', original_image.size)
# edge_image = Image.new('L', original_image.size)


# pixels = original_image.load()          # The original image
# modified_pixels = modified_image.load() # Applying the "convolution"
# edge_pixels = edge_image.load()         # Just looking at edges

# for y in range(1, height - 1):
#     for x in range(1, width - 1):
#         # Find compare the pixels on left and right of the pixel we are looking at.
#         result_pixel = int(pixels[x - 1, y] * 0.25 + pixels[x + 1, y] * -0.25 + pixels[x, y - 1] * 0.25 + pixels[x, y + 1] * -0.25)

#         if abs(result_pixel) > 10:
#             edge_pixels[x,y] = 255
#         else:
#             edge_pixels[x,y] = 0

#         modified_pixels[x, y] = (result_pixel + 128)
        


horizontal_edge_kernal = [[-10, 0, 10], [-10,0,10], [-10,0,10]]
vertical_edge_kernal = [[-10, -10, -10], [0,0,0], [10,10,10]]
# gaussian_blur_kernal = [[1,2,1],[2,4,2],[1,2,1]]
gaussian_blur_kernal = [[1,2,3,2,1],[2,4,6,4,2],[3,6,9,6,3],[2,4,6,4,2],[1,2,3,2,1]]

def apply_kernal(image: Image, kernal):
    assert len(kernal) == len(kernal[0]), "Invalid kernal"
    image = image.convert('L')
    new_image = Image.new('L', image.size)
    width, height = image.size
    kernal_half_width = len(kernal) // 2
    input_pixels = image.load()
    new_pixels  = new_image.load()
    for pixel_y in range(kernal_half_width, height - kernal_half_width):
        for pixel_x in range(kernal_half_width, width - kernal_half_width):
            pixel_sum = 0
            for k_x in range(-kernal_half_width, kernal_half_width+1):
                for k_y in range(-kernal_half_width, kernal_half_width+1):
                    kernal_value = kernal[k_y + kernal_half_width][k_x + kernal_half_width]
                    pixel_value = input_pixels[pixel_x + k_x, pixel_y + k_y]
                    pixel_sum += kernal_value * pixel_value
            kernal_sum = sum([sum(s) for s in kernal])
            new_pixels[pixel_x, pixel_y] = pixel_sum // (kernal_sum+1)

    return new_image


apply_kernal(apply_kernal(original_image, gaussian_blur_kernal), vertical_edge_kernal)
# original_image.show()
# modified_image.show()
# edge_image.show()