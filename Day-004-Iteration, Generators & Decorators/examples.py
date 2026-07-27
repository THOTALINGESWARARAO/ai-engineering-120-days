"""
Day 4 — Iteration, Iterators, Generators & Decorators
"""


# ============================================================
# PART 1 — ITERABLES, ITERATORS, iter(), next()
# ============================================================

# 1. Iterable -> Iterator

numbers = [10, 20, 30]

iterator = iter(numbers)

print("numbers:", numbers)
print("numbers type:", type(numbers))
print("iterator type:", type(iterator))
print("numbers is iterator:", numbers is iterator)
print()


# 2. iter() Obtains an Iterator — It Does Not Convert the List

numbers = [10, 20, 30]

iterator = iter(numbers)

print("Before/after iter(), numbers:", numbers)
print("numbers type:", type(numbers))
print("iterator:", iterator)
print("iterator type:", type(iterator))
print()


# The list remains a list.
#
# Conceptually:
#
# numbers ---> [10, 20, 30]
#                    ^
#                    |
#              iterator object
#
# iter(numbers) obtains an iterator.
# It does not turn numbers itself into an iterator.


# 3. Aliasing vs Creating an Iterator

a = [1, 2, 3]

b = a
it = iter(a)

print("a is b:", a is b)
print("a is it:", a is it)
print()


# a and b:
# -> two names referring to the same list object
#
# it:
# -> a different iterator object


# 4. next() Advances Iterator State

numbers = [10, 20, 30]
it = iter(numbers)

a = next(it)
b = next(it)

print("a:", a)
print("b:", b)
print("Original list:", numbers)
print()


# Conceptual iterator state:
#
# Initially:
#
# [10, 20, 30]
#  ^
#
# after next(it) -> 10:
#
# [10, 20, 30]
#      ^
#
# after next(it) -> 20:
#
# [10, 20, 30]
#          ^
#
# next() advances the iterator.
# It does not remove elements from the list.


# 5. Iterator State Continues Across Calls

it = iter(["A", "B", "C"])

print(next(it))
print(next(it))
print(next(it))
print()


# Output:
#
# A
# B
# C
#
# Each next() continues from the iterator's current state.


# 6. StopIteration

it = iter([10, 20])

print("First:", next(it))
print("Second:", next(it))

try:
    print(next(it))
except StopIteration:
    print("Iterator finished: StopIteration")

print()


# StopIteration is the iterator protocol's
# normal completion signal.


# 7. Why None Cannot Mean "Iteration Finished"

values = [10, None, 20]
it = iter(values)

print(next(it))
print(next(it))
print(next(it))

try:
    next(it)
except StopIteration:
    print("Finished")

print()


# None can itself be a valid element.
#
# Therefore:
#
# None
# -> possible data
#
# StopIteration
# -> iteration completion


# 8. Exhausted Iterator Stays Exhausted

it = iter([10])

print("Value:", next(it))

for attempt in range(2):
    try:
        next(it)
    except StopIteration:
        print(f"Attempt {attempt + 1}: still exhausted")

print()


# An exhausted iterator does not automatically restart.


# 9. Fresh Iterator from the Same Iterable

numbers = [10, 20]

it1 = iter(numbers)

print("it1:", next(it1))
print("it1:", next(it1))

try:
    next(it1)
except StopIteration:
    print("it1 exhausted")

it2 = iter(numbers)

print("it2 starts again:", next(it2))
print()


# Iterator exhaustion belongs to it1.
# The reusable list can provide another iterator.


# 10. Multiple Iterators Have Independent State

numbers = [10, 20, 30]

it1 = iter(numbers)
it2 = iter(numbers)

print("it1:", next(it1))
print("it1:", next(it1))
print("it2:", next(it2))
print("it1:", next(it1))
print("it2:", next(it2))
print()


# Conceptually:
#
# numbers ---> [10, 20, 30]
#                ^       ^
#                |       |
#               it1     it2
#
# Each iterator maintains its own traversal state.


# 11. Iterator Is Also Iterable

numbers = [10, 20, 30]

it = iter(numbers)

print("iter(it) is it:", iter(it) is it)
print("iter(numbers) is numbers:", iter(numbers) is numbers)
print()


