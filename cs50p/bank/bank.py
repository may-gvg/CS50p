def main():
    x = input("Greeting: ")
    if value(x).startswith("hello"):
        print("$0")
    elif value(x).startswith("h") and not x.startswith("hello"):
        print("$20")
    else:
        print("$100")


def value(greeting):
    return greeting.lower().replace(" ", "")


if __name__ == "__main__":
    main()
