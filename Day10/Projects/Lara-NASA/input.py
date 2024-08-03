import datetime
def get_date_from_user():
    while True:
        try:
            date_str = input('Please enter a date in the following format (yyyy-mm-dd): ').strip().split('-')
            return datetime.date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
        except Exception as e:
            print('Invalid date format.\n')
