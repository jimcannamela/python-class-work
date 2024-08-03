# Dictionaries in Python
# dictionary is a key value pair

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'strange berry', 'bedroll', 'bread loaf'],
    'is_new': False,
    'items': {
        'pocket': ['seashell', 'strange berry', 'lint'],
        'bag': ['water', 'food', 'map']
    }
}

print(type(inventory))
print(inventory)

# access the value of a key
print(inventory['gold'])    # --> 500
#print(inventory['pouches']) # --> None
print(inventory['pouch'])   # --> ['flint', 'twine', 'gemstone']

# .get()
print(inventory.get('items')) # -->  {'pocket': ['seashell', 'strange berry', 'lint'], 'bag': ['water', 'food', 'map']}
print(inventory.get('itemss', 'not found')) # --> not found

# multiple gets
# print(inventory.get('itemss', 'not found').get('pocket')) <-- not working

# add items to a dictionary
inventory['backpack'].append('bottle')
print(inventory['backpack']) # --> ['xylophone', 'strange berry', 'bedroll', 'bread loaf', 'bottle']

# sort a dictionary
inventory['backpack'].sort()
print(inventory['backpack']) # --> ['bedroll', 'bottle', 'bread loaf', 'strange berry', 'xylophone']

# pop
popped_item = inventory.pop('gold')
print(popped_item)  # --> 500
print(inventory)    # --> {'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['bedroll', 'bottle', 'bread loaf', 'strange berry', 'xylophone'], 'is_new': False, 'items': {'pocket': ['seashell', 'strange berry', 'lint'], 'bag': ['water', 'food', 'map']}}

print(inventory.keys())    # --> dict_keys(['pouch', 'backpack', 'is_new', 'items'])
print(inventory.values())  # --> dict_values([['flint', 'twine', 'gemstone'], ['bedroll', 'bottle', 'bread loaf', 'strange berry', 'xylophone'], False, {'pocket': ['seashell', 'strange berry', 'lint'], 'bag': ['water', 'food', 'map']}])
print(inventory.items())   # --> dict_items([('pouch', ['flint', 'twine', 'gemstone']), ('backpack', ['bedroll', 'bottle', 'bread loaf', 'strange berry', 'xylophone']), ('is_new', False), ('items', {'pocket': ['seashell', 'strange berry', 'lint'], 'bag': ['water', 'food', 'map']})])

# popitem method
# removes the last key value pair from the dictionary that was entered
# LIFO 
print(inventory.popitem()) # --> ('items', {'pocket': ['seashell', 'strange berry', 'lint'], 'bag': ['water', 'food', 'map']})
print(inventory)           # --> {'pouch': ['flint', 'twine', 'gemstone'], 'backpack': ['bedroll', 'bottle', 'bread loaf', 'strange berry', 'xylophone'], 'is_new': False}


