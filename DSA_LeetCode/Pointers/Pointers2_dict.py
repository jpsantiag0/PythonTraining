dict1 = {
    'value': 11
}

dict2 = dict1

print("Before dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

# id() gives us the address where dict1 and dict2 are stored
print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

dict2['value'] = 22

print("\nAfter dict2 value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

# id() gives us the address where num1 and num2 are stored
print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))