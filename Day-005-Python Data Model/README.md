
# Day 5 — Python Data Model (Magic Methods)
---

# 1. Python Data Model

The **Python Data Model** defines how objects behave inside the Python interpreter.

When we write code like:

```python
len(numbers)

print(student)

student1 == student2

for x in numbers:
    ...
```

Python does not treat these as special language keywords.

Instead, it delegates these operations to special methods implemented by the object's class.

Conceptually:

```text
Python Operation
        │
        ▼
Special Method
        │
        ▼
Object Decides Behavior
```

For example:

```text
len(obj)
      │
      ▼
obj.__len__()

--------------------

print(obj)
      │
      ▼
obj.__str__()

--------------------

obj1 == obj2
        │
        ▼
obj1.__eq__(obj2)

--------------------

iter(obj)
        │
        ▼
obj.__iter__()
```

The Python Data Model provides a common protocol that allows every object to define its own behavior.

---

# 2. Why Do We Need the Data Model?

Imagine Python had no common protocol.

For every type, the interpreter would need different logic.

```text
List
 │
Different Rules

Tuple
 │
Different Rules

String
 │
Different Rules
```

Instead, Python follows a uniform design.

```text
Python Operation
        │
        ▼
Special Method
        │
        ▼
Object Implementation
```

This allows built-in types and user-defined classes to behave consistently.

### Core Mental Model

```text
Python

↓

Doesn't implement behavior itself

↓

Asks the object

↓

Object responds using
special methods
```

---

# 3. Special Methods

Special methods are predefined methods that begin and end with double underscores.

Examples:

```python
__init__()

__str__()

__repr__()

__len__()

__eq__()

__iter__()

__next__()
```

These methods are often called **magic methods** or **dunder methods**.

They allow Python objects to integrate with the language itself.

For example:

```python
len(numbers)
```

internally follows the protocol:

```text
len(numbers)

      │

      ▼

numbers.__len__()

      │

      ▼

Return Length
```

Similarly,

```python
print(student)
```

conceptually becomes:

```text
print(student)

      │

      ▼

student.__str__()

      │

      ▼

Return String
```

### Core Rule

```text
Python Operations

↓

Special Methods

↓

Object Behavior
```

---

# 4. How the Interpreter Uses the Data Model

Consider:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Execution Flow:

```text
len(numbers)

      │

      ▼

Interpreter

      │

      ▼

Call __len__()

      │

      ▼

Return 3

      │

      ▼

Print 3
```

The same idea applies to many Python operations.

```text
Operation            Special Method

len(obj)      →      __len__()

print(obj)    →      __str__()

obj1 == obj2  →      __eq__()

iter(obj)     →      __iter__()

next(obj)     →      __next__()
```

---

# 5. Everything is Built on Objects

One of Python's core ideas is:

```text
Everything is an Object
```

Whether it is:

```python
10

"Hello"

[1, 2, 3]

{"a": 1}

Student()
```

each object can define how it behaves through the Data Model.

Object Model

```text
Python Object

┌─────────────────────┐
│ Data                │
│                     │
│ Special Methods     │
│ (__len__, __eq__...)│
└─────────────────────┘
```

Because every object follows the same protocol, Python can work with many different types using the same syntax.

---

# 6. Quick Revision

```text
Python Data Model

↓

Defines object behavior

--------------------

Python Operation

↓

Special Method

--------------------

len()

↓

__len__()

--------------------

print()

↓

__str__()

--------------------

==

↓

__eq__()

--------------------

iter()

↓

__iter__()

--------------------

Everything

↓

Object
```

---

# 7. Chapter 1 Mental Model

```text
Python Operation

        │

        ▼

Special Method

        │

        ▼

Object Implementation

        │

        ▼

Result Returned
```

---

# 8. Chapter 1 Completion Checklist

```text
✅ Python Data Model

✅ Why it exists

✅ Special Methods

✅ Interpreter delegation

✅ Common operations

✅ Mental model
```

---

# 2. Object Creation Protocol

Whenever we create an object:

```python
student = Student("Alice", 21)
```

Python does not create the object in a single step.

Instead, object creation happens in **two phases**:

```text
Student(...)
      │
      ▼
 __new__()
      │
Creates Object
      │
      ▼
 __init__()
      │
Initializes Object
      │
      ▼
 Ready to Use
```

The Object Creation Protocol defines how Python creates and initializes every object.

---

# 3. Calling a Class

Consider:

```python
class Student:
    pass

student = Student()
```

Although it looks like a function call,

```python
Student()
```

is actually a **class call**.

Execution Flow:

```text
Student()

    │

    ▼

Python Interpreter

    │

    ▼

Create New Object

    │

    ▼

Initialize Object

    │

    ▼

Return Object
```

Python performs these steps automatically using the Object Creation Protocol.

---

# 4. `__new__()`

The first step of object creation is:

```python
__new__(cls)
```

Its responsibility is to **create and return a new object**.

Conceptually:

```text
Need New Object

      │

      ▼

 __new__()

      │

      ▼

Create Object

      │

      ▼

Return Object
```

Without returning an object, there is nothing to initialize.

---

# 5. `__init__()`

Once the object is created, Python calls:

```python
__init__(self)
```

Its responsibility is to **initialize the newly created object**.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Object Model:

```text
Before __init__()

┌──────────────────┐
│ Student Object   │
│                  │
│ name : ?         │
│ age  : ?         │
└──────────────────┘


After __init__()

┌──────────────────┐
│ Student Object   │
│                  │
│ name : Alice     │
│ age  : 21        │
└──────────────────┘
```

### Core Rule

```text
__new__()

↓

Creates Object

--------------------

__init__()

↓

Initializes Object
```

---

# 6. `cls` vs `self`

These two parameters represent different things.

```text
cls

↓

Class


self

↓

Object
```

Object Model:

```text
Student Class

      │

      ▼

 __new__(cls)

      │

Creates

      ▼

Student Object

      │

      ▼

__init__(self)
```

Remember:

* `cls` refers to the **class**.
* `self` refers to the **object created from that class**.

---

# 7. Complete Object Creation Flow

For:

```python
student = Student("Alice", 21)
```

Execution Flow:

```text
Student("Alice", 21)

        │

        ▼

__new__()

        │

Creates Object

        ▼

__init__()

        │

Stores Attributes

        ▼

Return Object

        ▼

student
```

---

# 8. `__init__()` Does Not Create Objects

A common misconception is:

```text
__init__()

↓

Creates Object
```

This is **incorrect**.

Correct flow:

```text
__new__()

↓

Creates Object

↓

__init__()

↓

Initializes Object
```

If no object is created, `__init__()` is never called.

---

# 9. Quick Revision

```text
Student()

↓

Object Creation

--------------------

__new__()

↓

Create Object

--------------------

__init__()

↓

Initialize Object

--------------------

cls

↓

Class

--------------------

self

↓

Object

--------------------

Object Creation

↓

Create → Initialize
```

---

# 10. Chapter 2 Mental Model

```text
Student()

      │

      ▼

 __new__()

      │

Create Object

      │

      ▼

 __init__()

      │

Initialize Object

      │

      ▼

 Ready Object
```

---

# 11. Chapter 2 Completion Checklist

```text
✅ Object Creation Protocol

✅ Class Call

✅ __new__()

✅ __init__()

✅ cls vs self

✅ Object Creation Flow

✅ Common Misconception
```

---
# 3. Object Representation Protocol

Once an object has been created, Python needs a way to represent it as text.

For example:

```python
class Student:
    pass

student = Student()

print(student)
```

produces something like:

```text
<__main__.Student object at 0x7F8C...>
```

This behavior is defined by the **Object Representation Protocol**.

---

# 4. `__str__()`

`__str__()` defines the **human-readable representation** of an object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"
```

Now:

```python
student = Student("Alice")

print(student)
```

Output:

```text
Student: Alice
```

Execution Flow

```text
print(student)

      │

      ▼

student.__str__()

      │

      ▼

Return String

      │

      ▼

Display
```

### Core Rule

```text
print(obj)

↓

__str__()
```

---

# 5. `__repr__()`

`__repr__()` defines the **official/developer representation** of an object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"
```

Now:

```python
student
```

in the Python interpreter displays:

```text
Student('Alice')
```

Execution Flow

```text
Object in Interpreter

        │

        ▼

student.__repr__()

        │

        ▼

Return String

        │

        ▼

Display
```

---

# 6. `__str__()` vs `__repr__()`

Both methods return a string, but they serve different purposes.

| Method       | Purpose                        |
| ------------ | ------------------------------ |
| `__str__()`  | Human-readable output          |
| `__repr__()` | Developer/debug representation |

Mental Model

```text
print(obj)

      │

      ▼

__str__()

--------------------

Interpreter

      │

      ▼

__repr__()
```

---

# 7. Fallback Rule

If `__str__()` is not defined, Python automatically uses `__repr__()`.

Execution Flow

```text
print(obj)

      │

      ▼

Is __str__() available?

      │

   Yes │ No

      ▼   ▼

 __str__() __repr__()

      │

      ▼

Display
```

### Core Rule

```text
__str__() missing

↓

Use __repr__()
```

---

# 8. Both Must Return a String

Both methods **must return a string**.

Correct:

```python
def __str__(self):
    return "Student"
```

Incorrect:

```python
def __str__(self):
    return 100
```

Python raises:

```text
TypeError
```

because the returned value is not a string.

---

# 9. Quick Revision

