from unittest.mock import patch
import requests
from weather_api import get_current_forecast_by_citystate

def test_get_current_forecast_by_citystate_success():
    api_key = 'valid_api_key'
    city = 'Phoenix'
    state_code = 'AZ'
    units = 'imperial'

    expected_response = {'coord': {'lon': -112.0773, 'lat': 33.4486}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 37.88, 'feels_like': 39.57, 'temp_min': 36.26, 'temp_max': 39.38, 'pressure': 1009, 'humidity': 31, 'sea_level': 1009, 'grnd_level': 968}, 'visibility': 10000, 'wind': {'speed': 3.13, 'deg': 147, 'gust': 4.47}, 'clouds': {'all': 20}, 'dt': 1722020958, 'sys': {'type': 2, 'id': 2038866, 'country': 'US', 'sunrise': 1721997416, 'sunset': 1722047547}, 'timezone': -25200, 'id': 5308655, 'name': 'Phoenix', 'cod': 200}

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == expected_response


def test_get_current_forecast_by_citystate_success_no_city():
    api_key = 'valid_api_key'
    city = 'Phoenix'
    state_code = 'AZ'
    units = 'imperial'

    expected_response = {
        "cod": "404",
        "message": "city not found"
    }

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == 'city not found'

def test_get_current_forecast_by_citystate_success_unknown_error():
    api_key = 'valid_api_key'
    city = 'Phoenix'
    state_code = 'AZ'
    units = 'imperial'

    expected_response = {}

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == ''

def test_get_current_forecast_by_citystate_http_error():
    api_key = 'valid_api_key'
    city = 'Phoenix'
    state_code = 'AZ'
    units = 'imperial'

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == ''

def test_get_current_forecast_by_citystate_nonspecific_exception():
    api_key = "invalid_api_key"
    city = 'Pheonix'
    state_code = 'AZ'
    units = 'imperial'

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = Exception

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == ''

def test_get_current_forecast_by_citystate_success_misspell_city():
    api_key = 'valid_api_key'
    city = 'Pheonix'
    state_code = 'AZ'
    units = 'imperial'

    expected_response = []

    with patch('weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_current_forecast_by_citystate(city,state_code, units, api_key)
        assert response == ''