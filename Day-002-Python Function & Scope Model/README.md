# Day 2 — Python Function & Scope Model

## 1. Functions

A function is a reusable unit of computation.

```python
def square(x):
    return x * x
```

The important Python mental model is that executing `def` creates a **function object** and binds the function name to that object.

```text
square ─────► function object
```

Writing:

```python
square
```

refers to the function object.

Writing:

```python
square(5)
```

calls that function object.

### Functions are objects

Because functions are objects, another name can refer to the same function:

```python
def square(x):
    return x * x

operation = square
```

Object model:

```text
square ────────┐
               ▼
         function object
               ▲
               │
operation ─────┘
```

Therefore:

```python
operation(6)
```

returns:

```text
36
```

`operation = square` does not call the function and does not create an independent copy of it.

---

# 2. Parameters vs Arguments

A **parameter** is a name declared in a function definition.

```python
def square(x):
```

Here, `x` is a parameter.

An **argument** is the value/object supplied during a function call.

```python
square(6)
```

Here, `6` is the argument.

```text
def square(x)
           ↑
       parameter

square(6)
       ↑
    argument
```

During a call, Python binds parameter names to argument objects.

```python
value = 100

def inspect(x):
    print(x)

inspect(value)
```

Conceptually:

```text
value ───────┐
             ▼
            100
             ▲
             │
x ───────────┘
```

Python does not automatically copy the argument object.

---

# 3. Passing Mutable Objects to Functions

Consider:

```python
def add_score(scores):
    scores.append(90)

marks = [70, 80]
add_score(marks)
```

When the call begins:

```text
marks ─────────┐
               ▼
           [70, 80]
               ▲
               │
scores ────────┘
```

Then:

```python
scores.append(90)
```

mutates the shared list object.

Final state:

```text
marks ─────────┐
               ▼
        [70, 80, 90]
               ▲
               │
scores ────────┘
```

Therefore:

```python
print(marks)
```

prints:

```text
[70, 80, 90]
```

---

# 4. Mutation vs Rebinding Inside Functions

This distinction is fundamental.

## Mutation

```python
scores.append(90)
```

changes the existing object.

```text
scores ───► [70,80]
               ↓ mutate
scores ───► [70,80,90]
```

Every other reference to that same object observes the mutation.

## Rebinding

```python
scores = scores + [90]
```

The right side creates a new list, then assignment makes `scores` refer to it.

Before:

```text
marks ──────┐
            ▼
        [70, 80]
            ▲
            │
scores ─────┘
```

After:

```text
marks  ─────► [70, 80]

scores ─────► [70, 80, 90]
```

The original object was not mutated.

### Core rule

```text
Mutation → changes an object.

Rebinding → changes which object a name refers to.
```

---

# 5. Return Values

Consider:

```python
def square(x):
    result = x * x
    return result

answer = square(6)
```

Inside the function:

```text
x      ───► 6
result ───► 36
```

`return result` does not export the local name `result`.

It returns the object referred to by `result`.

The caller then binds:

```text
answer ───► 36
```

After the function finishes:

```python
print(result)
```

does not work outside the function because `result` was local.

---

# 6. Namespace

A **namespace** is a mapping from names to objects.

Conceptually:

```text
"x"      ───► 100
"name"   ───► "AI"
"train"  ───► function object
```

A useful conceptual representation is:

```python
{
    "x": 100,
    "name": "AI"
}
```

This does not mean every Python namespace must literally be implemented as an ordinary dictionary. The important idea is:

```text
name → object
```

---

# 7. Global Namespace

Names defined at module level belong to the module's global namespace.

```python
x = 100

def test():
    pass
```

Conceptually:

```text
GLOBAL NAMESPACE

x    ───► 100
test ───► function object
```

---

# 8. Local Namespace

Function calls establish local bindings.

```python
def test(value):
    result = value + 1
    return result

test(100)
```

While the function executes:

```text
LOCAL NAMESPACE

value  ───► 100
result ───► 101
```

These names are distinct from names in the global namespace.

---

# 9. Namespace vs Scope

These terms should not be treated as identical.

### Namespace

Think:

```text
Where are names bound/stored?
```

It represents name → object mappings.

### Scope

Think:

```text
From this region of the program, where can Python resolve a name?
```

A scope determines which bindings are directly accessible according to Python's name-resolution rules.

