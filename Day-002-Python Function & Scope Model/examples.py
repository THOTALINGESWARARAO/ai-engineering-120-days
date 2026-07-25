# 1. Functions are Objects

def square(x):
    return x * x


operation = square

print("square(6):", square(6))
print("operation(6):", operation(6))
print("operation is square:", operation is square)
print()


# 2. Parameters and Arguments

def greet(name):
    print("Hello,", name)


greet("Python")
print()


# 3. Function Argument — Mutation

def add_score(scores):
    scores.append(90)


marks = [70, 80]

add_score(marks)

print("marks:", marks)
print()


# 4. Function Argument — Rebinding

def add_score(scores):
    scores = scores + [90]
    print("Inside:", scores)


marks = [70, 80]

add_score(marks)

print("Outside:", marks)
print()


# 5. Return Values

def square(x):
    result = x * x
    return result


answer = square(6)

print("answer:", answer)
print()


# 6. Local and Global Scope

x = 100


def test():
    x = 200
    print("Local x:", x)


test()

print("Global x:", x)
print()


# 7. Global Name Lookup

x = 100


def test():
    print("x:", x)


test()
print()


# 8. Enclosing Scope

x = 100


def outer():
    x = 200

    def inner():
        print("x:", x)

    inner()


outer()
print()


# 9. Multiple Enclosing Scopes

x = 10


def outer():
    x = 20

    def middle():
        x = 30

        def inner():
            print("x:", x)

        inner()

    middle()


outer()
print()


# 10. Lexical Scope

x = 10


def first():
    x = 20
    second()


def second():
    print("x:", x)


first()
print()


# 11. Built-in Scope

numbers = [10, 20, 30]

print("Length:", len(numbers))
print()


# 12. Built-in Shadowing

len_value = len

print("Built-in len:", len_value([1, 2, 3]))
print()

# Avoid:
#
# len = 100
# len([1, 2, 3])
#
# This would raise TypeError because len
# would refer to an integer instead of
# the built-in function.


# 13. UnboundLocalError

x = 10


def test():
    # print(x)  # UnboundLocalError
    x = 20
    print("Local x:", x)


test()
print()


# 14. global

x = 10


def change():
    global x
    x = 20


change()

print("Global x:", x)
print()


# 15. Mutation Without global

scores = [70, 80]


def add_score():
    scores.append(90)


add_score()

print("scores:", scores)
print()


# 16. Global Rebinding

scores = [70, 80]


def reset_scores():
    global scores
    scores = []


reset_scores()

print("scores:", scores)
print()


# 17. nonlocal

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()

    print("x:", x)


outer()
print()


# 18. Nearest Enclosing Binding

x = 100


def outer():
    x = 200

    def middle():
        x = 300

        def inner():
            nonlocal x
            x = 400

        inner()

        print("Middle x:", x)

    middle()

    print("Outer x:", x)


outer()

print("Global x:", x)
print()


# 19. Positional Arguments

