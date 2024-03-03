# Numeric types
integer_variable = 10  # int
float_variable = 3.14  # float

# Sequence types
string_variable = "Hello, World!"  # str
list_variable = [1, 2, 3]  # list
tuple_variable = (4, 5, 6)  # tuple

# Set types
set_variable = {1, 2, 3}  # set
frozenset_variable = frozenset({4, 5, 6})  # frozenset

# Mapping type
dictionary_variable = {"key1": "value1", "key2": "value2"}  # dict

# Boolean type
boolean_variable = True  # bool

# None type
none_variable = None  # None

# Binary types
bytes_variable = b'binary data'  # bytes
bytearray_variable = bytearray([0, 1, 2])  # bytearray
memoryview_variable = memoryview(b'abc')  # memoryview

# Iterator (example using a list)
iterator_variable = iter([7, 8, 9])  # iterator

# File (example of reading from a file)
with open('example.txt', 'r') as file:
    file_content = file.read()

# Class (example class definition)
class MyClass:
    def __init__(self, value):
        self.value = value

# Exception (example using a try-except block)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

