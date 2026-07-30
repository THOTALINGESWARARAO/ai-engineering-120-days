"""
Day 5 — Python Data Model (Magic Methods)
"""

# ============================================================
# PART 1 — OBJECT CREATION PROTOCOL
# ============================================================

# 1. Class Call Triggers Object Creation

class Student:
    pass


student = Student()

print(student)
print(type(student))
print()

# Student()
#
#      │
#      ▼
#
# Create Object
#
#      │
#      ▼
#
# Return Student instance


# ------------------------------------------------------------

# 2. __new__ Executes Before __init__

class Demo:

    def __new__(cls):
        print("__new__ executed")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ executed")


obj = Demo()
print()

# Flow:
#
# Demo()
#
#    │
#    ▼
#
# __new__()
#
#    │
#    ▼
#
# __init__()
#
#    │
#    ▼
#
# Ready Object


# ------------------------------------------------------------

# 3. __new__ Creates the Object

class Sample:

    def __new__(cls):
        print("Creating object...")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object...")


s = Sample()

print()

# __new__()
#
# ↓
#
# Allocate Memory
#
# ↓
#
# Return Object


# ------------------------------------------------------------

# 4. __init__ Initializes Existing Object

class Person:

    def __init__(self, name):
        self.name = name


person = Person("Alice")

print(person.name)
print()

# Object before __init__
#
# ┌─────────────┐
# │ name : ?    │
# └─────────────┘
#
# Object after __init__
#
# ┌─────────────┐
# │ name: Alice │
# └─────────────┘


# ------------------------------------------------------------

# 5. cls vs self

class Employee:

    def __new__(cls):
        print("cls =", cls)
        return super().__new__(cls)

    def __init__(self):
        print("self =", self)


emp = Employee()

print()

# cls
#
# ↓
#
# Class Object
#
# self
#
# ↓
#
# Instance Object


# ============================================================
# PART 2 — OBJECT REPRESENTATION
# ============================================================

# 6. Default Representation

class Car:
    pass


car = Car()

print(car)
print(repr(car))
print()

# Without __str__() or __repr__()
#
# Python prints
#
# <__main__.Car object at ...>


# ------------------------------------------------------------

# 7. __str__()

class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"


book = Book("Python")

print(book)
print()

# print(book)
#
#      │
#      ▼
#
# book.__str__()
#
#      │
#      ▼
#
# Return String


# ------------------------------------------------------------

# 8. __repr__()

class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Laptop('{self.brand}')"


lap = Laptop("Dell")

print(repr(lap))
print()

# repr(obj)
#
#      │
#      ▼
#
# obj.__repr__()
#
#      │
#      ▼
#
# Developer Representation


# ------------------------------------------------------------

# 9. __str__ vs __repr__

class Mobile:

    def __str__(self):
        return "Readable Mobile"

    def __repr__(self):
        return "Developer Mobile"


m = Mobile()

print(str(m))
print(repr(m))
print()

# str()
#
# ↓
#
# __str__()
#
# repr()
#
# ↓
#
# __repr__()


# ------------------------------------------------------------

# 10. print() Uses __str__()

class Test:

    def __str__(self):
        print("__str__ called")
        return "Testing"


t = Test()

print(t)

print()

# print(object)
#
#      │
#      ▼
#
# __str__()
#
#      │
#      ▼
#
# Display Result

# ============================================================
# PART 3 — OBJECT COMPARISON PROTOCOL
# ============================================================

# 11. Default Equality Compares Object Identity

class Student:
    pass


s1 = Student()
s2 = Student()

print("s1 == s2 :", s1 == s2)
print("s1 is s2 :", s1 is s2)
print()

# Object Model
#
# s1 -----> Student Object A
#
# s2 -----> Student Object B
#
# Different objects
#
# Therefore:
#
# s1 == s2 -> False
# s1 is s2 -> False


# ------------------------------------------------------------

# 12. Two Names Can Refer To The Same Object

numbers = [10, 20, 30]

a = numbers
b = numbers

print("a == b :", a == b)
print("a is b :", a is b)

print()

