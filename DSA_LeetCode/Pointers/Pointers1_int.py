num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

# id() gives us the address where num1 and num2 are stored
print("\nnum1 points to: ", id(num1))
print("num2 points to: ", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

# id() gives us the address where num1 and num2 are stored
print("\nnum1 points to: ", id(num1))
print("num2 points to: ", id(num2))


