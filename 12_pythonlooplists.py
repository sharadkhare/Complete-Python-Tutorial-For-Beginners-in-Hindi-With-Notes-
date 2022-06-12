# loop through list

list = ["sharad", "banana", "orange"]
for i in list:
    print(i)

# Loop through the index number
list = ["sharad", "banana", "orange"]
for i in range(len(list)):
    print(list[i])

# using a while loop
list = ["sharad", "banana", "orange"]
i = 0
while i < len(list):
    print(list[i])
    i = i+1

# Looping using list Comprehension
list = ["sharad", "banana", "orange"]
[print(i) for i in list]

# list Comprehension

fruits = ["sharad", "banana", "orange", "cherry", "mango", "kiwi"]
newlist = []
for i in fruits:
    if "e" in i:
        newlist.append(i)
print(newlist)

# list Comprehension in 1 line code
fruits = ["sharad", "banana", "orange", "cherry", "mango", "kiwi"]
newlist = [i for i in fruits if "e" in i]
print(newlist)

