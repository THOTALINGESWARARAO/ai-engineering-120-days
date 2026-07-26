# Day 3 — Packing, Unpacking, Lambda & Closures

## 1. Sequence Packing

**Packing** means combining multiple values into a single tuple.

```python
values = 10, 20, 30
```

Python packs the values:

```text
10, 20, 30
     ↓
   packing
     ↓
(10, 20, 30)
```

Therefore:

```python
print(values)
print(type(values))
```

produces:

```text
(10, 20, 30)
<class 'tuple'>
```

The important syntax is the **comma**, not the parentheses.

For example:

```python
value = 10,
```

creates:

```text
(10,)
```

not:

```text
10
```

### Core rule

```text
comma-separated values
        ↓
usually form a tuple
```

---

# 2. Sequence Unpacking

Unpacking performs the reverse conceptual operation.

```python
a, b, c = (10, 20, 30)
```

Python distributes elements to targets:

```text
(10, 20, 30)
      ↓
   unpack
      ↓
a     b     c
│     │     │
▼     ▼     ▼
10    20    30
```

Final bindings:

```text
a ───► 10
b ───► 20
c ───► 30
```

Unpacking is not restricted to tuples.

```python
a, b, c = [10, 20, 30]
```

also works.

So it is better to think in terms of **iterables**, not just tuples.

---

# 3. Unpacking Requires Compatible Counts

Consider:

```python
a, b = [10, 20, 30]
```

There are:

```text
2 targets
3 values
```

Python cannot complete the unpacking.

Result:

```text
ValueError
```

Similarly:

```python
a, b, c = [10, 20]
```

also raises `ValueError`.

Conceptually:

```text
ordinary unpacking

number of targets
        ↕
number of produced values

must match
```

Extended unpacking gives us a way to relax this requirement.

---

# 4. Extended Iterable Unpacking

A starred target can collect multiple values.

```python
first, *middle, last = [10, 20, 30, 40, 50]
```

Bindings:

```text
first  ───► 10

middle ───► [20, 30, 40]

last   ───► 50
```

Conceptually:

```text
[10, 20, 30, 40, 50]
  │   └──────┬──────┘  │
  ▼          ▼          ▼
first      *middle     last
  │          │          │
  ▼          ▼          ▼
 10     [20,30,40]      50
```

---

# 5. Starred Assignment Target

The starred target collects zero or more values.

```python
first, *rest = [10, 20, 30]
```

Result:

```text
first ───► 10
rest  ───► [20, 30]
```

It can also collect zero values:

```python
first, *middle, last = [10, 20]
```

Result:

```text
first  ───► 10
middle ───► []
last   ───► 20
```

An important detail:

> A starred assignment target receives a **list**.

Even if the source is a tuple:

```python
first, *rest = (10, 20, 30)
```

`rest` is:

```text
[20, 30]
```

and its type is:

```text
list
```

---

# 6. `*` Means Different Things in Different Contexts

One of the most useful Day 3 distinctions is:

```text
* in assignment target
        ↓
      COLLECT


* in expression/call
        ↓
      EXPAND
```

For example:

```python
first, *rest = [10, 20, 30]
```

means:

```text
*rest
   ↓
collect
   ↓
[20, 30]
```

But:

```python
numbers = [10, 20, 30]

result = [0, *numbers, 40]
```

means:

```text
*numbers
    ↓
expand
    ↓
10, 20, 30
```

giving:

```text
[0, 10, 20, 30, 40]
```

---

# 7. Starred Expressions

Consider:

```python
numbers = (10, 20, 30)

result = [*numbers]
```

`*numbers` expands the iterable:

```text
numbers
   │
   ▼
(10,20,30)
   │
   ▼
*numbers
   │
   ▼
10, 20, 30
```

The surrounding syntax then determines the resulting container:

```python
[*numbers]
```

gives:

```text
[10, 20, 30]
```

while:

```python
(*numbers,)
```

gives:

```text
(10, 20, 30)
```

### Important rule

```text
source iterable type
        ≠
necessarily resulting container type
```

The surrounding expression determines the new container.

---

# 8. `*` Iterable Unpacking in Function Calls

At a function call site:

```text
*iterable
     ↓
expand into positional arguments
```

Example:

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

