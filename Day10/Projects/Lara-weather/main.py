import os
from termcolor import colored
from dotenv import load_dotenv
import user_input
import weather_api
import data_format

os.system('color')
load_dotenv()
key = os.getenv("OPENWEATHER_API_KEY")

print(colored('\n*********************** Weather App ***********************\n', 'cyan'))

while True:

    city = input('Please enter a US city: ').title()
    state_code = user_input.get_valid_us_state()
    units = user_input.get_valid_temp_measurement()
    weather_data = weather_api.get_current_forecast_by_citystate(city, state_code, units, key)

    if weather_data != '':
        data_format.display(weather_data, units)
    else:
        print(colored('An error occurred and we cannot currently get the weather for that city', 'red'))

    while True:
        again = input('\nWould you like to search weather data for another city? (y/n): ')
        if(again == 'n' or again == 'y'):
            break
        print('Invalid answer')
    if again == 'n':
        break

print(colored('\n***********************  Goodbye  ***********************\n', 'cyan'))