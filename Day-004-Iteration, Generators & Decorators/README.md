# Day 4 — Iteration, Iterators, Generators & Decorators

These notes follow the same detailed, diagram-heavy revision style as your Day 3 reference notes. 

---

# 1. Iteration

**Iteration** means obtaining values from an object one at a time.

For example:

```python
numbers = [10, 20, 30]

for x in numbers:
    print(x)
```

produces:

```text
10
20
30
```

At the surface level:

```text
[10, 20, 30]
      ↓
    for
      ↓
10 → 20 → 30
```

But internally, Python's iteration model is based on two important concepts:

```text
ITERABLE
    │
    │ iter()
    ▼
ITERATOR
    │
    │ next()
    ▼
  VALUE
    │
    │ next()
    ▼
  VALUE
    │
   ...
    ▼
StopIteration
```

This protocol is the foundation of Python iteration.

---

# 2. Iterable

An **iterable** is an object from which Python can obtain an iterator.

Common iterable objects include:

```python
list
tuple
str
dict
set
range
```

For example:

```python
numbers = [10, 20, 30]
```

Object model:

```text
numbers
   │
   ▼
┌─────────────────────┐
│     list object     │
│                     │
│   [10, 20, 30]      │
│                     │
│      ITERABLE       │
└─────────────────────┘
```

Because the list is iterable, Python can ask:

```python
iter(numbers)
```

and obtain an iterator.

### Core mental model

```text
ITERABLE
   │
   │ "Give me an iterator"
   │
 iter()
   ▼
ITERATOR
```

---

# 3. `iter()` Does Not Convert the Object

Consider:

```python
numbers = [10, 20, 30]

it = iter(numbers)
```

A tempting mental model is:

```text
list
 ↓
iter()
 ↓
list becomes iterator
```

That is incorrect.

The original list remains a list.

Instead:

```text
numbers
   │
   ▼
┌─────────────────────┐
│     list object     │
│   [10, 20, 30]      │
└─────────▲───────────┘
          │
          │ traversed by
          │
┌─────────┴───────────┐
│ list_iterator object│
└─────────▲───────────┘
          │
          │
         it
```

Therefore:

```python
type(numbers)
```

is still:

```text
<class 'list'>
```

while `it` is a list iterator object.

### Core rule

```text
iter(iterable)
      ↓
obtain iterator

NOT

convert original object
into iterator
```

---

# 4. `iter()` Is a Built-in Function

Another useful distinction:

```python
iter(numbers)
```

Here:

```text
iter
 ↓
Python built-in function
```

It is not correct to think of `iter()` itself as a method belonging specifically to the list.

At the protocol level, iterable objects commonly provide:

```python
__iter__()
```

and the built-in:

```python
iter(obj)
```

uses the iteration protocol to obtain an iterator.

For example, conceptually:

```text
iter(numbers)
      │
      ▼
iteration protocol
      │
      ▼
iterator object
```

---

# 5. Iterable vs Iterator

These two terms must not be treated as synonyms.

Consider:

```python
numbers = [10, 20, 30]

it = iter(numbers)
```

We now have:

```text
numbers
   │
   ▼
┌────────────────────┐
│ list               │
│                    │
│ ITERABLE           │
└────────────────────┘


it
 │
 ▼
┌────────────────────┐
│ list_iterator      │
│                    │
│ ITERATOR           │
│ traversal state    │
└────────────────────┘
```

The iterable is the object we want to traverse.

The iterator is the object responsible for producing successive values.

### Mental model

```text
Iterable
   ↓
"something I can iterate over"


Iterator
   ↓
"object performing/maintaining
 the traversal"
```

---

# 6. Aliasing vs Creating an Iterator

Consider:

```python
a = [1, 2, 3]

b = a
it = iter(a)
```

`b = a` creates another name for the same list:

```text
a ─────────────┐
               ▼
          ┌───────────┐
          │ [1,2,3]   │
          │ list      │
          └───────────┘
               ▲
               │
b ─────────────┘
```

Therefore:

```python
a is b
```

is:

```text
True
```

But:

```python
it = iter(a)
```

obtains a separate iterator object:

```text
a ─────────────┐
               ▼
          ┌───────────┐
          │ [1,2,3]   │
          │ list      │
          └─────▲─────┘
                │
                │ traverses
                │
it ───────► ┌───┴─────────────┐
            │ list_iterator   │
            └─────────────────┘
```

So:

```python
a is it
```

is:

```text
False
```

### Core distinction

```text
b = a
 ↓
aliasing
 ↓
same object


it = iter(a)
 ↓
iterator acquisition
 ↓
different object
```

---

# 7. Iterator

An **iterator** is a stateful object that produces successive values.

For:

```python
numbers = [10, 20, 30]
it = iter(numbers)
```

a useful conceptual model is:

```text
it
│
▼
┌──────────────────────┐
│ iterator object      │
│                      │
│ source → numbers     │
│                      │
│ next value → 10      │
└──────────────────────┘
```

The iterator maintains information about where traversal currently is.

This can be visualized conceptually as a position:

```text
[10, 20, 30]
 ↑
next
```

After consuming `10`:

```text
[10, 20, 30]
      ↑
     next
```

Then:

```text
[10, 20, 30]
          ↑
         next
```

This "position" is a learning model; the exact internal implementation is interpreter-specific.

---

# 8. `next()`

The built-in:

```python
next(it)
```

asks an iterator for its next value.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

x = next(it)
```

Flow:

```text
it
│
│ next()
▼
10
│
▼
x
```

Now:

```text
x ───► 10
```

and the iterator has advanced.

Conceptually:

```text
BEFORE

[10, 20, 30]
 ↑
next


next(it)
    ↓
   10


AFTER

[10, 20, 30]
      ↑
     next
```

---

# 9. Repeated `next()` Calls

Consider:

```python
numbers = [10, 20, 30]

it = iter(numbers)

a = next(it)
b = next(it)
c = next(it)
```

Flow:

```text
INITIAL

[10,20,30]
 ↑


next(it)
   ↓
  10

a ───► 10


iterator advances

[10,20,30]
     ↑


next(it)
   ↓
  20

b ───► 20


iterator advances

[10,20,30]
        ↑


next(it)
   ↓
  30

c ───► 30
```

The important point is:

> `next()` advances the **iterator's state**.

It does not remove items from the original list.

---

# 10. Iteration Does Not Consume the List

Consider:

```python
numbers = [10, 20, 30]
it = iter(numbers)

next(it)
next(it)
```

The iterator has consumed two positions.

But:

```python
print(numbers)
```

still produces:

```text
[10, 20, 30]
```

Object model:

```text
numbers
   │
   ▼
┌──────────────────────┐
│ [10, 20, 30]         │
│ unchanged list       │
└──────────▲───────────┘
           │
           │
           │ traversal
           │
it ────────┘
state: next item is 30
```

### Core rule

```text
next(iterator)
      ↓
advance iterator state

NOT

