import sys

from PIL import Image

logo = "shirt.png"

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 3:
            if sys.argv[1].split(".")[-1].lower() == sys.argv[2].split(".")[-1].lower():
                if sys.argv[1].split(".")[-1].lower() == "jpg" or sys.argv[1].split(".")[-1].lower() == "png" or \
                        sys.argv[1].split(".")[-1].lower() == "jpeg":
                    with Image.open(logo) as img_logo:
                        img_logo.load()
                    with Image.open(sys.argv[1].lower()) as koszula:
                        koszula.load()
                        new = koszula.resize((600, 800))
                        new = new.crop((0, 100, 600, 700))
                        new.paste(img_logo, (0, 0), img_logo)
                        new.save(sys.argv[2])
                        sys.exit()
            else:
                sys.exit("Could not read invalid_file.csv")
        else:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("Input does not exist")
