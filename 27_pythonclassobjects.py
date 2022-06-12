# create a class
class myclass:
    x = 5
print(myclass)

# create object
class myclass:
    x = 5
p1 = myclass()
print(p1.x)

# The_init_() function
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("sharad", 36)

print(p1.name)
print(p1.age)

# Object method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print ("Hello everyone my name is " + self.name)

p1 = person("sharad", 36)
p1.myfunc()

# the self parameter
class person:
    def __init__(sharadobject, name, age):
        sharadobject.name = name
        sharadobject.age = age
    def myfunc(abc):
        print("hello everyone my name is " + abc.name)
p1 = person("sharad", 36)
p1.myfunc()

# How to modify object properties.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("hello everyone my name is " + self.name)
    
p1 = person("sharad", 36)
p1.age = 40
print(p1.age)


# Delete Object properties
class person:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello everyone my name is " + self.name)
p1 = person("sharad", 36)
del p1.age
print(p1.name)

# how to delete object
class person:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello everyone my name is " + self.name)
p1 = person("sharad", 36)
del p1

# the pass statement
class person:
    pass