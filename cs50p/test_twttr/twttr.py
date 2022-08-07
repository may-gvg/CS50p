import re


def main():
    x = input("Input: ")
    print("Output: " + str(shorten(x)))


def shorten(word):
    return re.sub(r'[aeiouAEIOU]', '', word)


if __name__ == "__main__":
    main()
