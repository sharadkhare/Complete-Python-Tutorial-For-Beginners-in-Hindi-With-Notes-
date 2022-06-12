# try - block let you test a block of code for error.
# except - block lets you handle the error
# else - block lets you execute the code when there is no error.
# finally - block lets you ececute the code regardless of the result of try and except block.

# example of try block
try:
    print(x)
except:
    print("an error occoured")

# if try and except is not given
print(x)

# many exceptions -  you can even define many exception blocks
try:
    print(x)
except NameError:
    print("variable of x is not defined")
except:
    print("something else went wrong")

# else - you can use the else keyword to define a block of code to be executed if no error.
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

# finally - 

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try' except is finished")

# example
try:
    f = open("demofile.txt")
    try:
        f.write("sharad khare")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")

# Raise an exceptionx = -1
if x < 0:
    raise Exception("sorry, no number is below 0")

# raise a typeerror if x is not a n integer
x = "sharad"
if not type(x) is int:
    raise TypeError("only integer are allowed")
