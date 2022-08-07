import sys
from tabulate import tabulate
import csv

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 2:
            if sys.argv[1].split(".")[-1] == "csv":
                with open(sys.argv[1]) as file:
                    rows = []
                    reader =  csv.reader(file)
                    for row in reader:
                        rows.append(row)
                    print(tabulate(rows, tablefmt="grid", headers="firstrow"))
                    sys.exit()
            else:
                sys.exit("Not a csv file")
        else:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
