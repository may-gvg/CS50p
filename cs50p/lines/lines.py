import sys

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 2:
            if sys.argv[1].split(".")[-1] == "py":
                with open(sys.argv[1]) as file:
                    lines = file.readlines()
                    line_count = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
                    print(line_count)
                    sys.exit()
            else:
                sys.exit("Not a Python file")
        else:
            sys.exit("Too many command-line arguments")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except FileNotFoundError:
        sys.exit("File does not exist")
