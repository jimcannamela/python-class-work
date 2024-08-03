# Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list

# Given:

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# def add_spec_item(in_number1, in_number2, in_list):
#     out_list=in_list
#     for item in out_list:
#         print(f"Item: {item} Type: {type(item)}")
#         if type(item) == int and item == in_number2:
#             item.append(in_number1)
#         else:
#             type(item) == list
#             for item1 in item:
#                 print(item1)
#                 print(f"Item: {item1} Type: {type(item1)}")
#                 if type(item1) == int and item1 == in_number2:
#                     item1.append(in_number1)
#                 else:
#                     type(item1) == list               
#                 for item2 in item1:
#                     print(item2)
#                     print(f"Item: {item2} Type: {type(item2)}")
#                     if type(item2) == int and item == in_number2:
#                         item2.append(in_number1)
#                     else:
#                         type(item2) == list
    
#     return out_list

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# result = list1[2][2].append(7000)
# print(list1)

# Greg Keller
def add_element_to_nested_list(lst, element_to_find, element_to_add):
    for item in lst:
        if item == element_to_find:
            idx = lst.index(item) + 1
            lst.insert(idx, element_to_add)
        else:
            if isinstance(item, list):
                add_element_to_nested_list(item, element_to_find, element_to_add)
    return (lst)

element_to_add=7000
element_to_find=6000
lst=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]

expected_list=[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
actual_list=add_element_to_nested_list(lst, element_to_find, element_to_add) 

if actual_list == expected_list:
    print(f"Successful execution output list is:, {actual_list}")
else:
    print(f"Failed execution output list is: {actual_list}")

element_to_add=7000
element_to_find=9999
lst=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]

expected_list=[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
actual_list=add_element_to_nested_list(lst, element_to_find, element_to_add) 

if actual_list == expected_list:
    print(f"Successful execution output list is:, {actual_list}")
else:
    print(f"Failed execution output list is: {actual_list}")

# in_number1=7000
# in_number2=6000
# in_list=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# expected_list=[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# actual_list=add_spec_item(in_number1, in_number2, in_list) 

# if actual_list == expected_list:
#     print(f"Successful execution output list is:, {actual_list}")
# else:
#     print(f"Failed execution output list is: {actual_list}")

# Joe Caroll
# another recursive example
search_val = 6000
insert_val = 7000

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def recur(in_list):
    if len(in_list) > 1:
        for idx, val in enumerate(in_list):
            if isinstance(val, list):
                recur(val)
            else:
                if val == search_val:
                    in_list.insert(idx + 1, insert_val)
                    
recur(list1)
print(list1)