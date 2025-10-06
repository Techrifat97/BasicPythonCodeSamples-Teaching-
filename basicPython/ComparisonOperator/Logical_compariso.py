# simple logic and or not
# for example There are certian situtaion you will only do these task if two or more condition satisfied you will do the certain task

raining = False
wind = True

if raining and wind:
    print("will wear raincoat")
else:
    print("nice day!")

if raining and wind:
    print("need to wear raincoat")
elif raining and not wind:
    print("need take umbrela with you")
else:
    print("nice day!")

# or only we will use when if one condition satiafied

if raining or wind:
    print("will not go outside")
else:
    print("will go outside")

numbers = [1, 2, 4, 5, 7]

if 6 not in numbers:
    print("not available")
else:
    print("available")

# not also make a bolean value into oposite

print(not 2 > 4)  # it will print true the condition is not true just because of not
