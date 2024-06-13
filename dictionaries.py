# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Sydney"
}

# Access the values by using the keys as the "index"
print(my_dict["city"])

# info = ["Alice", 25, "Sydney"] <--- could do it this way but not as labelled

# Adding a new key-pair value
my_dict["email"] = "alice@example.com"
print(my_dict)

# Adding an item with an existing key overwrites the original value
my_dict["city"] = "Melbourne"
print(my_dict)

# Removing a key-value pair
del my_dict["age"]
print(my_dict)

# Alternatively, you can use .pop()
my_dict.pop("email")
print(my_dict)

# Checking for key existence
print("email" in my_dict)
print("name" in my_dict)

# https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())

print(list_of_values.index("Alice"))
print(list_of_keys[0])

#Iterate through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age":30}
}

print(nested_dict["person2"]["name"])

# Merging dictionaries (If any duplicate keys, the key from the 2nd dictionary will overwrite the key in the first dictionary)
merged_dict = my_dict | nested_dict
print(merged_dict)