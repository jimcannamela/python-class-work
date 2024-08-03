# some_list = []
# print(help(some_list))   

# our own customer class
# classes in python are blueprints for creating objects

class Cat:
    def __init__(self, name, age):     # constructor method
        self.name = name
        self.age = age

# print(Cat)                             # <class '__main__.Cat'>

whiskers = Cat("Whiskers", 3)

# print(whiskers)                        # <__main__.Cat object at 0x000002DA2A987C10>

garfield = Cat("Garfield", 5)          # <__main__.Cat object at 0x000002DA2A987D90>   <-- notice different location

# print(garfield)

colton = Cat("Colton", 2)

cat_dictionary = {
    whiskers.name: whiskers.age,
    garfield.name: garfield.age,
    colton.name: colton.age
}

max_of_cat = max(cat_dictionary, key=cat_dictionary.get)


class Dog:
    dog_id =1  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Dog.dog_id
        Dog.dog_id += 1

    def bark(self):
        return f"{self.name} says woooooof!"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and has an id of {self.id}"
    
    @classmethod
    def get_total_dogs(cls):
        return cls.dog_id -1
    
first_dog = Dog("Rex", 2)
second_dog = Dog("Buddy", 3)
third_dog = Dog("Lassie", 4)

print(first_dog.bark())
print(first_dog)
print(first_dog.id)
print(second_dog.id)

print(Dog.get_total_dogs())



