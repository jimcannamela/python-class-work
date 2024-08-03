# Minimum Value
def minimum_value(value1, value2):
    if value1 < value2:
        return value1
    else:
        return value2

#  Max of Three
def max_of_three(value1, value2, value3):
    # If value1 is greater than or equal to value2
    # and value1 is greater than or equal to value3
    if value1 >= value2 and value1 >= value3:                   
        # Return value1
        return value1                 
    # Otherwise, if value2 is greater than or equal to value1
    # and value2 is greater than or equal to value3
    elif value2 >= value1 and value2 >= value3:                 
        # Return value2
        return value2                 
    # Otherwise,
    else:   
        # Return value3
        return value3                   

# Can Skydive
def can_skydive(age, has_consent_form):
    # If the age is greater than or equal to 18 or they
    # have a consent form
    if age >= 18 or has_consent_form: 
        # Return True
        return True                   
    # Otherwise,
    else:   
        # Return False
        return False                    

# Is Palindrome
def is_palindrome(word):
    # Reverse the word into a list of letters
    # "hello" becomes ["o", "l", "l", "e", "h"]
    reversed_list_of_letters = reversed(word)

    # Join the letters together using the empty string
    # ["o", "l", "l", "e", "h"] becomes "olleh"
    reversed_word = "".join(reversed_list_of_letters)

    # If reversed_word equals word
    if reversed_word == word:         
        # return True
        return True                   
    # Otherwise
    else:   
        # return False
        return False                
    
# Divisible By 3
def is_divisible_by_3(number):
    # If number is divisible by 3
    if number % 3 == 0:       
        # return "fizz"
        return "fizz"         
    # Otherwise
    else:                     
        # return the number
        return number   
    
# Divisible By 5
def is_divisible_by_5(number):
    if number % 5 == 0:       
        return "buzz"         
    else:                     
        return number          

# FizzBuzz
def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:             
        return "fizzbuzz"     
    elif number % 3 == 0:     
        return "fizz"         
    elif number % 5 == 0:     
        return "buzz"         
    else:                     
        return number    

# Can Make Pasta
def can_make_pasta(ingredients):
    # If "flour" is in ingredients and "eggs" is
    # in ingredients and "oil" is in ingredients
    if (                      
        "flour" in ingredients
        and "eggs" in ingredients                       
        and "oil" in ingredients                        
    ):                        
        # return True
        return True           
    # Otherwise
    else:                     
        # return False
        return False              

# Is Inside Bounds
def is_inside_bounds(x, y):
    # If x is greater than or equal to 0 and y is greater than
    # or equal to 0 and x is less then or equal to 10 and y is
    # less than or equal to 10
    if x >= 0 and y >= 0 and x <= 10 and y <= 10:       
        # return True
        return True           
    # Otherwise
    else:                     
        # return False
        return False          

# Is Inside Bounds II
def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    # If x is greater than or equal to rect_x
    # and y is greater than or equal to rect_y
    # and x is less than or equal to rect_x + rect_width
    # and y is less than or equal to rect_y + rect_height
    if (                      
        x >= rect_x           
        and y >= rect_y       
        and x <= rect_x + rect_width                    
        and y <= rect_y + rect_height                   
    ):                        
        # return True
        return True           
    # Otherwise
    else:                     
        # return False
        return False                 

# Has Quorum
def has_quorum(attendees_list, members_list):
    # num_attendees = the number of attendees
    num_attendees = len(attendees_list)                 
    # num_members = the number of members
    num_members = len(members_list)                     
    # If the num_attendees divided by the num_members is
    # greater than 0.5
    if num_attendees / num_members >= 0.5:              
        # return True
        return True           
    # Otherwise
    else:                     
        # return False
        return False

# Gear For Day
def gear_for_day(is_workday, is_sunny):
    # Create an empty list that will hold the different gear
    # gear = new empty list
    gear = []
    # If it is a workday and it is not sunny
    if is_workday and not is_sunny:                     
        # Add "umbrella" to gear
        # gear.append("umbrella")
        gear.append("umbrella")                         
    # If it is a workday
    if is_workday:            
        # Add "laptop" to gear
        gear.append("laptop") 
    # Otherwise
    else:                     
        # Add "surfboard" to gear
        gear.append("surfboard")                        
    # Return the list of gear
    return gear               

# Calculate Average
def calculate_average(values):
    # If there are no items in the list of values
    if len(values) == 0:      
        # return None
        return None           
    # sum = 0
    sum = 0                   
    # for each item in the list of values
    for item in values:       
        # add it to the sum
        sum = sum + item      
    # return the sum divided by the number of items
    # in the list
    return sum / len(values)  

# Calculate Sum
def calculate_sum(values):
    # If there are no items in the list of values
    if len(values) == 0:      
        # return None
        return None           
    # sum = 0
    sum = 0                   
    # for each item in the list of values
    for item in values:       
        # add it to the sum
        sum = sum + item      
    # return the sum
    return sum          

