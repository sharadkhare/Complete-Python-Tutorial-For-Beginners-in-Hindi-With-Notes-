# Arrays are used to store multiple values in one single variables.
cars = ["ford", "valvo", "bmw"]
print(cars)

# Accessing the elements of an arrays
cars = ["ford", "valvo", "bmw"]
x = cars[1]
print(x)

# modifying the values of arrays
cars = ["ford", "valvo", "bmw"]
cars[0] = "Toyota"
print(cars)

# length of an array
cars = ["ford", "valvo", "bmw"]
x = len(cars)
print(x)

# looping an array elements

cars = ["ford", "valvo", "bmw"]
for i in cars:
    print(i)

# adding arrays elements
cars = ["ford", "valvo", "bmw"]
cars.append("Honda")
print(cars)

# removing an array elements
cars = ["ford", "valvo", "bmw"]
cars.pop(1)
print(cars)

# another remove function for removing
cars = ["ford", "valvo", "bmw"]
cars.remove("valvo")
print(cars)

# all types of arrays methods
# append()
# clear()
# copy()
# count()
# extend()
# index()
# pop()
# remove()