# For an iterator:
#
# iter(iterator)
# -> returns the same iterator
#
# Therefore every iterator is iterable.
#
# But a list is iterable without itself being an iterator.


# 12. Iterable Is Not Necessarily an Iterator

numbers = [10, 20, 30]

print("List is iterable:", iter(numbers))

try:
    next(numbers)
except TypeError as error:
    print("next(numbers) TypeError:", error)

print()


# list:
# -> iterable
#
# list_iterator:
# -> iterator
#
# Every iterator is iterable,
# but not every iterable is an iterator.


# ============================================================
# PART 2 — FOR LOOP AND ITERATION PROTOCOL
# ============================================================

# 13. for Loop

numbers = [10, 20, 30]

for x in numbers:
    print("for value:", x)

print()


# Conceptual model:
#
# iterator = iter(numbers)
#
# repeatedly:
#
#     x = next(iterator)
#
# until:
#
#     StopIteration


# 14. Manual Version of the for-Loop Protocol

numbers = [10, 20, 30]
it = iter(numbers)

while True:
    try:
        x = next(it)
        print("manual value:", x)
    except StopIteration:
        break

print()


# This is a conceptual Python-level model
# of the iterator protocol used by a for loop.


# 15. for Loop Over a Partially Consumed Iterator

it = iter([10, 20, 30])

print("Manual first value:", next(it))

for x in it:
    print("for-loop value:", x)

print()


# Output:
#
# Manual first value: 10
# for-loop value: 20
# for-loop value: 30
#
# Why?
#
# for asks iter(it).
#
# Since it is already an iterator:
#
# iter(it) is it
#
# The loop continues from the current state.


# 16. Loop Variable Remains Bound

for x in [10, 20, 30]:
    pass

print("x after loop:", x)
print()


# A for statement does not create a new local scope.
#
# During the loop:
#
# x -> 10
# x -> 20
# x -> 30
#
# After the loop:
#
# x -> 30


# 17. Empty Iterable Does Not Bind a New Loop Variable

def empty_loop_demo():
    for value in []:
        pass

    try:
        print(value)
    except NameError:
        print("value was never bound")

empty_loop_demo()
print()


# ============================================================
# PART 3 — GENERATOR FUNCTIONS, yield, SUSPEND/RESUME
# ============================================================

# 18. Generator Function Creates a Generator Object

def simple_generator():
    yield 10
    yield 20


g = simple_generator()

print("g:", g)
print("Type:", type(g))
print("iter(g) is g:", iter(g) is g)
print()


# simple_generator
# -> generator function
#
# simple_generator()
# -> generator object
#
# A generator object is an iterator.


# 19. Calling a Generator Function Does Not Execute Its Body

def demo():
    print("Generator body started")
    yield 10


print("Before generator creation")
g = demo()
print("After generator creation")
print()


# "Generator body started" has not printed yet.
#
# Calling demo() creates the generator object.
# The body starts when the generator is consumed.


# 20. First next() Starts Execution

print("Before next")
value = next(g)
print("Yielded value:", value)
print("After next")
print()


# Flow:
#
# next(g)
#    |
#    v
# start demo()
#    |
# print(...)
#    |
# yield 10
#    |
# produce 10 + suspend


# 21. yield Suspends and next() Resumes

def execution_flow():
    print("A")
    yield 10

    print("B")
    yield 20

    print("C")


g = execution_flow()

print("First next returned:", next(g))
print("--- generator is suspended ---")

print("Second next returned:", next(g))
print("--- generator is suspended again ---")

try:
    next(g)
except StopIteration:
    print("Generator finished")

print()


# Execution:
#
# next(g)
# -> print A
# -> yield 10
# -> SUSPEND
#
# next(g)
# -> RESUME after yield 10
# -> print B
# -> yield 20
# -> SUSPEND
#
# next(g)
# -> RESUME after yield 20
# -> print C
# -> function ends
# -> StopIteration


# 22. Generator Preserves Local State

def counter():
    count = 0

    while count < 3:
        yield count
        count += 1


g = counter()

print(next(g))
print(next(g))
print(next(g))
print()


# The function does not restart with count = 0
# on every next().
#
# Its suspended execution state is preserved.


