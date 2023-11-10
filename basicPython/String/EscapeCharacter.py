# BackSlash \n for new line
splitString = "This string is \nsplit in several \nparts"
print(splitString)

print("\n")
# Another way of splitString
splitString = """this is the way
you can split 
a string"""
print(splitString)

print("\n")
# Alternative happened if we use backslash after every line though we use three double qoutes
splitString = """this is the way \
you can split \
a string"""
print(splitString)

print("\n")
# BackSlash \t will create 4 character space
print("1\t 2\t 3\t 4")

print("\n")
# For using Single Quotes or double Quotes in a string there are a couple of way
print('"Hi my name is "Rifat ali shaon" and i am the elder son\'s of mozumder\'s family"')

print("Hey There are couple of way's you can add multiple\"s way to ah's in string")

print("""Hi i am going to use this'ssss thing's in my future code"s """)

print("\n")
# what will happen if we want to use backslash is our strings

print("C: \\Users \\timbuchka\\notes.txt")
print("Or we can use- " + r"C:\Users\tim\notes.txt")  # Raw String
