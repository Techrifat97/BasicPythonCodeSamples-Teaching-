age = 24
print("my age is " + str(age) + " years old")  # This is old format
print()
print("my age is {0} years old".format(age))  # this is called string format
print()
print("There are {0} days in {1}, {2} ,{3} , {4} and {5}"
      .format(31, 'jan', 'mar', 'may', 'jul', 'aug'))
print()

print("jan: {2}, feb:{0}, march:{2}, april:{1}, may:{2}, june:{1}, july:{2}"
      .format(28, 30, 31))
print()
print("""Jan:  {2}
Feb:  {0}
Mar: {2}
Apr:  {1}
May: {2}
Jun:  {1}
Jul:   {2}
""".format(28, 30, 31))
