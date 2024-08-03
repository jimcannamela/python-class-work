import requests

def get_current_forecast_by_citystate(city, state_code, units, key):
    API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    payload = {
        'q': f'{city},{state_code},USA',
        'appid': key,
        'units': units
    }

    try:
        response = requests.get(API_URL, params=payload)
        response.raise_for_status() # raise an HTTP error if the response code is not 200
        if response.json().get('cod') == '404':
            return response.json().get('message')
        if not response.json():
            return ''
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return ''
    except Exception as err:
        return ''