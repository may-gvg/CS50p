name = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl"]

total = []

while True:
    try:
        x = input()
        total.append(x)

    except EOFError:
        if len(total) == 1 and total[0] == name[0]:
            for i in total:
                print("Adieu, adieu, to " + str(total[0]))
            break

        elif len(total) == 2 and total[1] == name[1]:
            print("Adieu, adieu, to " + str(total[0]) + " and " + str(total[1]))
            break

        elif len(total) == 3 and total[2] == name[2]:
            print("Adieu, adieu, to " + str(total[0]) + ", " + str(total[1]) + ", and " + str(total[2]))
            break

        elif len(total) == 4 and total[3] == name[3]:
            print("Adieu, adieu, to " + str(total[0]) + ", " + str(total[1]) + ", " + str(total[2]) + ", and " + str(
                total[3]))
            break

        elif len(total) == 5 and total[4] == name[4]:
            print("Adieu, adieu, to " + str(total[0]) + ", " + str(total[1]) + ", " + str(total[2]) + ", " + str(
                total[3]) + ", and " + str(total[4]))
            break

        elif len(total) == 6 and total[5] == name[5]:
            print("Adieu, adieu, to " + str(total[0]) + ", " + str(total[1]) + ", " + str(total[2]) + ", " + str(total[3])
                  + ", " + str(total[4]) + ", and " + str(total[5]))
            break

        elif len(total) == 7 and total[6] == name[6]:
            print("Adieu, adieu, to " + str(total[0]) + ", " + str(total[1]) + ", " + str(total[2]) + ", " + str(total[3])
                  + ", " + str(total[4]) + ", " + str(total[5]) + ", and " + str(total[6]))
            break

        else:
            break