---

# 10. LEGB Name Resolution

Python's common name-resolution mental model is:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

When resolving a name, Python searches applicable scopes outward until it finds the binding.

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
  ↓
NameError if unresolved
```

---

# 11. Local Scope — L

```python
x = 100

def test():
    x = 200
    print(x)

test()
```

Inside `test()`:

```text
LOCAL
x ───► 200

GLOBAL
x ───► 100
```

Local lookup finds `x = 200`, so searching stops.

Output:

```text
200
```

---

# 12. Global Scope — G

```python
x = 100

def test():
    print(x)

test()
```

There is no local `x`.

Python searches outward and finds:

```text
GLOBAL
x ───► 100
```

Output:

```text
100
```

---

# 13. Built-in Scope — B

Python provides built-in names such as:

```text
print
len
sum
max
min
type
id
```

For:

```python
len([1, 2, 3])
```

if `len` isn't shadowed in a nearer applicable scope, lookup eventually reaches the built-in binding.

---

# 14. Shadowing

A nearer binding can hide an outer binding with the same name.

```python
len = 100

print(len([1, 2, 3]))
```

The global name:

```text
len ───► 100
```

shadows the built-in `len`.

Python effectively attempts to call the integer object:

```python
100(...)
```

resulting in a `TypeError`.

Avoid unnecessarily naming variables:

```python
list
dict
str
len
sum
max
```

because they can shadow useful built-ins.

---

# 15. Enclosing Scope — E

Enclosing scope becomes important with nested functions.

```python
x = 100

def outer():
    x = 200

    def inner():
        print(x)

    inner()

outer()
```

For `inner()`:

```text
LOCAL inner()
x → not found

ENCLOSING outer()
x ───► 200
```

Therefore:

```text
200
```

is printed.

---

# 16. Enclosing Scope Is Lexical

Enclosing scope depends on **where a function is defined**, not which function happened to call it.

```python
x = 10

def first():
    x = 20
    second()

def second():
    print(x)

first()
```

`second()` is defined globally, not inside `first()`.

Therefore `first()` is not an enclosing lexical scope of `second()`.

`second()` resolves:

```text
Local → not found
Global → x = 10
```

Output:

```text
10
```

### Important rule

```text
caller ≠ enclosing scope
```

Lexical nesting determines enclosing scopes.

---

# 17. Multiple Enclosing Scopes

```python
x = 10

def outer():
    x = 20

    def middle():
        x = 30

        def inner():
            print(x)

        inner()

    middle()

outer()
```

`inner()` searches outward and finds the nearest enclosing binding:

```text
inner local → no x

middle      → x = 30  ← FOUND

outer       → x = 20

global      → x = 10
```

Output:

```text
30
```

---

# 18. Assignment and Local Scope

Assignment inside a function normally creates/rebinds a local name.

```python
x = 10

def test():
    x = 20
```

Conceptually:

```text
GLOBAL
x ───► 10

LOCAL test()
x ───► 20
```

The global binding is unchanged.

---

# 19. `UnboundLocalError`

Consider:

```python
x = 10

def test():
    print(x)
    x = 20

test()
```

Because `x` is assigned somewhere inside the function, Python treats `x` as local to that function block unless declared otherwise.

Conceptually:

```text
GLOBAL
x ───► 10

LOCAL test()
x ───► unbound
```

When:

```python
print(x)
```

executes, Python attempts to access the local `x`, but no object has been bound to it yet.

Result:

```text
UnboundLocalError
```

Python does not continue to global lookup simply because the local binding is currently unbound.

---

# 20. `global`

`global` tells Python that specified names in the current block refer to global bindings.

```python
x = 10

def test():
    global x
    x = 20

test()
```

Before:

```text
GLOBAL
x ───► 10
```

After:

```text
GLOBAL
x ───► 20
```

A separate local `x` is not created for that assignment.

### Important misconception

You do not need `global` merely to read a global variable.

This works:

```python
x = 10

def test():
    print(x)
```

`global` becomes relevant when you want assignments to target the global binding.

---

# 21. Mutation Does Not Necessarily Require `global`

```python
scores = [70, 80]

def add_score():
    scores.append(90)
```

Name lookup finds global `scores`, and `.append()` mutates the object.

```text
scores ───► [70,80]
               ↓
            mutation
               ↓