add(*numbers)
```

Conceptually:

```text
numbers
   │
   ▼
[10,20,30]
   │
   ▼
*numbers
   │
   ▼
10, 20, 30
│    │    │
▼    ▼    ▼
a    b    c
```

Therefore:

```python
add(*numbers)
```

behaves like:

```python
add(10, 20, 30)
```

---

# 9. `*` Can Expand Other Iterables

The source doesn't need to be a list.

For example:

```python
def show(a, b, c):
    print(a)
    print(b)
    print(c)

show(*"AI!")
```

The string is iterable:

```text
"AI!"
 ↓
'A', 'I', '!'
```

So the call behaves like:

```python
show("A", "I", "!")
```

Bindings:

```text
a ───► "A"
b ───► "I"
c ───► "!"
```

---

# 10. `**` Mapping Unpacking in Calls

`**` at a call site expands a mapping into **keyword arguments**.

```python
def introduce(name, age):
    print(name, age)

person = {
    "name": "Ravi",
    "age": 21
}

introduce(**person)
```

Conceptually:

```text
{
    "name": "Ravi",
    "age": 21
}

        ↓ **

name="Ravi", age=21
```

So:

```python
introduce(**person)
```

behaves like:

```python
introduce(name="Ravi", age=21)
```

---

# 11. Mapping Keys Become Keyword Names

This is important.

For:

```python
person = {
    "name": "Ravi",
    "age": 21
}
```

the keys correspond to keyword names:

```text
"name" ───► name=
"age"  ───► age=
```

If instead:

```python
person = {
    "name": "Ravi",
    "years": 21
}
```

then:

```python
introduce(**person)
```

conceptually becomes:

```python
introduce(
    name="Ravi",
    years=21
)
```

If `introduce()` does not accept `years`, argument binding fails with a `TypeError`.

---

# 12. Duplicate Argument Binding

Consider:

```python
def introduce(name, age):
    print(name, age)

person = {
    "name": "Ravi",
    "age": 21
}

introduce("Krishna", **person)
```

First:

```text
"Krishna" ───► name
```

Then `**person` attempts:

```text
"Ravi" ───► name
21     ───► age
```

Now `name` has been supplied twice.

```text
"Krishna" ─────┐
               ▼
              name
               ▲
               │
"Ravi" ─────────┘
```

Result:

```text
TypeError
```

Keyword arguments do not simply override already-bound positional arguments in the same call.

---

# 13. Complete `*` / `**` Mental Model

Context determines the behavior.

```text
ASSIGNMENT

a, *rest = iterable

*rest
  ↓
COLLECT
  ↓
list
```

At a call site:

```text
function(*iterable)

*
↓
EXPAND
↓
positional arguments
```

And:

```text
function(**mapping)

**
↓
EXPAND
↓
keyword arguments
```

This also connects directly to Day 2:

```text
FUNCTION DEFINITION

*args
  ↓
COLLECT extra positional arguments

**kwargs
  ↓
COLLECT extra keyword arguments


FUNCTION CALL

*iterable
  ↓
EXPAND positional arguments

**mapping
  ↓
EXPAND keyword arguments
```

---

# 14. Unpacking Error Types

It is useful to distinguish assignment unpacking from function-call argument binding.

Assignment:

```python
a, b = [10, 20, 30]
```

fails with:

```text
ValueError
```

because the iterable cannot be unpacked into the requested targets.

Function call:

```python
def add(a, b):
    pass

add(*[10, 20, 30])
```

fails with:

```text
TypeError
```

because function argument binding fails.

---

# 15. Lambda Expressions

A lambda expression creates an anonymous function.

General form:

```python
lambda parameters: expression
```

Example:

```python
lambda x: x ** 2
```

The critical mental model is:

```text
lambda expression
       │
       ▼
creates function object
```

It does **not** immediately evaluate `x ** 2`.

---

# 16. Lambda Creates a Function Object

Consider:

```python
square = lambda x: x ** 2
```

Conceptually:

```text
lambda x: x ** 2
        │
        ▼
   function object
        ▲
        │
      square
```

Therefore:

```python
type(square)
```

is:

```text
<class 'function'>
```

There is not a separate ordinary runtime type called a "lambda object."

Lambda is syntax for creating a function object.

---

# 17. Function Creation vs Function Execution

Consider:

```python
f = lambda x: x * 10
```

At this point:

```text
function created
      ✓