```text
Object Representation

↓

__str__()

↓

Human-readable

--------------------

__repr__()

↓

Developer representation

--------------------

print()

↓

__str__()

--------------------

Interpreter

↓

__repr__()

--------------------

__str__() missing

↓

Fallback to __repr__()

--------------------

Both methods

↓

Return str
```

---

# 10. Chapter 3 Mental Model

```text
Need Text Representation

        │

        ▼

print(obj)

        │

        ▼

Is __str__() available?

     │          │

    Yes        No

     │          │

     ▼          ▼

 __str__()  __repr__()

     │

     ▼

Return String

     │

     ▼

Display
```

---

# 11. Chapter 3 Completion Checklist

```text
✅ Object Representation Protocol

✅ __str__()

✅ __repr__()

✅ __str__() vs __repr__()

✅ Fallback Rule

✅ Return Type
```

---
```
# 4. Object Comparison Protocol

Python provides the **Object Comparison Protocol** to determine whether two objects are equal.

For example:

```python
a = 10
b = 10

print(a == b)
```

produces:

```text
True
```

For built-in types, Python compares values automatically.

For user-defined classes, the default behavior is different.

---

# 5. Default Object Comparison

Consider:

```python
class Student:
    pass

s1 = Student()
s2 = Student()

print(s1 == s2)
```

Output:

```text
False
```

Execution Flow

```text
s1 == s2

      │

      ▼

Default Comparison

      │

      ▼

Different Objects

      │

      ▼

False
```

By default, Python compares the **identity** of user-defined objects.

---

# 6. `__eq__()`

To define custom equality, Python provides:

```python
__eq__(self, other)
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

Now:

```python
s1 = Student("Alice")
s2 = Student("Alice")

print(s1 == s2)
```

Output:

```text
True
```

Object Model

```text
s1 ─────► Student
          │
          └── name = Alice

s2 ─────► Student
          │
          └── name = Alice

        Compare

           │

           ▼

         True
```

### Core Rule

```text
==

↓

Calls __eq__()
```

---

# 7. How `==` Works

When Python sees:

```python
s1 == s2
```

it conceptually performs:

```python
s1.__eq__(s2)
```

Execution Flow

```text
s1 == s2

      │

      ▼

s1.__eq__(s2)

      │

      ▼

Return True / False
```

---

# 8. `==` vs `is`

These operators are **not** the same.

Consider:

```python
a = [1, 2]
b = [1, 2]
```

```python
print(a == b)
```

Output:

```text
True
```

```python
print(a is b)
```

Output:

```text
False
```

Object Diagram

```text
a ─────► [1, 2]

b ─────► [1, 2]

Equal Values

Different Objects
```

### Core Difference

```text
==

↓

Compare Values

--------------------

is

↓

Compare Identity
```

---

# 9. Identity Comparison

Now consider:

```python
a = [1, 2]
b = a
```

Object Model

```text
a ───────┐
          ▼
      [1, 2]
          ▲
b ─────────┘
```

Now:

```python
print(a == b)
```

```text
True
```

```python
print(a is b)
```

```text
True
```

Because both names refer to the **same object**.

---

# 10. Quick Revision

```text
Object Comparison

↓

==

↓

__eq__()

--------------------

Default

↓

Identity Comparison

--------------------

Override

↓

__eq__()

--------------------

==

↓

Compare Values

--------------------

is

↓

Compare Object Identity
```

---

# 11. Chapter 4 Mental Model

```text
s1 == s2

      │

      ▼

Is __eq__() defined?

      │

   Yes │ No

      ▼   ▼

Custom   Default

      │

      ▼

Return True / False
```

---

# 12. Chapter 4 Completion Checklist

```text
✅ Object Comparison Protocol

✅ Default Comparison

✅ __eq__()

✅ == execution

✅ == vs is

✅ Identity Comparison
```

---

# 5. Container Protocol

A **container** is an object that stores other objects.

Common container types include:

```python
list
tuple
dict
set
str
```

Python uses the **Container Protocol** to define how these objects behave.

For example:

```python
len(numbers)

numbers[0]

10 in numbers
```

Conceptually:

```text
Python Operation
        │
        ▼
Container Protocol
        │
        ▼
Special Method
```

---

# 6. `__len__()`

The special method:

```python
__len__()
```

returns the number of elements inside a container.

Example:

```python
numbers = [10, 20, 30]

len(numbers)
```

Execution Flow

```text
len(numbers)

      │

      ▼

numbers.__len__()

      │

      ▼

Return 3
```

Output:

```text
3
```

### Core Rule

```text
len(obj)

↓

__len__()
```

---

# 7. `__getitem__()`

Python uses:

```python
__getitem__(index)
```

to retrieve an element.

Example:

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Execution Flow

```text
numbers[1]

      │

      ▼

numbers.__getitem__(1)

      │

      ▼

Return 20
```

Object Model

```text
Index

0   1   2

│   │   │

▼   ▼   ▼

10 20 30
```

