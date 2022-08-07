import sys

import pandas as pd

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) == 3:
            if sys.argv[1].split(".")[-1] == "csv":
                df = pd.read_csv(sys.argv[1])
                df[['last', 'first']] = df['name'].str.split(',', n=1, expand=True)
                df = df[["first", "last", "house"]]
                df['first'] = df['first'].str.strip()
                df['last'] = df['last'].str.strip()
                df['house'] = df['house'].str.strip()
                df.to_csv(sys.argv[2], index=False)
                sys.exit()
            else:
                sys.exit("Could not read invalid_file.csv")
        else:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
