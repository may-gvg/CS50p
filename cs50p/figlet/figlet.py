import sys

from pyfiglet import Figlet

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        x = input()
        print(figlet.renderText(x))
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        x = input()
        print(figlet.renderText(x))
    else:
        sys.exit("Invalid usage")


main()