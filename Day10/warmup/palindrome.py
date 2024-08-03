# Create a function which determines if the entered string is a palidrome
import re

def is_palindrome(str):
    # upper case string
    upper_str=str.upper()
    # strip string remove all spaces
    # stripped_str=re.sub(r"\s+", "", upper_str, flags=re.UNICODE)
    # remove all spaces and special characters
    stripped_str=re.sub('[^A-Za-z0-9]+', '', upper_str)
    # reverse stripped string
    reversed_str=stripped_str[::-1]
    # compare stripped string to reversed string
    print (f"str: {str} upper: {upper_str} \n stripped: {stripped_str} reversed: {reversed_str}")
    return stripped_str == reversed_str

# Possible tests
#    racecar
#    madam in edam I'm adam
#    a toyota's a toyota
#    hello world
print(is_palindrome('madam'))
print(is_palindrome('Madam'))
print(is_palindrome('never odd or even'))
print(is_palindrome("A toyota's a toyota"))

#  Brad's code

# def is_palindrome(phrase):
#     filtered_phrase = filter(str.isalpha, phrase.lower())
#     filtered_string = "".join(filtered_phrase)

#     return filtered_string == filtered_string[::-1]