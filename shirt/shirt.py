import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    input = sys.argv[1]
    output = sys.argv[2]
    shirt = Image.open("shirt.png")
    size = shirt.size

    splited_input = input.split(".")
    splited_output = output.split(".")

    if len(splited_input) != 2:
        if splited_input[1] != "jpg" or splited_input[1] != "png":
            sys.exit("Not a PNG/JPEG file")
    if splited_input[1] != splited_output[1]:
        sys.exit("Output extension is different than the input format")
    try:
        with Image.open(input) as im:
            im = ImageOps.fit(im, size, bleed=0.0, centering=(0.5, 0.5))
            im.paste(shirt, shirt)
            im.save(output)

    except FileNotFoundError:
        sys.exit("File not found")
