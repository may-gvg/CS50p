dicto = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0.0
    while True:
        try:
            x = input("Item: ").title()
            if dicto.get(x):
                number = dicto.get(x)
                total += number
                z = "${:,.2f}".format(total)
                print('Total :', str(z))

        except EOFError:
            break


main()
