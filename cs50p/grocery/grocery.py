from collections import Counter


def main():
    total = []
    while True:
        try:
            x = input().upper()
            total.append(x)
        except EOFError:
            total.sort()
            dicto = Counter(total)
            for key, val in dicto.items():
                print(val, key)
            break


main()