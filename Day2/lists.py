# Lists in python
# lists are mutable

amazon_cart = ['notebook', 'sunglasses', 'toys', 'grapes', 'lights']

print(amazon_cart[0])  # indexing   -> notebooks

# amazon_cart[0] = 'laptop'   # reassigning

# print(amazon_cart)   # --> laptop

# slicing in python
print(amazon_cart[0:3])      # slicing             -->  ['notebook', 'sunglasses', 'toys']
print(amazon_cart[0::2])     # slicing with steps  -->  ['notebook',  'toys', 'lights']
print(amazon_cart[::-1])     # reverse order       -->  ['lights', 'grapes', 'toys', 'sunglasses', 'notebook']
print(amazon_cart[::])       # reverse order       -->  ['lights', 'grapes', 'toys', 'sunglasses', 'notebook']

# .append() method
# it modifies the original list
# it does not return anything
# it only adds 1 item at a time to the end of the list
amazon_cart.append('laptop')
print(amazon_cart)

# .extend() method
# it modifies the original list
# it does not return anything
# it adds multiple items at the same time to the end of the list
amazon_cart.extend(['table', 'chair'])
print(amazon_cart)

# .insert() method
# it modifies the original list
# it does not return anything
# it takes two arguments
# 1st argument in the index where you want to insert the element
# 2nd argument is the element you want to insert
# expensive as it requires a complete re-indexing of the list


# .clear() method

# .remove() method 
# it removes the first element from the list
# it modifies the original list
# it does not return anything
amazon_cart.remove('toys')    # can an index be used in this method also????

# .pop() method
# removes the last element of the list
# it modifies the original list
# it returns the element that is removed from the list

popped_item = amazon_cart.pop()
print(popped_item)
print(amazon_cart)

# deconstructing a list

a, b, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(other)
print(d)

# lists of lists to create matrixes

# .copy()
list1 = ['a', 'b', 'c']
list2 = list1

list2.append('d') # both lists impacted

print(list1)
print(list2)

list3 = list1.copy()
list4 = list1[:]

list3.append('e')
list4.append('f')

print(list1)
print(list2)
print(list3)
print(list4)

