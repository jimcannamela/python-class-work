# Weather App

## Overview
This is a Python command-line application that fetches and displays current weather information for a specified city in the United States. The application uses the OpenWeatherMap API to retrieve weather data and presents it to the user in a user-friendly format. 

## Features
Fetches current weather data based on city and state.
Allows users to choose between Celsius and Fahrenheit for temperature units.
Handles API errors and provides relevant feedback to the user.
Supports unit testing with pytest.

## Requirements
To run this application, you need to install the required Python packages. Use the `requirements.txt` file for this purpose:
- `pip install -r requirements.txt`

The application also uses environment variables for sensitive information. Ensure you have a .env file with the following content:
- `OPENWEATHER_API_KEY=your_openweathermap_api_key`

Replace your_openweathermap_api_key with your actual API key from OpenWeatherMap.

## Usage
1. Run the application:
- `python main.py`

2. Follow the prompts:
- Enter a city name when prompted.
- Provide a valid US state abbreviation or name when prompted.
- Choose the temperature unit (Celsius or Fahrenheit).

3. View the weather report: The application will display the current weather for the specified city and state.

4. Search again or exit: Decide whether to search for another city's weather or exit the application.

## Testing
1. Run pytest:
- `pytest`