delete value from iterable
```

---

# 11. `__next__()`

Iterator objects implement the iterator protocol.

The built-in:

```python
next(it)
```

uses the iterator's:

```python
it.__next__()
```

Conceptually:

```text
next(it)
   │
   ▼
it.__next__()
   │
   ▼
next value
```

An iterator therefore fundamentally supports:

```text
ITERATOR
│
├── __iter__()
│
└── __next__()
```

`__next__()` either produces another value or signals that iteration has ended.

---

# 12. `StopIteration`

Consider:

```python
it = iter([10, 20])

next(it)   # 10
next(it)   # 20
next(it)
```

The third request has no value remaining.

Flow:

```text
iterator
   │
next()
   ▼
  10
   │
next()
   ▼
  20
   │
next()
   ▼
NO VALUE
   │
   ▼
StopIteration
```

Python uses the `StopIteration` exception as the iterator protocol's completion signal.

---

# 13. Why Not Return `None` at the End?

Suppose the iterable itself contains:

```python
values = [10, None, 20]
```

`None` is legitimate data.

Iteration should produce:

```text
10
None
20
```

Therefore Python needs a separate mechanism to mean:

```text
"There are no more values."
```

That mechanism is:

```text
StopIteration
```

So:

```text
None
 ↓
possible real value


StopIteration
 ↓
iteration completion signal
```

---

# 14. Exhausted Iterator

Once an iterator reaches its end, it is **exhausted**.

```python
it = iter([10])

next(it)   # 10
```

State:

```text
it
│
▼
┌────────────────────┐
│ iterator           │
│                    │
│ EXHAUSTED          │
└────────────────────┘
```

Another:

```python
next(it)
```

raises:

```text
StopIteration
```

Calling `next(it)` again does not restart traversal.

It remains exhausted.

### Core rule

```text
iterator reaches end
        ↓
    EXHAUSTED
        ↓
does not automatically reset
```

---

# 15. Fresh Iterator from the Iterable

The iterator can be exhausted while the original list remains reusable.

```python
numbers = [10, 20]

it1 = iter(numbers)

next(it1)
next(it1)
```

`it1` is now exhausted.

But:

```python
it2 = iter(numbers)
```

creates another iterator.

Conceptually:

```text
             ┌────────────────┐
             │ [10,20]        │
             │ list           │
             └──────▲────▲────┘
                    │    │
                    │    │
                  it1   it2
                    │    │
              exhausted  next → 10
```

### Important distinction

```text
iterator exhausted
        ≠
iterable destroyed/exhausted
```

A reusable container such as a list can provide fresh iterators.

---

# 16. Multiple Iterators Have Independent State

Consider:

```python
numbers = [10, 20, 30]

it1 = iter(numbers)
it2 = iter(numbers)

a = next(it1)
b = next(it1)
c = next(it2)
```

Results:

```text
a → 10
b → 20
c → 10
```

Why?

Because:

```text
                 [10,20,30]
                   ▲    ▲
                   │    │
                  it1  it2
```

They are separate iterator objects.

After the calls:

```text
it1

[10,20,30]
        ↑
       next


it2

[10,20,30]
     ↑
    next
```

### Core rule

> Iterator state belongs to the iterator object.

Two iterators over the same iterable can therefore have independent traversal states.

---

# 17. Iterator Is Also Iterable

This is an important relationship.

For an iterator:

```python
it = iter([10, 20, 30])
```

calling:

```python
iter(it)
```

returns the iterator itself.

Therefore:

```python
iter(it) is it
```

is:

```text
True
```

Object diagram:

```text
it ────────────────┐
                   ▼
             ┌───────────┐
             │ iterator  │
             └───────────┘
                   ▲
                   │
iter(it) ──────────┘
```

So an iterator satisfies the iterable requirement too.

---

# 18. Iterable vs Iterator Relationship

A useful relationship is:

```text
             ITERABLE
                ▲
                │
                │
             ITERATOR
```

An iterator is iterable because:

```python
iter(iterator)
```

returns itself.

But many iterables are not iterators.

For example:

```python
numbers = [10, 20]
```

The list is iterable.

But:

```python
next(numbers)
```

does not work because the list itself is not its iterator.

Instead:

```python
it = iter(numbers)

next(it)
```

works.

### Core rule

> Every iterator is iterable, but not every iterable is an iterator.

---

# 19. Why Must `iter(iterator)` Return Itself?

Suppose:

```python
it = iter([10, 20, 30])
```

and we already consume:

```python
next(it)
```

which gives:

```text
10
```

Now iterator state is:

```text
[10,20,30]
     ↑
    next
```

Suppose we write:

```python
for x in it:
    print(x)
```

A `for` loop begins by obtaining an iterator:

```text
iter(it)
```

Since `it` is already an iterator:

```text
iter(it)
   ↓
same it
```

Therefore traversal continues from the current state:

```text
20
30
```

If `iter(it)` created a fresh traversal each time, this behavior would not match the iterator protocol.

---

# 20. How a `for` Loop Works

Consider:

```python
for x in [10, 20, 30]:
    print(x)
```

At a conceptual level, Python does something equivalent to:

```python
iterator = iter([10, 20, 30])

while True:
    try:
        x = next(iterator)
        print(x)

    except StopIteration:
        break
```

The exact interpreter implementation need not literally use this Python code, but this is the correct protocol model.

Flow:

```text
[10,20,30]
     │
     │ iter()
     ▼
  iterator
     │
     │ next()
     ▼
    10
     │
     ▼
   x = 10
     │
     ▼
 print(10)
     │
     │ next()
     ▼
    20
     │
     ▼
   x = 20
     │
     ▼
 print(20)
     │
     │ next()
     ▼
    30
     │
     ▼
 print(30)
     │
     │ next()
     ▼
StopIteration
     │
     ▼
 loop ends
```

---

# 21. `for` Handles `StopIteration`

When manually calling:

```python
next(it)
```

on an exhausted iterator, we may see:

```text
StopIteration
```

But normally:

```python
for x in iterable:
    ...
```

does not expose this exception to us.

The loop uses it as the normal completion signal.

Conceptually:

```text
next(iterator)
      │
      ├── value
      │     ↓
      │   loop body
      │
      └── StopIteration
              ↓
           stop loop
```

---

# 22. `for` Over a Partially Consumed Iterator

Consider:

```python
it = iter([10, 20, 30])

print(next(it))

for x in it:
    print(x)
```

First:

```text
next(it)
   ↓
  10
```

Iterator state becomes:

```text
[10,20,30]
     ↑
    next
```

Then:

```python
for x in it:
```

asks:

```python
iter(it)
```

which returns:

```text
same iterator
```

So output is:

```text
10
20
30
```

The first `10` comes from the explicit `next(it)`.

The loop itself produces:

```text
20
30
```

---

# 23. Loop Variable Binding

Consider:

```python
for x in [10, 20, 30]:
    pass
```

During execution:

```text
iteration 1

x ───► 10


iteration 2

x ───► 20


iteration 3

