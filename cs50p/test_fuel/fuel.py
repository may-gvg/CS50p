def main():
    x = input("Fraction: ")
    print(gauge(convert(x)))


def convert(fraction):
    calc = fraction.split("/")
    x = int(calc[0])
    y = int(calc[1])
    if y == 0:
        raise ZeroDivisionError

    elif x > y:
        raise ValueError
    else:
        z = eval(str(x / y))
        z = int(z * 100)
        return z


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return "{:.0%}".format(percentage / 100)


if __name__ == "__main__":
    main()
