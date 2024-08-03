def find_second_largest(values):
    if len(values) == 0 or len(values) == 1:
        return None
    maximum = max(values)
    values.remove(maximum)
    SecondMax = max(values)
    return SecondMax