function body executed
      ✗
```

Only:

```python
f(5)
```

calls the function.

Then:

```text
x ───► 5

x * 10
   ↓
50
```

So:

```python
f(5)
```

returns:

```text
50
```

### Core rule

```text
lambda expression
      ↓
function creation

function(...)
      ↓
function execution
```

---

# 18. Lambda Has an Expression-Based Body

The syntax is:

```python
lambda parameters: expression
```

Example:

```python
lambda a, b: a + b
```

The part:

```python
a + b
```

is an expression.

When the function is called, Python evaluates that expression.

---

# 19. Lambda's Implicit Returned Value

Consider:

```python
add = lambda a, b: a + b
```

Then:

```python
result = add(10, 20)
```

Execution:

```text
a ───► 10
b ───► 20

a + b
  ↓
30
  ↓
function result
```

Therefore:

```text
result ───► 30
```

Lambda doesn't use an explicit `return` statement.

The expression's value becomes the result of calling the lambda function.

---

# 20. Expressions vs Statements in Lambda

A lambda body must be an **expression**.

This is valid:

```python
lambda x: x * 2
```

This is also valid:

```python
lambda x: print(x)
```

because a function call is an expression.

`print(x)` evaluates to `None`, so the lambda returns `None` after printing.

But:

```python
lambda x: return x
```

is invalid because `return` is a statement.

Similarly:

```python
lambda x: x = 10
```

is invalid because ordinary assignment is a statement.

### Precise rule

Do not think:

```text
lambda cannot perform actions
```

Think:

```text
lambda body must be an expression
```

---

# 21. Lambda vs Normal `def` Return Behavior

Compare:

```python
f = lambda x: x ** 2
```

with:

```python
def g(x):
    x ** 2
```

Calling:

```python
f(4)
```

returns:

```text
16
```

because the lambda expression's value becomes the function result.

But:

```python
g(4)
```

returns:

```text
None
```

because:

```python
x ** 2
```

is evaluated but not explicitly returned.

To make `g` equivalent:

```python
def g(x):
    return x ** 2
```

---

# 22. Lambda vs `def`

Compare:

```python
def square(x):
    return x ** 2
```

and:

```python
square = lambda x: x ** 2
```

Both create function objects, but they are not identical language constructs.

```text
def
 │
 ├── function definition statement
 ├── supports a suite of statements
 ├── explicit return
 └── suitable for substantial logic


lambda
 │
 ├── expression
 ├── creates function object
 ├── body is one expression
 └── expression value becomes result
```

A useful rule is:

```text
small inline function
        ↓
lambda may be useful

multi-step logic
        ↓
prefer def
```

---

# 23. Lambda Function `__name__`

Functions are objects and expose attributes.

For:

```python
def square(x):
    return x ** 2
```

```python
square.__name__
```

gives:

```text
square
```

Now:

```python
double = lambda x: x * 2
```

`double` is the name referring to the function object.

But:

```python
double.__name__
```

is normally:

```text
<lambda>
```

Mental model:

```text
double ─────► function object
                  │
                  └── __name__ → "<lambda>"
```

The variable name and the function object's own metadata should not be treated as the same concept.

---

# 24. Higher-Order Functions

A **higher-order function** can accept functions as arguments, return functions, or otherwise operate with functions as values.

Because Python functions are objects:

```text
function object
      ↓
can be passed as argument
```

This makes lambda particularly useful when a small function is required inline.

---

# 25. Lambda with `sorted()`

Consider:

```python
words = ["AI", "Python", "ML"]

result = sorted(
    words,
    key=lambda word: len(word)
)
```

The lambda is passed as the `key` function.

Conceptually:

```text
"AI"
  ↓
lambda
  ↓
2

"Python"
  ↓
lambda
  ↓
6

"ML"
  ↓
lambda
  ↓