# Calculate Grade
def calculate_grade(values):
    if len(values) == 0:      
        return None           
    sum = 0                   
    for item in values:       
        sum = sum + item      
    average = sum / len(values)                         
    if average >= 90:         
        return "A"            
    elif average >= 80:       
        return "B"            
    elif average >= 70:       
        return "C"            
    elif average >= 60:       
        return "D"            
    else:                     
        return "F"            

# Max In List
def max_in_list(values):
    # if there are no items in the values list
    if len(values) == 0:      
        # return None
        return None           
    # max value = first item in the values list
    max_value = values[0]     
    # for each item in the values list
    for item in values:       
        # if item is greater than the max value
        if item > max_value:  
            # max value = item
            max_value = item  
    # return the max value
    return max_value          

# Remove Duplicate Letters
def remove_duplicate_letters(s):
    # result = new empty string
    result = ""               
    # for every letter in the string s
    for letter in s:          
        # if the letter is not in the result
        if letter not in result:                        
            # add it to the end of the result
            result = result + letter                    
    # return the result
    return result             

# Find Second Largest
def find_second_largest(values):
    if len(values) <= 1:
        return None
    max_value = values[0]
    second_largest = None
    for value in values[1:]:
        if value > max_value:
            second_largest = max_value
            max_value = value
        elif second_largest is None or value > second_largest:
            second_largest = value
    return second_largest

# Sum of Squares
def sum_of_squares(values):
    if len(values) <= 1:      
        return None           
    result = 0                
    for value in values:      
        result += value * value                         
    return result  

# Sum of First n Numbers
def sum_of_first_n_numbers(limit):
    if limit < 0:             
        return None           
    sum = 0                   
    for i in range(limit + 1):
        sum = sum + i         
    return sum                
                        
# Sum of First n Even Numbers
def sum_of_first_n_even_numbers(n):
    if n < 0:                 
        return None           
    sum = 0                   
    for i in range(n + 1):    
        sum = sum + i * 2     
    return sum                
                        
# Count Letters and Digits
def count_letters_and_digits(s):
    # number of letters = 0
    num_letters = 0           
    # number of digits = 0
    num_digits = 0            
    # for each character c in s
    for c in s:               
        # if the character c is a digit (c.isdigit())
        if c.isdigit():       
            # add one to the number of digits
            num_digits += 1   
        # if the character c is a letter (c.isalpha())
        if c.isalpha():       
            # add one to the number of letters
            num_letters += 1  
    # return number of letters, number of digits
    return num_letters, num_digits                      
                        
# Pad Left
def pad_left(number, length, pad):
    # s = convert number to a string
    s = str(number)           
    # while the length of s is less than length
    while len(s) < length:    
        # s = pad + s
        s = pad + s           
    # return s
    return s                  
                        
# Reverse Dictionary
def reverse_dictionary(dictionary):
    # new_dictionary = new empty dictionary
    new_dictionary = {}       
    # for each key, value in dictionary.items()
    for key, value in dictionary.items():               
        # new_dictionary[value] = key
        new_dictionary[value] = key                     
    # return new_dictionary
    return new_dictionary     
                        
# Add CSV Lines
def add_csv_lines(csv_lines):
    # result_list = new empty list
    result_list = []          
    # for each item in the csv_lines
    for item in csv_lines:    
        # pieces = split the item on the comma
        pieces = item.split(",")                        
        # line_sum = 0
        line_sum = 0          
        # for each piece in pieces
        for piece in pieces:  
            # value = convert the piece into an int
            value = int(piece)
            # add the value to sum
            line_sum += value 
        # append sum to the result_list
        result_list.append(line_sum)                    
    # return result_list
    return result_list   

# Pairwise Add
def pairwise_add(list1, list2):
    results = []              
    for value1, value2 in zip(list1, list2):            
        results.append(value1 + value2)                 
    return results          

# Find Indexes
def find_indexes(search_list, search_term):
    results = []              
    for index, value in enumerate(search_list):         
        if value == search_term:                        
            results.append(index)                       
    return results            
                        
# Translate
def translate(key_list, dictionary):
    result = []               
    for key in key_list:      
        result.append(dictionary.get(key))              
    return result             
                        
# Make Sentences
def make_sentences(subjects, verbs, objects):
    # sentences = new empty list
    sentences = []            
    # for each subject in subjects
    for subject in subjects:  
        # for each verb in verbs
        for verb in verbs:    
            # for each object in objects
            for object in objects:                      
                # sentence = subject + " " + verb + " " + object
                sentence = subject + " " + verb + " " + object      
                # append sentence to sentences
                sentences.append(sentence)              
    # return sentences
    return sentences          
                        
