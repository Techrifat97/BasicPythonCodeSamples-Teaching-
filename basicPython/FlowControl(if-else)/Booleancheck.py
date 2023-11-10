temperature = 28
day = "saturday"
raining = True
if day == "saturday" and temperature > 27 and not raining:
    print("GO swimming")
else:
    print("Learn python")

print("-" * 80)

if (day == "saturday" and temperature > 27) or not raining:
    print("GO swimming")
else:
    print("Learn python")
print(type(raining))
