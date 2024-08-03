# generate a unique id for each student

def id_assigner(list_of_names):
    names_dict={}
    for index, name in enumerate(list_of_names):
        names_dict[str(index + 1)] = name

    return names_dict