# 23. yield vs return

def normal_function():
    return 10
    print("Never reached")


def generator_function():
    yield 10
    print("Resumed after yield")
    yield 20


print("Normal function:", normal_function())

g = generator_function()

print("Generator first:", next(g))
print("Generator second:", next(g))
print()


# return:
# -> produce result
# -> terminate the function invocation
#
# yield:
# -> produce value
# -> suspend execution
# -> resume later


# 24. Generator Completion

def two_values():
    yield "A"
    yield "B"


g = two_values()

print(next(g))
print(next(g))

try:
    next(g)
except StopIteration:
    print("StopIteration after generator finishes")

print()


# ============================================================
# PART 4 — LAZY PRODUCTION AND GENERATOR EXPRESSIONS
# ============================================================

# 25. Lazy Production

def lazy_squares(n):
    for x in range(n):
        print("Producing square for:", x)
        yield x * x


g = lazy_squares(3)

print("Generator created")
print("Request 1:", next(g))
print("Request 2:", next(g))
print("Request 3:", next(g))
print()


# Values are produced only as iteration requests them.


# 26. Generator Used by for Loop

def squares(n):
    for x in range(n):
        yield x * x


for value in squares(4):
    print(value)

print()


# Generator object
#     |
#   iter()
#     |
# same generator
#     |
# repeated next()
#     |
# yield values
#     |
# StopIteration


# 27. Generator Expression

g = (x * x for x in range(5))

print("g:", g)
print("Type:", type(g))
print("First:", next(g))
print("Second:", next(g))
print()


# (expression for item in iterable)
# -> generator expression
# -> generator object


# 28. List Comprehension vs Generator Expression

list_result = [x * x for x in range(5)]
generator_result = (x * x for x in range(5))

print("List:", list_result)
print("List type:", type(list_result))

print("Generator:", generator_result)
print("Generator type:", type(generator_result))
print()


# [x * x for x in range(5)]
# -> creates a list
# -> results are materialized
#
# (x * x for x in range(5))
# -> creates a generator
# -> results are produced lazily


# 29. Generator Expression Is Not a Tuple

g = (x for x in [10, 20, 30])

print("Type:", type(g))
print("As tuple after consumption:", tuple(g))
print()


# Parentheses around a comprehension-style generator expression
# create a generator, not a tuple of all results.


# 30. list() Consumes a Generator

g = (x * x for x in range(3))

first_list = list(g)
second_list = list(g)

print("First list(g):", first_list)
print("Second list(g):", second_list)
print()


# First list(g):
# -> consumes 0, 1, 4
#
# Generator becomes exhausted.
#
# Second list(g):
# -> no values remain
# -> []


# 31. Partial Consumption + list()

g = (x * 10 for x in range(5))

print("First manual value:", next(g))
print("Remaining values:", list(g))
print()


# The same generator state is shared across
# next(), for, list(), tuple(), etc.


# 32. Lazy Evaluation Becomes Visible

def announce(x):
    print("Computing:", x)
    return x * 2


g = (announce(x) for x in range(3))

print("Expression created")
print("First result:", next(g))
print("Remaining:", list(g))
print()


# Creating the generator expression does not
# immediately call announce() for every value.
#
# Consumption drives computation.


# ============================================================
# PART 5 — DECORATORS
# ============================================================

# 33. Functions Are Objects

def greet():
    print("Hello")


another = greet

print("greet:", greet)
print("another:", another)
print("another is greet:", another is greet)
print()


# Two names can refer to the same function object.


# 34. Function Reference vs Function Call

def message():
    print("Python")


function_object = message

print("Function reference:", function_object)
print("Calling now:")
function_object()
print()


# message
# -> function object reference
#
# message()
# -> call the function


# 35. Passing a Function as an Argument

def execute(operation):
    return operation(5)


def square(x):
    return x * x


print("execute(square):", execute(square))
print()


# operation and square refer to the same
# function object during execute().


# 36. Returning an Inner Function

def outer():
    def inner():
        return "Inside"

    return inner


f = outer()

print("f:", f)
print("f():", f())
print()


# return inner
# -> return function object
#
# return inner()
# -> call inner and return its result


# 37. Manual Decorator