2
```

These key values guide sorting.

Result:

```python
["AI", "ML", "Python"]
```

The original elements are returned in sorted order.

The key values themselves are not the output.

---

# 26. `key=` Mental Model

Consider:

```python
students = [
    ("Ravi", 85),
    ("Anu", 92),
    ("Kiran", 78)
]
```

Then:

```python
sorted(
    students,
    key=lambda student: student[1]
)
```

The lambda extracts:

```text
("Ravi", 85)  ───► 85
("Anu", 92)   ───► 92
("Kiran", 78) ───► 78
```

Python uses those values to determine ordering:

```text
78 < 85 < 92
```

Then returns the original objects reordered:

```python
[
    ("Kiran", 78),
    ("Ravi", 85),
    ("Anu", 92)
]
```

Mental model:

```text
original object
      ↓
 key function
      ↓
comparison key
      ↓
sorting
      ↓
original objects reordered
```

---

# 27. Nested Functions

Python allows functions to be defined inside functions.

```python
def outer():
    def inner():
        print("Hello")

    inner()
```

Here:

```text
outer
  │
  └── inner
```

`inner` is lexically nested inside `outer`.

This connects directly to Day 2's **Enclosing scope**.

---

# 28. Enclosing Scope Revisited

Consider:

```python
def outer():
    x = 10

    def inner():
        print(x)

    inner()
```

Inside `inner()`:

```text
L → Local
x not found

E → Enclosing
x ───► 10
```

Therefore:

```text
10
```

is printed.

At this point, ordinary LEGB explains the behavior because `outer()` is still executing.

Closures become more interesting when the inner function survives beyond the enclosing function call.

---

# 29. Returning an Inner Function

Consider:

```python
def outer():
    x = 10

    def inner():
        print(x)

    return inner

f = outer()
```

Notice:

```python
return inner
```

not:

```python
return inner()
```

The first returns the function object.

The second would call the function and return its result.

Therefore:

```text
outer()
   │
   ▼
creates inner function
   │
   ▼
return inner
   │
   ▼
f ───► inner function object
```

`inner()` has not yet executed.

---

# 30. The Closure Problem

Now:

```python
f = outer()
```

has finished executing `outer()`.

But later:

```python
f()
```

still prints:

```text
10
```

This raises the important question:

```text
outer() has returned
       ↓
why can inner still access x?
```

The answer leads to **closures**.

---

# 31. Free Variables

Consider:

```python
def outer():
    x = 10

    def inner():
        y = 20
        return x + y

    return inner
```

From `inner`'s perspective:

```text
y
↓
bound inside inner
↓
local variable
```

But:

```text
x
↓
referenced by inner
↓
not locally bound in inner
↓
obtained from enclosing function scope
↓
free variable
```

So:

```text
inner locals:
y

inner free variables:
x
```

---

# 32. Not Every Outer Variable Is Captured

Consider:

```python
def outer():
    x = 10
    message = "Hello"

    def inner():
        return x

    return inner
```

`inner` references:

```text
x
```

but not:

```text
message
```

Therefore `x` participates as a free variable of `inner`, while `message` does not merely because it exists in `outer`.

### Core idea

```text
outer variable exists
        ≠
automatically captured

inner actually references binding
        ↓
relevant to closure
```

---

# 33. What Makes a Closure?

A useful mental model is:

> A closure is a function together with retained access to bindings for free variables from its enclosing function scopes.

Consider:

```python
def outer():
    x = 10

    def inner():
        return x

    return inner
```

Conceptually:

```text
outer execution
      │
      ├── x binding
      │
      └── inner function
                │
                └── needs x
```

When `inner` escapes:

```text
f ───► inner function
           │
           ▼
    retained access
           │
           ▼
       x binding
```

This is more precise than saying:

```text
"inner remembers outer"
```

The entire outer function execution does not need to be thought of as a frozen snapshot.

---

# 34. Closure Cells

Python uses **cell objects** as part of its closure machinery.

A useful conceptual model is:

```text
function object
      │
      ▼
closure
      │
      ▼
cell
      │
      ▼
captured binding/object
```

For:

```python
def outer():
    x = 10

    def inner():
        return x

    return inner
```

think:

```text
inner function
      │
      ▼
closure cell
      │
      ▼
     10
```

The cell provides the indirection needed for the captured binding.

---

# 35. `co_freevars`

Python lets us inspect the names of a function's free variables.

```python
f.__code__.co_freevars
```

For our example:

```text
('x',)
```

This means `x` is a free-variable name used by the function.

The trailing comma indicates a one-element tuple:

```text
('x',)
```

not simply:

```text
'x'
```

---

# 36. `__closure__`

Function objects expose:

```python
f.__closure__
```

When closure cells exist, this is a tuple containing cell objects.

Conceptually:

```text
f
│
└── __closure__
        │
        ▼
     (cell,)
        │
        ▼
       10
