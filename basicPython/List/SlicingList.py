# In list slicing first value means the start of the list
# second value means the stop of the list / stop value will not be print
# Third value means step

my_list = [0, 1, 2, 3, 4, 5]
sliced = my_list[1:4]  # This will be [1, 2, 3]

first_three = my_list[:3]  # This will be [0, 1, 2]
from_third = my_list[3:]  # This will be [3, 4, 5]

last_three = my_list[-3:]  # This will be [3, 4, 5]

every_other = my_list[::2]  # This will be [0, 2, 4]
reverse = my_list[::-1]     # Reverses the list, will be [5, 4, 3, 2, 1, 0]

reversed_slice = my_list[4:1:-1]  # This will be [4, 3, 2]

