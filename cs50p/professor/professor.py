import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                pass
        except ValueError:
            pass


# numb
def generate_integer(level):
    score = 0
    times = 11
    cc = 0
    while times > 0:
        try:

            times -= 1
            if times == 0:
                break

            if cc == 3:
                task = x + y
                print(str(x) + " + " + str(y) + " = " + str(task))
                cc = 0

            if cc == 0 and level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)

            if cc == 0 and level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)

            if cc == 0 and level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)

            task = x + y
            y1 = str(x) + " + " + str(y) + " = "
            ans = int(input(y1))
            if ans == task:
                score += 1
                cc = 0
            else:
                cc += 1
                print("EEE")
                continue
        except ValueError:
            cc += 1
            print("EEE")
    print("Score: " + str(score))


if __name__ == "__main__":
    main()
