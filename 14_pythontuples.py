x = ("sharad", "banana", "orange")
print(x)

# tuple Lenght
x = ("sharad", "banana", "orange")
print(len(x))

# Create tuple with one item
x = ("sharad",)
print(type(x))

# Not a tuple
x = ("sharad")
print(type(x))

# tuple items _ data type(String, int, boolean)
x = ("sharad", "banana", "orange")
y = (1, 2, 3, 4, 5)
z = (True, False, True)
print(x)
print(y)
print(z)

# tuple can also contain different data tye
x = ("sharad", 35, True, 50, "male")
print(x)

# the Tuple() constructor
sharad = tuple(("apple", "banana", "cherry"))
print(type(sharad))

# Access tuple Items
x = ("sharad", "banana", "orange")
print(x[1])

# access tuple items through negative indexing
x = ("sharad", "banana", "orange")
print(x[-1])

# access tuple items through range of indexes
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango")
print(x[2:5])

# access tuple items through range of indexes but some index not included.
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango")
print(x[2:])

# access tuple items through  negative range of indexes.
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango")
print(x[-4:-1])

# check if the item exists
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "khare")
if "orange" in x:
    print("Yes, 'orange' is in x")

# (Very Important) Changing of Tuple values.

x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "khare")
print(type(x))
y = list(x)
print(type(y))
y[1] = "python"
x = tuple(y)
print(x)
print(type(x))

# Add items in tuple(Very Important)
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "khare")
print(type(x))
y = list(x)
print(type(y))
y.append("lastvalue")
x = tuple(y)
print(x)

# Adding tuple to a tuple
x = ("apple", "orange", "banana")
y = ("cherry",)
x += y
print(x)

# Removing items from a tuple
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "khare")
print(type(x))
y = list(x)
print(type(y))
y.remove("khare")
x = tuple(y)
print(x)

# how to delete tuple
x = ("sharad", "banana", "orange", "cherry", "papaya", "kiwi", "mango", "melon", "nuts", "khare")
del x

# Packing a tuple (when we assign a values to tuple)
x = ("sharad", "khare", "banana")

# Unpacking the tuple (when we extract the value from the tuple)
x = ("sharad", "khare", "banana")
(green, yellow, red) = x

print(green)
print(yellow)
print(red)

# how to assign for the rest of the values in tuple
x = ("sharad", "khare", "banana", "cherry", "apple")
(green, yellow, *red) = x
print(green)
print(yellow)
print(red)