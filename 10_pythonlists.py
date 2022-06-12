from pickle import FALSE, TRUE


x = ["apple", "banana", "orange"]
print(x)

#duplicate values

x = ["apple", "banana", "orange", "apple"]
print(x)

#list length
x = ["apple", "banana", "orange"]
print(len(x))

#list items - Data Types

x = ["a", "b", "c"]
y = [1, 4, 5, 7, 9]
Z = [TRUE, FALSE, TRUE]

# A list with strings, int and boolean
x = ["sharad", 35, True, 50, "Male"]
print(x)

# data type for Lists

# A list with strings, int and boolean
x = ["sharad", 35, True, 50, "Male"]
print(type(x))

#the List() Constructor
x = list(("sharad", 50, True, 50, "Male"))
print(x) # the double round brackets same as square brackets.

# Pythons Collecttions (Arrays)
# 4 types of data types in python :
# 1. List, 2. Tuple, 3. Set, 4. Dictionary

# How to Access items.
x = ["apple", "banana", "orange"]
print(x[1])

# Range of Indexes
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
print(x[2:5])

# Negative Indexing
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"] 
print(x[-6:-1])

# Leaving out the start value
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
print(x[:4])

# Leaving out the Ending value
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
print(x[1:])

# How to Check if the items Exists in List 
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
if "apple" in  x:
    print("Yes, 'apple' is in the List")

# Change the Item value of List
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
x[1] = "Watermelon"
print(x)

# Change a Range of Items values in List
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
x[1:3] = ["Watermelon", "Chiku"]
print(x)

# Change of one value by replacing it with 2 Values

x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
x[1:2] = ["Watermelon", "Nuts"]
print(x)

# Change of 2 values by replacing it with 1 value
x = ["apple", "banana", "orange", "cherry", "Mango", "sharad"]
x[1:3] = ["watermelon"]
print(x)