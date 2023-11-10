letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[
      25:0:-1])  # This will start from position 25 and reverse back to position as there is negative step value -1  and not including the position 0

print(letters[25::-1])  # this will include position 0

print(letters[25:: -2])

print(letters[10:: -3])

print(letters[16:13:-1])

print(letters[4:: -1])

print(letters[25:17:-1])
print(letters[:-9:-1])

# String reverse

print(letters[-4:])  # for last 4 items of a string
print(letters[-1:])  # for last item
print(letters[:1])  # for first item
print(letters[0])  # for first item  but if the string is empty it will crash
