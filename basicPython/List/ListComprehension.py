# Creating a list of squares for numbers from 0 to 9
squares = [x**2 for x in range(10)]
# squares will be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Creating a list of even numbers using a conditional
evens = [x for x in range(10) if x % 2 == 0]
# evens will be [0, 2, 4, 6, 8]

# Combining multiple for loops
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# pairs will be [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(pairs)
# Using list comprehension with functions
import math
roots = [math.sqrt(n) for n in range(5)]
# roots will be [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0]

