from termcolor import colored

temp_unit_dict = {
    'metric': 'C',
    'imperial': 'F'
}

def display(weather_data, units):
    print(colored((f'\nThe current weather for {weather_data['name']} is as follows: '), 'light_cyan'))
    print(colored(f'\tDescription: {weather_data['weather'][0]['description']}', 'light_cyan'))
    print(colored(f'\tTemp: {weather_data['main']['temp']}\xb0{temp_unit_dict[units]}', 'light_cyan'))
    print(colored(f'\tHumidity: {weather_data['main']['humidity']}%', 'light_cyan'))