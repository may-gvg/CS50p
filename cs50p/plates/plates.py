def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    con1 = plate[:2].isalpha()
    con2 = len(plate) <= 6
    con3 = len(plate) >= 2
    con4 = plate[0] != "0"
    con5 = plate.isalnum()
    if any(char.isdigit() for char in plate):
        con6 = plate[-1].isdigit()
    else:
        con6 = True

    return con1 and con2 and con3 and con4 and con5 and con6



main()
