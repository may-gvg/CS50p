def main():
    while True:
        try:
            calc = input("Fraction: ").split("/")
            x = int(calc[0])
            y = int(calc[1])
            z = eval(str(x / y))

            if round(z,2) == 0.25 or round(z,1) == 0.5 or round(z,2) == 0.75:
                print("{:.0%}".format(z))
                break
            elif round(z) == 0:
                print("E")
                break
            elif round(z) == 1:
                print("F")
                break
            else:
                pass
        except ZeroDivisionError:
            pass

        except ValueError:
            pass


main()
