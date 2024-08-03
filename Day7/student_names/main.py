# create and activate virtual environment

# python -m venv my_students_env
# .\my_students_env\Scripts\activate

# to take some names in the names.txt file and print them out

# import our read_name_file function
import read_name_file
import id_assigner
import reverse_names_in_list

# get list of names from names.txt file
names = read_name_file.read_name_from_file("names.txt")
#print(names)

reversed_names=reverse_names_in_list.reverse_names_in_list(names)

# sort the names in alphabetical order
sorted_names = sorted(reversed_names)
#print(sorted_names)

# add ids to students
# {1: 'John, 2: 'Jane', 3: 'Doe'}

names_dict = id_assigner.id_assigner(sorted_names)
print(names_dict)

### End of Program ###