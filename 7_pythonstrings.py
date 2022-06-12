x = "sharad"
y = 'sharad'
print(x)
print(y)

# Single Line String
x = "Sharad"

#Multiline String

z = '''Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows'''
print(z)

#strings are Arrays

a = "Sharad Khare"
print(a[1])

#Looping through the string
for x in "banana":
    print(x)

#String Length
a = '''Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements!'''
print(len(a))

#Check String
txt = "In this tutorial everything is free"
print("free" in txt)

#Check String with If for user friendly"
txt = "In this tutorial everything is free"
if "free" in txt:
    print("Yes, 'free' is present.")
#check if "free is not present"
txt = "In this tutorial everything is free"
print("sharad" not in txt)

# print only if "sharad" is not present

txt = "In this tutorial everything is free"
if "sharad" not in txt:
    print("No, 'sharad' is Not Present")
