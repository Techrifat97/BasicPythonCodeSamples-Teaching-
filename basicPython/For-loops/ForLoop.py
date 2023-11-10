from typing import List

parrot = "1234s567h099a98o99n"
name = ""
for char in parrot:
    if not char.isnumeric():
        name = name + char
print(name)
print("-" * 100)

for i in range(1, 10):
    print(i)

print("-" * 100)
parrot = "Norwegian Blue"
name = ""
for char in parrot:
    if not char == " ":
        name = name + char
print(name)
