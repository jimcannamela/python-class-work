# from calendar import isleap

# def is_leap_day(year, month, day):
#     if isleap(year) and month == 2 and day == 29:
#         return True
#     else:
#         return False

# def another_function():
#     pass

# print(is_leap_day(2020, 2, 29))

from calendar import isleap

def is_leap_day(year, month, day):
    if isleap(year) and month == 2 and day == 29:
        return True
    else:
        return False

def another_function():
    return "this is another function"

# print("hello")


class MyClass:
    party = "hello"


if __name__ == "__main__":
    print("is_leap.py is being run directly")
    # is_leap_day()
    another_function()
else:
    print("is_leap.py is being imported into another module")