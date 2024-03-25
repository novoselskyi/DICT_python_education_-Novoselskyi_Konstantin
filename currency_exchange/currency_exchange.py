import requests

def get_exchange_rates(currency_code):
    response = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json")
    data = response.json()
    rates = {}
    for currency in data.values():
        rates[currency['code']] = currency['rate']
    return rates

def main():
    cache = {}
    while True:
        from_currency = input("Enter the currency code you have (or press Enter to exit): ").upper()
        if not from_currency:
            break
        if from_currency not in cache:
            print("Checking the cache...")
            cache[from_currency] = get_exchange_rates(from_currency)
        to_currency = input("Enter the currency code you want to exchange to: ").upper()
        amount = float(input("Enter the amount of money you want to exchange: "))
        if to_currency in cache[from_currency]:
            print("It is in the cache!")
            result = amount * cache[from_currency][to_currency]
        else:
            print("Sorry, but it is not in the cache!")
            rates = get_exchange_rates(from_currency)
            cache[from_currency] = rates
            result = amount * rates[to_currency]
        print(f"You received {result:.2f} {to_currency}.")

if __name__ == "__main__":
    main()
