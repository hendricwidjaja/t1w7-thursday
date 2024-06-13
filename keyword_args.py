def greet(fname, lname):
    print(f"Hello, {fname} {lname}!!")

greet("Max", "Brenner")

# Using keyword args
greet(fname="Max", lname="Brenner")

greet(lname="Brenner", fname="Max")


def describe_pet(pet_name, animal_type="dog"): #animal_type has a default value
    print(f"I have a {animal_type} named {pet_name}")

# Positional Argument (if you only have input one argument when it takes 2 arguments, it will put the argument in the first one)
describe_pet("Willie")

# Positional and default argument
describe_pet("Harry", "Hamster")

# Keyword Arguments
describe_pet(animal_type="cat", pet_name="Whiskers")