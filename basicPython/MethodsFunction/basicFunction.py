def line_gaps():
    print("\n")
    print("*" * 50)
    print("\n")

#basic priniting using function
def name_print(name):
    print(f"Hi {name}")
    
myName =input("what is your name?: ")
name_print(myName)

line_gaps()

#basic addition using fucntion with return
def add_values(num1, num2):
    sum_value = num1 + num2
    
    return sum_value

num1 = int(input("First value for add: "))
num2 = int(input("2nd value for add: "))

result = add_values(num1, num2)
print(result)