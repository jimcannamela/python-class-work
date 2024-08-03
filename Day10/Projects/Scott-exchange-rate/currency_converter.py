import os
import requests
import pprint
from dotenv import load_dotenv
load_dotenv()
import json
#
currency_base_url = "https://api.freecurrencyapi.com/v1/latest"
api_key = os.getenv("FREECURRENCY_API_KEY")
#
params ={
    "apikey":api_key
}


def get_currency_data():
    currency_data = {} 
    try:
        response = requests.get(currency_base_url, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        currency_data = response.json()

        pprint.pprint(currency_data)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'An error occurred: {err}')
    return currency_data