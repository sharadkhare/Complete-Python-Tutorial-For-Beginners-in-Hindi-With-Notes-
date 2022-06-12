#BUilt-in Data Types

'''Text type : str
Numeric types: int, float, complex
Sequence Type: List , Tuple, range
mapping: dict
set type: set, frozenset
boolean type: bool
Binary type: bytes, bytearray, memoryview'''

x=5
y="sharad"

print(type(y))

x = "sharad khare" #str
x = 20 #int
x=20.5 #float
x = 1j #complex
x = ["sharad", "khare"] #List
x = ("sharad", "Khare") #tuple
x = range(5) #range
x = {"name" : "sharad", "age" : "50"} #dict
x = {"apple", "banana", "orange"} #set
x = True #bool
x = b"sharad" #bytes 
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview

#Setting out the specific Data Type

x = str("Sharad Khare")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("orange", "sdsdsd"))
x = tuple(("apple", "banana"))
x = range(5)
x = dict(name="sharad", age=36)
x = set(("apple", "nanana"))
x = frozenset(("apple", "sharad"))
x = bool(12)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
