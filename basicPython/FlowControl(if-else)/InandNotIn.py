demoString = "Norwegian Blue"
find = input("Enter character: ")
if find in demoString.casefold():
    print(f"Yes character {find} is in {demoString}")
else:
    print(f"Not in {demoString}")

print("-"*80)

activity = input("what do you want to do today?")

if "cinema" not in activity.casefold():
    print("I want to watch cinema")
else:
    print("Hurrah")
