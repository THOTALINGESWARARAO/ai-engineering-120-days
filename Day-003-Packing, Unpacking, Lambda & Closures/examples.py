
# 1. Sequence Packing

values = 10, 20, 30

print("values:", values)
print("Type:", type(values))
print()


# 2. Single-Value Tuple Packing

value = 10,

print("value:", value)
print("Type:", type(value))
print()


# 3. Sequence Unpacking

a, b, c = (10, 20, 30)

print("a:", a)
print("b:", b)
print("c:", c)
print()


# 4. List Unpacking

a, b, c = [10, 20, 30]

print("a:", a)
print("b:", b)
print("c:", c)
print()


# 5. Extended Iterable Unpacking

first, *middle, last = [10, 20, 30, 40, 50]

print("first:", first)
print("middle:", middle)
print("last:", last)
print("middle type:", type(middle))
print()


# 6. Starred Target Collecting Remaining Values

first, *rest = [10, 20, 30, 40]

print("first:", first)
print("rest:", rest)
print()


# 7. Starred Target Can Collect Zero Values

first, *middle, last = [10, 20]

print("first:", first)
print("middle:", middle)
print("last:", last)
print()


# 8. Starred Expression — List

numbers = (10, 20, 30)

result = [0, *numbers, 40]

print("result:", result)
print("Type:", type(result))
print()


# 9. Starred Expression — Tuple

numbers = [10, 20, 30]

result = (0, *numbers, 40)

print("result:", result)
print("Type:", type(result))
print()


# 10. Positional Argument Unpacking with *

def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

result = add(*numbers)

print("Result:", result)
print()


# 11. * Can Unpack Other Iterables

def show(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)


show(*"AI!")
print()


# 12. Keyword Argument Unpacking with **

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


person = {
    "name": "Ravi",
    "age": 21
}

introduce(**person)
print()


# 13. Collect vs Expand

