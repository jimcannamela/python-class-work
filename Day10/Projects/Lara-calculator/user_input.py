import operator

def get_float_input():
    while True:
        try:
            num = float(input('Please enter a number:'))
            break
        except ValueError:
            print('Incorrect input. Please enter a valid number')
            
    return num

def get_operator_input():
    operator_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '%': operator.mod
    }
    
    while True:
         op = input(f'Please enter an operator ({', '.join(operator_dict.keys())}): ')
         if(op in operator_dict):
             return operator_dict[op]
         print('Operator is invalid')