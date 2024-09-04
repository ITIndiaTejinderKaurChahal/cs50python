import sys
import requests

def main():                                                                                    # Command-Line Argument Handling
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The number of Bitcoins must be a number.")

    try:                                                                                        # Fetching Bitcoin Price
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")            # Send GET request to CoinDesk API
        response.raise_for_status()                                                             # Raise an HTTPError for bad responses
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except (requests.RequestException, KeyError) as e:
        sys.exit(f"Error: Could not retrieve Bitcoin price. {e}")

    cost = bitcoins * bitcoin_price                                                             # Cost Calculation and Output
    print(f"The cost of {bitcoins:.4f} Bitcoins is ${cost:,.4f}")                               # Print USD cost with 1k separator & 4 decimal

if __name__ == "__main__":
    main()
