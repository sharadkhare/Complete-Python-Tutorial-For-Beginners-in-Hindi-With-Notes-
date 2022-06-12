# Append()
x = ["apple", "banana", "orange"]
x.append("cherry")
print(x)

#Insert()
x = ["apple", "banana", "orange"]
x.insert(1, "cherry")
print(x)

# Extend()
x = ["apple", "banana", "orange"]
y = ["mango", "pineapple", "papaya"]
x.extend(y)
print(x)

# Remove List Items
x = ["apple", "banana", "orange"]
x.remove("banana")
print(x)

# Remove Specified Index
x = ["apple", "banana", "orange"]
x.pop(1)
print(x)

# remove Last Index without knowing the length
x = ["apple", "banana", "orange"]
x.pop()
print(x)

# Using Del for specified index
x = ["apple", "banana", "orange"]
del x[0]
print(x)

# Deleting the list completely
x = ["apple", "banana", "orange"]
del x

# Clear the List method
x = ["apple", "banana", "orange"]
x.clear()
print(x)