```

If no closure cells are needed:

```python
f.__closure__
```

can be:

```text
None
```

---

# 37. `cell_contents`

The contents of a closure cell can be inspected:

```python
f.__closure__[0].cell_contents
```

For:

```python
x = 10
```

the result is:

```text
10
```

We can connect the introspection:

```text
co_freevars        __closure__
───────────        ───────────
('x',)             (cell,)
   │                  │
   └──────────────────┤
                      ▼
                     10
```

So:

```text
co_freevars
→ names

__closure__
→ cells

cell_contents
→ object currently contained/referenced through cell
```

---

# 38. Global Lookup Is Not the Same as Closure Capture

Consider:

```python
x = 100

def outer():
    def inner():
        return x

    return inner
```

From `inner`:

```text
L → x not found
E → x not found
G → x = 100
```

`x` comes from the global scope.

So this should not be mentally modeled as `inner` capturing `outer`'s `x`, because `outer` has no such binding.

Conceptually:

```text
inner
  │
  ▼
global lookup
  │
  ▼
x ───► 100
```

A nested function does **not automatically** have meaningful captured enclosing state.

---

# 39. Independent Closure State

Consider:

```python
def outer():
    x = 10

    def inner():
        return x

    return inner

f1 = outer()
f2 = outer()
```

There were two separate executions of `outer()`.

Conceptually:

```text
outer() call #1
      │
      ▼
cell #1 → x → 10
      ▲
      │
     f1


outer() call #2
      │
      ▼
cell #2 → x → 10
      ▲
      │
     f2
```

Even though both values are `10`, the closure cells are independent.

Therefore conceptually:

```python
f1.__closure__[0] is f2.__closure__[0]
```

is:

```text
False
```

This is how closures can maintain independent state.

---

# 40. Retained State with Closures

Consider:

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

Now:

```python
counter = make_counter()
```

creates:

```text
counter
   │
   ▼
increment function
   │
   ▼
closure cell
   │
   ▼
count → 0
```

Calling:

```python
counter()
```

changes:

```text
count
0 → 1
```

Calling again:

```text
1 → 2
```

and again:

```text
2 → 3
```

The state survives between calls because the returned function retains access to the captured binding.

---

# 41. Independent Counters

```python
counter1 = make_counter()
counter2 = make_counter()
```

Each `make_counter()` call creates independent captured state.

```text
counter1
   │
   ▼
cell #1
count → 0


counter2
   │
   ▼
cell #2
count → 0
```

Therefore:

```python
counter1()  # 1
counter1()  # 2

counter2()  # 1

counter1()  # 3
```

The counters do not interfere with one another.

---

# 42. Closures + `nonlocal`

Inside:

```python
def increment():
    nonlocal count
    count += 1
```

`nonlocal count` tells Python that rebinding `count` should target the suitable enclosing function binding.

Without `nonlocal`:

```python
def increment():
    count += 1
```

assignment causes `count` to be treated as local to `increment`.

Conceptually:

```text
LOCAL increment()
count → unbound
```

Then:

```python
count += 1
```

needs to read the local `count` before rebinding it.

But it has no value yet.

Result:

```text
UnboundLocalError
```

---

# 43. Closure Mutation vs Rebinding

This directly connects Day 1, Day 2 and Day 3.

Consider:

```python
def outer():
    values = []

    def add(x):
        values.append(x)
        return values

    return add
```

No `nonlocal` is required.

Why?

Because:

```python
values.append(x)
```

does not rebind `values`.

It mutates the existing list.

```text
closure binding
      │
      ▼
values ───► []
             ↓ mutate
values ───► [10]
             ↓ mutate
values ───► [10,20]
```

The binding remains.

---

# 44. Rebinding Requires `nonlocal`

Now:

```python
def outer():
    values = []

    def add(x):
        values = values + [x]
        return values

    return add
