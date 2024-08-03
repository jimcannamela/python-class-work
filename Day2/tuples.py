# tuples
'''
What are Tuples in Python? A tuple is an ordered collection of elements, enclosed in parentheses.
Unlike lists, tuples are immutable, which means that once a tuple is created, its elements cannot 
be modified. Tuples can contain elements of different data types, such as integers, strings, 
floats, or even other tuples.
'''

# - immutable
# - ordered
# - allows duplicate elements
# - allows different data types
# - represented by ()
my_tuple = ('Jim', 'has', 'a', 'tuple')
print(type(my_tuple))
# zip() method
# - it combines two into a list of tuples
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3]
list3 = [4, 5, 6]
print(list(zip(list1, list2, list3)))