# an iterator is an object which implements the iterators protocol, which consist of the 2 methods: __iter__() and __next__()

# iterators vs iterable
# all of the 4 data type i.e list, set, dictionary and tuples are iterators
# iterators methods

sharad = ("apple", "banana", "cherry")
isharad = iter(sharad)
print(next(isharad))
print(next(isharad))
print(next(isharad))

# a new example
sharad = "banana"
datacode = iter(sharad)
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))
print(next(datacode))

# looping through an iterator
sharad = ("apple", "banana", "cherry")
for i in sharad:
    print(i)

# looping through a string as iterate
sharad = "banana"
for i in sharad:
    print(i)

# Create an Iterators
# to create an object or class you will have to imlement __iter__() and __next__() to the object.
#all classes have a function which is called __init__(), which allows you to do some initialization.
# example for better understanding
class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# stopiteration - to prevent the iteration to go over forever, we use the stopiteration statement
class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = mynumber()
myiter = iter(myclass)
for i in myiter:
    print(i)