### Core Rule

```text
obj[index]

↓

__getitem__(index)
```

---

# 8. `__setitem__()`

Assignment using an index follows:

```python
numbers[1] = 100
```

Conceptually:

```text
numbers[1] = 100

        │

        ▼

numbers.__setitem__(1, 100)

        │

        ▼

Update Value
```

Object Model

Before

```text
[10, 20, 30]
```

After

```text
[10, 100, 30]
```

### Core Rule

```text
obj[index] = value

↓

__setitem__(index, value)
```

---

# 9. `__contains__()`

Membership testing uses:

```python
__contains__(item)
```

Example:

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Execution Flow

```text
20 in numbers

       │

       ▼

numbers.__contains__(20)

       │

       ▼

Return True
```

Output:

```text
True
```

### Core Rule

```text
item in obj

↓

__contains__(item)
```

---

# 10. Common Container Operations

| Python Operation     | Special Method   |
| -------------------- | ---------------- |
| `len(obj)`           | `__len__()`      |
| `obj[index]`         | `__getitem__()`  |
| `obj[index] = value` | `__setitem__()`  |
| `item in obj`        | `__contains__()` |

---

# 11. Container Protocol Flow

```text
len(obj)
      │
      ▼
 __len__()

--------------------

obj[index]
      │
      ▼
__getitem__()

--------------------

obj[index] = value
      │
      ▼
__setitem__()

--------------------

item in obj
      │
      ▼
__contains__()
```

---

# 12. Quick Revision

```text
Container

↓

Stores Objects

--------------------

len()

↓

__len__()

--------------------

[]

↓

__getitem__()

--------------------

[]=

↓

__setitem__()

--------------------

in

↓

__contains__()
```

---

# 13. Chapter 5 Mental Model

```text
Python Container Operation

          │

          ▼

Special Method

          │

          ▼

Container Object

          │

          ▼

Return Result
```

---

# 14. Chapter 5 Completion Checklist

```text
✅ Container Protocol

✅ __len__()

✅ __getitem__()

✅ __setitem__()

✅ __contains__()

✅ Common Container Operations
```

---
# 6. Iterator Protocol

Many Python objects can be used in a `for` loop.

For example:

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

But how does Python know **which element comes next**?

The answer is the **Iterator Protocol**.

It is built on two special methods:

* `__iter__()`
* `__next__()`

---

# 7. Why Do We Need the Iterator Protocol?

Suppose Python had no iterator protocol.

```text
List

How to get next element?

--------------------

Tuple

How to get next element?

--------------------

String

How to get next character?

--------------------

Dictionary

How to get next key?
```

Every object would need a different implementation.

Instead, Python uses one common protocol.

```text
for loop

      │

      ▼

Iterator Protocol

      │

      ▼

Object decides
how iteration works
```

---

# 8. Iterable vs Iterator

These two terms are often confused.

## Iterable

An **iterable** is an object that can produce an iterator.

Examples:

```python
list
tuple
str
dict
set
```

## Iterator

An **iterator** is an object that returns one item at a time.

Mental Model

```text
Iterable

(list)

     │

     ▼

__iter__()

     │

     ▼

Iterator

     │

     ▼

__next__()

     │

     ▼

Next Value
```

---

# 9. `__iter__()`

The special method:

```python
__iter__()
```

returns an **iterator**.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)
```

Conceptually:

```text
iter(numbers)

      │

      ▼

numbers.__iter__()

      │

      ▼

Iterator Object
```

### Core Rule

```text
iter(obj)

↓

__iter__()
```

---

# 10. `__next__()`

Once we have an iterator,

Python repeatedly calls:

```python
__next__()
```

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

next(it)
```

Execution Flow

```text
next(it)

    │

    ▼

it.__next__()

    │

    ▼

Return 10
```

Calling it again:

```text
next(it)

    │

    ▼

Return 20
```

Again:

```text
next(it)

    │

    ▼

Return 30
```

---

# 11. End of Iteration

After the last element,

Python raises:

```text
StopIteration
```

Execution Flow

```text
Iterator

10

↓

20

↓

30

↓

StopIteration
```

This exception tells Python that there are no more values.

---

# 12. How a `for` Loop Works

Consider:

```python
numbers = [10, 20, 30]

for x in numbers:
    print(x)
```

Conceptually, Python performs:

```python
it = iter(numbers)

while True:
    x = next(it)
    print(x)
```

Execution Flow

```text
for loop

    │

    ▼

iter(numbers)

    │

    ▼

Iterator

    │

    ▼

next()

    │

    ▼

Value

    │

    ▼

Repeat

    │

    ▼

StopIteration

    │

    ▼

Loop Ends
```

---

# 13. Object State During Iteration

Initially

```text
Iterator

┌──────────────┐
│ 10 │20 │30 │
└──────────────┘
   ↑
 Current Position
```

After one `next()`

