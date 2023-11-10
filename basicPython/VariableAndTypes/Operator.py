a = 12 # 12, 3 are  also expression  they are technical expression a and b also expression but not in the first two line because left of assignment operator can not be an expression
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # 4.0
print(a // b)  # rounded down a value no float number
print(a % b)

print()

for i in range(1, 4):
    print(i)

# for i in range(1, a / b):   always give error as single forward slash will provide a result with float number so the loop in case will not work  TO solve this we need to use two forward slash
#     print(i)

for i in range(1, a // b):  # here 1 and  a//b is also expression
    print(i)
