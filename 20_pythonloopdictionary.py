# loop through the dictionary
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
for i in sharad:
    print(i)

# with looping print all the values in the dictionary, one by one
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
for i in sharad:
    print(sharad[i])

# Values() method to return values of a dict.
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
for i in sharad.values():
    print(i)

# keys() method to return the key of the dict.
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
for i in sharad.keys():
    print(i)

# Now loop through both the keys and values , by using the items() method.
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
for i, y in sharad.items():
    print(i, y)

# How to copy the dict.
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
sharad1 = sharad.copy()
print(sharad1)

# another way to make a copy is to use dict().built in function
sharad = {
    "brand":"ford",
    "model":"xyz",
    "year":"2020"
}
sharad1 = dict(sharad)
print(sharad1)

# Nested dictionary, a dict can able to contain another dict.

myfamily = {
    "child1" : {
        "name": "ram", 
        "year": "10"
    },
    "child2": {
        "name": "laxman",
        "year": "8"
    }, 
    "child3": {
        "name": "bharat",
        "year": "6"

    }
}
print(myfamily)

# if you want to add 3 dict into a new dict.

child1 = {
        "name": "ram", 
        "year": "10"
    },
child2 = {
        "name": "laxman",
        "year": "8"
    }, 
child3 = {
        "name": "bharat",
        "year": "6"

    }
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

# python dictionary methods()
# clear()
# copy()
# get()
# items()
# keys()
# fromkeys()
# pop()
# popitem()
# update()
# values()
# setdefault


