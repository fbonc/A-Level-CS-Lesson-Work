from PIL import Image, ImageFilter, ImageOps

import tkinter
from tkinter import filedialog

def ascii_converter(image_path, base_width):

    grayscale = " .:-=+*#%@"

    image = Image.open(image_path).convert('L')

    wpercent = (base_width / float(image.size[0]))
    height = int((float(image.size[1]) * float(wpercent)) * 0.55)

    image = image.resize((base_width, height), Image.Resampling.LANCZOS)
    image = ImageOps.autocontrast(image)
    
    pixels = image.load()
    ascii_image = ""


    for y in range(image.size[1]):
        for x in range(image.size[0]):
            ascii_image += f"{grayscale[int(pixels[x,y] / (255/len(grayscale) + 1))]}"
        ascii_image += "\n"

    return ascii_image



if __name__ == "__main__":

    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename()

    base_width = int(input("Choose a base width: "))

    print(file_path)
    print(ascii_converter(file_path, base_width))



