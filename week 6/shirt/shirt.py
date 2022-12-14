from PIL import Image
from PIL import ImageOps
import sys


try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ####
    input_name, output_name = sys.argv[1], sys.argv[2]
    input_name = input_name.lower()
    output_name = output_name.lower()
    input_name_list = input_name.split(".")
    output_name_list = output_name.split(".")
    ####
    if (".") not in sys.argv[2] or (".") not in sys.argv[1]:
        sys.exit("Invalid input")
    ####
    if input_name_list[1] and output_name_list[1] in ["jpg", "jpeg", "png"]:
        if input_name_list[1] != output_name_list[1]:
            sys.exit("Input and output have different extensions")
        elif input_name_list[1] not in ["jpg", "jpeg", "png"]:
            sys.exit("Invalid input")
        elif output_name_list[1] not in ["jpg", "jpeg", "png"]:
            sys.exit("Ivalid output")
        else:
            first_image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            print(shirt.size)
            cfi = first_image.copy()
            ###
            cfi = ImageOps.fit(
                cfi, shirt.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
            )
            cfi.paste(shirt, shirt)
            ###
            cfi.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("Input does not exist")