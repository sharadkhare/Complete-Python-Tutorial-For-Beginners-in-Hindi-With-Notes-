# how to change the values of the dictionary
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad["year"] = 2018
print(sharad)

# update() method
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad.update({"year": "2018"})
print(sharad)

# how to add the items in dictionary
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad["color"] = "red"
print(sharad)

# adding the items with update() method
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad.update({"color": "red"})
print(sharad)

# removing itens from the dictionary
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad.pop("model")
print(sharad)

# removing Last inserted item.
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad.popitem()
print(sharad)

# Del() keyword removes the items with the specified key name.
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
del sharad["model"]
print(sharad)

# the Del Keyword can also delete the whole dictionary
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
del sharad

# clear() method is used to empty the dictionary
sharad = {
    "brand": "ford",
    "model": "XYZ",
    "year": "2022"
}
sharad.clear()
print(sharad)