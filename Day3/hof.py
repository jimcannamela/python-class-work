# map, filter, reduce, zip

# def multiple_by_2(list):
#     new_list = []
#     for item in list:
#         new_list.append(item * 2)
#     return new_list

# print("function output:")
# print(multiple_by_2([1,2,3]))  # -> [2, 4, 6]

# map() method
# - it takes two arguments
# map(helper function(action), what data? (list))

# my_list = [1,2,3]
# new_list = [2,3,4]

# def multiply_by_2(item):
#     return item * 2

# print("\nmap() output:")
# print(list(map(multiply_by_2, my_list)))

# def multiply_nums(a,b):
#     return a*b

# print("\nmore map() output:")
# print(list(map(multiply_nums, my_list, new_list)))

# filter method

# def only_odd(item):
#     return item % 2 != 0

# print("\nfilter output:")
# print(list(filter(only_odd, [1,2,3,4,5,6])))


# reduce method
from functools import reduce
print(reduce)
scores = [75, 80, 85, 45]
# How we would do it in our head
# 0 + 75 = 75
# 75 + 80 = 155
# 155 + 85 = 240
# 240 + 45 = 285

def accumulator(acc, item):
    return acc + item

print("\nReduce output")
print(reduce(accumulator, scores, 0)) # 285