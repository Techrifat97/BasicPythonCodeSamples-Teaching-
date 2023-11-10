# In python, you can assign a value to a variable
# python use the variable name as a reference and  assign  a value which is given  by us
# When we create a variable python allocates memory for this variable
# a variable in other programming languages is called a name in Python.

Name = "Rifat Ali Shaon"  # assign a string value to the variable (variable are bound to value)
Age = 20  # assign a Int value to Age variable
print(Name, " ", Age)
# In python when assign a specific type of value to a variable we can only  do things that make sense for the type of value

# Python variable name must begin with a letter either upper case or lower case or an underscore_character
# Underscore character use for a purpose not to change the variable
# python variable are case-sensitive
# binding and unbinding
a = 10
b = 30
c = a
print(a, b, c) # object 10 have two names  a and c
a = b
print(a, b, c) # object 30 have two names and 10 have one name
# same thing happen if we do it for a list
a = [1, 2]
b = a
print(a, b)
a.append(3)
print(a)
print(b)
b.append(10)
print(a, b)
