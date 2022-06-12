import kjdsjdksj as ns


x = 1
y = 2.5
z = 1j
print(type(x))
print(type(y))
print(type(z))

#int numeric type
x = 1
y = 45637821356454
z = -54678
print(type(x))
print(type(y))
print(type(z))

#Float or floating point number Data Type
x = 1.10
y = 1.0
z = -25.47
print(type(x))
print(type(y))
print(type(z))

#float can also be scientific numbers with an "e" = power of 10

x = 35e3
y = 12E4
z = -87.7e155
print(type(x))
print(type(y))
print(type(z))

#complex numbers are written with a "j" as the imaginary part.
x = 3+5j
y = 7j
z = -8j
print(type(x))
print(type(y))
print(type(z)) 

#Type Conversion

x = 1
y = 2.8
z = 1j

#convert from int to float
a = float(x)
print(a)

#convert from float to int
b = int(y)
print(b)

#convert from int to complex

c = complex(x)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number
import random
print(random.randrange(1, 10))

