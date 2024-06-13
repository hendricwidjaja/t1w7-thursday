# Creating a set
my_set = {1, 2, 3, 4}

print(my_set)

# Adding an element

my_set.add(5)
print(my_set)

# Remove an element
my_set.remove(2)
print(my_set)

# Membership testing
print(2 in my_set)
print(3 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union = set_a + set_b values. Therefore union of both sets would result with {1, 2, 3, 4, 5} NOTE: duplicate of 3 is removed as there can't be duplicate values in a set
# Even though unordered, it will put numbers in ascending order
# Union example
union_value = set_b.union(set_a)
print(union_value)

# Intersection = trying to find an intersection of 2x sets, it will give you the common value/s in both sets. Above example would result in {3}. If there aren't any common values, it will result with an empty set.
intersection_value = set_a.intersection(set_b)
print(intersection_value)

# Difference = set_a - set_b (it will remove any duplicate values. But will only provide values for first set). Above example would result in {1, 2}
difference_value = set_a.difference(set_b)
print(difference_value)
