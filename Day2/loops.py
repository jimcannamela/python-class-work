# loops

# for loop_var in some_list
#   logic

# looping through a list
colors = ['red', 'green', 'blue']

print(type(colors))

for color in colors:
    print(color)

print('\n\n')

for i in range(6):
    print(f"Looping... we have looped {i} times")

print('\n\n')

for i in range(1,6):
    print(f"Looping... we have looped {i} times")

print('\n\n')

for i in range(2, 11, 2):
    print(f"Looping... we have looped {i} times")

print('\n\n')

nums = list(range(11))
print(nums)

print('\n\n')
# looping through tuples

colors_2 = ('purple', 'brown', 'black')

print(type(colors_2))

for color in colors_2:
    print(color.title())

print('\n\n')

# looping through a dictionary
fav_colors = {
    "jay": "red",
    "mike": "green",
    "jan": "blue"
}

# default behavior - prints out keys
for color in fav_colors:
    print(color)

print('\n')

for key in fav_colors.keys():
    print(key)

print('\n')

for value in fav_colors.values():
    print(value)

print('\n')

for item in fav_colors.items():
    print(item)

print('\n')

for key, value in fav_colors.items():
    print(key, value)

print('\n')

count = 0

while True:
    if count == 1000:
        break
    print(f"The loop is looping... We have looped {count} times")
    count += 1

count = 0

while count < 100:
    if count == 1000:
        break
    print(f"The loop is looping... We have looped {count} times")
    count += 1