```text
Iterator

┌──────────────┐
│ 10 │20 │30 │
└──────────────┘
        ↑
 Current Position
```

After another `next()`

```text
Iterator

┌──────────────┐
│ 10 │20 │30 │
└──────────────┘
             ↑
 Current Position
```

After the final value

```text
End

↓

StopIteration
```

---

# 14. Common Iterator Operations

| Python Operation | Special Method  |
| ---------------- | --------------- |
| `iter(obj)`      | `__iter__()`    |
| `next(it)`       | `__next__()`    |
| End of iteration | `StopIteration` |

---

# 15. Quick Revision

```text
Iterable

↓

__iter__()

↓

Iterator

--------------------

next()

↓

__next__()

--------------------

No More Items

↓

StopIteration

--------------------

for Loop

↓

iter()

↓

next()

↓

Repeat
```

---

# 16. Chapter 6 Mental Model

```text
Iterable

      │

      ▼

__iter__()

      │

      ▼

Iterator

      │

      ▼

__next__()

      │

      ▼

Next Value

      │

      ▼

StopIteration

      │

      ▼

Loop Ends
```

---

# 17. Chapter 6 Completion Checklist

```text
✅ Iterator Protocol

✅ Iterable

✅ Iterator

✅ __iter__()

✅ __next__()

✅ StopIteration

✅ for loop execution
```

---
# 7. Attribute Access Protocol

Every Python object stores **attributes** (variables) and **methods**.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Alice"

student = Student()

print(student.name)
```

Output

```text
Alice
```

But when we write:

```python
student.name
```

Python doesn't directly read the attribute.

Instead, it follows the **Attribute Access Protocol**.

---

# 8. Why Do We Need the Attribute Access Protocol?

Whenever we:

* Read an attribute
* Assign an attribute
* Delete an attribute

Python follows predefined rules.

Instead of:

```text
student.name

↓

Read Memory Directly
```

Python performs:

```text
student.name

      │

      ▼

Attribute Access Protocol

      │

      ▼

Return Value
```

This protocol allows Python classes to customize attribute behavior.

---

# 9. `__getattribute__()`

Every attribute lookup goes through:

```python
__getattribute__(self, name)
```

Example:

```python
student.name
```

Conceptually becomes:

```text
student.name

      │

      ▼

student.__getattribute__("name")

      │

      ▼

Return Value
```

### Core Rule

```text
obj.attribute

↓

__getattribute__()
```

> **Note:** `__getattribute__()` is called for **every** attribute access.

---

# 10. `__getattr__()`

Suppose an attribute does not exist.

```python
student.age
```

If Python cannot find `"age"`,

it calls:

```python
__getattr__(self, name)
```

Execution Flow

```text
student.age

      │

      ▼

__getattribute__()

      │

Attribute Found?

   │          │

 Yes         No

  │           │

  ▼           ▼

Return    __getattr__()

              │

              ▼

Return Value / Raise Error
```

Example:

```python
class Student:

    def __getattr__(self, name):
        return "Attribute Not Found"
```

Now,

```python
student.age
```

returns

```text
Attribute Not Found
```

---

# 11. `__setattr__()`

Whenever we assign an attribute,

```python
student.name = "Bob"
```

Python performs:

```text
student.name = "Bob"

        │

        ▼

student.__setattr__("name", "Bob")

        │

        ▼

Store Value
```

### Core Rule

```text
obj.attribute = value

↓

__setattr__()
```

---

# 12. `__delattr__()`

Deleting an attribute also follows a protocol.

Example:

```python
del student.name
```

Execution Flow

```text
del student.name

       │

       ▼

student.__delattr__("name")

       │

       ▼

Remove Attribute
```

### Core Rule

```text
del obj.attribute

↓

__delattr__()
```

---

# 13. Complete Attribute Access Flow

Suppose we execute:

```python
student.name
```

Execution Flow

```text
student.name

      │

      ▼

__getattribute__()

      │

Attribute Exists?

   │         │

 Yes        No

  │          │

  ▼          ▼

Return   __getattr__()

              │

              ▼

Return Value
```

---

# 14. Object State Example

Initially

```text
Student Object

┌──────────────────┐
│ name : Alice     │
│ age  : 21        │
└──────────────────┘
```

After

```python
student.name = "Bob"
```

```text
Student Object

┌──────────────────┐
│ name : Bob       │
│ age  : 21        │
└──────────────────┘
```

After

```python
del student.age
```

```text
Student Object

┌──────────────────┐
│ name : Bob       │
└──────────────────┘
```

---

# 15. Common Attribute Operations

| Python Operation   | Special Method       |
| ------------------ | -------------------- |
| `obj.attr`         | `__getattribute__()` |
| Missing attribute  | `__getattr__()`      |
| `obj.attr = value` | `__setattr__()`      |
| `del obj.attr`     | `__delattr__()`      |

---

# 16. Quick Revision

```text
Read Attribute

