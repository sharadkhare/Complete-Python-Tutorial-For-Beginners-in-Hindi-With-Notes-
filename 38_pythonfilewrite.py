# 2 modes for writing in the file
# "a", "w"

f = open("demofile.txt", "a")
f.write("Now this file has one more content")
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

# 1st open the file and overwrite the content.
f = open("demofile.txt", "w")
f.write("yes, finally now we have overwritten the content")
f.close()

# open and read the file after the appending
f = open("demofile.txt", "r")
print(f.read())

# Creating a new file
# "x" - create a file
# "a" - append a file
# "w" -  will write or create a file

f = open("myfile.txt", "x")

# how to delete a file
import os
os.remove("myfile.txt")

# check if the file exist and give the condition
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("the file does not exist")

# how to delete the existing folder
import os
os.rmdir("myfolder") # this command can only remove empty folder.