```

This contains:

```python
values = ...
```

That is rebinding.

Without `nonlocal`, `values` becomes local to `add`, causing an `UnboundLocalError` when the right side attempts to read it.

To target the enclosing binding:

```python
def add(x):
    nonlocal values
    values = values + [x]
    return values
```

### Core distinction

```text
values.append(x)
        ↓
mutation
        ↓
no rebinding


values = values + [x]
        ↓
rebinding
        ↓
nonlocal needed to target enclosing binding
```

---

# 45. Closures Capture Bindings, Not Frozen Snapshots

This is one of the deepest Day 3 ideas.

Consider:

```python
def outer():
    x = 10

    def inner():
        return x

    x = 50

    return inner
```

Then:

```python
f = outer()

print(f())
```

returns:

```text
50
```

Why not `10`?

Because a better mental model is not:

```text
inner created
     ↓
save x's current value forever
     ↓
10
```

Instead:

```text
inner
  │
  ▼
captured binding/cell for x
  │
  ├── initially → 10
  │
  └── later     → 50
```

When `inner()` eventually reads `x`, it obtains the value through that captured binding.

### Core rule

```text
closure
   ↓
retained access to binding

NOT necessarily
   ↓
frozen snapshot of old value
```

---

# 46. Late Binding

This captured-binding model explains an important Python behavior.

```python
def create_functions():
    functions = []

    for i in range(3):
        functions.append(lambda: i)

    return functions
```

During the loop:

```text
iteration 1
i → 0
create lambda #1

iteration 2
i → 1
create lambda #2

iteration 3
i → 2
create lambda #3
```

A tempting but incorrect mental model is:

```text
lambda #1 → saved 0
lambda #2 → saved 1
lambda #3 → saved 2
```

Instead, the lambdas reference the same relevant enclosing `i` binding.

After the loop:

```text
                         ┌── lambda #1
                         │
i binding → 2 ◄──────────┼── lambda #2
                         │
                         └── lambda #3
```

Therefore:

```python
f1, f2, f3 = create_functions()

f1()
f2()
f3()
```

produce:

```text
2
2
2
```

This behavior is commonly described as **late binding**.

---

# 47. Why the Lambda Did Not Save `i`

Remember:

```python
lambda: i
```

creates a function.

It does not immediately evaluate and store the result of `i`.

Conceptually it means:

```text
"When I am called,
resolve/read i."
```

Therefore:

```text
function creation time
        ↓
don't necessarily freeze i's current value

function call time
        ↓
read captured binding
```

This explains why changing the binding before the lambdas are called affects all of them.

---

# 48. Fixing the Late-Binding Loop with a Default Argument

A common technique is:

```python
def create_functions():
    functions = []

    for i in range(3):
        functions.append(lambda i=i: i)

    return functions
```

This connects directly to Day 2's default-argument rule:

> Default argument expressions are evaluated when the function is created/defined.

During iteration 1:

```text
outer i → 0

lambda i=i: i
         ↑
evaluate outer i now
         ↓
default → 0
```

Conceptually:

```python
lambda i=0: i
```

Iteration 2:

```python
lambda i=1: i
```

Iteration 3:

```python
lambda i=2: i
```

Therefore:

```python
f1, f2, f3 = create_functions()

f1()  # 0
f2()  # 1
f3()  # 2
```

---

# 49. Why `lambda i=i: i` Works

The two occurrences of `i` play different roles.

```python
lambda i=i: i
       ↑ ↑   ↑
       │ │   └── local parameter used by body
       │ │
       │ └── default expression evaluated now
       │
       └── parameter
```

For the first iteration:

```text
outer i = 0
     │
     ▼
default expression i
     │
     ▼
0
```

The lambda now has a local parameter with default `0`.

When:

```python
f1()
```

is called with no argument, Python uses that stored default.

---

# 50. Explicit Arguments Override Lambda Defaults

Consider:

```python
f = lambda i=10: i
```

Calling:

```python
f()
```

gives:

```text
10
```

because no argument was supplied.

But:

```python
f(999)
```

gives:

```text
999
```

because the explicitly supplied argument binds the parameter.

```text
f()
 ↓
no argument
 ↓
default i = 10


f(999)
 ↓
argument supplied
 ↓
i = 999
```

The default is a fallback, not a permanently forced value.

---

# 51. Complete Packing & Unpacking Mental Model

```text
PACKING

