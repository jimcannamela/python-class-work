import rover
import apollo
import input
import webbrowser

def start_rover(key):
    date = input.get_date_from_user()
    photo_url = rover.get_by_date(date, key)
    open_in_browser(f'Opening browser to display a Mars Rover photo from {date}', f'There is no photo from {date}', photo_url)

def start_apollo():
    photo_url = apollo.get_photo()
    open_in_browser(f'Opening browser to display an Apollo photo', f'There is no photo', photo_url)

def open_in_browser(success_msg, error_msg, photo_url):
    if photo_url !='':
        print(success_msg)
        webbrowser.open(photo_url)
    else:
        print(error_msg)