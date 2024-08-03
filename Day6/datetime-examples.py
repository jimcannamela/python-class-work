# Example 1: Getting the Current Date and Time
# Fetching the current date and time is a frequent requirement in programming.

import datetime

# The current date and time
now = datetime.datetime.now()

# Getting just the current date
today = datetime.date.today()

print(f"Now: {now} Today: {today}")

# Example 2: Creating Specific Date and Time Objects
# Creating date and time objects for specific moments.

# Turning July 4, 1776 as a datetime object
independence_day = datetime.date(1776, 7, 4)

print(f"Independence Day: {independence_day}")

# Turning 12:00 PM into a datetime object
# Note: This is a generic 12:00 PM time and has no date 
noon = datetime.time(12, 0, 0)

print(f"Noon: {noon}")

# Example 3: Date and Time Arithmetic
# Performing arithmetic operations like addition and subtraction.

# Adding days to a date
tomorrow = today + datetime.timedelta(days=1)

# Calculating the difference between two dates
duration = tomorrow - today

print(f"Tomorrow: {tomorrow} Duration: {duration}")

# Example 4: Formatting Dates and Times
# Converting dates and times to formatted strings.

now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted)

# Example 5: Parsing Date and Time Strings
# Creating date/time objects from strings.

date_string = "2021-04-30"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# Example 6: Working with Timezones
# Handling timezone-aware datetime objects.

from datetime import timezone

# UTC time
utc_time = datetime.datetime.now(timezone.utc)
print("UTC Time:", utc_time)