x ───► 30
```

After the loop:

```text
x ───► 30
```

because Python's `for` statement does not create a separate local scope.

Therefore:

```python
print(x)
```

prints:

```text
30
```

---

# 24. Empty Iterable and Loop Variable

Consider:

```python
for x in []:
    pass

print(x)
```

The iterable produces no values.

Therefore the loop body never gets a value to bind to `x`.

Conceptually:

```text
[]
 │
iter()
 │
 ▼
iterator
 │
next()
 │
 ▼
StopIteration
 │
 ▼
no assignment to x
```

If `x` did not already exist, then:

```python
print(x)
```

raises:

```text
NameError
```

---

# 25. Complete Iteration Mental Model

```text
ITERABLE
   │
   │ iter()
   ▼
ITERATOR
   │
   │ next()
   ▼
 VALUE
   │
   │ next()
   ▼
 VALUE
   │
   ...
   │
   │ next()
   ▼
StopIteration
```

And:

```text
for x in iterable
        │
        ▼
   iter(iterable)
        │
        ▼
     iterator
        │
        ▼
 repeated next()
        │
        ├── values → x → loop body
        │
        └── StopIteration → stop
```

---

# 26. Generator

A **generator** is a convenient Python mechanism for producing values lazily while preserving execution state between iterations.

Consider:

```python
def numbers():
    yield 10
    yield 20
    yield 30
```

Because the function contains `yield`, it is a **generator function**.

Calling:

```python
g = numbers()
```

creates a:

```text
generator object
```

---

# 27. Generator Function vs Generator Object

This distinction is essential.

```python
def numbers():
    yield 10
```

Here:

```text
numbers
   │
   ▼
generator function object
```

But:

```python
g = numbers()
```

gives:

```text
g
│
▼
generator object
```

So:

```text
GENERATOR FUNCTION
       │
       │ call
       ▼
GENERATOR OBJECT
```

Do not treat the function and the object returned by calling it as the same thing.

---

# 28. Calling a Generator Function Does Not Run Its Body Immediately

Consider:

```python
def test():
    print("A")
    yield 10

g = test()
```

At:

```python
g = test()
```

Python creates the generator object.

Conceptually:

```text
g
│
▼
┌─────────────────────┐
│ generator object    │
│                     │
│ state: CREATED      │
│ body not started    │
└─────────────────────┘
```

So `"A"` is not printed yet.

Execution begins when the generator is consumed.

For example:

```python
next(g)
```

---

# 29. First `next()` Starts Generator Execution

Given:

```python
def test():
    print("A")
    yield 10

g = test()
```

Now:

```python
x = next(g)
```

Execution begins:

```text
START generator
      │
      ▼
print("A")
      │
      ▼
      A
      │
      ▼
yield 10
      │
      ├────► produce 10
      │
      ▼
   SUSPEND
```

So:

```text
x ───► 10
```

and the generator is paused at the `yield`.

---

# 30. `yield`

`yield` has two major effects:

```text
yield value
    │
    ├── produce value to consumer
    │
    └── suspend generator execution
```

Example:

```python
def test():
    x = 10
    yield x

    x = 20
    yield x
```

First:

```python
next(g)
```

reaches:

```text
yield 10
```

and pauses.

The generator preserves the execution state necessary to continue later.

---

# 31. Suspended Generator State

After:

```python
x = next(g)
```

the generator can be visualized as:

```text
g
│
▼
┌────────────────────────┐
│ generator object       │
│                        │
│ state: SUSPENDED       │
│                        │
│ local x → 10           │
│                        │
│ resume after yield 10  │
└────────────────────────┘
```

This is one of the biggest differences between an ordinary function call and generator execution.

The generator can stop temporarily without losing its execution context.

---

# 32. `next()` Resumes Instead of Restarting

Consider:

```python
def test():
    print("A")
    yield 10

    print("B")
    yield 20

    print("C")
```

First:

```python
next(g)
```

produces:

```text
A
```

and yields:

```text
10
```

The generator pauses.

Second:

```python
next(g)
```

does **not** restart from:

```python
print("A")
```

Instead it resumes after the previous `yield`.

```text
previous yield
     │
     ▼
   RESUME
     │
     ▼
print("B")
     │
     ▼
yield 20
     │
     ▼
  SUSPEND
```

---

# 33. Generator Execution Timeline

For:

```python
def test():
    print("A")
    yield 10

    print("B")
    yield 20

    print("C")
```

the lifecycle is:

```text
g = test()

CREATED
   │
   │ next(g)
   ▼
RUNNING
   │
print A
   │
yield 10
   ▼
SUSPENDED
   │
   │ next(g)
   ▼
RUNNING
   │
print B
   │
yield 20
   ▼
SUSPENDED
   │
   │ next(g)
   ▼
RUNNING
   │
print C
   │
function ends
   ▼
FINISHED
   │
   ▼
StopIteration
```

---

# 34. Why `"C"` Does Not Execute After `yield 20`

Consider:

```python
x = next(g)
y = next(g)
```

The second `next(g)` executes until:

```python
yield 20
```

At that exact point:

```text
produce 20
    +
suspend
```

Python does not continue automatically to:

```python
print("C")
```

A third request is required:

```python
next(g)
```

Then:

```text
RESUME
  │
  ▼
print("C")
  │
  ▼
function ends
  │
  ▼
StopIteration
```

### Core rule

> `yield` means: produce this value and suspend here until another iteration request resumes execution.

---

# 35. Generator Preserves Local State

Consider:

```python
def counter():
    x = 0

    while x < 3:
        yield x
        x += 1
```

First:

```python
next(g)
```

produces:

```text
0
```

Generator state:

```text
x → 0
SUSPENDED
```

Next:

```python
next(g)
```

resumes:

```text
x += 1
   ↓
x → 1
   ↓
yield 1
```

Next:

```text
x → 2
yield 2
```

The generator doesn't recreate `x = 0` on every `next()`.

Its execution state persists across suspension.

---

# 36. `yield` vs `return`

This is a critical distinction.

Normal function:

```python
def f():
    return 10
```

Flow:

```text
function call
    │
    ▼
return 10
    │
    ├── produce 10
    │
    └── terminate invocation
```

Generator:

```python
def g():
    yield 10
```

Flow:

```text
next(generator)
      │
      ▼
yield 10
      │
      ├── produce 10
      │
      └── suspend
```

### Core rule

```text
return
  ↓
produce result
  +
terminate


yield
  ↓
produce value
  +
suspend
```

---

# 37. Generator Completion

Eventually the generator function reaches its end.

Example:

```python
def numbers():
    yield 10
    yield 20
```

Consumption:

```text
next(g) → 10
next(g) → 20
next(g) → StopIteration
```

So generator completion connects directly to the iterator protocol.

---

# 38. Generator Object Is an Iterator

A generator object behaves as an iterator.

For:

```python
g = numbers()
```

we can call:

```python
next(g)
```

directly.

Also:

```python
iter(g) is g
```

is:

```text
True
```

Relationship:

```text
ITERABLE
   ▲
   │