# numbers
#      ▲
#      │
#   ┌──┴──┐
#   │     │
#   │     │
#   a     b
#
# Both names refer to the SAME object.


# ------------------------------------------------------------

# 13. == vs is

a = [1, 2]
b = [1, 2]

print("a == b :", a == b)
print("a is b :", a is b)

print()

# ==
#
# Compare values
#
# is
#
# Compare identity


# ------------------------------------------------------------

# 14. Custom Equality (__eq__)

class Employee:

    def __init__(self, eid):
        self.eid = eid

    def __eq__(self, other):
        return self.eid == other.eid


e1 = Employee(101)
e2 = Employee(101)
e3 = Employee(102)

print(e1 == e2)
print(e1 == e3)

print()

# Python internally
#
# e1 == e2
#
# ↓
#
# e1.__eq__(e2)


# ------------------------------------------------------------

# 15. __eq__ Receives Another Object

class Product:

    def __init__(self, pid):
        self.pid = pid

    def __eq__(self, other):
        print("self :", self.pid)
        print("other:", other.pid)

        return self.pid == other.pid


p1 = Product(1)
p2 = Product(1)

print(p1 == p2)

print()

# self
#
# ↓
#
# Left object
#
# other
#
# ↓
#
# Right object


# ============================================================
# PART 4 — CONTAINER PROTOCOL
# ============================================================

# 16. __len__()

class Basket:

    def __len__(self):
        return 5


basket = Basket()

print(len(basket))

print()

# len(basket)
#
# ↓
#
# basket.__len__()
#
# ↓
#
# 5


# ------------------------------------------------------------

# 17. __getitem__()

class Numbers:

    def __getitem__(self, index):
        values = [10, 20, 30]
        return values[index]


numbers = Numbers()

print(numbers[0])
print(numbers[1])
print(numbers[2])

print()

# numbers[1]
#
# ↓
#
# numbers.__getitem__(1)


# ------------------------------------------------------------

# 18. __setitem__()

class Scores:

    def __init__(self):
        self.data = [90, 80, 70]

    def __setitem__(self, index, value):
        self.data[index] = value


scores = Scores()

print(scores.data)

scores[1] = 100

print(scores.data)

print()

# scores[1] = 100
#
# ↓
#
# scores.__setitem__(1,100)


# ------------------------------------------------------------

# 19. __contains__()

class Fruits:

    def __contains__(self, item):
        return item in ["Apple", "Banana", "Orange"]


fruits = Fruits()

print("Apple" in fruits)
print("Mango" in fruits)

print()

# item in object
#
# ↓
#
# object.__contains__(item)


# ------------------------------------------------------------

# 20. Complete Container Example

class Inventory:

    def __init__(self):
        self.items = ["Mouse", "Keyboard", "Monitor"]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __contains__(self, item):
        return item in self.items


inventory = Inventory()

print("Length :", len(inventory))

print("Item 0 :", inventory[0])

inventory[0] = "Laptop"

print("Updated :", inventory[0])

print("Laptop" in inventory)

print()

# Object Model
#
# Inventory
#
# ┌──────────────────────────┐
# │ Mouse                    │
# │ Keyboard                 │
# │ Monitor                  │
# └──────────────────────────┘
#
# Supports:
#
# len()
# []
# [] =
# in
#
# through the Container Protocol.
# ============================================================
# PART 5 — ITERATOR PROTOCOL
# ============================================================

# 21. iter() Returns An Iterator

numbers = [10, 20, 30]

iterator = iter(numbers)

print("numbers:", numbers)
print("iterator:", iterator)

print("numbers type:", type(numbers))
print("iterator type:", type(iterator))

print()

# numbers
#
#      │
# iter()
#      │
#      ▼
#
# list_iterator


# ------------------------------------------------------------

# 22. Iterator Maintains State

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))

print()

# Iterator State
#
# Initially
#
# [10,20,30]
#  ^
#
# after first next()
#
# [10,20,30]
#      ^
#
# after second next()
#
# [10,20,30]
#          ^


# ------------------------------------------------------------

# 23. StopIteration

it = iter([1, 2])

print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration:
    print("Iterator Finished")

