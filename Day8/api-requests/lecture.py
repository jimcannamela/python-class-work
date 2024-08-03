# import os, requests

#print(requests)

# to create a requirements.txt file
# pip freeze > requirements.txt

# URL TO GET DATA FROM 
# jsonplaceholder.typicode.com

# API_URL_POSTS = "https://jsonplaceholder.typicode.com/posts?_limit=5"
# API_URL_POSTS = "https://api.disneyapi.dev/character/"

# response = requests.get(API_URL_POSTS).json()

# print(response)

'''
Response
[{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}, {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}, {'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}, {'userId': 1, 'id': 4, 'title': 'eum et est occaecati', 'body': 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit'}, {'userId': 1, 'id': 5, 'title': 'nesciunt quas odio', 'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'}] 
'''

import requests

api_key = "DRmrvSEjggbV0PgSlJ44057kSQFFvnvnGJ6y1fkE"



# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

# my_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=DRmrvSEjggbV0PgSlJ44057kSQFFvnvnGJ6y1fkE")
# my_request = requests.get(f"{API_URL}?api_key={api_key}")

# print(my_request.json())


def get_nasa_apod(api_key):

    API_URL = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        apod_data = response.json()

        return apod_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

apod_data = get_nasa_apod(api_key)

if 'error' in get_nasa_apod(api_key):
    print("An error occurred")
else:
    # print(f"Today's NASA APOD is: {get_nasa_apod(api_key)['title']}")
    print(f"Title: {apod_data['title']}")
    print(f"Date: {apod_data['date']}")
    print(f"Explanation: {apod_data['explanation']}")
    print(f"URL: {apod_data['url']}")







# print(get_nasa_apod(api_key))


import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NASA_API_KEY")

# pip install python-dotenv


# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

# my_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=DRmrvSEjggbV0PgSlJ44057kSQFFvnvnGJ6y1fkE")
# my_request = requests.get(f"{API_URL}?api_key={api_key}")

# print(my_request.json())


def get_nasa_apod(api_key):

    API_URL = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        apod_data = response.json()

        return apod_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

apod_data = get_nasa_apod(api_key)
print(apod_data)

# # open the apod image in a browser
# import webbrowser

# webbrowser.open(apod_data['url'])








# if 'error' in get_nasa_apod(api_key):
#     print("An error occurred")
# else:
    # print(f"Today's NASA APOD is: {get_nasa_apod(api_key)['title']}")
    # print(f"Title: {apod_data[0].get('title')}")
    # print(f"Date: {apod_data['date']}")
    # print(f"Explanation: {apod_data['explanation']}")
    # print(f"URL: {apod_data['url']}")







# print(get_nasa_apod(api_key))

'''
## Project Instructions

1. Create a new git lab project - done
2. Clone it to your machine     - done
3. CD INTO THAT FOLDER          - done 
4. Create a virtual env         - done
5. PIP freeze > requirements.txt - done
6. create a main.py file where you will have all your api calls - Done
7. pip install requests or any other library you wish to use. AND any other imports you may need - done
8. git add and git commit and push to test - done
9. pip install python-dotenv - done  
10. handle the .env file and bring your apikey into your main.py file - done
11. 
@Stephen Druessel
 - do whatever he says!
'''