# Check Password
def check_password(password):
    has_lowercase_letter = False              
    has_uppercase_letter = False              
    has_digit = False                         
    has_special_char = False                  
    for character in password:                
        if character.isalpha():               
            if character.isupper():           
                has_uppercase_letter = True   
            else:   
                has_lowercase_letter = True   
        elif character.isdigit():             
            has_digit = True                  
        elif character == "$" or character == "!" or character == "@":  
            has_special_char = True           
    return (        
        len(password) >= 6                    
        and len(password) <= 12               
        and has_lowercase_letter              
        and has_uppercase_letter              
        and has_digit                         
        and has_special_char                  
    )               
              
# Count Word Frequencies
def count_word_frequencies(sentence):               
    # words = split the sentence
    words = sentence.split()                        
    # counts = new empty dictionary
    counts = {}           
    # for each word in words
    for word in words:    
        # if the word is not in counts
        if word not in counts:                      
            # counts[word] = 0
            counts[word] = 0                        
        # add one to counts[word]
        counts[word] += 1 
    # return counts
    return counts  
       
# Sum Two Numbers
def sum_two_numbers(x, y):              
    return x + y                        

# Halve the List
def halve_the_list(input):    
    return (                  
        input[0:len(input) // 2 + (len(input) % 2)],    
        input[len(input) // 2 + (len(input) % 2):],     
    )                         
     
# or
     
def halve_the_list(input):     
    first_list = []           
    second_list = []          
    first_list_len = len(input) // 2 + (len(input) % 2)  
    for i in range(first_list_len):                     
        first_list.append(input[i])                     
    for i in range(len(input) // 2):                    
        index = i + first_list_len                      
        second_list.append(input[index])                
    return first_list, second_list                      

# Safe Divide
import math           
                    
def safe_divide(numerator, denominator):         
    if denominator == 0:                        
        return math.inf                         
    return numerator / denominator              

# Generate Lottery Numbers
from random import randint                   
                       
def generate_lottery_numbers():                  
    numbers = []      
    while len(numbers) < 6:                     
        number = randint(1, 40)          
        if number not in numbers:               
            numbers.append(number)              
    return numbers    
                       
# or                  
import random                       

def generate_lottery_numbers():                  
    numbers = list(range(1, 41))                
    random.shuffle(numbers)                     
    return numbers[0:6]       
                  
# Username From Email
def username_from_email(email):     
    return email.split("@")[0]      

# Check Input
def check_input(input):             
    if input == "raise":            
        raise ValueError            
    return input                    

# Simple Roman
def simple_roman(number):           
    lookup = {                      
        1: "I",                     
        2: "II",                    
        3: "III",                   
        4: "IV",                    
        5: "V",                     
        6: "VI",                    
        7: "VII",                   
        8: "VIII",                  
        9: "IX",                    
        10: "X",                    
    }     
    return lookup[number]           

# Number Concatenation
def num_concat(m, n):           
    return str(m) + str(n)      

# Sum Fraction Sequence
def sum_fraction_sequence(n):           
    sum = 0   
    for i in range(1, n + 1):           
        sum += i / (i + 1)              
    return sum

# Group Cities By State
def group_cities_by_state(cities):          
    output = {}   
    for city in cities:                     
        name, state = city.split(",")       
        state = state.strip()               
        if state not in output:             
            output[state] = []              
        output[state].append(name)          
    return output 

# Specific Random
import random     

def specific_random():                       
    good_numbers = []                       
    for i in range(10, 501):                
        if i % 35 == 0:                     
            good_numbers.append(i)          
    return random.choice(good_numbers)      

# Only Odds
def only_odds(nums):                
    output = []                     
    for num in nums:                
        if num % 2 == 1:            
            output.append(num)      
    return output                   

# Remove Duplicates
def remove_duplicates(values):      
    output = []                     
    for value in values:            
        if value not in output:     
            output.append(value)    
    return output                   

# Basic Calculator
def basic_calculator(left, op, right):      
    if op == "+": 
        return left + right                 
    if op == "-": 
        return left - right                 
    if op == "*": 
        return left * right                 
    if op == "/": 
        return left / right                 

# Shift Letters
def shift_letters(word):                        
    new_word = ""     
    for letter in word:                         
        if letter == "Z":                       
            new_letter = "A"                    
        elif letter == "z":                     
            new_letter = "a"                    
        else:         
            new_letter = chr(ord(letter) + 1)   
        new_word += new_letter                  
    return new_word   

# Temperature Differences
def temperature_differences(highs, lows):       
    differences = []  
    for high, low in zip(highs, lows):          
        differences.append(high - low)          
    return differences

# Biggest Gap
def biggest_gap(nums):
    max_gap = abs(nums[1] - nums[0])            
    for i in range(1, len(nums) - 1):           
        gap = abs(nums[i + 1] - nums[i])        
        if gap > max_gap:                       
            max_gap = gap                       
    return max_gap    
