# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with some initial key-value pairs
my_dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}


# Accessing a value using its key
name = my_dict['name']  # Outputs 'Alice'

# Using get() method to access a value which is safer
age = my_dict.get('age')  # Outputs 25

# Adding a new key-value pair
my_dict['address'] = '123 Street Name'

# Modifying an existing key-value pair
my_dict['email'] = 'new_email@example.com'

# Removing a key-value pair using del
del my_dict['address']

# Removing a key-value pair and returning the value using pop()
removed_value = my_dict.pop('email')

# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print("Name is present in the dictionary")

# Getting the number of key-value pairs
length = len(my_dict)

# Creating a nested dictionary
nested_dict = {'dict1': {'key1': 1, 'key2': 2}, 'dict2': {'key3': 3, 'key4': 4}}
