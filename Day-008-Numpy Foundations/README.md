Here are your **Day 8 notes for everything we covered today so far**.

# 🚀 Day 8/120 — NumPy Foundations

## 1. Why NumPy?

Python already provides lists:

```python
numbers = [10, 20, 30, 40]
```

But Python lists are **general-purpose containers**. NumPy arrays are designed specifically for efficient numerical computation.

### Python List vs NumPy Array

```python
python_list = [1, 2, 3]
python_list * 2
```

Output:

```text
[1, 2, 3, 1, 2, 3]
```

For lists, `*` means **sequence repetition**.

With NumPy:

```python
import numpy as np

a = np.array([1, 2, 3])
a * 2
```

Output:

```text
[2 4 6]
```

For an `ndarray`, this is **element-wise multiplication**.

Mental model:

```text
Python List
┌─────┬─────┬─────┐
│ ref │ ref │ ref │
└──│──┴──│──┴──│──┘
   ▼     ▼     ▼
   1     2     3
 Python objects


NumPy numeric array
┌─────┬─────┬─────┐
│  1  │  2  │  3  │
└─────┴─────┴─────┘
   homogeneous data
```

This representation is one reason NumPy can perform numerical operations efficiently.

---

# 2. `ndarray`

The fundamental NumPy array type is:

```python
numpy.ndarray
```

`ndarray` means **N-dimensional array**.

Create one using:

```python
a = np.array([10, 20, 30])
```

Check its type:

```python
type(a)
```

Output:

```python
<class 'numpy.ndarray'>
```

Important distinction:

```text
np.array()   → array creation function

np.ndarray   → array class/type
```

Python's object model still applies:

```text
a ───────────────► ndarray object
```

The variable `a` is a name referring to the array object.

---

# 3. Element-Wise Operations

Consider:

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b
```

Output:

```text
[11 22 33]
```

Mental model:

```text
[ 1   2   3 ]
  +   +   +
[10  20  30]
  │   │   │
  ▼   ▼   ▼
[11  22  33]
```

Similarly:

```python
a * 2
a + 5
a ** 2
```

operate element-wise.

This style of whole-array numerical computation is central to **vectorized NumPy code**.

---

# 4. Array Dimensions — `ndim`

`ndim` tells us:

> **How many axes does this array have?**

### 1D

```python
a = np.array([10, 20, 30])

a.ndim
# 1
```

```text
[10 20 30]

one axis
```

### 2D

```python
b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b.ndim
# 2
```

Mental model:

```text
             axis 1
             ─────►

           10 20 30
axis 0     40 50 60
   │
   ▼
```

Important:

> `ndim = 2` does **not** mean two rows.

It means the array has **two axes**.

Prefer NumPy terminology:

```text
axis 0
axis 1
axis 2
...
```

rather than thinking only in terms of x/y axes.

---

# 5. Array Shape — `shape`

`shape` tells us:

> **How many elements exist along each axis?**

Example:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Then:

```python
a.shape
# (2, 3)
```

Meaning:

```text
axis 0 → size 2
axis 1 → size 3

shape → (2, 3)
```

Another example:

```python
b = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
```

```python
b.shape
# (4, 2)
```

Mental model:

```text
        axis 1 → 2
       ┌───────┐
       │ 1   2 │
axis 0 │ 3   4 │
  ↓    │ 5   6 │
  4    │ 7   8 │
       └───────┘

shape = (4, 2)
```

Relationship:

```python
a.ndim == len(a.shape)
```

---

# 6. One-Dimensional Shape

This distinction is important.

```python
a = np.array([10, 20, 30])
```

Its properties are:

```python
a.ndim
# 1

a.shape
# (3,)
```

`(3,)` means:

> One axis containing three elements.

It does **not** mean three dimensions.

Compare:

```text
[10, 20, 30]

shape = (3,)
ndim  = 1
```

versus:

```text
[[10, 20, 30]]

