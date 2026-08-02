# Day 9/120 — NumPy Array Manipulation & Broadcasting

## 1. Multi-Dimensional Indexing

### 1.1 Why Multi-Dimensional Indexing?

NumPy arrays can have more than one dimension.

For example:


import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Array information:

```text
a.ndim  = 2
a.shape = (3, 3)
```

Conceptually:

```text
                 axis 1
              0    1    2
            ┌────┬────┬────┐
axis 0   0  │ 10 │ 20 │ 30 │
         1  │ 40 │ 50 │ 60 │
         2  │ 70 │ 80 │ 90 │
            └────┴────┴────┘
```

Multi-dimensional indexing allows us to select data along these different axes.

---

## 2. Core Mental Model — One Index Per Axis

For a 2-D array:

```python
a[i, j]
```

Think of this as:

```text
a[axis_0_index, axis_1_index]
```

Therefore:

```python
a[1, 2]
```

means:

```text
axis 0 → index 1
axis 1 → index 2
```

For:

```text
[
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

we get:

```python
a[1, 2]
# 60
```

### Important Mental Model

It is convenient to think:

```text
axis 0 → rows
axis 1 → columns
```

for a 2-D matrix.

However, the more general NumPy model is:

```text
Each index corresponds to an axis.
```

This model extends naturally to arrays with 3, 4, or more dimensions.

---

# 3. Integer Indexing Along One Axis

Consider:

```python
x = a[2]
```

Only one integer index has been supplied.

That integer indexes `axis 0`.

```text
index 0 → [10, 20, 30]

index 1 → [40, 50, 60]

index 2 → [70, 80, 90]
           ↑
         selected
```

Therefore:

```python
x = a[2]

print(x)
# [70 80 90]
```

Array metadata:

```text
x.ndim  = 1
x.shape = (3,)
```

---

# 4. Integer Indexing Removes an Axis

This is one of the important indexing rules.

Original array:

```text
a.shape = (3, 3)
            ↑  ↑
          axis0 axis1
```

Operation:

```python
a[2]
```

An integer was supplied for `axis 0`.

Therefore that axis is consumed.

```text
(3, 3)
 ↑
integer index
 ↓

(3,)
```

Result:

```python
a[2]
# array([70, 80, 90])
```

So:

```text
Before

ndim  = 2
shape = (3, 3)

        ↓ a[2]

After

ndim  = 1
shape = (3,)
```

### Rule

> Integer indexing consumes/removes the indexed axis from the result.

---

# 5. Indexing Multiple Axes

Consider:

```python
x = a[2, 1]
```

Now NumPy receives an integer index for both axes.

```text
axis 0 → index 2
axis 1 → index 1
```

Visual representation:

```text
                 axis 1
              0    1    2
            ┌────┬────┬────┐
axis 0   0  │ 10 │ 20 │ 30 │
         1  │ 40 │ 50 │ 60 │
         2  │ 70 │ 80 │ 90 │
            └────┴─▲──┴────┘
                   │
                  80
```

Therefore:

```python
x = a[2, 1]

print(x)
# 80
```

---

# 6. Why Isn't the Result `[80]`?

A common misconception is expecting:

```python
a[2, 1]
```

to return:

```text
[80]
```

But both axes have been indexed using integers.

Start with:

```text
shape = (3, 3)

         axis 0
            ↓
           (3, 3)
               ↑
             axis 1
```

Now:

```python
a[2, 1]
```

consumes both axes.

```text
(3, 3)
 ↑  ↑
 2  1
 │  │
 consumed
    ↓

   ()
```

Therefore:

```python
x = a[2, 1]

x.ndim
# 0

x.shape
# ()
```

The result is a **0-dimensional NumPy scalar value**, rather than a one-element 1-D array.

---

# 7. 0-D vs 1-D Array

These are different concepts.

### Scalar / 0-D

```text
80

ndim  = 0
shape = ()
```

### One-element 1-D array

```text
[80]

