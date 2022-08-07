import random

while True:
    try:
        n = int(input("Level: "))
        num = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        check = int(input("Guess: "))
        if check > num:
            print("Too large!")
        elif check < num:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
