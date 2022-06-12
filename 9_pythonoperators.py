# Arithmetic Operators
# Assignment operators
# Comparison Operators
# Logical Operators
# Identity Operators
# membership Operators
# Bitwise Operators

# Arithmetic Operators

x = 10
y = 5
print(x+y)

x = 10
y = 5
print(x-y)

x = 10
y = 5
print(x*y)

x = 10
y = 5
print(x/y)

x = 10
y = 5
print(x%y)

x = 10
y = 5
print(x ** y) # same as 10*10*10*10*10 

# Assignment operators

# x=5
# x=x+5 same as x+=5
# x=x-3 same as x-=3
# x=x*3 same as x*=3
# x=x/3 same as x/=3
# x=x%3 same as x%=3
# x=x**3 same as x**=3

x = 5
x*=3
print(x)


# Comparison Operators

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y)

x = 5
y = 3
print(x >= y)

x = 5
y = 3
print(x <= y)

# Logical Operators

x = 5
print(x>3 and x<10)

x = 5
print(x>3 or x<4)

x = 5
print(not(x>3 and x<10))

# Identity Operators

x = ["sharad", "khare"]
y = ["sharad", "khare"]
z = x

print(x is z) # returns true because z is the same object as x.

print(x is y)
#return false because x is not the same object as y even if they have the same content.

print(x == y)
# to demonstrate the difference between "is" and "==" . this comparison returns True because x is equal to y. 


# membership Operators

x = ["apple" , "banana", "laddu", "peda"]
print("banana" in x)

x = ["apple" , "banana", "laddu", "peda"]
print("basdsfd" in x)

x = ["apple" , "banana", "laddu", "peda"]
print("pineapple" not in x)

x = ["apple" , "banana", "laddu", "peda"]
print("banana" not in x)



