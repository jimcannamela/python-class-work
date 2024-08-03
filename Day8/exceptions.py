# exception handling in python is done using the try and except block


# indexError - trying to access an index that does not exist
# AssertionError - raised when an assert statement fails
# KeyError - raised when a dictionary key is not found
# attributeError - raised when an attribute reference or assignment fails
# importError - raised when an import statement fails
# typeError - raised when an operation or function is applied to an object of an inappropriate type
# valueError - raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
# nameError - raised when a local or global name is not found
# zeroDivisionError - raised when the second operator in the division is zero


import math

class MyCustomError(Exception):
    pass


def fifty_by(number):
    if number == 0:
        raise ValueError("Number cannot be zero")
    if number == 1:
        raise MyCustomError("Number cannot be 1")
    try:
        return 50 / number
    except ZeroDivisionError:
        return "Number cannot be zero"
    except TypeError:
        return "Number must be an integer"
    except Exception as e:
        return e
    except:
        raise Exception("An error occurred")
    finally:
        print("This will always run")



print(fifty_by(0))


### Refactor of Brad's code

#def divide(x, y):
#     if float(y) == 0:
#         return '', "Cannot divide by zero"
#     else:
#         return float(x) / float(y), ''


class DivisionError(Exception):
    pass


def divide_numbers(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError("Numerator and denominator must be numbers")

        if denominator == 0:
            raise DivisionError("Denominator cannot be zero")

        result = numerator / denominator
        return result

    except DivisionError as e:
        return str(e)
    except Exception as e:
        return str(e)

# # result = divide_numbers("10", 10)
# # print(result)

# result = divide_numbers(10, 2)
# print(result)
