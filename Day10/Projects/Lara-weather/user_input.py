us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

temp_unit_dict = {
    'C': 'metric',
    'F': 'imperial'
}

# Prompts user for US state and returns the 2-digit state code. Input is not case sensitive. Function can handle if user inputs full state name
def get_valid_us_state():
    while True:
        state_input = input('Please enter a US state (e.g. AZ or arizona): ')
        if state_input.title() in us_state_to_abbrev: # in case user inputs a full state
            return us_state_to_abbrev[state_input.title()]
        if state_input.upper() in us_state_to_abbrev.values():
            return state_input.upper()
        print('Invalid state')

def get_valid_temp_measurement():
    while True:
        unit = input('Enter \'F\' to see weather in Fahrenheit or enter \'C\' to see weather in Celsius: ').upper()
        if(unit in temp_unit_dict):
            return temp_unit_dict[unit]
        print('Invalid input')
