# Creating an initial list
my_list = [1, 2, 3, 'hello', 4.5]

# Adding elements
my_list.append(4)  # Adds 4 to the end of the list
my_list.insert(1, 'new')  # Inserts 'new' at index 1

# Removing elements
my_list.remove('hello')  # Removes the first occurrence of 'hello'
del my_list[1]  # Deletes the element at index 1

# Other useful list functions
popped_item = my_list.pop()# Removes and returns the last item in the list
print(popped_item)
another_list = [6, 7]
my_list.extend(another_list)  # Extends my_list with another_list

count = my_list.count(4)  # Counts how many times 4 appears in the list
#index_of_new = my_list.index('new')  # Finds the index of 'new'

my_list.clear()  # Removes all elements from my_list
copied_list = my_list.copy()  # Creates a shallow copy of my_list