scores ───► [70,80,90]
```

No rebinding of `scores` occurred.

Contrast:

```python
def reset():
    scores = []
```

This normally creates/rebinds a local `scores`.

To rebind the global name:

```python
def reset():
    global scores
    scores = []
```

### Core distinction

```text
scores.append(...) → mutate object

scores = ...       → rebind name
```

---

# 22. `nonlocal`

`nonlocal` is used with nested functions when an inner function needs to rebind an existing variable from an enclosing function scope.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)
```

Without `nonlocal`:

```text
outer x ───► 10
inner x ───► 20
```

With `nonlocal`:

```text
outer x ───► 10
              ↓ rebind
outer x ───► 20
```

Output:

```text
20
```

---

# 23. `global` vs `nonlocal`

```text
global x
    ↓
target the module/global binding

nonlocal x
    ↓
target an existing binding in an enclosing function scope
```

Example:

```python
x = 100

def outer():
    x = 200

    def inner():
        nonlocal x
        x = 300

    inner()
```

Final state:

```text
GLOBAL
x ───► 100

outer()
x ───► 300
```

The global binding remains unchanged.

---

# 24. Nearest Enclosing Binding with `nonlocal`

```python
def outer():
    x = 100

    def middle():
        x = 200

        def inner():
            nonlocal x
            x = 300
```

`nonlocal x` selects the nearest applicable enclosing binding:

```text
inner
  ↓
middle x = 200  ← target
  ↓
outer x = 100
```

After assignment:

```text
middle x ───► 300
outer x  ───► 100
```

`nonlocal` also requires a suitable pre-existing enclosing binding; it cannot simply create an arbitrary enclosing variable.

---

# 25. Positional Arguments

```python
def train(model, epochs, lr):
    pass

train("CNN", 10, 0.001)
```

Arguments bind according to position:

```text
"CNN" ───► model
10    ───► epochs
0.001 ───► lr
```

Python does not infer meaning from parameter names or argument values.

---

# 26. Keyword Arguments

Arguments can be supplied using parameter names:

```python
train(
    lr=0.001,
    model="CNN",
    epochs=10
)
```

Bindings:

```text
model  ───► "CNN"
epochs ───► 10
lr     ───► 0.001
```

Keyword arguments make the intended binding explicit.

---

# 27. Mixing Positional and Keyword Arguments

This is valid:

```python
train("CNN", epochs=10, lr=0.001)
```

Result:

```text
model  ───► "CNN"
epochs ───► 10
lr     ───► 0.001
```

In ordinary calls, positional arguments normally precede keyword arguments.

---

# 28. Duplicate Argument Binding

A parameter cannot receive two argument values in the same call.

```python
train("CNN", model="RNN", epochs=10, lr=0.001)
```

`model` first receives `"CNN"` positionally and is then given `"RNN"` by keyword.

Result:

```text
TypeError: got multiple values for argument 'model'
```

---

# 29. Parameter Kinds

Python supports several important parameter kinds:

```text
positional-only
positional-or-keyword
var-positional (*args)
keyword-only
var-keyword (**kwargs)
```

Two syntax markers are particularly useful:

```text
/
*
```

Example:

```python
def experiment(model, /, epochs, *, verbose):
    pass
```

Interpretation:

```text
model     → positional-only
epochs    → positional-or-keyword
verbose   → keyword-only
```

---

# 30. Positional-Only Parameters — `/`

Parameters before `/` must be supplied positionally.

```python
def power(x, y, /):
    return x ** y
```

Valid:

```python
power(2, 3)
```

Invalid:

```python
power(x=2, y=3)
```

`/` itself is not a parameter. It marks the positional-only boundary.

---

# 31. Positional-or-Keyword Parameters

Ordinary parameters between `/` and `*`, or ordinary parameters when those markers are absent, can generally be supplied positionally or by keyword.

```python
def train(model, epochs):
    pass
```

Both are valid:

```python
train("CNN", 10)
```

```python
train(model="CNN", epochs=10)
```

---

# 32. Keyword-Only Parameters — `*`

Parameters after `*` must be supplied by keyword.

```python
def train(model, *, lr):
    pass
```

Valid:

```python
train("CNN", lr=0.001)
```

Invalid:

```python
train("CNN", 0.001)
```

Keyword-only parameters are especially useful for configuration-style APIs where explicit names improve readability.