ITERATOR
   ▲
   │
GENERATOR OBJECT
```

So:

> Every generator object is an iterator.

---

# 39. Generator and `for`

Because a generator object is an iterator:

```python
for x in numbers():
    print(x)
```

works naturally.

Conceptual flow:

```text
numbers()
    │
    ▼
generator object
    │
    │ iter()
    ▼
same generator
    │
    │ next()
    ▼
yield 10
    │
    ▼
x = 10
    │
    │ next()
    ▼
yield 20
    │
    ▼
x = 20
    │
    │ next()
    ▼
StopIteration
    │
    ▼
loop ends
```

---

# 40. Lazy Production

Generators are **lazy**.

Consider a list:

```python
squares = [x * x for x in range(1_000_000)]
```

The resulting list materializes all those square results.

Conceptually:

```text
calculate
   ↓
0
1
4
9
...
   ↓
store result references
   ↓
large list
```

A generator can instead produce results progressively:

```python
def squares(n):
    for x in range(n):
        yield x * x
```

Conceptually:

```text
consumer asks
      │
      ▼
produce ONE result
      │
      ▼
pause
      │
consumer asks again
      │
      ▼
produce NEXT result
```

This is **lazy production**.

---

# 41. Why Lazy Production Matters

Suppose you only need the first few values from a very large sequence.

An eager approach may construct many values you never use.

A generator can instead work incrementally:

```text
SOURCE
  │
  ▼
one item
  │
transform
  │
  ▼
consumer
  │
  ▼
next item
```

This can reduce the need to materialize large intermediate collections.

This idea becomes important in data-processing and machine-learning pipelines.

---

# 42. Generator Expression

Python provides a compact syntax for creating generators.

```python
g = (x * x for x in range(5))
```

This creates a:

```text
generator object
```

not a tuple.

Object model:

```text
g
│
▼
┌─────────────────────────┐
│ generator object        │
│                         │
│ expression: x * x       │
│ source: range(5)        │
│ lazy iteration state    │
└─────────────────────────┘
```

---

# 43. Generator Expression vs List Comprehension

Compare:

```python
a = [x * x for x in range(5)]
```

with:

```python
b = (x * x for x in range(5))
```

The syntax differs mainly by brackets, but the resulting objects are fundamentally different.

### List comprehension

```text
range(5)
   │
   ▼
calculate all results
   │
   ▼
[0,1,4,9,16]
   │
   ▼
a
```

### Generator expression

```text
range(5)
   │
   ▼
generator computation/state
   │
   ▼
b
```

Values are produced as the generator is consumed.

---

# 44. List Comprehension Materializes Results

For:

```python
a = [x * x for x in range(3)]
```

after the expression finishes:

```text
a
│
▼
┌────────────────────┐
│ list object        │
│                    │
│ [0, 1, 4]          │
│                    │
│ results already    │
│ materialized       │
└────────────────────┘
```

The resulting collection can be iterated repeatedly.

---

# 45. Generator Expression Produces Lazily

For:

```python
b = (x * x for x in range(3))
```

conceptually:

```text
b
│
▼
┌─────────────────────┐
│ generator object    │
│                     │
│ computation/state   │
│                     │
│ values produced     │
│ as requested        │
└─────────────────────┘
```

Then:

```python
next(b)
```

produces:

```text
0
```

another:

```python
next(b)
```

produces:

```text
1
```

and another:

```text
4
```

---

# 46. Generator Expression Is Not a Tuple Comprehension

This:

```python
(x * x for x in range(3))
```

may visually resemble tuple syntax.

But:

```python
type(x * x for x in range(3))
```

is:

```text
<class 'generator'>
```

Conceptually:

```text
(...)
 +
for expression
      ↓
generator expression
      ↓
generator object
```

It should not be mentally modeled as:

```text
(0, 1, 4)
```

---

# 47. Generator Function vs Generator Expression

Generator function:

```python
def squares(n):
    for x in range(n):
        yield x * x
```

Usage:

```python
g = squares(5)
```

Generator expression:

```python
g = (x * x for x in range(5))
```

Both produce generator objects.

Conceptually:

```text
GENERATOR FUNCTION

def ...
 yield ...
    │
   call
    ▼
generator object
```

and:

```text
GENERATOR EXPRESSION

(expression for x in iterable)
          │
          ▼
   generator object
```

A generator expression is a compact way of expressing lazy generator-based iteration.

---

# 48. Generator Consumption

Generators can be consumed explicitly:

```python
next(g)
```

but explicit `next()` is not the only consumer.

For example:

```python
list(g)
```

iterates over `g` to construct a list.

Conceptually:

```text
list(g)
   │
   ▼
consume g
   │
   ├── next → 0
   ├── next → 1
   ├── next → 4
   └── StopIteration
           │
           ▼
       [0,1,4]
```

So `list(g)` can exhaust the generator.

---

# 49. Generator Exhaustion

Consider:

```python
g = (x * x for x in range(3))

print(list(g))
print(list(g))
```

First:

```python
list(g)
```

consumes:

```text
0
1
4
StopIteration
```

and creates:

```text
[0, 1, 4]
```

Now:

```text
g
│
▼
EXHAUSTED
```

The second:

```python
list(g)
```

immediately encounters completion.

So:

```text
[]
```

is created.

Output:

```text
[0, 1, 4]
[]
```

---

# 50. Lazy Does Not Mean Explicit `next()` Only

A common misconception is:

```text
generator executes
only if I literally write next(g)
```

That is incorrect.

Many consumers can drive iteration:

```text
generator
   │
   ├── next(g)
   ├── for x in g
   ├── list(g)
   ├── tuple(g)
   └── other iteration consumers
```

The better rule is:

> A lazy generator produces values when an iteration consumer requests them.

---

# 51. Complete Generator Mental Model

```text
GENERATOR FUNCTION
       │
       │ call
       ▼
GENERATOR OBJECT
       │
       │ next()
       ▼
    RUNNING
       │
       ▼
     yield
       │
       ├── produce value
       │
       └── suspend
       ▼
   SUSPENDED
       │
       │ next()
       ▼
     RESUME
       │
       ▼
     yield
       │
      ...
       ▼
function finishes
       │
       ▼
StopIteration
```

---

# 52. Decorators

A **decorator** is a callable that receives another callable and returns a callable, commonly to add or modify behavior around the original function.

Conceptually:

```text
ORIGINAL FUNCTION
        │
        ▼
     DECORATOR
        │
        ▼
   WRAPPED CALLABLE
```

Decorators build directly on concepts from previous days:

```text
Functions are objects
        +
Functions can be arguments
        +
Functions can be returned
        +
Nested functions
        +
Closures
        ↓
    DECORATORS
```

---

# 53. Why Decorators Are Useful

Suppose:

```python
def greet():
    print("Hello")
