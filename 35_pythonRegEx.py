# RegEx - Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx Module

import re
txt = "the rain is falling in india"
x = re.search("^the.*india$", txt)
if x:
    print("Yes, match is true")
else:
    print("no match")

# regex functions
# findall()
# search()
# split()
# sub()

# Metacharacters
# \d - escape charaters
# . - any character(except newline character)
# ^ - start with
# $ - ends with
# * - zero or more occurance
# + - one or more occurance
# ? - zero or one occurance
# {} - Exactly the specified number of occurance
# | - Either or
# () - capture and group


# the findall() function
import re
txt = "the rain in spain"
x = re.findall("in", txt)
print(x)

# if in findall no condition is given than it will show empty list.
import re
txt = "the rain in spain"
x = re.findall("india", txt)
print(x)

# the search() function
import re
txt = "the rain in spain"
x = re.search("\s", txt)
print("white space is located in ", x.start())

# when nothing found in search() function
import re
txt = "the rain in spain"
x = re.search("india", txt)
print(x)

# the split() function

import re
import re
txt = "the rain in spain"
x = re.split("\s", txt)
print(x)

# you can control the number of occurance by specifying the maxsplit parameter.
import re
txt = "the rain in spain"
x = re.split("\s", txt, 1)
print(x)

# the sub() function - replaces the matches with the text of your choise.
import re
txt = "the rain in spain"
x = re.sub("\s", "5", txt)
print(x)

# you can control the number of replacement by specifying the count parameter.
import re
txt = "the rain in spain"
x = re.sub("\s", "5", txt, 2)
print(x)

# Match Object
import re
txt = "the rain in spain"
x = re.search("in", txt)
print(x)


