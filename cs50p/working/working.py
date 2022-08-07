def main():
    print(convert(input("Hours: ")))


def convert(s):
    lista = []
    words = s.lower().split(" ")
    for word in words:
        lista.append(word)

    if len(lista) == 5 and lista[2] == "to":
        x = str(lista[0]).split(":")
        y = str(lista[3]).split(":")


        if len(lista[0]) == 1:
            if lista[1] == "pm":
                lista[0] = int(lista[0]) + 12
                lista[0] = str(lista[0]) + ":00"
            elif lista[1] == "am":
                lista[0] = "0" + str(lista[0]) + ":00"

        elif len(lista[0]) == 2:
            if lista[1] == "pm":
                if lista[0] == "12":
                    lista[0] = "12:00"
                else:
                    x[0] = int(x[0]) + 12
                    lista[0] = str(x[0]) + ":00"
            elif lista[1] == "am":
                if lista[0] == "12":
                    lista[0] = "00:00"
                else:
                    lista[0] = str(lista[0]) + ":00"

        elif len(lista[0]) == 4:
            if x[1] < "60":

                if lista[1] == "pm":
                    lista[0] = int(lista[0][0]) + 12
                    lista[0] = str(lista[0]) + ":" + str(x[1])
                elif lista[1] == "am":
                    lista[0] = "0" + str(lista[0])
            else: raise ValueError
            
        elif len(lista[0]) == 5:
            if x[1] < "60":
                if lista[1] == "pm":
                    if x[0] == "12":
                        lista[0] = "12:00"

                    else:
                        x[0] = int(x[0]) + 12
                        lista[0] = str(x[0]) + ":" + str(x[1])
                elif lista[1] == "am":
                    if x[0] == "12":
                        lista[0] = "00:00"
                    else:
                        lista[0] = str(lista[0])
            else: raise ValueError
        if len(lista[3]) == 1:
            if lista[4] == "pm":
                lista[3] = int(lista[3]) + 12
                lista[3] = str(lista[3]) + ":00"
            elif lista[4] == "am":
                lista[3] = "0" + str(lista[3]) + ":00"

        elif len(lista[3]) == 2:
            if lista[4] == "pm":
                if lista[3] == "12":
                    lista[3] = "12:00"
                else:
                    y[0] = int(y[0]) + 12
                    lista[3] = str(y[0]) + ":00"
            elif lista[4] == "am":
                if lista[3] == "12":
                    lista[3] = "00:00"
                else:
                    lista[3] = str(lista[3]) + ":00"

        elif len(lista[3]) == 4:
            if y[1] < "60":
                if lista[4] == "pm":
                    lista[3] = int(lista[3][0]) + 12
                    lista[3] = str(lista[3]) + ":" + str(y[1])
                elif lista[4] == "am":
                    lista[3] = "0" + str(lista[3])
            else: raise ValueError

        elif len(lista[3]) == 5:
            if y[1] < "60":
                if lista[4] == "pm":
                    if y[0] == "12":
                        lista[3] = "12:00"
                    else:
                        y[0] = int(y[0]) + 12
                        lista[3] = str(y[0]) + ":" + str(y[1])
                elif lista[4] == "am":
                    if y[0] == "12":
                        lista[3] = "00:00"
                    else:
                        lista[3] = str(lista[3])
            else: raise ValueError

        return str(lista[0] + " " + lista[2] + " " + lista[3])
    else:
        raise ValueError


if __name__ == "__main__":
    main()