shape = (1, 3)
ndim  = 2
```

Same number of values, but different array structures.

This distinction becomes important when preparing input shapes for ML models.

---

# 7. Array Size — `size`

`size` gives:

> **Total number of elements in the array.**

Example:

```python
a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])
```

```python
a.shape
# (4, 2)

a.size
# 8
```

Because:

```text
4 × 2 = 8
```

For:

```python
x = np.zeros((3, 4, 5))
```

we have:

```text
ndim  = 3

shape = (3, 4, 5)

size  = 3 × 4 × 5
      = 60
```

General mental model:

```text
shape = (d₀, d₁, d₂, ...)

size = d₀ × d₁ × d₂ × ...
```

---

# 8. `ndim` vs `shape` vs `size`

This is today's most important distinction so far:

```text
┌─────────┬────────────────────────────┐
│ ndim    │ Number of axes             │
├─────────┼────────────────────────────┤
│ shape   │ Size along every axis      │
├─────────┼────────────────────────────┤
│ size    │ Total number of elements   │
└─────────┴────────────────────────────┘
```

Example:

```python
x = np.zeros((3, 4, 5))
```

```text
ndim
 ↓
 3

shape
 ↓
(3, 4, 5)

size
 ↓
3 × 4 × 5 = 60
```

---

# 9. Creating Arrays

## `np.array()`

Creates an `ndarray` from array-like input.

```python
a = np.array([1, 2, 3])
```

---

## `np.zeros()`

Creates an array filled with zeros.

```python
a = np.zeros((2, 3))
```

Conceptually:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

Shape:

```text
(2, 3)
```

---

## `np.ones()`

Creates an array filled with ones.

```python
a = np.ones((2, 3))
```

Conceptually:

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

Useful when numerical storage needs to be initialized before computation.

The reason these values commonly appear as `0.` and `1.` involves **`dtype`**, which is still to be covered.

---

# 10. `np.arange()`

Syntax:

```python
np.arange(start, stop, step)
```

Mental model:

> **Use `arange()` when you know the step size.**

Example:

```python
a = np.arange(2, 12, 3)
```

Sequence:

```text
2 → 5 → 8 → 11 → STOP
```

Result:

```text
[2 5 8 11]
```

Important:

> `stop` is excluded.

Properties:

```python
a.ndim
# 1

a.shape
# (4,)

a.size
# 4
```

---

# 11. `np.linspace()` — Current Stopping Point

Syntax:

```python
np.linspace(start, stop, num)
```

Mental difference:

```text
arange
   ↓
"I know the STEP."

linspace
   ↓
"I know HOW MANY values I want."
```

Example:

```python
np.linspace(0, 10, 5)
```

asks NumPy for:

> **5 evenly spaced values between 0 and 10.**

Unlike `arange()`, `linspace()` includes the endpoint by default.

We stopped here before working through the result.

---

# 🧠 Unified Mental Map

```text
                    NumPy
                      │
                   ndarray
                      │
        ┌─────────────┼─────────────┐
        │             │             │
      ndim          shape          size
        │             │             │
        ▼             ▼             ▼
   # of axes      size/axis     total values


Array Creation
│
├── np.array()
│
├── np.zeros()
│
├── np.ones()
│
├── np.arange()
│      └── specify STEP
│
└── np.linspace()
       └── specify NUMBER OF VALUES
```

## 🤖 AI/ML Connection

ML data is naturally represented using multidimensional numerical arrays.

For example:

```text
Single feature vector
shape = (10,)

Dataset
shape = (1000, 10)
         │      │
       samples features

Image
shape = (224, 224, 3)
         │    │    │
      height width channels

Image batch
shape = (32, 224, 224, 3)
         │    │    │    │
       batch  H    W  channels
```

Understanding `ndim`, `shape`, and `size` is therefore fundamental before working with NumPy, scikit-learn, PyTorch, or TensorFlow.

---
