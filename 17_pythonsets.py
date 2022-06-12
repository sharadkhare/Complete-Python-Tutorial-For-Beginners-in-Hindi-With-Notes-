# what are sets (unordered, unchangable, unindexed)
x = {"apple", "banana","cherry" }
print(x)

#duplicate not allowed
x = {"a", "b", "c", "a"}
print(x)

#get the length of the Set
sharad = {"apple","banana", "cherry"}
print(len(sharad))

# How to checK the Data types of Set
set1 = {"a", "b", "c"}
set2 = {1,5,9,7,6}
set3 = {True, False, True}
print(type(set1))
print(type(set2))
print(type(set3))

# A set with string , integer and Boolean means all data types
set1 = {"abc", 35, True, 40, "male" }
print(set1)

# the Set() Constructor
thisset = set(("a", "b", "c"))
print(thisset)

# How to Access Items in set through looping
sharad = {"a", "b", "c"}
for i in sharad:
    print(i)

# check if banana is present or not
sharad = {"apple", "banana", "mango"}
print("banana" in sharad)

# Adding set items
sharad = {"apple", "banana", "mango"}
sharad.add("orange")
print(sharad)

# how to add items from another set into the current set
sharad = {"apple", "banana", "cherry"}
sanjay = {"pineapple", "mango", "papaya"}
sharad.update(sanjay)
print(sharad)

# How to remove set items
sharad = {"red" , "blue", "green"}
sharad.remove("blue")
print(sharad)

# how to use discard() for removing the items in set
sharad = {"red" , "blue", "green"}
sharad.discard("red")
print(sharad)

# remove the last item by using the pop() method will raise the error or you will get the wrong output.

sharad = {"black" , "pink", "orange"}
x = sharad.pop()
print(x)
print(sharad)

# the clear() method is used for empty the set
sharad = {"red" , "blue", "green"}
sharad.clear()
print(sharad)

# the Del keyword is used to delete the set completly
sharad = {"red" , "blue", "green"}
del sharad

# How to loop through the set
sharad = {"watermelon", "orange", "black"}
for i in sharad:
    print(i)

# how to join the two sets by union()
set1 = {"red" , "blue", "green"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# how to join the two sets by update()
set1 = {"red" , "blue", "green"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# keep only duplicate items intersection_update()
x = {"apple", "banana","cherry"}
y = {"google", "sharad", "banana"}
x.intersection_update(y)
print(x)

# intersection method with return a new set for common or duplicate items
x = {"apple", "banana","cherry"}
y = {"google", "sharad", "banana"}
z = x.intersection(y)
print(z)

# Keep all , but NOT the Duplicate or common items
x = {"apple", "banana","cherry"}
y = {"google", "sharad", "banana"}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() method will return a new set that contain only the elements that are NOT present in Both sets
x = {"apple", "banana","cherry"}
y = {"google", "sharad", "banana"}
z = x.symmetric_difference(y)
print(z)

# All python Built in Set Methods
# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# pop()
# remove()
# union()
# update()
# symmetric_difference()
# symmetric_difference_update()