↓

__getattribute__()

--------------------

Missing Attribute

↓

__getattr__()

--------------------

Assign Attribute

↓

__setattr__()

--------------------

Delete Attribute

↓

__delattr__()
```

---

# 17. Chapter 7 Mental Model

```text
Attribute Operation

        │

        ▼

Read?

        │

        ▼

__getattribute__()

        │

 Exists?

   │          │

 Yes         No

  │           │

  ▼           ▼

Return   __getattr__()

----------------------------

Write?

↓

__setattr__()

----------------------------

Delete?

↓

__delattr__()
```

---

# 18. Chapter 7 Completion Checklist

```text
✅ Attribute Access Protocol

✅ __getattribute__()

✅ __getattr__()

✅ __setattr__()

✅ __delattr__()

✅ Attribute lookup flow

✅ Object state changes
```

# 8. Callable Objects & Function Protocol

In Python, **functions are objects**.

That means they can be:

* Assigned to variables
* Passed as arguments
* Returned from functions
* Called

But how does Python know an object can be called using `()`?

The answer is the **Callable Protocol**.

It is built around the special method:

```python id="g7s1v2"
__call__()
```

---

# 9. What is a Callable?

A **callable** is any object that can be invoked using parentheses `()`.

Examples:

```python id="x4k9pq"
print()

len()

sum()

Student()

function()

callable_object()
```

Conceptually:

```text id="m8z2ra"
Object

   │

Can it be called?

   │

   ▼

Yes

   │

   ▼

()
```

---

# 10. How Function Calls Work

Consider:

```python id="n5p3wt"
def greet():
    print("Hello")

greet()
```

Execution Flow

```text id="r7h8dk"
greet()

    │

    ▼

Function Object

    │

    ▼

Execute Function Body

    │

    ▼

Return Result
```

Functions are callable because they implement the callable protocol internally.

---

# 11. `__call__()`

Python allows **objects** to behave like functions by implementing:

```python id="a2m6jf"
__call__(self)
```

Example:

```python id="b9t4xe"
class Greeter:

    def __call__(self):
        print("Hello")
```

Now:

```python id="u3k5yn"
g = Greeter()

g()
```

Output

```text id="f8v1qc"
Hello
```

Execution Flow

```text id="d6p9ws"
g()

 │

 ▼

g.__call__()

 │

 ▼

Execute Method

 │

 ▼

Return
```

### Core Rule

```text id="l1z8me"
obj()

↓

__call__()
```

---

# 12. Object State

Before calling

```text id="h4y7kn"
g

│

▼

Greeter Object
```

After

```python id="q6v8rc"
g()
```

```text id="v2x5sb"
Greeter Object

│

Executes __call__()

│

Returns Result
```

Unlike `__init__()`, calling an object **does not create a new object**.

It simply executes `__call__()` on the existing object.

---

# 13. `callable()`

Python provides a built-in function to check whether an object is callable.

Example:

```python id="t8r3mn"
callable(print)
```

Output

```text id="j9w2ka"
True
```

Example:

```python id="g2u4ld"
callable([1, 2, 3])
```

Output

```text id="z5f7pe"
False
```

Example:

```python id="k1c8yv"
g = Greeter()

callable(g)
```

Output

```text id="m4n6bx"
True
```

Execution Flow

```text id="w3q9hf"
callable(obj)

      │

      ▼

Has __call__()?

   │         │

 Yes        No

  │          │

  ▼          ▼

True      False
```

---

# 14. Function Objects vs Callable Objects

| Function Object        | Callable Object       |
| ---------------------- | --------------------- |
| Created using `def`    | Created using `class` |
| Called with `()`       | Called with `()`      |
| Executes function body | Executes `__call__()` |

Mental Model

```text id="y8d4ps"
Function

 │

 ▼

()

--------------------

Object

 │

 ▼

__call__()

 │

 ▼

()
```

---

# 15. AI/ML Connection

Many machine learning libraries use callable objects.

Example:

```python id="p7x2ma"
model(input)

loss(prediction, target)

transform(image)
```

Although they look like function calls, many of these objects implement `__call__()` internally, allowing them to be used just like functions.

---

# 16. Quick Revision

```text id="c6r5zn"
Callable

↓

Can use ()

--------------------

obj()

↓

__call__()

--------------------

callable(obj)

↓

True / False

--------------------

Functions

↓

Callable Objects
```

---

# 17. Chapter 8 Mental Model

```text id="e1k7ut"
Object

   │

Use ()

   │

   ▼

__call__()

   │

   ▼

Execute

   │

   ▼

Return Result
```

---

# 18. Chapter 8 Completion Checklist

```text id="n3v8qy"
✅ Callable Protocol

✅ Callable Objects

✅ __call__()

✅ callable()

✅ Function vs Callable Object

