# Sort the list alphabetically
from audioop import reverse


x = ["orange", "mango", "kiwi", "pineapple", "banana"]
x.sort()
print(x)

# Sort the list numerically
x = [100, 50, 65, 82, 23]
x.sort()
print(x)

# sorting the list in decending order
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
x.sort(reverse=True)
print(x) 

# sorting the list of numeric in decending order
x = [100, 50, 65, 82, 23]
x.sort(reverse=True)
print(x) 

# customize sort functions
def myfunc(n):
    return abs(n-50)
x = [100, 50, 65, 82, 23]
x.sort(key = myfunc)
print(x)

# reverse the sorting order
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
x.reverse()
print(x)


# How to Copy a list
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = x.copy()
print(y)

# make a copy of list with built in method
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = list(x)
print(y)

# Joining the List
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = [1, 2, 3, 4, 5]
z = x + y
print(z)

# another way of joining through append()
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = [1, 2, 3, 4, 5]

for i in y:
    x.append(i)
print(x)

# another way of joining through extend()
x = ["orange", "mango", "kiwi", "pineapple", "banana"]
y = [1, 2, 3, 4, 5]
x.extend(y)
print(x)

# List Methods
# append()
# clear()
# copy()
# Count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()