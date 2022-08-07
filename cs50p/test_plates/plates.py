def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    con1 = s[:2].isalpha()
    con2 = len(s) <= 6
    con3 = len(s) >= 2
    con4 = s[0] != "0"
    con5 = s.isalnum()
    if any(char.isdigit() for char in s):
        con6 = s[-1].isdigit()
    else:
        con6 = True

    return con1 and con2 and con3 and con4 and con5 and con6


if __name__ == "__main__":
    main()