10, 20, 30
     ↓
tuple
     ↓
(10, 20, 30)
```

```text
UNPACKING

(10, 20, 30)
      ↓
a, b, c
↓  ↓  ↓
10 20 30
```

```text
EXTENDED UNPACKING

a, *middle, b
      ↓
starred target collects
      ↓
list
```

```text
CALL-SITE *

*iterable
    ↓
expand
    ↓
positional arguments
```

```text
CALL-SITE **

**mapping
    ↓
expand
    ↓
keyword arguments
```

---

# 52. Complete Lambda Mental Model

```text
lambda parameters: expression
             │
             ▼
       function object
             │
             ▼
       referenced/passed
             │
             ▼
          called
             │
             ▼
   parameters are bound
             │
             ▼
 expression is evaluated
             │
             ▼
 value becomes function result
```

Important distinctions:

```text
lambda creation ≠ lambda execution

lambda ≠ separate runtime object type

lambda body → expression

def body → statement suite

lambda expression value
        ↓
function result
```

---

# 53. Complete Closure Mental Model

```text
ENCLOSING FUNCTION
        │
        ▼
creates binding
        │
        ▼
creates inner function
        │
        ▼
inner references enclosing binding
        │
        ▼
free variable / closure machinery
        │
        ▼
closure cell
        │
        ▼
outer function returns
        │
        ▼
inner function survives
        │
        ▼
captured binding remains accessible
```

And:

```text
co_freevars
     ↓
names of free variables

__closure__
     ↓
closure cells

cell_contents
     ↓
current cell content
```

---

# 54. Day 1 + Day 2 + Day 3 Unified Mental Model

The first three days now connect.

```text
DAY 1
NAMES REFER TO OBJECTS
        │
        ▼
assignment establishes/rebinds references
        │
        ▼
mutation changes objects
```

Then:

```text
DAY 2
FUNCTIONS ARE OBJECTS
        │
        ▼
parameters are names
        │
        ▼
arguments provide objects
        │
        ▼
scope controls name resolution
        │
        ▼
L → E → G → B
```

And now:

```text
DAY 3
FUNCTIONS CAN BE CREATED AND PASSED
        │
        ▼
lambda creates function objects
        │
        ▼
nested functions can use enclosing bindings
        │
        ▼
closures retain access to those bindings
        │
        ▼
nonlocal can rebind them
```

The common foundation is still:

```text
NAME
  │
  ▼
OBJECT
```

plus:

```text
Where is the name bound?

Which object does it currently reference?

Is the object being mutated?

Or is the name being rebound?

Which scope does lookup use?
```

These questions explain a large amount of Python behavior.

---

# 55. Common Misconceptions Corrected

**Misconception:** Packing requires parentheses.

**Correct:** Commas are central to tuple packing; parentheses often provide grouping.

---

**Misconception:** Unpacking only works with tuples.

**Correct:** Iterable unpacking works with suitable iterable objects.

---

**Misconception:** A starred assignment target receives a tuple.

**Correct:** Extended iterable unpacking collects into a list.

---

**Misconception:** `*` always means multiplication.

**Correct:** Its meaning depends on syntax and context; it can also participate in packing/unpacking-related syntax.

---

**Misconception:** `*args` and `*values` at a call site do the same operation.

**Correct:**

```text
definition *args
→ collect

call *values
→ expand
```

---

**Misconception:** `**mapping` passes dictionary values positionally.

**Correct:** Mapping keys become keyword names and values become corresponding argument values.

---

**Misconception:** Lambda immediately evaluates its body.

**Correct:** A lambda expression creates a function object; its body is evaluated when that function is called.

---

**Misconception:** Lambda creates a special non-function object.

**Correct:** Lambda creates a function object.

---

**Misconception:** Lambda can contain ordinary statement suites like `def`.

**Correct:** Lambda's body is an expression.

---

**Misconception:** A normal `def` automatically returns its final expression.

**Correct:** Without an executed `return`, a normal function returns `None`.

---

**Misconception:** Every nested function is automatically a closure over every outer variable.

**Correct:** Relevant enclosing bindings are those referenced as free variables by the nested function.

---

**Misconception:** A closure simply stores a frozen copy of every captured value.

**Correct:** A more accurate model is retained access to captured bindings through closure machinery.

---

**Misconception:** Two calls to the same outer function necessarily share closure state.

**Correct:** Separate executions can create independent captured bindings/cells.

---

**Misconception:** `nonlocal` is necessary whenever a closure uses a mutable object.

**Correct:** Reading an enclosing binding and mutating the referenced object does not itself rebind that name. `nonlocal` matters when assignment needs to target the enclosing binding.

---

**Misconception:** Lambdas created in a loop automatically remember each loop value.

**Correct:** If they reference the same free variable, later calls can observe the final/current value of that shared binding.

---

# 56. AI/ML Connection

These concepts appear frequently in Python AI/ML code.

## Lambda as a key function

Data often needs sorting or lightweight transformation logic.

```python
results = [
    ("model_a", 0.91),
    ("model_b", 0.95),
    ("model_c", 0.89)
]

