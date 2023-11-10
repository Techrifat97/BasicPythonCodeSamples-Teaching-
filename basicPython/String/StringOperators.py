# String has three sequence types built in :
# 1. string type
# 2.  list
# 3. tuple
# 4. range // can not be concatenated multiply
# 5. bytes and bytearray

string1 = 'he\'s '
string2 = 'probably '
string3 = 'pining '
string4 = 'for the '
string5 = 'fjords'

print(string1 + string2 + string3 + string4 + string5)  # Concatenation

print("he's " "probably " "pining " "for the " "fjords")

print("hello " * 5)
print("hello " * (5 + 4))
print("hello " * 5 + "4")

today = "friday"
print("fri" in today)
print("day" in today)
print("parrot" in today)