---

# 33. `*args`

`*args` collects additional positional arguments into a tuple.

```python
def train(model, *scores):
    print(scores)

train("CNN", 91, 87, 95)
```

Bindings:

```text
model  ───► "CNN"
scores ───► (91, 87, 95)
```

Therefore:

```python
type(scores)
```

is:

```text
tuple
```

The name `args` is only a convention.

This is equally valid:

```python
def test(*values):
    pass
```

The `*` provides the special behavior.

---

# 34. `**kwargs`

`**kwargs` collects additional keyword arguments into a dictionary.

```python
def train(**config):
    print(config)

train(lr=0.001, epochs=10)
```

Result:

```python
{
    "lr": 0.001,
    "epochs": 10
}
```

Therefore:

```text
*args    → tuple of extra positional arguments
**kwargs → dict of extra keyword arguments
```

Again, `kwargs` is only a conventional name.

---

# 35. Combining Normal Parameters, `*args`, and `**kwargs`

```python
def train(model, *scores, **config):
    pass

train(
    "CNN",
    91,
    87,
    optimizer="adam",
    lr=0.001
)
```

Bindings:

```text
model
  └──► "CNN"

scores
  └──► (91, 87)

config
  └──► {
          "optimizer": "adam",
          "lr": 0.001
       }
```

---

# 36. Argument Unpacking with `*`

In a function **definition**, `*args` collects arguments.

At a function **call site**, `*iterable` unpacks values into positional arguments.

```python
def add(a, b, c):
    return a + b + c

values = [10, 20, 30]

add(*values)
```

Conceptually:

```text
values ───► [10,20,30]

*values
   ↓
10, 20, 30
 ↓   ↓   ↓
 a   b   c
```

So:

```text
definition: * → collect positional arguments

call:       * → unpack into positional arguments
```

---

# 37. Argument Unpacking with `**`

At a call site, `**mapping` unpacks a mapping into keyword arguments.

```python
def train(model, epochs, lr):
    pass

config = {
    "model": "CNN",
    "epochs": 10,
    "lr": 0.001
}

train(**config)
```

Conceptually equivalent to:

```python
train(
    model="CNN",
    epochs=10,
    lr=0.001
)
```

Therefore:

```text
*iterable → positional unpacking
**mapping → keyword unpacking
```

---

# 38. Default Arguments

Defaults allow parameters to receive a predefined value when the caller omits that argument.

```python
def train(model, epochs=10):
    pass
```

Call:

```python
train("CNN")
```

Bindings:

```text
model  ───► "CNN"
epochs ───► 10
```

But:

```python
train("CNN", 20)
```

produces:

```text
model  ───► "CNN"
epochs ───► 20
```

The explicitly supplied argument overrides the default.

---

# 39. Required vs Defaulted Parameters

```python
def train(model, epochs=10):
```

Here:

```text
model     → required
epochs    → has default
```

Therefore:

```python
train()
```

is invalid because `model` is missing.

But:

```python
train("CNN")
```

is valid.

---

# 40. Default Parameter Ordering

For ordinary positional-or-keyword parameters, required parameters must appear before defaulted parameters.

Valid:

```python
def train(model, epochs=10, lr=0.001):
    pass
```

Invalid:

```python
def train(model="CNN", epochs):
    pass
```

Parameter-kind boundaries such as `/` and `*` introduce additional rules, so this rule should be understood within an ordinary parameter group.

---

# 41. When Are Default Arguments Evaluated?

This is one of the most important Day 2 rules:

> Default argument expressions are evaluated when the function definition executes, not every time the function is called.

Example:

```python
value = 10

def show(x=value):
    print(x)

value = 20

show()
```

When the `def` executes:

```text
value ───► 10

show ───► function object
              │
              └── default x ───► 10
```

Later:

```python
value = 20
```

rebinds the global name:

```text
value ───► 20
```

but doesn't reevaluate the stored default.

Therefore:

```python
show()
```

prints:

```text
10
```

---

# 42. Function Defaults and `__defaults__`

Python function objects expose positional default values through:

```python
function.__defaults__
```

For example:

```python
def show(x=10):
    pass

print(show.__defaults__)
```

conceptually gives:

```text
(10,)
```

This reinforces the mental model that defaults are associated with the function object.

Keyword-only defaults are exposed separately through `__kwdefaults__`.

