# Parenthesis  , Exponents , Division / Multiplication , addition / subtraction
# Multiplication and division have same priority or precedence
# addition and subtraction has also same priority or precedence
# So for same priority we should use left to right pattern

a = 12
b = 3

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print(((a + b) / 3 - 4) * 12)

print(a / (b * a) / b)  # division is always done  by the rules where value end of forward slash consider as divisor and back of the slash consider as dividend
# from where we start consider as the left point and start left to right precedence pattern, and then we will continue
print(2 + 2**3)