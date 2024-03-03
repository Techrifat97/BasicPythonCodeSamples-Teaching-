# Creating a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
first_element_first_list = nested_list[0][0]  # Outputs 1
second_list = nested_list[1]                 # Outputs [4, 5, 6]

# Modifying elements
nested_list[2][1] = 10  # Changes 8 to 10 in the third list
