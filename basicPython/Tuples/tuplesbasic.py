# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with mixed data types
my_tuple = (1, "hello", 3.14)

# Single element tuple (note the comma)
single_element_tuple = (2,)

# Accessing the first element (indexing starts at 0)
first_element = my_tuple[0]  # Outputs 1

# Accessing the last element (negative indexing)
last_element = my_tuple[-1]  # Outputs 3.14

# Slicing a tuple, getting elements from index 1 to 2
sliced = my_tuple[1:3]  # Outputs ('hello', 3.14)

# Finding the length of a tuple
length = len(my_tuple)  # Outputs 3

# Looping through tuple elements
for item in my_tuple:
    print(item)

# Concatenating tuples
concatenated = my_tuple + (5.6, 7)

# Repeating tuples
repeated = my_tuple * 2

# Checking if an item exists in a tuple
if "hello" in my_tuple:
    print("Yes, 'hello' is in the tuple")

# Trying to change an element (this will raise an error)
# my_tuple[0] = 2  # Uncommenting this line will cause TypeError

# Assigning tuple values to variables
a, b, c = my_tuple
print(a)  # Outputs 1
print(b)  # Outputs 'hello'
