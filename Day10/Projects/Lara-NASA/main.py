import os
import nasa
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NASA_API_KEY")

while True:
    try:
        option = int(input('\nChoose from the following options (1, 2, or 3):\n1. I want to see a photo taken by Rover on a given date\n2. I want to see a random Apollo photo\n3. Exit\n'))
        if option == 1:
            nasa.start_rover(key)
        elif option == 2: 
           nasa.start_apollo()
        elif option == 3:
            print('\nGoodbye!\n')
            break
    except ValueError:
        print('Please enter a number (1, 2, or 3)')