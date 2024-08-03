import requests
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv()

nasa_key = os.getenv("NASA_API_KEY")

NASA_EPIC_API_URL="https://api.nasa.gov/EPIC/api/natural/images"
NASA_EPIC_IMAGE_API_URL="https://api.nasa.gov/EPIC/archive/natural"
NASA_APOD_API_URL="https://api.nasa.gov/planetary/apod"

# print(f"{NASA_API_URL}?api_key={nasa_key_key}")

# my_request = requests.get(f"{NASA_API_URL}?api_key={nasa_key}")

# print(my_request.json())

#JOKE_API_URL="https://icanhazdadjoke.com/"

def get_response(api_key,api_url):

    params = {
        "api_key": api_key,
        "limit" : 1
    }

    try:
        response = requests.get(api_url, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        response = response.json()
        # print(response.url)
        return response
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

epic_data = get_response(nasa_key,NASA_EPIC_API_URL)
# print(epic_data)

if 'error' in epic_data:
    print("An error occurred accessing the NASA EPIC API")
else:
    print(f"Most recent Natural Color Image from NASA EPIC is:")
    img=epic_data[0].get('image')
    print(f"Name: {img}")
    imgdate=epic_data[0].get('date')
    print(f"    Date: {imgdate}")
    print(f"    Caption: {epic_data[0].get('caption')}")
    print(f"    Coordinates: {epic_data[0].get('centroid_coordinates')}")
    IMAGE_URL=f"{NASA_EPIC_IMAGE_API_URL}/{imgdate[:4]}/{imgdate[5:7]}/{imgdate[8:10]}/png/{img}.png"
    print(f"    Image URL: {IMAGE_URL}")
    webbrowser.open(f"{IMAGE_URL}?api_key={nasa_key}")

### End of Program ###