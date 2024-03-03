#basic tuple unpacking
stockPrice = [('gp', 110), ('robi', 90), ('airtel', 85)]

for item, item2 in stockPrice:
    print(item,item2)
    

work_hours = [('Prince', 100), ('Amy', 200), ('Esteben', 500)] #list of tuples

def most_hardworking_employee(work_hours):
    current_hours = 0
    em_name = " "
    for name, hours in work_hours:
        if hours > current_hours :
            current_hours = hours
            em_name = name
        else:
            pass
    return (em_name, current_hours)

name, hours = most_hardworking_employee(work_hours)
print(name, hours)
            
