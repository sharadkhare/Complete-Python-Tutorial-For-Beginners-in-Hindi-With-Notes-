# file handling - open()
f = open("demofile.txt")
# or
f = open("demofile.txt", "rt")

# there are 4 different modes of opening file
#"r", "a", "w", "x"

# to open the file using built in open() and read()
f = open("demofile.txt", "r")
print(f.read())

# open a file in different location
f = open("S:\Tutorial Sharad Khare\Sharad Khare Python tutorial in hindi\demofile.txt", "r")
print(f.read())

# read only parts of the file
f = open("S:\Tutorial Sharad Khare\Sharad Khare Python tutorial in hindi\demofile.txt", "r")
print(f.read(7))

# how to read lines
f = open("S:\Tutorial Sharad Khare\Sharad Khare Python tutorial in hindi\demofile.txt", "r")
print(f.readline())
print(f.readline()) 

# looping through the line by line:
f = open("S:\Tutorial Sharad Khare\Sharad Khare Python tutorial in hindi\demofile.txt", "r")
for i in f:
    print(i)

# How to close the open file
f = open("S:\Tutorial Sharad Khare\Sharad Khare Python tutorial in hindi\demofile.txt", "r")
print(f.readline())
f.close()
