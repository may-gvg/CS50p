import sys
import requests
import pandas as pd


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()


df = pd.json_normalize(o)
x = list(df['bpi.USD.rate_float'])
price = x[0]

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        elif len(sys.argv) == 2:
            n = sys.argv[1]
            amount = float(n) * price
            print(f"${amount:,.4f}")
            sys.exit()
        else:
            sys.exit()
    except ValueError:
        sys.exit("Command-line argument is not a number")
