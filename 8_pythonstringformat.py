#wrong method (Dont do it)
'''age = 50
txt = "My age is " + age
print(txt)'''

#use format method for concatenation
age = 50
txt = "My age is {}"
print(txt.format(age))

#format unlimited arguments
qty = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item number {} for price {} Rupees."
print(myorder.format(qty, itemno, price))

#format unlimited arguments with Indexing

qty = 3
itemno = 567
price = 49.95
myorder = "I want pay {2} Rupees for {0} pieces of item number {1}."
print(myorder.format(qty, itemno, price))
