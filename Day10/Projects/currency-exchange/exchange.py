# sample api call
# https://v6.exchangerate-api.com/v6/3e8c81daf4949bb95068e585/latest/USD

import requests
import os
import webbrowser
from dotenv import load_dotenv

# API variables
load_dotenv()

api_key = os.getenv("MY_API_KEY")

EXCHANGE_API_URL="https://v6.exchangerate-api.com/v6/"

# print(f"{EXCHANGE_API_URL}{api_key}/latest/USD")

# READ IN COUNTRY.DAT AND CREATE A LIST OF DICTIONARIES CONTAINING EXCHANGE COUNTRIES

# country_list=open("country.dat",'r').read()

import ast
with open("country.dat", 'r') as f:
        country_list = ast.literal_eval(f.read())

# print(type(country_list))

# print(country_list)

def validate_country(country):
    for x in range(len(country_list)):
        if country_list[x].get('country') == from_country:
            # print(country_list[x])
            return country_list[x]
        else:
            return 'XXX'


# ASK USER FOR AMOUNT TO CONVERT

#     VALIDATE THAT A NUMERIC AMOUNT WAS ENTERED

# ASK USE FOR COUNTRY CONVERTING FROM 

# from_country=input(;ksmfslkfskm)

from_country='Guinea'

while True:
    if validate_country(from_country) == 'XXX':
        print("I'm sorry the country you entered is not in the list of available exchange rates.")
        print("Please try a different country name.")
    else:
         pass
        
         



#     VALIDATE COUNTRY ENTERED AGAINST LIST

# ASK USER FOR COUNTRY CONVERTING TO 

#     VALIDATE COUNTRY ENTERED AGAINST LIST

# FORMAT URL 

# REQUEST DATA FROM API 

# SELECT CORRECT EXCHANGE RATE FROM DATA RETURNED

# CACLULATE NEW AMOUNT

# DISPLAY AMOUNT TO USER


# my_request = requests.get(f"{EXCHANGE_API_URL}{api_key}/latest/USD")

# print(my_request.json())

# def get_response(api_key,api_url):

#     params = {
#         "api_key": api_key,
#         "limit" : 1
#     }

#     try:
#         response = requests.get(api_url, params=params)
#         # raise an HTTP error if the response code is not 200
#         response.raise_for_status()
#         response = response.json()
#         # print(response.url)
#         return response
#     except requests.exceptions.HTTPError as http_err:
#         return f"HTTP error occurred: {http_err}"

#     except Exception as err:
#         return f"An error occurred: {err}"

# epic_data = get_response(nasa_key,NASA_EPIC_API_URL)
# # print(epic_data)

# if 'error' in epic_data:
#     print("An error occurred accessing the NASA EPIC API")
# else:
#     print(f"Most recent Natural Color Image from NASA EPIC is:")
#     img=epic_data[0].get('image')
#     print(f"Name: {img}")
#     imgdate=epic_data[0].get('date')
#     print(f"    Date: {imgdate}")
#     print(f"    Caption: {epic_data[0].get('caption')}")
#     print(f"    Coordinates: {epic_data[0].get('centroid_coordinates')}")
#     IMAGE_URL=f"{NASA_EPIC_IMAGE_API_URL}/{imgdate[:4]}/{imgdate[5:7]}/{imgdate[8:10]}/png/{img}.png"
#     print(f"    Image URL: {IMAGE_URL}")
#     webbrowser.open(f"{IMAGE_URL}?api_key={nasa_key}")

### End of Program ###
