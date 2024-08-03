import requests
from random import randint

def get_photo():
    API_URL = 'https://images-api.nasa.gov/search'
    payload = {
        'q': 'apollo'
    }

    try:
        response = requests.get(API_URL, params=payload)
        response.raise_for_status() # raise an HTTP error if the response code is not 200
        items_list = response.json()['collection']['items']
        item_idx = randint(0, len(items_list))
        return response.json()['collection']['items'][item_idx]['links'][0]['href']
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occured: {http_err}'
    except IndexError as err:
        return ''
    except Exception as err:
        return f'An error occurred: {err}'