---

# 43. Mutable Default Argument Pitfall

Consider:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The default list is created when the `def` statement executes.

```text
add_item
    │
    ▼
function object
    │
    └── default items ───► []
```

First call:

```python
add_item("AI")
```

uses the default object and mutates it:

```text
default ───► ["AI"]
```

Second call:

```python
add_item("ML")
```

uses the **same object**:

```text
default ───► ["AI", "ML"]
```

Therefore:

```python
print(add_item("AI"))
print(add_item("ML"))
```

produces progressively shared state rather than two independent fresh lists.

The underlying reason is not a special exception for lists.

It is:

```text
default expression evaluated once
            +
mutable object
            +
object mutated during calls
            ↓
state persists across calls
```

---

# 44. Why the Default List Survives

After a function call finishes, its local parameter binding is no longer available.

But the default list does not disappear because the **function object still references it**.

```text
function object
      │
      └────► mutable default object
```

This is a direct application of Python's object/reference model.

---

# 45. Correct Pattern — `None` Sentinel

When a fresh mutable object is required for each call, a common pattern is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Now:

```python
a = add_item("AI")
b = add_item("ML")
```

First call:

```text
items → None
          ↓
       create []
          ↓
       ["AI"]
          ↑
          a
```

Second call:

```text
items → None
          ↓
       create NEW []
          ↓
       ["ML"]
          ↑
          b
```

Therefore:

```python
a is b
```

is:

```text
False
```

because two different list objects were created.

---

# 46. Explicit Mutable Arguments Still Remain Shared

The `None` pattern does not copy objects explicitly supplied by the caller.

```python
shared = []

a = add_item("AI", shared)
b = add_item("ML", shared)
```

Both calls receive the same caller-provided list object.

Therefore mutations are shared:

```text
shared ─────┐
            ▼
      ["AI", "ML"]
         ▲      ▲
         │      │
         a      b
```

---

# 47. Mutable Default Identity Example

```python
def collect(value, bucket=[]):
    bucket.append(value)
    return bucket

a = collect(1)
b = collect(2)
c = collect(3, [])
d = collect(4)
```

The default object ends as:

```text
              a
              │
              ▼
          [1, 2, 4]
              ▲
              │
              b
              ▲
              │
              d

function default ───► same object
```

But:

```python
collect(3, [])
```

was explicitly given a fresh list:

```text
c ───► [3]
```

Therefore, after all calls:

```python
print(a)  # [1, 2, 4]
print(b)  # [1, 2, 4]
print(c)  # [3]
print(d)  # [1, 2, 4]

print(a is b)  # True
print(a is d)  # True
print(a is c)  # False
```

An important lesson:

```text
a ───► object
```

does not mean `a` stores a frozen snapshot of that object's state.

If the object later mutates, accessing it through `a` reveals its current state.

---

# 48. Complete Function Parameter Mental Model

For:

```python
def experiment(model, /, epochs=10, *scores, lr=0.001, **config):
    pass
```

think:

```text
model
  ↓
positional-only

epochs
  ↓
positional-or-keyword
with default 10

scores
  ↓
collect additional positional arguments
into tuple

lr
  ↓
keyword-only
with default 0.001

config
  ↓
collect additional keyword arguments
into dict
```

---

# 49. Complete Scope Mental Model

```text
NAME RESOLUTION

L → Local
E → Enclosing
G → Global
B → Built-in
```

But LEGB alone is not enough.

Also remember:

```text
normal assignment inside function
            ↓
        local binding

global x
            ↓
        global binding

nonlocal x
            ↓
nearest applicable enclosing-function binding
```

And:

```text
mutation
   ↓
changes object

rebinding
   ↓
changes name → object relationship
```

---

# 50. Day 1 + Day 2 Unified Mental Model

The deepest lesson is that Python's function behavior follows naturally from its object model.

```text
FUNCTIONS ARE OBJECTS
        │
        ▼
function names refer to function objects

ARGUMENTS ARE OBJECTS
        │
        ▼
parameters become names bound to those objects

NAMES LIVE IN NAMESPACES
        │
        ▼
scope controls name resolution

NAME LOOKUP
        │
        ▼
L → E → G → B

ASSIGNMENT
        │
        ▼
normally establishes/rebinds a local name

global / nonlocal
        │
        ▼
change which scope a binding targets

MUTATION
        │
        ▼
changes an existing object

DEFAULT ARGUMENTS
        │
        ▼
evaluated when the function definition executes

MUTABLE DEFAULT
        │
        ▼
same object can be reused across calls
```