def decorate(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def hello():
    print("Hello")


new_hello = decorate(hello)

new_hello()
print()


# Object model:
#
# new_hello ---> wrapper
#                  |
#                  | closure
#                  v
#             original hello


# 38. Decorator Closure Inspection

def decorate(func):
    def wrapper():
        return func()

    return wrapper


def original():
    return "Original result"


wrapped = decorate(original)

print("wrapped():", wrapped())
print("Free variables:", wrapped.__code__.co_freevars)

if wrapped.__closure__:
    print(
        "Captured function is original:",
        wrapped.__closure__[0].cell_contents is original
    )

print()


# wrapper retains access to func through a closure.


# 39. @decorator Syntax

def logger(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")

    return wrapper


@logger
def say_python():
    print("Python")


say_python()
print()


# Conceptually:
#
# say_python = logger(say_python)
#
# After decoration:
#
# say_python ---> wrapper
#                   |
#                   | closure
#                   v
#             original say_python


# 40. Decorated Name References Wrapper

def decorate(func):
    def wrapper():
        return func()

    return wrapper


@decorate
def sample():
    return 10


print("sample.__name__ without wraps:", sample.__name__)
print()


# The name sample now refers to the returned wrapper.
# Therefore its __name__ is "wrapper" without metadata preservation.


# 41. Problem with a Zero-Argument Wrapper

def no_argument_decorator(func):
    def wrapper():
        return func()

    return wrapper


@no_argument_decorator
def add(a, b):
    return a + b


try:
    add(10, 20)
except TypeError as error:
    print("TypeError:", error)

print()


# add(10, 20)
# actually calls:
#
# wrapper(10, 20)
#
# But wrapper() accepts zero arguments.


# 42. Decorator with *args and **kwargs

def flexible_decorator(func):
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return func(*args, **kwargs)

    return wrapper


@flexible_decorator
def introduce(name, age, city="Unknown"):
    return f"{name}, {age}, {city}"


print(introduce("Ravi", 21, city="Vijayawada"))
print()


# In wrapper definition:
#
# *args
# -> collects positional arguments
#
# **kwargs
# -> collects keyword arguments
#
# In:
#
# func(*args, **kwargs)
#
# *args
# -> expands positional arguments
#
# **kwargs
# -> expands keyword arguments


# 43. Decorator Preserving Return Value

def trace(func):
    def wrapper(*args, **kwargs):
        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@trace
def multiply(a, b):
    print("Multiplying")
    return a * b


x = multiply(4, 5)

print("Returned to caller:", x)
print()


# Flow:
#
# multiply(4, 5)
#      |
#      v
# wrapper(4, 5)
#      |
# print Before
#      |
# original multiply(4, 5)
#      |
# return 20
#      |
# result = 20
#      |
# print After
#      |
# return 20
#      |
# x = 20


# 44. Wrapper Swallows Result If It Does Not Return

def broken_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Original returned inside wrapper:", result)
        # no return result

    return wrapper


@broken_decorator
def subtract(a, b):
    return a - b


answer = subtract(10, 3)

print("Caller receives:", answer)
print()


# Original function:
# -> returns 7 to wrapper
#
# Wrapper:
# -> reaches its end
# -> implicitly returns None
#
# Caller:
# -> receives None


# 45. Metadata Problem Without functools.wraps

def plain_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@plain_decorator
def divide(a, b):
    """Divide a by b."""
    return a / b


print("divide.__name__:", divide.__name__)
print("divide.__doc__:", divide.__doc__)
print()


# divide now refers to wrapper.
# The original function's metadata is not
# automatically exposed through that wrapper.


# 46. functools.wraps Preserves Important Metadata

from functools import wraps


def metadata_preserving_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@metadata_preserving_decorator
def power(base, exponent):
    """Raise base to exponent."""
    return base ** exponent


print("power(2, 5):", power(2, 5))
print("power.__name__:", power.__name__)
print("power.__doc__:", power.__doc__)
print("Has __wrapped__:", hasattr(power, "__wrapped__"))
print()


# @wraps(func)
# -> wrapper still exists
# -> important metadata is updated from func
# -> __wrapped__ points to the wrapped function


# 47. Inspecting __wrapped__

print("Decorated callable:", power)
print("Original callable:", power.__wrapped__)
print(
    "Original name:",
    power.__wrapped__.__name__
)
print()


# Conceptually:
#
# power ---> wrapper
#              |
#              +---- closure ------> original power
#              |
#              +---- __wrapped__ --> original power


# 48. Complete General Decorator Pattern

def timer_like(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")

        return result

    return wrapper


@timer_like
def predict(x, scale=2):
    """Simple prediction example."""
    return x * scale


prediction = predict(5, scale=3)

print("Prediction:", prediction)
print("Name:", predict.__name__)
print("Doc:", predict.__doc__)
print()


# ============================================================
# PART 6 — CONCEPT MIX
# ============================================================

# 49. Generator + for Loop + Lazy Transformation

def generate_numbers(limit):
    for number in range(limit):
        print("Generating:", number)
        yield number


squares = (x * x for x in generate_numbers(4))

for value in squares:
    print("Square:", value)

print()


# Flow:
#
# for asks generator expression for a value
#      |
# generator expression asks generate_numbers
#      |
# generate_numbers yields one number
#      |
# expression squares it
#      |
# for receives one result
#      |
# repeat lazily


# 50. Decorator + Generator Function

def log_generator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Creating generator from:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log_generator
def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number


g = even_numbers(6)

print("Generator returned:", g)

for value in g:
    print("Even:", value)

print()


# Important:
#
# wrapper calls even_numbers(...)
#
# Since even_numbers is a generator function,
# that call creates and returns a generator object.
#
# The generator body itself is then driven later
# by the for loop.


# 51. Decorator Around Generator Consumption

def trace_iteration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Generator wrapper started")

        for value in func(*args, **kwargs):
            print("Wrapper saw:", value)
            yield value

        print("Generator wrapper finished")

    return wrapper


@trace_iteration
def model_inputs():
    yield 10
    yield 20
    yield 30


for item in model_inputs():
    print("Consumer received:", item)

print()


# This mixes:
#
# decorator
#     +
# closure
#     +
# *args / **kwargs
#     +
# generator function
#     +
# yield
#     +
# for-loop iteration protocol


# 52. Lazy Data Pipeline Mental Model

def source():
    for value in range(1, 6):
        print("SOURCE:", value)
        yield value


def transform(values):
    for value in values:
        print("TRANSFORM:", value)
        yield value * 10


pipeline = transform(source())

print("Pipeline created")
print("First pipeline result:", next(pipeline))
print("Remaining pipeline results:", list(pipeline))
print()


# Conceptual AI/ML-style pipeline:
#
# source
#   |
#   v
# one item
#   |
#   v
# transform
#   |
#   v
# consumer
#
# Values flow progressively instead of requiring
# every transformed value to be materialized first.


# ============================================================
# DAY 4 CORE MODEL
# ============================================================

"""
ITERABLE:

    An object from which Python can obtain
    an iterator.

    Examples:

        list
        tuple
        str
        dict
        set
        range


iter(iterable):

    Obtains an iterator.

    It does NOT convert the original iterable
    object into an iterator.


ITERATOR:

    A stateful object that produces successive
    values during iteration.


next(iterator):

    Requests the next item and advances
    iterator state.


__iter__():

    Part of Python's iteration protocol.

    For an iterator:

        iter(iterator) is iterator


__next__():

    Produces the next value or signals
    completion with StopIteration.


StopIteration:

    Normal iterator-completion signal.

    It is separate from None because None
    can itself be valid data.


ITERATOR STATE:

    Belongs to the iterator object.

    Calling next(iterator) advances that
    iterator's traversal state.

    It does not remove values from a list.


MULTIPLE ITERATORS:

    Two iterators created from the same
    iterable can maintain independent states.


EXHAUSTION:

    Once an iterator reaches its end,
    it remains exhausted.

    A reusable iterable such as a list
    can usually provide a fresh iterator.


ITERABLE VS ITERATOR:

    Every iterator is iterable.

    Not every iterable is an iterator.


FOR LOOP:

    Conceptually:

        iterator = iter(iterable)

        repeatedly:
            value = next(iterator)

        until:
            StopIteration

    The for statement handles normal
    iteration completion automatically.


GENERATOR FUNCTION:

    A function containing yield.

    Calling it creates a generator object.


GENERATOR OBJECT:

    An iterator whose execution can suspend
    and resume.


GENERATOR CREATION:

    g = generator_function()

    Creates the generator object.

    The function body does not begin normal
    execution merely because the generator
    object was created.


next(generator):

    Starts or resumes generator execution.


yield:

    Produces a value and suspends execution.

    The generator can later resume after
    that yield point.


SUSPENDED STATE:

    The generator retains the execution
    context needed to continue later,
    including relevant local state.


return VS yield:

    return:
        produce result
        terminate invocation

    yield:
        produce value
        suspend execution


GENERATOR COMPLETION:

    When the generator function finishes,
    iteration completes via StopIteration.


LAZY PRODUCTION:

    Values are produced as an iteration
    consumer requests them.

    They do not all need to be materialized
    in advance.


GENERATOR EXPRESSION:

    (expression for item in iterable)

    Creates a generator object.


LIST COMPREHENSION:

    [expression for item in iterable]

    Creates a list containing the
    materialized results.


GENERATOR CONSUMPTION:

    A generator can be consumed by:

        next(g)
        for x in g
        list(g)
        tuple(g)
        other iteration consumers


GENERATOR EXHAUSTION:

    The same generator object is single-pass.

    Once exhausted, it does not
    automatically restart.


FUNCTION OBJECTS:

    Functions are objects.

    They can be:

        stored in names
        passed as arguments
        returned from functions


FUNCTION REFERENCE:

    function_name

    Refers to the function object.


FUNCTION CALL:

    function_name()

    Calls the function.


DECORATOR:

    A callable that receives another callable
    and returns a callable.

    A common pattern creates a wrapper around
    the original function.


WRAPPER:

    A function that surrounds the original
    function call with additional behavior.


DECORATOR + CLOSURE:

    wrapper retains access to func from
    the enclosing decorator scope.


@decorator:

    For a basic function decorator, the
    central mental model is:

        function = decorator(function)


AFTER DECORATION:

    In a wrapper-based decorator:

        name ---> wrapper
                    |
                    | closure
                    v
                 original


*args IN WRAPPER DEFINITION:

    Collects positional arguments into
    a tuple.


**kwargs IN WRAPPER DEFINITION:

    Collects keyword arguments into
    a dictionary.


func(*args, **kwargs):

    Expands the collected arguments and
    forwards them to the wrapped function.


RETURN-VALUE PRESERVATION:

    result = func(*args, **kwargs)
    return result

    The wrapper must return the original
    result if the caller should receive it.


MISSING WRAPPER RETURN:

    If wrapper reaches its end without
    return result:

        caller receives None


functools.wraps:

    Commonly used on wrapper functions to
    preserve important metadata from the
    wrapped function.


__wrapped__:

    functools.wraps establishes a reference
    to the wrapped callable, supporting
    introspection and tooling.


DAY 4 CORE FLOW:

    ITERATION:

        iterable
            |
          iter()
            v
        iterator
            |
          next()
            v
          value
            |
           ...
            v
        StopIteration


    GENERATOR:

        generator function
            |
           call
            v
        generator object
            |
          next()
            v
           run
            |
          yield
          /   \
         /     \
      value   suspend
                |
              next()
                |
              resume


    GENERATOR EXPRESSION:

        (expression for x in iterable)
                    |
                    v
             generator object
                    |
                    v
              lazy production


    DECORATOR:

        original function
                |
                v
             decorator
                |
                v
              wrapper
                |
                +---- closure ----> original
                |
                +---- *args/**kwargs
                |
                +---- return result
                |
                +---- functools.wraps
                |
                v
          decorated function name


AI/ML CONNECTION:

    Iterators and generators provide the
    mental model for progressive data flow:

        data source
            |
            v
        one item / batch
            |
            v
        transform
            |
            v
        consumer / model

    Decorators provide a reusable pattern
    for cross-cutting behavior such as:

        logging
        timing
        tracing
        validation
        caching
        instrumentation

    Library-specific behavior should still
    be learned from that library's official
    documentation rather than assuming every
    ML data API is a plain Python generator.
"""
