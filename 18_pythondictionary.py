# defination of Dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
print(sharad)

# if you want to print "brand" value from the dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
print(sharad["brand"])

# Duplicate not allowed
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "year": 2022
}
print(sharad)

# How to find dictionary length
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "year": 2022
}
print(len(sharad))

# dictionary items - Data type
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "color": ["red", "white", "blue"]
}
print(sharad)

# how to know the Type of Function
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "color": ["red", "white", "blue"]
}
print(type(sharad))

# accessing items of Dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "color": ["red", "white", "blue"]
}
x = sharad["model"]
print(x)

# Accessing items of dictionary through get()
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "color": ["red", "white", "blue"]
}
x =sharad.get("model")
print(x)

# key() methods will return all the keys in the dictionary.
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020, 
    "color": ["red", "white", "blue"]
}
x = sharad.keys()
print(x)

# adding  keys and values items to the original dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
x = sharad.keys()
print(x) # before the change
sharad["color"] = "white"
print(x) # after the change

# How to get the values of dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
x = sharad.values()
print(x)

# adding  values and keys items to the original dictionary
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
x = sharad.values()
print(x) # before the change
sharad["color"] = "red"
print(x) # after the change

# How to Get each items in a dictionary as tuples in the list
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
x = sharad.items()
print(x)

# check if the key exists
sharad = {
    "brand":"ford", 
    "model":"DT", 
    "year": 2020
}
if "model" in sharad:
    print("Yes, 'model' is present in the sharad")