✅ AI/ML Connection
```

---
```
# 9. Context Manager Protocol

Python provides the **Context Manager Protocol** to automatically manage resources such as:

* Files
* Database connections
* Network sockets
* Locks

Instead of manually releasing resources, Python does it automatically.

Example:

```python
with open("data.txt") as file:
    content = file.read()
```

The `with` statement uses the Context Manager Protocol.

---

# 10. Why Do We Need Context Managers?

Without a context manager:

```python
file = open("data.txt")

content = file.read()

file.close()
```

If an exception occurs before `close()`, the file remains open.

Execution Flow

```text
Open File

    │

    ▼

Read Data

    │

 Exception?

 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼

Program     close()
Stops
```

This can cause **resource leaks**.

---

# 11. The `with` Statement

Python provides:

```python
with ...
```

to automatically manage resources.

Example:

```python
with open("data.txt") as file:
    print(file.read())
```

Execution Flow

```text
with

 │

 ▼

Acquire Resource

 │

 ▼

Execute Block

 │

 ▼

Release Resource
```

The resource is released even if an exception occurs.

---

# 12. `__enter__()`

When execution enters a `with` block,

Python calls:

```python
__enter__()
```

Its responsibility is to **prepare and return the resource**.

Conceptually:

```text
with object

      │

      ▼

__enter__()

      │

      ▼

Resource Ready

      │

      ▼

Execute Block
```

### Core Rule

```text
Enter with block

↓

__enter__()
```

---

# 13. `__exit__()`

After the `with` block finishes,

Python automatically calls:

```python
__exit__()
```

Its responsibility is to **clean up the resource**.

Execution Flow

```text
End of Block

      │

      ▼

__exit__()

      │

      ▼

Release Resource
```

### Core Rule

```text
Exit with block

↓

__exit__()
```

---

# 14. Complete Context Manager Flow

Consider:

```python
with open("data.txt") as file:
    print(file.read())
```

Execution Flow

```text
with

 │

 ▼

__enter__()

 │

 ▼

Open File

 │

 ▼

Execute Code

 │

 ▼

__exit__()

 │

 ▼

Close File
```

---

# 15. Exception Handling

One major advantage of context managers is automatic cleanup.

Even if an exception occurs:

```python
with open("data.txt") as file:
    x = 10 / 0
```

Python still executes:

```text
Exception

     │

     ▼

__exit__()

     │

     ▼

Close Resource

     │

     ▼

Propagate Exception
```

This ensures resources are never left open.

---

# 16. Object State

Before entering

```text
File Object

┌─────────────┐
│ Closed      │
└─────────────┘
```

Inside `with`

```text
File Object

┌─────────────┐
│ Open        │
└─────────────┘
```

After leaving

```text
File Object

┌─────────────┐
│ Closed      │
└─────────────┘
```

---

# 17. Common Context Manager Operations

| Python Statement | Special Method |
| ---------------- | -------------- |
| `with obj`       | `__enter__()`  |
| Exit block       | `__exit__()`   |

---

# 18. AI/ML Connection

Context managers are widely used in AI/ML for safely managing resources.

Examples:

```python
with open("dataset.csv") as f:
    ...

with torch.no_grad():
    ...

with lock:
    ...
```

The `with` statement ensures resources are correctly managed without manual cleanup.

---

# 19. Quick Revision

```text
with

↓

Context Manager

--------------------

Enter Block

↓

__enter__()

--------------------

Exit Block

↓

__exit__()

--------------------

Automatic Cleanup

↓

Resources Released

--------------------

Exceptions

↓

Cleanup Still Happens
```

---

# 20. Chapter 9 Mental Model

```text
with Object

      │

      ▼

__enter__()

      │

      ▼

Execute Block

      │

      ▼

__exit__()

      │

      ▼

Cleanup Complete
```

---

# 21. Chapter 9 Completion Checklist

```text
✅ Context Manager Protocol

✅ with statement

✅ __enter__()

✅ __exit__()

✅ Automatic cleanup

✅ Exception handling

✅ AI/ML connection
```

---
```

# 10. Complete Python Data Model Summary

By now we've learned that Python does not hardcode the behavior of objects.

Instead, it asks the object **how it should behave** through special methods (magic methods).

This idea is the foundation of Python's Data Model.

---

# 11. Complete Data Model Flow

Suppose we write the following program:

```python
student = Student("Alice")

print(student)

len(student)

student[0]

student == other

for x in student:
    ...

student()

with student:
    ...
```

Conceptually, Python executes:

```text
Student("Alice")
      │
      ▼
 __new__()
      │
      ▼
 __init__()
      │
      ▼
Object Created
      │
      ▼
 __str__()
      │
      ▼
 __len__()
      │
      ▼
 __getitem__()
      │
      ▼
 __eq__()
      │
      ▼
 __iter__()
      │
      ▼
 __next__()
      │
      ▼
 __call__()
      │
      ▼
 __enter__()
      │
      ▼
 Execute Block
      │
      ▼
 __exit__()
