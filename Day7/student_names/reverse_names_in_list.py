
def reverse_names_in_list(name_list):
    reversed_names=[]

    for name in name_list:
        name_list = name.split()
        rev_name=name_list[-1]
        rev_name=rev_name + ', ' + name_list[0]
        if len(name_list) > 2:
            rev_name=rev_name + ' ' + name_list[1]
        #print(f"Input name: {name_list} Reversed Name: {rev_name}")
        reversed_names.append(rev_name)

    return reversed_names