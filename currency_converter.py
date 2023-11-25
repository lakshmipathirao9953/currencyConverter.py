import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(target_currency)
    else:
        return None

def convert_currency(amount, exchange_rate):
    if exchange_rate is not None:
        return amount * exchange_rate
    else:
        return None

def currency_converter():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'

    # Prompt user for input
    base_currency = input("Enter the source currency code: ").upper()
    target_currency = input("Enter the target currency code: ").upper()

    amount = input("Enter the amount to convert: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Fetch exchange rate
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

    # Perform currency conversion
    converted_amount = convert_currency(amount, exchange_rate)

    # Display the result
    if converted_amount is not None:
        print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        print(f"Exchange rate: 1 {base_currency} = {exchange_rate:.4f} {target_currency}")
    else:
        print("Unable to fetch exchange rate. Please check your input and try again.")

if __name__ == "__main__":
    currency_converter()