```

Every operation is delegated to a special method.

---

# 12. Complete Protocol Map

| Python Operation        | Special Method              |
| ----------------------- | --------------------------- |
| `Student()`             | `__new__()`, `__init__()`   |
| `print(obj)`            | `__str__()`                 |
| `repr(obj)`             | `__repr__()`                |
| `obj1 == obj2`          | `__eq__()`                  |
| `len(obj)`              | `__len__()`                 |
| `obj[index]`            | `__getitem__()`             |
| `obj[index] = value`    | `__setitem__()`             |
| `item in obj`           | `__contains__()`            |
| `iter(obj)`             | `__iter__()`                |
| `next(iterator)`        | `__next__()`                |
| `obj.attribute`         | `__getattribute__()`        |
| Missing attribute       | `__getattr__()`             |
| `obj.attribute = value` | `__setattr__()`             |
| `del obj.attribute`     | `__delattr__()`             |
| `obj()`                 | `__call__()`                |
| `with obj:`             | `__enter__()`, `__exit__()` |

---

# 13. Mental Model

Instead of thinking:

```text
Python performs every operation.
```

Think:

```text
Python

     │

Receives an Operation

     │

     ▼

Looks for the Correct Special Method

     │

     ▼

Calls that Method

     │

     ▼

Object Decides the Behavior

     │

     ▼

Returns the Result
```

This is the core philosophy of the Python Data Model.

---

# 14. Protocol Relationships

```text
                Python Object
                      │
 ┌────────────────────┼────────────────────┐
 │                    │                    │
 ▼                    ▼                    ▼
Creation        Representation      Comparison
 │                    │                    │
__new__()        __str__()          __eq__()
__init__()       __repr__()
 │
 └────────────────────┬────────────────────┐
                      │
                      ▼
              Container Protocol
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 __len__()     __getitem__()   __contains__()
                     │
                     ▼
               __setitem__()
                      │
                      ▼
              Iterator Protocol
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
 __iter__()                     __next__()
                      │
                      ▼
            Attribute Protocol
                      │
 ┌────────────┬────────────┬────────────┐
 ▼            ▼            ▼            ▼
__getattribute__()
__getattr__()
__setattr__()
__delattr__()
                      │
                      ▼
            Callable Protocol
                      │
                 __call__()
                      │
                      ▼
         Context Manager Protocol
                      │
         __enter__() / __exit__()
```

---

# 15. How AI/ML Libraries Use These Protocols

Many AI/ML libraries feel "natural" because they implement these protocols.

| Protocol                     | Example                                  |
| ---------------------------- | ---------------------------------------- |
| `__call__()`                 | `model(input)`                           |
| `__iter__()`                 | `for batch in dataloader:`               |
| `__getitem__()`              | `dataset[0]`                             |
| `__len__()`                  | `len(dataset)`                           |
| `__enter__()` / `__exit__()` | `with torch.no_grad():`                  |
| `__repr__()`                 | Displaying a neural network architecture |
| `__eq__()`                   | Custom object comparisons                |

Understanding the Data Model helps explain why these libraries behave like built-in Python objects.

---

# 16. Day 5 Mind Map

```text
                 Python Data Model
                         │
 ┌──────────────┬──────────────┬──────────────┐
 │              │              │              │
 ▼              ▼              ▼              ▼
Creation   Representation  Comparison   Container
 │              │              │              │
 ▼              ▼              ▼              ▼
Iterator   Attribute     Callable     Context Manager
```

---

# 17. Key Takeaways

```text
✓ Everything in Python is an object.

✓ Objects define their behavior using special methods.

✓ Python delegates operations to these methods.

✓ Different protocols handle different kinds of operations.

✓ This design makes user-defined classes behave like built-in types.

✓ Modern AI/ML frameworks rely heavily on these protocols.
```

---

# 18. Day 5 Completion Checklist

```text
✅ Python Data Model

✅ Object Creation Protocol

✅ Object Representation Protocol

✅ Object Comparison Protocol

✅ Container Protocol

✅ Iterator Protocol

✅ Attribute Access Protocol

✅ Callable Protocol

✅ Context Manager Protocol

✅ Complete Protocol Flow

✅ AI/ML Connections
```

---

# 🎯 Day 5 Completed

```text
Day 5 : Python Data Model (Magic Methods)

Completed Topics

✅ Python Data Model
✅ Object Creation (__new__, __init__)
✅ Object Representation (__str__, __repr__)
✅ Object Comparison (__eq__)
✅ Container Protocol
✅ Iterator Protocol
✅ Attribute Access Protocol
✅ Callable Objects (__call__)
✅ Context Managers (__enter__, __exit__)
✅ Complete Revision

