import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

elif len(sys.argv) == 2:
    sys.argv[1] = sys.argv[1].replace(",",".")
    if float(sys.argv[1]):
            rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            rate = rate["bpi"]["USD"]["rate"]
            rate = rate.replace(",","")
            qty = sys.argv[1]
            res = float(qty) * float(rate)
            print(f"${res:,.4f}")
    else:
            sys.exit("Command-line argument is not a number")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


