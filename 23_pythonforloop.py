# print each items of variable in list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# looping through string
for i in "banana":
    print(i)

# the break statement
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
    if i == "banana":
        break

# exit the loop when i is "banana", but this time the break comes before print.
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    print(i)

# the continue statement

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        continue
    print(i)

# the range() function
for i in range(6):
    print(i)

# example of some deep range()
for i in range(2, 6):
    print(i)

# you can specify value of increment by adding the 3rd parameter.

for i in range(2, 30, 3):
    print(i)

# Else in for loop
for i in range(6):
    print(i)
else:
    print("yeei, Finally it finished")

# now we will break the loop i in 3 and the else will be garbage now.
for i in range(6):
    if i == 3: break
    print(i)
else:
    print("finally finished")

# nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for y in fruits:
        print(i, y)

# the pass statement
for i in [0, 1, 2]:
    pass

