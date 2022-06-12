class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

x = person("sharad", "khare")
x.printname()

# Creating a Child Class
class student(person):
    pass
# testing the student class
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    pass
x = student("sharad", "kharenew")
x.printname()

# Adding __init__() function

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)
x = student("sharad", "khare")
x.printname()

# using the super() function
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = student("sharad", "kharenew1")
x.printname()

# How to add the properties
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2022
x = student("sharad", "khare")
print(x.graduationyear)

# you can pass the object property in student directly
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = student("sharad", "khare", "2021")
print(x.graduationyear)
