# What is Scope? - a variable is only available from inside the region it is created and this is called scope.

# what is local Scope
def myfunc():
    x = 300
    print(x)

myfunc()

# function inside function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# what is Global Scope
x = 300

def myfunc():
    print(x)

myfunc()

# naming variable - python will treat the 2 vaiable as a seperate variables. 

x = 3000

def sharad():
    x = 2000
    print(x)

sharad()
print(x)

# Global keyword - if you need to create a global variable locally then you should use global keyword.

def sharad():
    global x
    x = 30000
sharad()
print(x)

# you can also use the global keyword if you want to make a change to a global vaiable inside the function.

x = 500
def sharad():
    global x
    x = 200
sharad()

print(x)
