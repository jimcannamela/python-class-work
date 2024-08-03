# api is currently udergoing maintenance so I wasn't able to test

# def get_photo(api_key):
#     API_URL = 'https://api.nasa.gov/planetary/earth/imagery?lon=-108.845556&lat=50.594444&date=2014-02-01&api_key=ZXVyhZaKoL1MXBjH8GbypwE2Fsjpm4cJ3YT0CQxQ'
#     params = {
#         'api_key': key
#     }

#     #50°35'40"N 108°50'44"W

#     try:
#         response = requests.get(API_URL, params)
#         response.raise_for_status() # raise an HTTP error if the response code is not 200
#         apod_data = response.json()
#         return apod_data
#     except requests.exceptions.HTTPError as http_err:
#         return f'HTTP error occured: {http_err}'
#     except Exception as err:
#         return f'An error occurred: {err}'