```

We want:

```text
Before
Hello
After
```

We could modify `greet()` directly.

But suppose many functions need the same behavior:

```text
login()
predict()
train()
save()
```

Repeatedly editing every function mixes cross-cutting behavior with the function's main responsibility.

A decorator lets us conceptually do:

```text
original behavior
       │
       ▼
      wrap
       │
       ▼
extra behavior
+
original behavior
```

Common use cases include logging, timing, caching, validation, authentication, tracing, and instrumentation.

---

# 54. Functions Are Objects

Consider:

```python
def greet():
    print("Hello")
```

Python creates a function object.

```text
greet
  │
  ▼
┌────────────────────┐
│ function object    │
│                    │
│ greet              │
└────────────────────┘
```

Because functions are objects, we can assign another name:

```python
another = greet
```

Now:

```text
greet ─────────┐
               ▼
          ┌──────────────┐
          │ function     │
          │ object       │
          └──────────────┘
               ▲
               │
another ───────┘
```

Two names reference one function object.

---

# 55. Function Reference vs Function Call

These are fundamentally different:

```python
greet
```

and:

```python
greet()
```

`greet` means:

```text
get/reference function object
```

while:

```python
greet()
```

means:

```text
greet
  │
  ▼
function object
  │
  │ ()
  ▼
execute function
```

This distinction is essential for decorators.

---

# 56. Passing a Function to Another Function

Because functions are objects:

```python
def execute(func):
    func()
```

we can write:

```python
execute(greet)
```

Notice:

```python
greet
```

not:

```python
greet()
```

During `execute`:

```text
greet ────────────┐
                  ▼
            ┌──────────────┐
            │ greet        │
            │ function     │
            └──────────────┘
                  ▲
                  │
func ─────────────┘
```

So:

```python
func()
```

calls the same function object referenced by `greet`.

---

# 57. Returning a Function

Functions can also create and return functions.

```python
def outer():

    def inner():
        print("Inside")

    return inner
```

Then:

```python
result = outer()
```

Because we wrote:

```python
return inner
```

rather than:

```python
return inner()
```

the inner function object is returned.

```text
result
  │
  ▼
