from datetime import datetime
import sys


def print_date(z):
    try:
        x = datetime.strptime(z, '%m/%d/%Y').date()
    except Exception:
        x = 0

    try:
        y = datetime.strptime(z, '%B %d, %Y').date()
    except Exception:
        y = 0

    if x:
        print(x.strftime('%Y-%m-%d'))
        sys.exit(0)
    elif y:
        print(y.strftime('%Y-%m-%d'))
        sys.exit(0)
    else:
        pass


while True:
    z = input("Date: ")
    print_date(z)
