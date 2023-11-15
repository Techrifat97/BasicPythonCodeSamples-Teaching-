# Sets themselves are mutable, but elements must be immutable
# my_set.add([10, 11])  # Uncommenting this line will cause a TypeError

# Creating an empty set (cannot use {}, as it creates an empty dictionary)
empty_set = set()

# Creating a set with some elements
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list (automatically removes duplicates)
my_set_from_list = set([1, 2, 2, 3, 4])

# Adding an element to a set
my_set.add(6)

# Adding multiple elements (can also add sets)
my_set.update([7, 8, 9])

# Removing an element, raises KeyError if element not present
my_set.remove(3)

# Discarding an element, does not raise an error if element not present
my_set.discard(10)

# Removing and returning an arbitrary element, set should not be empty
popped_item = my_set.pop()

# Checking if an element is in the set
if 2 in my_set:
    print("2 is in the set")
# Other set operations
another_set = {4, 5, 6, 7}

# Union of two sets (elements in either set)
union_set = my_set.union(another_set)

# Intersection (elements common to both sets)
intersection_set = my_set.intersection(another_set)

# Difference (elements in my_set but not in another_set)
difference_set = my_set.difference(another_set)

# Symmetric difference (elements in either set, but not in both)
symmetric_difference_set = my_set.symmetric_difference(another_set)

# Getting the number of elements in a set
length = len(my_set)

# Iterating over set elements
for item in my_set:
    print(item)
