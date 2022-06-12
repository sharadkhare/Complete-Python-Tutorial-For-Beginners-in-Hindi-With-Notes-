print("hello this is sharad khare")

# creating and calling a function
def my_function():
    print("hello this is  new sharad khare")

my_function()

# Definiation of Arguments (args) - arguments are specified after the function name and inside the parentheses.
def my_function(fname):
    print(fname + " Khare")
my_function("Sharad")
my_function("Sanjay")
my_function("dilip")

# number of arguments - 2 args
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("sharad", "khare")

# Arbitrary Arguments, *args
def my_functions(*kids):
    print("The youngest child is " + kids[2])
my_functions("chintu", "mintu", "pinku")

# Keyword Arguments key=value
def my_function(child1, child2, child3):
    print("The youngest child is " + child3)
my_function(child3="chintu", child1="mintu", child2="pinku")

# Arbitrary keyword arguments **kwargs

def my_function(**kids):
    print("His last name is  " + kids["lname"])
my_function(fname = "sharad", lname = "khare")

# Default parameter value
def my_function(country = "india"):
    print(" I am from " + country)
my_function("Canada")
my_function("UK")
my_function()
my_function("Australia")


# passing a list as an argument
def my_function(food):
    for i in food:
        print(i)
fruits= ["apple" , "banana", "cherry"]
my_function(fruits)

#Return values - To let a function return a value then you use return statement
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# the pass statement
def my_function():
    pass 