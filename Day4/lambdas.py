# lamba expressions
# are a 1 time anonymous function that you don't need any more than once
# lamba param: action(parm)

from functools import reduce
print(reduce)

def accumulator(acc, item):
    return acc + item

list3 = [1, 2, 3, 4, 5]

my_mapped_list=list(map(lambda item: item * 2, list3))
print(my_mapped_list)

my_calculated_sum = reduce(lambda acc, item: acc +item, list3, 1)
print(my_calculated_sum)

add = lambda a, b: a + b
print(add(2,3))

# list comprehension

