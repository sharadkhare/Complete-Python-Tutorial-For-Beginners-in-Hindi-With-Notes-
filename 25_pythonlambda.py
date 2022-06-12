# syntax lambda arguments : expression

x = lambda a: a + 10
print(x(5))

# lamda function can even take multiple arguments and return result.
x = lambda a, b: a * b
print(x(5, 6))

# 3 arguments in lambda function
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# why use lambda function

def myfunc(n):
    return lambda a: a * n
mydouble = myfunc(2)
print(mydouble(11))

# new function for double and triple
def myfunc(n):
    return lambda a: a * n
mydouble = myfunc(2)
mytriple = myfunc(3)

print(mydouble(11))
print(mytriple(11))