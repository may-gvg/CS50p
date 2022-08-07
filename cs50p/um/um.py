def main():
    print(count(input("Text: ")))


def count(s):
    lista = []
    lista2 = []
    for word in s.lower().split():
        lista.append(word)
        if word.startswith('um', 0):
            lista2.append(word)

    return len(lista2)


if __name__ == "__main__":
    main()
