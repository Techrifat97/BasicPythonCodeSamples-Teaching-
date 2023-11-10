#   Slicing in string
#               01234567890123
parrot = "Norwegian Blue"
print(parrot[:])
print(parrot[:9])
print(parrot[10:])
print(parrot[0:6])
print(parrot[5:10])
print()
# Negative slicing in string for negative indexing will start from -1 and from the right side
print(parrot[-4: -2])
print(parrot[-4: 12])

print()
print(parrot[-14:-5])
print(parrot[-4:])
print(parrot[-14: 6])
print(parrot[-9:9])
print()

# step in slice
print(parrot[0: 6: 2])  # NRE
print(parrot[0: 6: 3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
values = "".join(char if char not in number else " " for char in number).split()
print([int(val) for val in values])



