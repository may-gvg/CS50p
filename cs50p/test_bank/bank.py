def main():
    x = input("Greeting: ").lower().replace(" ", "")
    if value(x) == 0:
        print("$0")
    elif value(x) == 20:
        print("$20")
    else:
        print("$100")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.lower().startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