print()

# next()
#
# ↓
#
# Value
#
# ...
#
# ↓
#
# StopIteration


# ------------------------------------------------------------

# 24. Custom Iterator

class Counter:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        value = self.current

        self.current += 1

        return value


counter = Counter(3)

print(next(counter))
print(next(counter))
print(next(counter))

print()

# Counter
#
# current = 1
#
# ↓
#
# current = 2
#
# ↓
#
# current = 3
#
# ↓
#
# StopIteration


# ------------------------------------------------------------

# 25. iter(iterator) Returns Same Iterator

it = iter([10, 20, 30])

print(iter(it) is it)

print()

# Iterator
#
# iter(iterator)
#
# ↓
#
# Same Iterator


# ------------------------------------------------------------

# 26. Every Iterator Is Iterable

class SimpleIterator:

    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.value == 3:
            raise StopIteration

        self.value += 1

        return self.value


it = SimpleIterator()

for value in it:
    print(value)

print()

# for
#
# ↓
#
# iter(it)
#
# ↓
#
# Same iterator


# ------------------------------------------------------------

# 27. Manual Version Of for Loop

numbers = [100, 200, 300]

it = iter(numbers)

while True:

    try:

        value = next(it)

        print(value)

    except StopIteration:

        break

print()

# Conceptually
#
# iterator = iter(numbers)
#
# while True
#
#      value = next(iterator)
#
# until StopIteration


# ------------------------------------------------------------

# 28. for Loop Internally Uses Iterator Protocol

numbers = [10, 20, 30]

for number in numbers:
    print(number)

print()

# for numbers
#
# ↓
#
# iter(numbers)
#
# ↓
#
# next()
#
# ↓
#
# next()
#
# ↓
#
# next()
#
# ↓
#
# StopIteration


# ------------------------------------------------------------

# 29. Iterator Cannot Restart Automatically

it = iter([10, 20])

print(next(it))
print(next(it))

try:
    next(it)
except StopIteration:
    print("Iterator Exhausted")

try:
    next(it)
except StopIteration:
    print("Still Exhausted")

print()

# Once exhausted
#
# iterator
#
# ↓
#
# remains exhausted


# ------------------------------------------------------------

# 30. Fresh Iterator Starts Again

numbers = [10, 20]

it1 = iter(numbers)

print(next(it1))
print(next(it1))

try:
    next(it1)
except StopIteration:
    print("it1 finished")

print()

it2 = iter(numbers)

print(next(it2))
print(next(it2))

print()

# numbers
#
#      │
#
# iter()
#
#      │
#
#      ▼
#
# it1
#
# (finished)
#
# New iter()
#
#      │
#
#      ▼
#
# it2
#
# starts from beginning
# ============================================================
# PART 6 — ATTRIBUTE ACCESS PROTOCOL
# ============================================================

# 31. __getattribute__() Is Called For Every Attribute Access

class Student:

    def __init__(self):
        self.name = "Alice"
        self.age = 20

    def __getattribute__(self, item):
        print(f"Accessing -> {item}")
        return object.__getattribute__(self, item)


student = Student()

print(student.name)
print(student.age)

print()

# student.name
#
#       │
#       ▼
#
# __getattribute__("name")
#
#       │
#       ▼
#
# Return "Alice"


# ------------------------------------------------------------

# 32. __getattr__() Is Called Only If Attribute Is Missing

class Employee:

    def __init__(self):
        self.id = 101

    def __getattr__(self, item):
        print(f"{item} not found")
        return "Default Value"


employee = Employee()

print(employee.id)

print(employee.salary)

print()

# Existing Attribute
#
# employee.id
#
#       │
#       ▼
#
# __getattribute__()
#
#
# Missing Attribute
#
# employee.salary
#
#       │
#       ▼
#
# __getattribute__()
#
#       │
# AttributeError
#
#       ▼
#
# __getattr__()


# ------------------------------------------------------------

# 33. Difference Between __getattribute__() and __getattr__()

class Demo:

    def __init__(self):
        self.value = 100

    def __getattribute__(self, item):
        print("__getattribute__ called")
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print("__getattr__ called")
        return None


