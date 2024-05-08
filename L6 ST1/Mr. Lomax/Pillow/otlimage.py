from PIL import Image

filename = 'L6 ST1\Mr. Lomax\Pillow\image.otl'



def load_image(filename):
    with open(filename, 'r') as file:
        text = file.read().split("\n")

        for i in range(len(text) - 1):
            text[i] = text[i].split(" ")

        width = int(text[0][0])
        height = int(text[0][1])

        image = Image.new('RGB', (width, height))
        pixels = image.load()

        del text[0]

        for y in range(height):
            for x in range(width):
                linenum = (x*height) + y
                r,g,b = [int(i) for i in text[linenum]]
                pixels[x,y] = (r, g, b)


    image.show()



def save_image(image, filename):

    pixels = image.load()
    width, height = image.size



    with open(filename, 'w') as file:

        file.write(f"{width} {height}\n")

        for y in range(height):
            for x in range(width):
                rgb = list(map(str, pixels[x,y]))

                file.write(f"{" ".join(rgb)}\n")
                

        
image = Image.open(r"L6 ST1\Mr. Lomax\Pillow\car.jpg")


save_image(image, "bruh.otl")





