i = 2
j = 2
while i < 13195:
    if 13195 % i == 0:
        while j < i:
            if i % j == 0:
                continue
            else:
                print(i)
            j += 1
    i += 1
