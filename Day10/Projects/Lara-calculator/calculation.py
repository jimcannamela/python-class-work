def perform_calculation(operation, operand1, operand2):
    try:
        return operation(operand1, operand2)
    except ZeroDivisionError:
        return 'undefined'
    except TypeError:
        return 'undefined'