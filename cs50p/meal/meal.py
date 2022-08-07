from datetime import datetime


def main():
    time = input("What time is it? ")
    x = convert(time)
    if 7 <= x <= 8:
        print("breakfast time  ", end='')
    elif 12 <= x <= 13:
        print("lunch time  ", end='')
    elif 18 <= x <= 19:
        print("dinner time", end='')
    else:
        print("")


def convert(time):
    time = datetime.strptime(time, '%H:%M')
    x = time.hour + time.minute / 60.0
    return x


if __name__ == "__main__":
    main()