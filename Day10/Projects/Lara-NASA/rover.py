import requests

def get_by_date(date, api_key):
    API_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    payload = {
        'earth_date': date,
        'api_key': api_key
    }

    try:
        response = requests.get(API_URL, params=payload)
        response.raise_for_status() # raise an HTTP error if the response code is not 200
        return response.json()['photos'][0]['img_src']
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occured: {http_err}'
    except IndexError as err:
        return ''
    except Exception as err:
        return f'An error occurred: {err}'