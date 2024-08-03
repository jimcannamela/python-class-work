'''
Project A
Objective:
Build a simple command-line calculator that can perform basic arithmetic operations: addition, subtraction, multiplication, and division

Features:

Calculator should be able to handle two numbers at a time.
The user should be prompted to enter two numbers and the operation they want to perform
The calculator should display the result of the operation
After displaying the result, the calculator should ask the user if they want to perform another calculation.
The application should handle basic error checking, such as division by zero and input validation.
Hints:

Each arithmetic operation can be a function
Write a function that prompts the user to input two numbers and ensure these are valid numbers
you may use try… except block to handle exceptions and validate the input
Implement a loop to allow the user to keep using the calculator without restarting the script
Improvements:

Allow calculator to handle floating-point numbers
Extend the calculator with more operations (e.g., exponentiation, square root, modulus, etc..)
'''

def Calculator(operation,num1,num2 = 0):    
    try:
        if operation == 1:
            result = num1 + num2
        elif operation == 2:
             result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 / num2
        elif operation == 5:
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 % num2
        elif operation == 6:
            result = num1 ** num2
        elif operation == 7:
            result = num1 ** 0.5         
        else:
            pass
        if int(str(result).split('.')[1]) == 0:
            return int(result)
        else:
            return result
    except:
       raise ValueError
    # finally:
    #     return "The end"
print("Welcome to the Edgar/Jim Calculator")
print("Please select which operation you woul dlike to perform from the following list:")
print("    1. Addition")
print("    2. Subtraction")
print("    3. Multiplication")
print("    4. Division" )    
print("    5. Modulus" )  
print("    6. Exponentiation" ) 
print("    7. Square root," ) 
operation = 0
while True:
    while True:        
        operation = input("Please type your operation: ")
        if not operation.isdigit():            
            print("Please enter a valid number")
            continue
        if (1 <= int(operation) <= 7):
            break      
        else:
            print("You have to type between 1 to 7")
    while True:
        num1 = input("Enter first number: ")
        try:
            x = float(num1)
            break
        except:
            print("Please enter a valid number")
    if int(operation) != 7:
        while True:
            num2 = input("Enter second number: ")
            try:
                x = float(num2)
                break
            except:
                print("Please enter a valid number")
    else:
        num2 = 0  
    print(Calculator(int(operation),float(num1),float(num2)))
    keepGoing = input("You want another calculation? (Y / N) ")
    if keepGoing.upper() != "Y":
        break