┌────────────────────┐
│ inner function     │
└────────────────────┘
```

Therefore:

```python
result()
```

prints:

```text
Inside
```

---

# 58. Building a Decorator Manually

Consider:

```python
def decorate(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper
```

And:

```python
def greet():
    print("Hello")
```

Now:

```python
new_greet = decorate(greet)
```

Let's trace it.

---

# 59. Decorator Receives Original Function

At:

```python
decorate(greet)
```

the original function is passed as an object.

```text
greet
  │
  ▼
┌────────────────────┐
│ original greet     │
│ function           │
└────────────────────┘
  ▲
  │
func
```

Inside `decorate`, the parameter `func` references the same original function object.

---

# 60. Decorator Creates Wrapper Function

Inside:

```python
def wrapper():
    print("Before")
    func()
    print("After")
```

Python creates another function object.

```text
wrapper
   │
   ▼
┌──────────────────────┐
│ wrapper function     │
│                      │
│ uses func            │
└──────────────────────┘
```

Because `wrapper` references `func` from the enclosing `decorate()` scope, this connects directly to closures.

---

# 61. Wrapper Closure

The wrapper needs the original function even after `decorate()` finishes.

Conceptually:

```text
wrapper function
      │
      │ closure
      ▼
     func
      │
      ▼
original greet function
```

This is why closures are fundamental to understanding many decorators.

---

# 62. Decorator Returns Wrapper

The decorator ends with:

```python
return wrapper
```

So:

```python
new_greet = decorate(greet)
```

gives:

```text
new_greet
    │
    ▼
┌──────────────────────┐
│ wrapper function     │
│                      │
│ closure              │
│ func ────────────────┼────► original greet
└──────────────────────┘
```

`new_greet` references the wrapper.

---

# 63. Calling the Wrapped Function

Now:

```python
new_greet()
```

actually calls:

```text
wrapper()
```

Flow:

```text
new_greet()
     │
     ▼
wrapper()
     │
     ▼
print("Before")
     │
     ▼
func()
     │
     ▼
original greet()
     │
     ▼
print("Hello")
     │
     ▼
return to wrapper
     │
     ▼
print("After")
```

Output:

```text
Before
Hello
After
```

---

# 64. Manual Decoration

Instead of using another name:

```python
new_greet = decorate(greet)
```

we can rebind the original name:

```python
greet = decorate(greet)
```

This is the key operation behind basic decorator syntax.

Before:

```text
greet
  │
  ▼
ORIGINAL FUNCTION
```

Evaluate:

```text
decorate(greet)
       │
       ▼
    WRAPPER
```

Then assignment:

```text
greet = wrapper
```

After:

```text
greet
  │
  ▼
WRAPPER
  │
  │ closure
  ▼
ORIGINAL GREET
```

---

# 65. `@decorator` Syntax

Python provides decorator syntax:

```python
@decorate
def greet():
    print("Hello")
```

For this simple case, the central mental model is:

```python
greet = decorate(greet)
```

The transformation is:

```text
1. create original greet function

greet ───► ORIGINAL


2. apply decorator

decorate(ORIGINAL)
       │
       ▼
    WRAPPER


3. bind greet to returned callable

greet ───► WRAPPER
              │
              │ closure
              ▼
           ORIGINAL
```

---

# 66. What Does the Decorated Name Reference?

After:

```python
@decorate
def hello():
    print("Python")
```

the name `hello` typically directly references the callable returned by `decorate`.

In our decorator, that is:

```text
wrapper
```

So:

```text
hello
  │
  ▼
┌────────────────────┐
│ wrapper function   │
└─────────┬──────────┘
          │ closure
          ▼
┌────────────────────┐
│ original hello     │
└────────────────────┘
```

### Core rule

```text
before decoration:

hello → original


after our decorator:

hello → wrapper → original
```

---

# 67. Decorators and Closures Connection

Day 3:

```text
inner function
      │
      │ closure
      ▼
enclosing binding
```

Day 4 decorator:

```text
wrapper
   │
   │ closure
   ▼
func
   │
   ▼
original function
```

So decorators are not a completely separate Python idea.

They combine several earlier concepts:

```text
function objects
      +
function arguments
      +
nested functions
      +
closures
      +
returning functions
      ↓
decorator pattern
```

---

# 68. Problem: Wrapper Accepts No Arguments

Our first wrapper was:

```python
def wrapper():
    func()
```

Now suppose:

```python
@decorate
def add(a, b):
    return a + b
```

After decoration:

```text
add ───► wrapper
```

So:

```python
add(10, 20)
```

really attempts to call:

```python
wrapper(10, 20)
```

But:

```python
wrapper()
```

accepts no arguments.

Therefore argument binding fails with a:

```text
TypeError
```

---

# 69. `*args` and `**kwargs` in Decorators

A common general wrapper pattern is:

```python
def wrapper(*args, **kwargs):
```

This connects directly to Day 3.

Suppose:

```python
add(10, 20)
```

Because `add` references the wrapper:

```text
wrapper(10, 20)
```

Inside:

```text
args
 ↓
(10, 20)

kwargs
 ↓
{}
```

Then:

```python
func(*args, **kwargs)
```

expands those arguments.

```text
args = (10,20)
      │
      │ *args
      ▼
    10, 20
      │
      ▼
func(10,20)
      │
      ▼
original add(10,20)
```

---

# 70. General Decorator Argument Flow

Consider:

```python
def decorate(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Flow:

```text
CALLER

add(10,20)
    │
    ▼
WRAPPER

args → (10,20)
kwargs → {}
    │
    ▼
func(*args, **kwargs)
    │
    ▼
ORIGINAL ADD

a → 10
b → 20
    │
    ▼
a + b
    │
    ▼
30
```

This is why `*args` and `**kwargs` are common in decorators intended to wrap functions with varying signatures.

---

# 71. Preserving the Original Return Value

Consider:

```python
def multiply(a, b):
    return a * b
```

Suppose the wrapper does:

```python
result = func(*args, **kwargs)
```

The original function returns:

```text
20
```

but that value initially returns **to the wrapper**.

```text
original multiply
       │
       │ return 20
       ▼
    wrapper
       │
       ▼
result → 20
```

The wrapper must return it again if the caller should receive it:

```python
return result
```

---

# 72. What Happens If Wrapper Does Not Return?

Suppose:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
```

There is no:

```python
return result
```

Then:

```python
x = multiply(4, 5)
```

after decoration actually means:

```text
x = wrapper(4,5)
```

Flow:

```text
wrapper
   │
   ▼
original multiply
   │
   ▼
return 20
   │
   ▼
wrapper receives 20
   │
   ▼
result = 20
   │
   ▼
wrapper reaches end
   │
   ▼
implicit return None
   │
   ▼
x → None
```

### Core rule

> The original function's return value does not automatically pass through the wrapper.

The wrapper must return it.

---

# 73. Robust Basic Decorator Pattern

We now have:

```python
def decorate(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

This handles:

```text
arguments
    ↓
*args / **kwargs

original call
    ↓
func(*args, **kwargs)

return value
    ↓
result

caller receives result
    ↓
return result
```

---

# 74. Decorator Execution Example

```python
@decorate
def multiply(a, b):
    print("Multiplying")
    return a * b


x = multiply(4, 5)

print(x)
```

Flow:

```text
multiply(4,5)
      │
      ▼
wrapper(4,5)
      │
      ▼
print Before
      │
      ▼
func(4,5)
      │
      ▼
original multiply
      │
      ▼
print Multiplying
      │
      ▼
return 20
      │
      ▼
wrapper
result → 20
      │
      ▼
print After
      │
      ▼
return 20
      │
      ▼
x → 20
```

Output:

```text
Before
Multiplying
After
20
```

---

# 75. Decorator Metadata Problem

Consider:

```python
def decorate(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorate
def add(a, b):
    """Add two numbers."""
    return a + b
```

After decoration:

```text
add
 │
 ▼
wrapper function
```

Therefore:

```python
add.__name__
```

would normally reflect the wrapper's name:

```text
wrapper
```

rather than:

```text
add
```

The same issue can affect metadata such as the docstring.

---

# 76. Why Metadata Changes

Before decoration:

```text
add
 │
 ▼
┌────────────────────────┐
│ original add           │
│                        │
│ __name__ = "add"       │
│ __doc__ = "Add two..." │
└────────────────────────┘
```

After a basic wrapper decorator:

```text
add
 │
 ▼
┌────────────────────────┐
│ wrapper function       │
│                        │
│ __name__ = "wrapper"   │
│ __doc__ = ...          │
└──────────┬─────────────┘
           │ closure
           ▼
┌────────────────────────┐
│ original add           │
│                        │
│ __name__ = "add"       │
│ __doc__ = "Add two..." │
└────────────────────────┘
```

The original metadata still exists.

But `add` now references the wrapper.

---

# 77. `functools.wraps`

Python's standard library provides:

```python
functools.wraps
```

A standard pattern is:

```python
from functools import wraps


def decorate(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return wrapper
```

`@wraps(func)` updates the wrapper with important metadata from the wrapped function.

---

# 78. What `@wraps(func)` Changes Conceptually

Without `wraps`:

```text
add
 │
 ▼
WRAPPER
 │
 ├── __name__ → "wrapper"
 │
 └── closure → original add
```

With `wraps`:

```text
add
 │
 ▼
WRAPPER
 │
 ├── __name__ → "add"
 ├── __doc__  → original docstring
 ├── __wrapped__ ─────────► original add
 │
 └── closure ─────────────► original add
```

The wrapper still exists.

`wraps` does **not** turn the wrapper back into the original function.

---

# 79. `__wrapped__`

`functools.wraps` also establishes:

```python
wrapper.__wrapped__
```

pointing to the wrapped function.

Conceptually:

```text
decorated function name
        │
        ▼
     WRAPPER
        │
        ├── closure → original
        │
        └── __wrapped__ → original
```

This is useful for introspection and tools that need to understand wrapped functions.

---

# 80. Standard Decorator Template

A strong general template is:

```python
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # behavior before

        result = func(*args, **kwargs)

        # behavior after

        return result

    return wrapper
```

Mental model:

```text
ORIGINAL FUNCTION
       │
       ▼
decorator(func)
       │
       ▼
create wrapper
       │
       ├── closure → func
       ├── accepts *args/**kwargs
       ├── calls func
       ├── preserves result
       └── @wraps preserves metadata
       │
       ▼
return wrapper
       │
       ▼
original function name
now references wrapper
```

---

# 81. Complete Decorator Mental Model

```text
FUNCTION OBJECT
      │
      │ passed into
      ▼
   DECORATOR
      │
      ▼
creates nested WRAPPER
      │
      ├── closure keeps original function
      │
      ├── *args collects positional args
      │
      ├── **kwargs collects keyword args
      │
      ├── func(*args, **kwargs)
      │       ↓
      │   original function
      │
      ├── captures return value
      │
      └── returns result
      │
      ▼
returns WRAPPER
      │
      ▼
function name rebound
      │
      ▼
NAME → WRAPPER → ORIGINAL
```

With `functools.wraps`:

```text
NAME
 │
 ▼
WRAPPER
 │
 ├── metadata resembles original
 ├── __wrapped__ → ORIGINAL
 └── closure → ORIGINAL
```

---

# 82. Iteration vs Generator

These concepts are connected but not identical.

### Iterator

```text
stateful object
    ↓
next()
    ↓
next value
```

### Generator

```text
special convenient iterator mechanism
    ↓
generator execution
    ↓
yield
    ↓
produce + suspend
    ↓
resume later
```

Relationship:

```text
ITERABLE
   ▲
   │
ITERATOR
   ▲
   │
GENERATOR OBJECT
```

So generators fit into the iterator protocol rather than replacing it.

---

# 83. Generator Function vs Normal Function

Normal function:

```text
CALL
 ↓
execute
 ↓
return
 ↓
finish
```

Generator function:

```text
CALL
 ↓
create generator object

        later...

next()
 ↓
execute
 ↓
yield
 ↓
suspend

next()
 ↓
resume
 ↓
yield
 ↓
suspend
```

This is the central execution-model difference.

---

# 84. Generator Expression vs List Comprehension

```text
LIST COMPREHENSION

[x*x for x in data]
        │
        ▼
produce/materialize resulting list
        │
        ▼
      LIST
```

versus:

```text
GENERATOR EXPRESSION

(x*x for x in data)
        │
        ▼
generator object
        │
        ▼
lazy production
```

A list stores the resulting references.

A generator maintains iteration/computation state and produces values as consumed.

---

# 85. Decorator vs Ordinary Function Call

Suppose:

```python
decorate(greet)
```

This is an ordinary function call returning some object.

The special-looking syntax:

```python
@decorate
def greet():
    ...
```

uses decoration semantics around function definition.

The essential transformation for our simple decorator is:

```text
create greet function
       ↓
decorate(greet)
       ↓
return wrapper
       ↓
bind greet to wrapper
```

So the decorator mechanism builds on ordinary Python object and function behavior.

---

# 86. Common Misconceptions Corrected

**Misconception:** An iterable and iterator are the same object.

**Correct:** An iterable is something Python can obtain an iterator from. An iterator maintains traversal state.

---

**Misconception:** `iter()` converts the list into an iterator.

**Correct:** The list remains a list; `iter()` obtains an iterator.

---

**Misconception:** Calling `next()` removes items from the list.

**Correct:** `next()` advances the iterator's traversal state.

---

**Misconception:** If an iterator is exhausted, its list is exhausted too.

**Correct:** A reusable iterable such as a list can provide another fresh iterator.

---

**Misconception:** Two iterators over the same list share one traversal position.

**Correct:** Separate iterator objects can maintain independent state.

---

**Misconception:** An iterator cannot itself be used as an iterable.

**Correct:** `iter(iterator)` returns the iterator itself.

---

**Misconception:** A `for` loop accesses list elements through some completely unrelated mechanism.

**Correct:** The iterator protocol provides the central model: `iter()` followed by repeated iteration until `StopIteration`.

---

**Misconception:** `StopIteration` means something went wrong with a normal iteration.

**Correct:** It is the iterator protocol's normal completion signal.

---

**Misconception:** Calling a generator function immediately executes its body.

**Correct:** Calling it creates a generator object. Execution begins when the generator is consumed.

---

**Misconception:** Every `next()` restarts the generator function.

**Correct:** The generator resumes from its suspended execution point.

---

**Misconception:** `yield` is simply another spelling of `return`.

**Correct:** `yield` produces a value and suspends; `return` terminates the function invocation.

---

**Misconception:** A generator forgets local variables after yielding.

**Correct:** Generator execution state is preserved across suspension.

---

**Misconception:** A generator expression creates a tuple.

**Correct:** `(x for x in iterable)` creates a generator object.

---

**Misconception:** Lazy means the generator only runs if we explicitly write `next(g)`.

**Correct:** Any consumer that iterates the generator can drive its execution.

---

**Misconception:** `list(g)` merely views the generator without changing it.

**Correct:** `list(g)` consumes the generator.

---

**Misconception:** An exhausted generator automatically restarts when used again.

**Correct:** The same generator object remains exhausted.

---

**Misconception:** `@decorator` means Python permanently modifies the original function object.

**Correct:** A decorator is called with the function, and the relevant name is bound to the callable returned by the decorator.

---

**Misconception:** After decoration, the function name necessarily still directly references the original function.

**Correct:** In our wrapper decorator, the name directly references the returned wrapper.

---

**Misconception:** The wrapper magically knows the original function.

**Correct:** In our pattern, the wrapper retains access to `func` through a closure.

---

**Misconception:** The original function's return value automatically passes through the decorator.

**Correct:** The wrapper needs to return that value if it should reach the caller.

---

**Misconception:** `@wraps` removes the wrapper.

**Correct:** The wrapper remains. `wraps` updates metadata and provides `__wrapped__`.

---

# 87. AI/ML Connection

These Day 4 concepts become increasingly useful when reading AI/ML Python code.

## Iterables and Iterators

ML workloads frequently process collections incrementally:

```text
dataset
   │
   ▼
iterator
   │
   ▼
sample / batch
   │
   ▼
model
```

Rather than mentally assuming that every data API is "just a list," understanding Python's iterable/iterator protocol prepares you to reason about dataset and data-loading abstractions.

When we reach NumPy, pandas, scikit-learn, and PyTorch, we'll use their official documentation to learn their actual iteration and data-loading semantics rather than assuming all library objects behave identically to built-in lists.

---

# 88. Generators in Data Pipelines

Generators establish the mental model for incremental processing:

```text
large source
    │
    ▼
produce item
    │
    ▼
transform
    │
    ▼
consume
    │
    ▼
request next
```

Instead of:

```text
large source
    │
    ▼
materialize every intermediate result
    │
    ▼
process everything
```

This can be valuable when data is large, streamed, generated dynamically, or consumed progressively.

---

# 89. Decorators in AI/ML Engineering

Decorators are useful for cross-cutting behavior around functions.

For example, conceptually:

```python
@timer
def train_model():
    ...
```

can add timing behavior.

Or:

```python
@logger
def predict(data):
    ...
```

can add logging around prediction.

The conceptual flow is:

```text
predict
   │
   ▼
wrapper
   │
   ├── logging
   │
   ▼
original predict
   │
   ▼
result
   │
   ▼
wrapper
   │
   └── more logging
```

Decorators also appear throughout Python frameworks and libraries, so understanding the object transformation is more useful than merely memorizing `@something`.

---

# 90. Day 1 + Day 2 + Day 3 + Day 4 Unified Mental Model

The first four days now connect strongly.

### Day 1

```text
NAME
 │
 ▼
OBJECT
```

Variables are names referring to objects.

Aliasing, identity, mutability, copying, and assignment all build on this.

---

### Day 2

```text
FUNCTION
   │
   ▼
function object

arguments
   │
   ▼
parameter bindings

name lookup
   │
   ▼
LEGB
```

Functions introduce execution frames, argument binding, and scope.

---

### Day 3

```text
functions are objects
       │
       ▼
can be passed / returned
       │
       ▼
nested functions
       │
       ▼
closures
       │
       ▼
retained enclosing bindings
```

Packing/unpacking also gives us:

```text
*args / **kwargs
```

which becomes directly useful in decorators.

---

### Day 4

```text
ITERATION

iterable
   ↓
iterator
   ↓
stateful next()
```

Then:

```text
GENERATOR

iterator
   +
suspend/resume execution
   +
yield
```

And:

```text
DECORATOR

function objects
   +
function arguments
   +
closures
   +
*args / **kwargs
   +
returning functions
   ↓
wrapped behavior
```

Everything continues to build on Python's object model.

---

# 91. Day 4 Quick Revision Sheet

```text
ITERATION
→ obtain successive values from an object

ITERABLE
→ object from which Python can obtain an iterator

iter(iterable)
→ obtain iterator

ITERATOR
→ stateful object producing successive values

next(iterator)
→ request next value

__iter__()
→ part of iterable/iterator protocol

__next__()
→ produce next item or signal completion

StopIteration
→ iterator completion signal

ITERATOR STATE
→ belongs to iterator, not ordinary reusable container

MULTIPLE ITERATORS
→ can maintain independent traversal state

iter(iterator)
→ returns same iterator

EVERY ITERATOR
→ is iterable

EVERY ITERABLE
→ is NOT necessarily an iterator

FOR LOOP
→ obtains iterator and repeatedly consumes it

EXHAUSTED ITERATOR
→ remains exhausted

FRESH ITERATOR
→ can often be obtained again from reusable iterable
```

Generator revision:

```text
GENERATOR FUNCTION
→ function containing yield

CALL GENERATOR FUNCTION
→ creates generator object

GENERATOR OBJECT
→ iterator with suspend/resume execution

next(generator)
→ start or resume execution

yield
→ produce value + suspend

NEXT next()
→ resume after previous yield

GENERATOR LOCAL STATE
→ preserved while suspended

return
→ terminate

yield
→ suspend

GENERATOR COMPLETION
→ StopIteration

LAZY PRODUCTION
→ values produced as requested

GENERATOR EXPRESSION
→ compact syntax creating generator

(x for x in data)
→ generator

[x for x in data]
→ list

list(generator)
→ consumes generator

EXHAUSTED GENERATOR
→ does not automatically restart
```

Decorator revision:

```text
FUNCTION
→ object

FUNCTION NAME
→ reference to function object

function
→ reference function

function()
→ call function

FUNCTIONS
→ can be passed as arguments

FUNCTIONS
→ can be returned

DECORATOR
→ receives callable and returns callable

WRAPPER
→ callable surrounding original behavior

CLOSURE
→ allows wrapper to retain access to original func

@decorator
→ applies decorator during function definition

SIMPLE MENTAL MODEL
→ func = decorator(func)

AFTER WRAPPING
→ func name commonly references wrapper

*args
→ collect arbitrary positional arguments

**kwargs
→ collect arbitrary keyword arguments

func(*args, **kwargs)
→ forward collected arguments

return result
→ preserve original function's return value

functools.wraps
→ preserve important wrapped-function metadata

__wrapped__
→ reference to wrapped/original callable
```

---

# 92. Final Day 4 Mental Map

```text
                         ITERATION
                             │
                             ▼
                         ITERABLE
                             │
                           iter()
                             ▼
                         ITERATOR
                             │
                           next()
                             ▼
                           VALUE
                             │
                            ...
                             ▼
                      StopIteration
```

Then:

```text
                         GENERATOR
                             │
                             ▼
                    GENERATOR FUNCTION
                             │
                            call
                             ▼
                     GENERATOR OBJECT
                             │
                           next()
                             ▼
                           RUN
                             │
                           yield
                          /     \
                         /       \
                    value       suspend
                                  │
                                next()
                                  │
                                resume
                                  │
                                  ▼
                           function ends
                                  │
                                  ▼
                          StopIteration
```

Generator expression:

```text
(x*x for x in iterable)
          │
          ▼
    generator object
          │
          ▼
     lazy production
          │
          ▼
      single pass
```

And decorators:

```text
                    ORIGINAL FUNCTION
                           │
                           │ passed to
                           ▼
                       DECORATOR
                           │
                           ▼
                    creates WRAPPER
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          closure       *args        **kwargs
             │             │             │
             ▼             └──────┬──────┘
       original func              │
             ▲                    ▼
             └──────── func(*args, **kwargs)
                                  │
                                  ▼
                                result
                                  │
                                  ▼
                           return result
                                  │
                                  ▼
                           return wrapper
                                  │
                                  ▼
                     FUNCTION NAME REBOUND
                                  │
                                  ▼
                         NAME → WRAPPER
                                  │
                                  ▼
                              ORIGINAL
```

With metadata preservation:

```text
NAME
 │
 ▼
WRAPPER
 │
 ├── closure ──────► ORIGINAL
 │
 ├── __wrapped__ ──► ORIGINAL
 │
 ├── __name__ reflects original
 │
 └── __doc__ reflects original
```

---

# 93. Day 4 Completion Checklist

```text
ITERATION
✅ Iteration model
✅ Iterable
✅ iter()
✅ __iter__()
✅ Iterable vs iterator
✅ Iterator object
✅ Iterator state
✅ next()
✅ __next__()
✅ StopIteration
✅ Iterator exhaustion
✅ Fresh iterators
✅ Multiple independent iterators
✅ Iterator is iterable
✅ iter(iterator) is iterator
✅ for-loop internals
✅ Partially consumed iterators
✅ Loop-variable binding
```

```text
GENERATORS
✅ Generator function
✅ Generator object
✅ Generator creation
✅ Lazy execution
✅ yield
✅ Suspended execution
✅ Resume execution
✅ Preserved local state
✅ yield vs return
✅ Generator lifecycle
✅ Generator as iterator
✅ Generator + for-loop
✅ Lazy production
```

```text
GENERATOR EXPRESSIONS
✅ Generator-expression syntax
✅ Generator object creation
✅ List comprehension comparison
✅ Lazy evaluation
✅ next() consumption
✅ list() consumption
✅ Generator exhaustion
✅ Single-pass behavior
```

```text
DECORATORS
✅ Functions as objects
✅ Function reference vs call
✅ Passing functions
✅ Returning functions
✅ Manual decorator construction
✅ Wrapper function
✅ Decorator + closure connection
✅ @decorator syntax
✅ Function-name rebinding
✅ *args / **kwargs forwarding
✅ Return-value preservation
✅ Decorator metadata problem
✅ functools.wraps
✅ __wrapped__
```

# Day 4 Complete ✅

## Iteration, Iterators, Generators & Decorators

The central principle:

> **Python iteration separates the object being traversed from the stateful iterator performing traversal; generators build on the iterator protocol by allowing execution to suspend and resume lazily; and decorators build on Python's first-class functions, closures, argument forwarding, and name rebinding to wrap callable behavior without rewriting the original function's core logic.**

The most important Day 4 flow to remember is:

```text
ITERABLE
   ↓ iter()
ITERATOR
   ↓ next()
VALUE
   ↓
StopIteration


GENERATOR FUNCTION
   ↓ call
GENERATOR OBJECT
   ↓ next()
RUN
   ↓ yield
VALUE + SUSPEND
   ↓ next()
RESUME


ORIGINAL FUNCTION
   ↓
DECORATOR
   ↓
WRAPPER
   ↓ closure
ORIGINAL FUNCTION
```

**Day 4/120 — Complete. ✅**