demo = Demo()

print(demo.value)

print()

print(demo.price)

print()

# Existing Attribute
#
# __getattribute__()
#
#
# Missing Attribute
#
# __getattribute__()
#
#       │
#       ▼
#
# __getattr__()


# ------------------------------------------------------------

# 34. __setattr__()

class Product:

    def __setattr__(self, key, value):
        print(f"Setting {key} = {value}")
        object.__setattr__(self, key, value)


product = Product()

product.name = "Laptop"
product.price = 65000

print(product.__dict__)

print()

# Assignment
#
# product.name = "Laptop"
#
#        │
#        ▼
#
# __setattr__()


# ------------------------------------------------------------

# 35. __delattr__()

class Book:

    def __init__(self):
        self.title = "Python"

    def __delattr__(self, item):
        print(f"Deleting {item}")
        object.__delattr__(self, item)


book = Book()

print(book.__dict__)

del book.title

print(book.__dict__)

print()

# del book.title
#
#        │
#        ▼
#
# __delattr__()


# ============================================================
# PART 7 — CALLABLE OBJECTS
# ============================================================

# 36. Objects Can Behave Like Functions

class Adder:

    def __call__(self, a, b):
        return a + b


adder = Adder()

print(adder(10, 20))

print()

# adder(10,20)
#
#      │
#      ▼
#
# adder.__call__(10,20)


# ------------------------------------------------------------

# 37. callable()

class Calculator:

    def __call__(self):
        print("Calculator Called")


calculator = Calculator()

print(callable(calculator))

calculator()

print()

# callable(obj)
#
#      │
#      ▼
#
# Does object implement __call__() ?


# ------------------------------------------------------------

# 38. Function Objects Are Also Callable

def greet():
    print("Hello")


print(callable(greet))

greet()

print()

# Python Function
#
# implements
#
# __call__()
#
# internally


# ------------------------------------------------------------

# 39. Callable Object Maintains State

class Counter:

    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


counter = Counter()

print(counter())
print(counter())
print(counter())

print()

# Counter Object
#
# count = 0
#
# call()
#
# count = 1
#
# call()
#
# count = 2
#
# call()
#
# count = 3


# ------------------------------------------------------------

# 40. Object Behaving Like Function

class Multiplier:

    def __init__(self, value):
        self.value = value

    def __call__(self, number):
        return self.value * number


double = Multiplier(2)
triple = Multiplier(3)

print(double(8))
print(triple(8))

print()

# Object
#
# stores state
#
# +
#
# behaves like function
#
# using __call__()

# ============================================================
# PART 8 — CONTEXT MANAGER PROTOCOL
# ============================================================

# 41. Using a Built-in Context Manager

with open("sample.txt", "w") as file:
    file.write("Hello Python Data Model")

print("File Closed :", file.closed)

print()

# with statement
#
#        │
#        ▼
#
# file.__enter__()
#
#        │
#        ▼
#
# Execute Block
#
#        │
#        ▼
#
# file.__exit__()


# ------------------------------------------------------------

# 42. Simple Custom Context Manager

class Database:

    def __enter__(self):
        print("Connecting...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing Connection")


with Database():
    print("Executing Queries")

print()

# with Database()
#
#        │
#        ▼
#
# __enter__()
#
#        │
#        ▼
#
# Block Executes
#
#        │
#        ▼
#
# __exit__()


# ------------------------------------------------------------

# 43. __enter__ Can Return Any Object

class FileManager:

    def __enter__(self):
        print("Opening Resource")
        return "Python"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing Resource")


with FileManager() as value:
    print(value)

print()

# __enter__()
#
#        │
#        ▼
#
# Return Object
#
#        │
#        ▼
#
# variable after 'as'


# ------------------------------------------------------------

# 44. __exit__ Handles Exceptions

class SafeExecution:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Exception Type :", exc_type)
        print("Cleaning Resources")

        return True


with SafeExecution():

    print(10 / 0)

print("Program Continues")

print()

# Exception
#
#      │
#      ▼
#
# __exit__()
#
#      │
#      ▼
#
# return True
#
#      │
#      ▼
#
# Exception Suppressed