def collect(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


values = [10, 20]

config = {
    "name": "Python",
    "level": "Intermediate"
}

collect(*values, **config)
print()


# In a function definition:
#
# *args
# -> collects positional arguments into a tuple
#
# **kwargs
# -> collects keyword arguments into a dictionary
#
# In a function call:
#
# *iterable
# -> expands positional arguments
#
# **mapping
# -> expands keyword arguments


# 14. Lambda Creates a Function Object

double = lambda x: x * 2

print("double(25):", double(25))
print("Type:", type(double))
print()


# 15. Lambda Function Reference

double = lambda x: x * 2

operation = double

print("double(10):", double(10))
print("operation(10):", operation(10))
print("operation is double:", operation is double)
print()


# 16. Lambda with Multiple Parameters

add = lambda a, b: a + b

print("add(10, 20):", add(10, 20))
print()


# 17. Lambda Implicit Return

square = lambda x: x ** 2

print("square(4):", square(4))
print()


# 18. Lambda vs def Return Behavior

square_lambda = lambda x: x ** 2


def square_without_return(x):
    x ** 2


def square_with_return(x):
    return x ** 2


print("Lambda:", square_lambda(4))
print("def without return:", square_without_return(4))
print("def with return:", square_with_return(4))
print()


# 19. Lambda Expression Calling a Function

show_value = lambda x: print("Value:", x)

result = show_value(10)

print("Returned:", result)
print()


# print(x) is a function-call expression.
# print() itself returns None.
#
# Therefore the lambda above also returns None.


# 20. Lambda __name__

def square(x):
    return x ** 2


double = lambda x: x * 2

print("square.__name__:", square.__name__)
print("double.__name__:", double.__name__)
print()


# 21. Higher-Order Function

def apply_operation(value, operation):
    return operation(value)


square = lambda x: x ** 2

result = apply_operation(5, square)

print("Result:", result)
print()


# 22. Lambda Directly as an Argument

def apply_operation(value, operation):
    return operation(value)


result = apply_operation(
    5,
    lambda x: x * 2
)

print("Result:", result)
print()


# 23. Lambda with sorted()

words = ["AI", "Python", "ML"]

result = sorted(
    words,
    key=lambda word: len(word)
)

print("Sorted words:", result)
print()


# 24. Lambda Sorting Structured Data

students = [
    ("Ravi", 85),
    ("Anu", 92),
    ("Kiran", 78)
]

result = sorted(
    students,
    key=lambda student: student[1]
)

print("Sorted students:", result)
print()


# 25. Nested Function

def outer():
    def inner():
        print("Inside inner")

    inner()


outer()
print()


# 26. Enclosing Scope

def outer():
    x = 10

    def inner():
        print("x:", x)

    inner()


outer()
print()


# 27. Returning an Inner Function

def outer():
    x = 10

    def inner():
        return x

    return inner


f = outer()

print("f:", f)
print("f():", f())
print()


# return inner
# -> returns the function object
#
# return inner()
# -> executes inner and returns its result


# 28. Free Variable

def outer():
    x = 10

    def inner():
        y = 20
        return x + y

    return inner


f = outer()

print("Result:", f())
print("Free variables:", f.__code__.co_freevars)
print()


# x:
# -> free variable of inner
#
# y:
# -> local variable of inner


# 29. Only Referenced Enclosing Variables are Free Variables

def outer():
    x = 10
    message = "Hello"

    def inner():
        return x

    return inner


f = outer()

print("Free variables:", f.__code__.co_freevars)
print()


# message exists in outer,
# but inner does not reference it.


# 30. Inspecting __closure__

def outer():
    x = 10

    def inner():
        return x

    return inner


f = outer()

print("__closure__:", f.__closure__)
print()


# 31. Inspecting Closure Cell Contents

def outer():
    x = 10

    def inner():
        return x

    return inner


f = outer()

print("Free variables:", f.__code__.co_freevars)
print(
    "Cell contents:",
    f.__closure__[0].cell_contents
)
print()


# 32. Global Lookup is Not a Closure Capture

x = 100


def outer():
    def inner():
        return x

    return inner


f = outer()

print("f():", f())
print("__closure__:", f.__closure__)
print()


# x is found in Global scope,
# not Enclosing scope.


# 33. Independent Closure Cells

def outer():
    x = 10

    def inner():
        return x

    return inner


f1 = outer()
f2 = outer()

print("f1():", f1())
print("f2():", f2())

print(
    "Same closure cell:",
    f1.__closure__[0] is f2.__closure__[0]
)

print()


# Each call to outer() creates its own
# captured x binding / closure cell.


# 34. Closure Retained State

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()

print("counter():", counter())
print("counter():", counter())
print("counter():", counter())
print()


# 35. Independent Closure State

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = make_counter()
counter2 = make_counter()

print("counter1:", counter1())
print("counter1:", counter1())
print("counter2:", counter2())
print("counter1:", counter1())
print()


# 36. Closure Mutation Without nonlocal

def make_collector():
    values = []

    def add(value):
        values.append(value)
        return values

    return add


collector = make_collector()

print("collector(10):", collector(10))
print("collector(20):", collector(20))
print()


# values.append(...)
# mutates the existing list.
#
# It does not rebind the name values.


# 37. Closure Rebinding with nonlocal

def make_collector():
    values = []

    def add(value):
        nonlocal values
        values = values + [value]
        return values

    return add


collector = make_collector()

print("collector(10):", collector(10))
print("collector(20):", collector(20))
print()


# values = values + [value]
#
# rebinds values.
#
# nonlocal makes that assignment target
# the enclosing values binding.


# 38. Captured Binding — Not Frozen Value

def outer():
    x = 10

    def inner():
        return x

    x = 50

    return inner


f = outer()

print("f():", f())
print(
    "Cell contents:",
    f.__closure__[0].cell_contents
)
print()


# The closure does not simply freeze x = 10.
#
# inner retains access to the captured binding.
#
# The binding later refers to 50.


# 39. Late Binding

def create_functions():
    functions = []

    for i in range(3):
        functions.append(lambda: i)

    return functions


f1, f2, f3 = create_functions()

print("f1():", f1())
print("f2():", f2())
print("f3():", f3())
print()


# All three lambdas refer to the same
# captured i binding.
#
# After the loop:
#
# i = 2
#
# Therefore:
#
# f1() -> 2
# f2() -> 2
# f3() -> 2


# 40. Late Binding After Another Rebinding

def create_functions():
    functions = []

    for i in range(3):
        functions.append(lambda: i)

    i = 100

    return functions


f1, f2, f3 = create_functions()

print("f1():", f1())
print("f2():", f2())
print("f3():", f3())
print()


# 41. Shared Closure Cell in Late Binding

def create_functions():
    functions = []

    for i in range(3):
        functions.append(lambda: i)

    return functions


f1, f2, f3 = create_functions()

print(
    "f1 and f2 same cell:",
    f1.__closure__[0] is f2.__closure__[0]
)

print(
    "f2 and f3 same cell:",
    f2.__closure__[0] is f3.__closure__[0]
)

print(
    "Captured i:",
    f1.__closure__[0].cell_contents
)

print()


# 42. Fixing Late Binding with Default Arguments

def create_functions():
    functions = []

    for i in range(3):
        functions.append(
            lambda i=i: i
        )

    return functions


f1, f2, f3 = create_functions()

print("f1():", f1())
print("f2():", f2())
print("f3():", f3())
print()


# Default arguments are evaluated when
# each function object is created.
#
# Conceptually:
#
# iteration 1:
# lambda i=0: i
#
# iteration 2:
# lambda i=1: i
#
# iteration 3:
# lambda i=2: i


# 43. Lambda Default Argument Override

f = lambda i=10: i

print("f():", f())
print("f(999):", f(999))
print()


# 44. Closure as a Function Factory

def make_multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print("double(10):", double(10))
print("triple(10):", triple(10))
print()


# 45. Closure State Inspection

def make_multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


double = make_multiplier(2)

print(
    "Free variables:",
    double.__code__.co_freevars
)

print(
    "Captured factor:",
    double.__closure__[0].cell_contents
)

print()


"""
PACKING:

    values = 10, 20, 30

    Multiple comma-separated values can
    be packed into a tuple.


UNPACKING:

    a, b, c = iterable

    Elements from an iterable are assigned
    to multiple targets.


EXTENDED UNPACKING:

    first, *middle, last = iterable

    A starred assignment target collects
    zero or more values into a list.


* IN ASSIGNMENT:

    *rest

    Collects values.


* IN A FUNCTION CALL:

    function(*iterable)

    Expands iterable elements into
    positional arguments.


** IN A FUNCTION CALL:

    function(**mapping)

    Expands mapping entries into
    keyword arguments.


COLLECT VS EXPAND:

    Function definition:

        *args
        -> collects positional arguments

        **kwargs
        -> collects keyword arguments

    Function call:

        *iterable
        -> expands positional arguments

        **mapping
        -> expands keyword arguments


LAMBDA:

    lambda parameters: expression

    A lambda expression creates a
    function object.


LAMBDA CREATION:

    lambda x: x * 2

    Creates a function.

    It does not execute the body yet.


LAMBDA EXECUTION:

    f(10)

    Calls the function and evaluates
    the lambda body expression.


LAMBDA RETURN:

    The value of the body expression
    becomes the function result.


LAMBDA VS def:

    lambda:
        expression
        one expression body
        implicit result

    def:
        function-definition statement
        supports a statement suite
        explicit return when a value
        should be returned


HIGHER-ORDER FUNCTIONS:

    Functions are objects.

    They can be:

        stored in names
        passed as arguments
        returned from functions


NESTED FUNCTION:

    A function defined inside another
    function.


FREE VARIABLE:

    A name referenced by a function
    that is not locally bound there.

    In closure examples, the binding
    comes from an enclosing function scope.


CLOSURE:

    A function together with retained
    access to relevant bindings from
    enclosing function scopes.


co_freevars:

    Contains the names of a function's
    free variables.


__closure__:

    Contains closure cells associated
    with captured free-variable bindings.

    It can be None when no closure cells
    are required.


cell_contents:

    Gives the current contents of a
    closure cell.


INDEPENDENT CLOSURES:

    Separate executions of an outer
    function can create separate
    closure cells and independent state.


nonlocal:

    Allows assignment to rebind an
    applicable enclosing-function binding.


MUTATION:

    values.append(x)

    Changes the existing object.

    The values binding itself is not
    rebound.


REBINDING:

    values = values + [x]

    Changes which object the name
    values refers to.

    nonlocal is required when this
    assignment should target the
    enclosing binding.


CAPTURED BINDING:

    Closures should not be thought of
    as always freezing a value when the
    inner function is created.

    They retain access to captured
    bindings through closure machinery.


LATE BINDING:

    lambda: i

    Multiple lambdas created in a loop
    can refer to the same captured
    loop-variable binding.

    If the final value is 2:

        f1() -> 2
        f2() -> 2
        f3() -> 2


LATE BINDING FIX:

    lambda i=i: i

    The default expression is evaluated
    when each lambda function is created.

    This can preserve each iteration's
    current value as that function's
    default argument.


DAY 3 CORE MODEL:

    Packing / Unpacking
        -> collect and distribute values

    Lambda
        -> creates function objects

    Nested Functions
        -> introduce enclosing scope

    Free Variables
        -> names obtained from outside
           the function's local scope

    Closures
        -> retain access to relevant
           enclosing bindings

    Closure Cells
        -> support captured bindings

    nonlocal
        -> rebind enclosing bindings

    Late Binding
        -> explains why closures should
           be understood in terms of
           bindings rather than frozen
           snapshots
"""

