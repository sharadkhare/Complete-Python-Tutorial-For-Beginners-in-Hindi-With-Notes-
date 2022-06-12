# python conditions and if statement
# Equal a == b
# Not eqaul a != b
# less than a < b
# Less than or equal to a <= b
# Greater than a > b
# Greater than or equal to a >= b 

#example of if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

# the Elif keyword is python way of saying" if the previous condition is not true than please try the new condition

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are same")

# else catches anything which isn't cought by any preceeding condition.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are same")
else:
    print("a is greater than b")

# you can also have an else without the elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("now b is not greater than a") 

# short hand if
a = 200
b = 33
if a > b: print("a is greater than b")

# short hand if...else
a = 2
b = 300
print("yes a is greater than b") if a > b else print("no it is not greater")

# one line if else statement with 3 conditions
a = 100
b = 100
print("A") if a > b else print("both are equal") if a == b else print("B")

# And is a logical operator and it is used to combine the conditional statement.
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both the conditions are true")

# or is also a logical operator and it is used to combine logical statement.

a = 200
b = 33
c = 500
if a > b or a > c:
    print("at least one of the 2 condition is true")

# nested if statement - you can have if statement inside if statement. (Very important/must read)
x = 41
if x > 10:
    print("it is above 10, ")
    if x > 20:
        print("and it is also above 20")
    else:
        print("but it is bot above 20")

# the pass statement - if with any reason if  statement has no content than you can pass the stement for avoiding the error in program

a = 33
b = 200
if b > a:
    pass