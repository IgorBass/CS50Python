import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif len(sys.argv) > 1:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r_dict = r.json()
        bpi_dict = r_dict["bpi"]
        USD_dict = bpi_dict["USD"]
        rate = USD_dict.get("rate_float")
        total_price = rate * float(sys.argv[1])
        print(f"${total_price:,.4f}")
except requests.RequestException:
    sys.exit()