def train(model, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


train("CNN", 10, 0.001)
print()


# 20. Keyword Arguments

def train(model, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


train(
    lr=0.001,
    model="CNN",
    epochs=10
)

print()


# 21. Positional and Keyword Arguments

def train(model, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


train(
    "CNN",
    epochs=10,
    lr=0.001
)

print()


# 22. Positional-Only Parameters

def power(x, y, /):
    return x ** y


print("power(2, 3):", power(2, 3))
print()

# power(x=2, y=3)
# TypeError


# 23. Keyword-Only Parameters

def train(model, *, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


train(
    "CNN",
    epochs=10,
    lr=0.001
)

print()


# 24. Positional-Only and Keyword-Only Parameters

def experiment(model, /, epochs, *, verbose):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Verbose:", verbose)


experiment(
    "CNN",
    10,
    verbose=True
)

print()


# 25. *args

def show_scores(model, *scores):
    print("Model:", model)
    print("Scores:", scores)
    print("Type:", type(scores))


show_scores(
    "CNN",
    91,
    87,
    95
)

print()


# 26. **kwargs

def show_config(**config):
    print("Config:", config)
    print("Type:", type(config))


show_config(
    optimizer="Adam",
    lr=0.001,
    epochs=10
)

print()


# 27. *args and **kwargs

def train(model, *scores, **config):
    print("Model:", model)
    print("Scores:", scores)
    print("Config:", config)


train(
    "CNN",
    91,
    87,
    optimizer="Adam",
    lr=0.001
)

print()


# 28. Positional Argument Unpacking

def add(a, b, c):
    return a + b + c


values = [10, 20, 30]

result = add(*values)

print("Result:", result)
print()


# 29. Keyword Argument Unpacking

def train(model, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


config = {
    "model": "CNN",
    "epochs": 10,
    "lr": 0.001
}

train(**config)
print()


# 30. Positional and Keyword Unpacking

def experiment(model, epochs, lr):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


args = ["CNN", 10]

config = {
    "lr": 0.001
}

experiment(*args, **config)
print()


# 31. Default Arguments

def train(model, epochs=10):
    print("Model:", model)
    print("Epochs:", epochs)


train("CNN")
train("CNN", 20)
print()


# 32. Default Argument Override

def train(model, epochs=10, lr=0.001):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Learning rate:", lr)


train(
    "CNN",
    epochs=20,
    lr=0.01
)

print()


# 33. Default Arguments are Evaluated at Definition Time

value = 10


def show(x=value):
    print("x:", x)


value = 20

show()
print()


# 34. Function __defaults__

def train(epochs=10, lr=0.001):
    pass


print("Defaults:", train.__defaults__)
print()


# 35. Mutable Default Argument

def collect(value, bucket=[]):
    bucket.append(value)
    return bucket


a = collect("Python")
b = collect("ML")

print("a:", a)
print("b:", b)
print("a is b:", a is b)
print()


# 36. Mutable Default Object Identity

def collect(value, bucket=[]):
    print("bucket id:", id(bucket))
    bucket.append(value)
    return bucket


a = collect(1)
b = collect(2)

print("a:", a)
print("b:", b)
print("a is b:", a is b)
print()


# 37. Explicit Mutable Argument

def collect(value, bucket=[]):
    bucket.append(value)
    return bucket


a = collect(1)
b = collect(2)
c = collect(3, [])

print("a:", a)
print("b:", b)
print("c:", c)

print("a is b:", a is b)
print("a is c:", a is c)
print()


# 38. Safe Mutable Default with None

def collect(value, bucket=None):
    if bucket is None:
        bucket = []

    bucket.append(value)

    return bucket


a = collect("Python")
b = collect("ML")

print("a:", a)
print("b:", b)
print("a is b:", a is b)
print()


# 39. Caller-Provided Shared Object

def collect(value, bucket=None):
    if bucket is None:
        bucket = []

    bucket.append(value)

    return bucket


shared = []

a = collect("Python", shared)
b = collect("ML", shared)

print("shared:", shared)
print("a:", a)
print("b:", b)

print("a is b:", a is b)
print("a is shared:", a is shared)
print()


# 40. Complete Parameter Example

def experiment(
    model,
    /,
    epochs=10,
    *scores,
    lr=0.001,
    **config
):
    print("Model:", model)
    print("Epochs:", epochs)
    print("Scores:", scores)
    print("Learning rate:", lr)
    print("Config:", config)


experiment(
    "CNN",
    20,
    91,
    87,
    lr=0.01,
    optimizer="Adam",
    device="cuda"
)

"""
Functions:
    def creates a function object.
    Calling the function creates local parameter bindings.

Scope:
    L -> Local
    E -> Enclosing
    G -> Global
    B -> Built-in

Assignment:
    Normally creates/rebinds a local name inside a function.

global:
    Targets a global binding.

nonlocal:
    Targets the nearest applicable enclosing-function binding.

Mutation:
    Changes an existing object.

Rebinding:
    Changes which object a name refers to.

*args:
    Collects extra positional arguments into a tuple.

**kwargs:
    Collects extra keyword arguments into a dictionary.

*iterable in a call:
    Unpacks positional arguments.

**mapping in a call:
    Unpacks keyword arguments.

Default arguments:
    Evaluated when the function definition executes.

Mutable defaults:
    Can reuse the same mutable object across calls.

Common safe pattern:
    Use None as the default and create a fresh mutable
    object inside the function when needed.
"""