# ------------------------------------------------------------

# 45. __exit__ Without Suppression

class Example:

    def __enter__(self):
        print("Entered")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving")
        return False


try:

    with Example():

        print(10 / 0)

except ZeroDivisionError:

    print("Handled Outside")

print()

# return False
#
#       │
#       ▼
#
# Python Re-raises Exception


# ============================================================
# PART 9 — COMBINING MULTIPLE PROTOCOLS
# ============================================================

# 46. Container + Iterator

class Numbers:

    def __init__(self):
        self.data = [1, 2, 3]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)


numbers = Numbers()

print(len(numbers))

print(numbers[0])

for value in numbers:
    print(value)

print()

# Numbers
#
# ┌────────────┐
# │1│2│3│
# └────────────┘
#
# Supports
#
# len()
# indexing
# iteration


# ------------------------------------------------------------

# 47. Representation + Callable

class Greeter:

    def __repr__(self):
        return "Greeter()"

    def __call__(self, name):
        return f"Hello {name}"


g = Greeter()

print(g)

print(g("Alice"))

print()

# print(g)
#
#      │
#      ▼
#
# __repr__()
#
#
# g("Alice")
#
#      │
#      ▼
#
# __call__()


# ------------------------------------------------------------

# 48. Attribute Access Logging

class Logger:

    def __setattr__(self, key, value):
        print(f"SET -> {key}")
        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        print(f"GET -> {item}")
        return object.__getattribute__(self, item)


obj = Logger()

obj.name = "Python"

print(obj.name)

print()

# Every Read
#
# ↓
#
# __getattribute__()
#
# Every Write
#
# ↓
#
# __setattr__()


# ------------------------------------------------------------

# 49. Python Internally Uses These Protocols

values = [10, 20, 30]

print(len(values))

print(values[0])

print(20 in values)

for value in values:
    print(value)

print()

# len()
# ↓
# __len__()
#
# []
# ↓
# __getitem__()
#
# in
# ↓
# __contains__()
#
# for
# ↓
# __iter__()
# ↓
# __next__()


# ------------------------------------------------------------

# 50. Complete Data Model Flow

class Demo:

    def __new__(cls):
        print("__new__")
        return super().__new__(cls)

    def __init__(self):
        print("__init__")

    def __repr__(self):
        return "Demo Object"

    def __call__(self):
        print("__call__")


obj = Demo()

print(obj)

obj()

print()

# Demo()
#
#    │
#    ▼
#
# __new__()
#
#    │
#    ▼
#
# __init__()
#
#    │
#    ▼
#
# Object Ready
#
#    │
#    ├──────── print(obj)
#    │              │
#    │              ▼
#    │          __repr__()
#    │
#    └──────── obj()
#                   │
#                   ▼
#               __call__()


# ============================================================
# DAY 5 CORE MODEL
# ============================================================

"""
Python Data Model (Magic Methods)
=================================

Python objects communicate with the interpreter through special methods.

Creation
--------
Class()
    ├── __new__()
    └── __init__()

Representation
--------------
print(obj)      -> __str__()
repr(obj)       -> __repr__()

Comparison
----------
==              -> __eq__()
is              -> Identity Comparison

Container
---------
len(obj)        -> __len__()
obj[i]          -> __getitem__()
obj[i] = x      -> __setitem__()
x in obj        -> __contains__()

Iterator
--------
iter(obj)       -> __iter__()
next(obj)       -> __next__()

Attribute Access
----------------
obj.x           -> __getattribute__()
Missing attr    -> __getattr__()
obj.x = value   -> __setattr__()
del obj.x       -> __delattr__()

Callable
--------
obj()           -> __call__()

Context Manager
---------------
with obj:
    __enter__()
    __exit__()

===============================================================

Mental Model

Python rarely performs operations directly.

Instead, almost every operation is translated into a
special method call.

             Python Syntax

                   │

                   ▼

         Special (Magic) Method

                   │

                   ▼

          Your Object's Behavior
Understanding the Python Data Model means understanding
how Python itself thinks.
"""