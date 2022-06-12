# What is a Module?
# Consider a module to be as same as a code library like a file containing a set of functions you want to nlcude in a application.

# Create a module.
import imp
import mymodule
mymodule.greeting("Sharad")

# Variables in Module
# a Module can contain functions but also variables of all types.

import mymodule1
a = mymodule1.person1["age"]
print(a)

# Naming and re-naming a Module with as keyword
import mymodule1 as mx
a = mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)

# using th dir() function
import platform
x = dir(platform)
print(x)

# Import from module - you can choose to import only parts of a module by from keyword

from mymodule2 import person1
print(person1["age"]) 
# do not write like 
#"x = mymodule2.person1["age"]