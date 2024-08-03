# scope
# types of scope in python

# 1. local scope
# 2. Enclosing scope (non local)
# 3. Global scope
# 4. Built in scope

# def say_hello():
#     my_variable = "Hello"
#     print(my_variable)

# say_hello()
# print(my_variable)  # NameError: name 'my_variable' is not defined -> Out of Scope


### Example of enclosing scope
### A variable define in the enclosing function (outer_function) can be used in the nested function (inner_function)

# def outer_function():
#     name = "John"

#     def inner_function():
#         print(name)

#     inner_function()

# outer_function()

# my_variable = "global variable"

# def my_function():
#   print(my_variable)

# built in scope - python built functions

# len() print() sum() max() min() sorted()

# LEGB scope rule

# 1. local scope
# 2. Enclosing scope (non local)
# 3. Global scope
# 4. Built in scope

def super_func(*args):    # unknown number of input args

    return sum(args)

print(super_func(1,2,3,4,5,6,7,8,9))