---

# 51. Common Misconceptions Corrected

**Misconception:** `def` immediately executes the function body.

**Correct:** Executing `def` creates a function object; the body executes when the function is called.

---

**Misconception:** Parameters contain copies of argument objects.

**Correct:** Parameter names are bound to argument objects according to Python's call semantics.

---

**Misconception:** `return variable` makes that local variable globally accessible.

**Correct:** `return` passes the referenced result back to the caller; the local name remains local.

---

**Misconception:** LEGB always continues searching if a local access fails.

**Correct:** If a name is classified as local but has not yet been bound, accessing it can raise `UnboundLocalError`.

---

**Misconception:** `global` is necessary to read a global variable.

**Correct:** Ordinary lookup can read globals. `global` changes how that name is bound within the block.

---

**Misconception:** Calling another function makes the caller an enclosing scope.

**Correct:** Enclosing scopes are determined lexically by function nesting.

---

**Misconception:** `nonlocal` means global.

**Correct:** `nonlocal` targets a suitable binding in an enclosing function scope.

---

**Misconception:** `*args` is a list.

**Correct:** Extra positional arguments are collected into a tuple.

---

**Misconception:** `**kwargs` is a tuple.

**Correct:** Extra keyword arguments are collected into a dictionary.

---

**Misconception:** Default values are recreated every call.

**Correct:** Default expressions are evaluated when the function definition executes.

---

**Misconception:** `items=[]` gives every call a fresh list.

**Correct:** The same default list object is reused unless another argument is supplied.

---

# 52. AI/ML Connection

These concepts become important throughout AI/ML Python code.

Libraries commonly expose APIs with defaults and keyword arguments:

```python
train(
    model,
    epochs=10,
    lr=0.001
)
```

Configuration-heavy APIs benefit from keyword-only parameters:

```python
def train(model, *, epochs=10, lr=0.001):
    ...
```

Framework abstractions frequently forward arguments:

```python
def wrapper(*args, **kwargs):
    return model(*args, **kwargs)
```

Mutable objects are routinely passed through preprocessing and training functions:

```python
def preprocess(batch):
    ...
```

Understanding whether code **mutates an existing list/array/tensor-like object or rebinds a local name** is critical when debugging data pipelines and model code.

Closures and nested functions also rely on enclosing scope and `nonlocal`, making today's scope model useful later when studying decorators, callbacks, higher-order functions, and framework internals.

---

# 53. Day 2 Quick Revision Sheet

```text
FUNCTION
→ object created by executing def

PARAMETER
→ name in function definition

ARGUMENT
→ value/object supplied during call

NAMESPACE
→ mapping of names to objects

SCOPE
→ region/rules determining accessible bindings

LEGB
→ Local → Enclosing → Global → Built-in

SHADOWING
→ nearer binding hides an outer binding

ASSIGNMENT IN FUNCTION
→ normally creates/rebinds local name

UnboundLocalError
→ local name accessed before it has a value

global
→ use global binding for listed name

nonlocal
→ use nearest applicable enclosing-function binding

POSITIONAL ARGUMENT
→ bound according to position

KEYWORD ARGUMENT
→ bound using parameter name

/
→ parameters before it are positional-only

*
→ parameters after bare * are keyword-only

*args
→ collects extra positional arguments into tuple

**kwargs
→ collects extra keyword arguments into dict

*iterable in call
→ unpack into positional arguments

**mapping in call
→ unpack into keyword arguments

DEFAULT ARGUMENT
→ used when caller omits that argument

DEFAULT EVALUATION
→ occurs when function definition executes

MUTABLE DEFAULT
→ same object may be reused across calls

SAFE FRESH-MUTABLE PATTERN
→ use None, then create the mutable object inside the call

MUTATION
→ change object

REBINDING
→ change which object a name refers to
```

# Day 2 Complete ✅

## Python Function & Scope Model

The central principle:

> Python functions are part of Python's object and name-binding model: functions are objects, parameters are local names bound to argument objects, scope determines how names are resolved, and mutation versus rebinding determines whether existing objects or name bindings are changed.
