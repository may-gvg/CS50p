import sys
from datetime import date, datetime

import inflect

p = inflect.engine()


def main():
    print(birth(input("Date of Birth: ")))


def birth(s):
    try:
        today = date.today()
        s = datetime.strptime(s, "%Y-%m-%d").date()
        diff = today - s
        diff_minutes = diff.total_seconds() / 60
        words = p.number_to_words(round(diff_minutes)).capitalize().replace(" and ", " ")

        return words + " minutes"
    except ValueError:
        sys.exit("error")


if __name__ == "__main__":
    main()