sorted(
    results,
    key=lambda result: result[1]
)
```

The lambda extracts the metric used for ordering.

---

## Higher-order APIs

Python ML/data libraries frequently accept callable objects.

Conceptually:

```python
operation(data, function)
```

Understanding:

```text
function name
      ↓
function object
```

makes callback- and transformation-based APIs much easier to reason about.

---

## Packing and Unpacking

Model/data pipelines frequently involve structured values:

```python
features, labels = batch
```

and APIs often forward arguments using:

```python
*args
**kwargs
```

Framework wrappers commonly use patterns conceptually like:

```python
def wrapper(*args, **kwargs):
    return model(*args, **kwargs)
```

Understanding **collect vs expand** is essential when reading such APIs.

---

## Closures

Closures are useful for creating configured functions.

```python
def make_threshold(threshold):
    def check(score):
        return score >= threshold

    return check
```

Then:

```python
high_confidence = make_threshold(0.9)
```

conceptually retains access to:

```text
threshold → 0.9
```

This general pattern appears in callbacks, decorators, configuration helpers, function factories, and framework internals.

---

# 57. Day 3 Quick Revision Sheet

```text
PACKING
→ combine comma-separated values into tuple-like packing structure

UNPACKING
→ distribute iterable elements to targets

EXTENDED UNPACKING
→ starred target collects zero or more elements

*a in assignment target
→ collect into list

*iterable in expression/call
→ expand iterable elements

*iterable in call
→ positional argument unpacking

**mapping in call
→ keyword argument unpacking

MAPPING KEY
→ keyword argument name

LAMBDA
→ expression that creates a function object

LAMBDA SYNTAX
→ lambda parameters: expression

LAMBDA CREATION
→ does not execute body

LAMBDA CALL
→ evaluates body expression

LAMBDA RESULT
→ value of body expression

LAMBDA BODY
→ expression, not ordinary statement suite

LAMBDA __name__
→ normally "<lambda>"

HIGHER-ORDER FUNCTION
→ operates with functions as values

sorted(..., key=function)
→ function extracts comparison key

NESTED FUNCTION
→ function lexically defined inside another function

FREE VARIABLE
→ referenced by function but not locally bound there;
  in our closure examples, supplied by enclosing function scope

CLOSURE
→ function with retained access to relevant enclosing bindings

co_freevars
→ names of free variables

__closure__
→ tuple of closure cells, or None

cell_contents
→ current contents of a closure cell

RETAINED STATE
→ captured binding can survive outer function return

SEPARATE OUTER CALLS
→ can create independent closure cells/state

nonlocal
→ rebind suitable enclosing-function binding

MUTATION
→ change existing object

REBINDING
→ change name → object relationship

CLOSURE CAPTURE
→ think binding/cell, not frozen snapshot

LATE BINDING
→ free-variable value is resolved when function executes

LAMBDA LOOP TRAP
→ multiple lambdas can share same loop-variable binding

lambda i=i: i
→ uses function default evaluation to preserve each iteration's value
```

# Day 3 Complete ✅

## Packing, Unpacking, Lambda & Closures

The central principle:

> Python's packing/unpacking behavior controls how values are collected and expanded, lambda expressions create ordinary function objects that can be passed around, and closures allow those function objects to retain access to bindings from enclosing function scopes even after the enclosing call has finished.

These notes follow the detailed structure and level of explanation of your Day 2 notes. 