ndim  = 1
shape = (1,)
```

They may contain the same numerical value, but their dimensional structures are different.

---

# 8. Integer Indexing vs Slicing — Preview

Compare:

```python
a[2, 1]
```

with:

```python
a[2, 1:2]
```

The first uses integer indexing on both axes.

Conceptually:

```text
a[2, 1]

axis 0 → consumed
axis 1 → consumed

Result
   ↓

shape = ()
```

The second keeps the second axis through slicing:

```text
a[2, 1:2]

axis 0 → integer
axis 1 → slice

Result
   ↓

shape = (1,)
```

This leads to an important distinction:

```text
Integer indexing
      ↓
can remove dimensions

Slicing
      ↓
can preserve dimensions
```

We will explore this more deeply when continuing Day 9.

---

# 9. Object-State Mental Model

Consider:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Initial state:

```text
a
│
├── ndim  = 2
├── shape = (3, 3)
│
└── logical structure
      │
      ├── axis 0 → 3 positions
      └── axis 1 → 3 positions
```

Operation:

```python
x = a[2]
```

State transformation:

```text
a
shape (3,3)
   │
   │ integer index axis 0
   ▼
x
shape (3,)
```

Operation:

```python
y = a[2,1]
```

State transformation:

```text
a
shape (3,3)
   │
   ├── integer index axis 0
   └── integer index axis 1
              │
              ▼
              y
           shape ()
           ndim 0
```

---

# 10. General Mental Model

Never restrict the idea of NumPy indexing to:

```text
row, column
```

Instead think:

```text
NumPy Array
     │
     ├── axis 0
     ├── axis 1
     ├── axis 2
     ├── ...
     └── axis N
```

An indexing expression specifies what should happen along those axes.

For example:

```python
x[i, j, k]
```

conceptually means:

```text
i → axis 0
j → axis 1
k → axis 2
```

This becomes especially important when working with tensors.

---

# 11. AI/ML Connection

Machine-learning data commonly has multiple dimensions.

### Tabular dataset

```text
(samples, features)
```

Example:

```text
(10000, 20)
```

### Grayscale image batch

```text
(batch, height, width)
```

### Deep-learning image tensor

Common layouts include:

```text
(batch, channels, height, width)
```

or

```text
(batch, height, width, channels)
```

### Transformer representations

A common conceptual shape is:

```text
(batch, sequence_length, hidden_dimension)
```

Therefore, thinking in terms of **axes rather than only rows and columns** prepares us for later tensor operations in deep-learning libraries.

---

# 12. Misconceptions Corrected

### Misconception 1

```python
a[2]
```

selects the second row.

Incorrect.

NumPy uses zero-based indexing:

```text
0 → first
1 → second
2 → third
```

---

### Misconception 2

```python
a[2,1]
```

returns:

```text
[80]
```

Incorrect.

Both axes are integer-indexed, so both axes are consumed.

Result:

```text
80

ndim  = 0
shape = ()
```

---

### Misconception 3

Always think about NumPy indexing as:

```text
row → column
```

This is incomplete.

Better mental model:

```text
index 0 → axis 0
index 1 → axis 1
index 2 → axis 2
...
```

---

# 13. Quick Revision Sheet

```text
a.shape = (3,3)

a[2]
    ↓
[70,80,90]

ndim  = 1
shape = (3,)
```

```text
a[2,1]
    ↓
80

ndim  = 0
shape = ()
```

Core rule:

```text
INTEGER INDEX
      ↓
consumes an axis
```

General indexing model:

```text
a[i, j, k, ...]

i → axis 0
j → axis 1
k → axis 2
...
```

---

# Day 9 Progress

Completed today:

* [x] Multi-dimensional indexing fundamentals
* [x] Axis-based indexing mental model
* [x] Integer indexing
* [x] Dimension reduction from integer indexing
* [x] 0-D vs 1-D distinction
* [x] Initial integer-indexing vs slicing distinction

## Resume Point

Continue with:

x = a[1:3]
```

and investigate:

```text
x       = ?
x.ndim  = ?
x.shape = ?

