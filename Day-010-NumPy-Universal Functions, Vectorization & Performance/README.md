# Day 10/120 — NumPy: Universal Functions, Vectorization & Performance

## 🎯 Today's Goal

Understand how NumPy performs array operations efficiently and why vectorized NumPy operations are generally much faster than equivalent element-by-element Python loops.

Today's topics:

1. Universal Functions (`ufuncs`)
2. Vectorization
3. Performance

---

## 1. Universal Functions — `ufuncs`

### What is a ufunc?

A **universal function**, or `ufunc`, is a NumPy function that operates on `ndarray` objects in an element-by-element manner.

Examples include:

```python
np.add()
np.subtract()
np.multiply()
np.divide()
np.sqrt()
np.exp()
```

Many familiar NumPy array operators are implemented using ufuncs.

```python
a + b
```

is related to:

```python
np.add(a, b)
```

### Why do we need ufuncs?

Without NumPy, we might perform element-wise operations using Python loops:

```python
result = []

for x in values:
    result.append(x * 2)
```

With NumPy:

```python
result = values * 2
```

The operation is expressed at the **array level** instead of manually processing every element in Python.

---

## 2. Unary and Binary ufuncs

### Unary ufunc

Operates on one input.

```python
np.sqrt(a)
np.exp(a)
np.abs(a)
```

Conceptually:

```text
a
│
├── a[0] ── sqrt ──► result[0]
├── a[1] ── sqrt ──► result[1]
└── a[2] ── sqrt ──► result[2]
```

### Binary ufunc

Operates on two inputs.

```python
np.add(a, b)
np.multiply(a, b)
```

Conceptually:

```text
a ──┐
    ├── add ──► result
b ──┘
```

For compatible shapes:

```text
[1, 2, 3]
     +
[4, 5, 6]

     ↓

[5, 7, 9]
```

---

## 3. Operators and ufuncs

NumPy overloads many Python operators for arrays.

```python
a + b
a - b
a * b
a / b
```

Corresponding NumPy operations include:

```python
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
```

---

## 4. Useful ufunc Methods

Some ufuncs provide methods such as:

```python
np.add.reduce(a)
np.add.accumulate(a)
np.multiply.reduce(a)
np.add.outer(a, b)
```

These allow a ufunc to perform operations beyond simple element-wise evaluation.

We will study their behavior through experiments.

---

# 5. Vectorization

## Core Idea

Vectorization means expressing computation using **whole-array operations** instead of explicitly writing Python loops over individual elements.

Python-style approach:

```python
for i in range(len(a)):
    result[i] = a[i] * 2
```

Vectorized NumPy approach:

```python
result = a * 2
```

Mental model:

```text
Python loop

Python
 ↓
element
 ↓
Python
 ↓
element
 ↓
Python
 ↓
element


NumPy array operation

Python
 ↓
NumPy operation
 ↓
compiled numerical loop
 ↓
entire array
```

Vectorization does **not** mean that no loop exists.

The important distinction is:

> The element-wise loop is moved out of Python-level code and performed by NumPy's optimized implementation.

---

# 6. Why Vectorization Matters

Python loops execute Python-level operations repeatedly.

For numerical workloads, this introduces overhead from activities such as:

* Python interpreter execution
* dynamic object handling
* repeated indexing
* repeated operation dispatch

NumPy arrays store homogeneous data using a compact array representation.

This allows many numerical operations to execute using optimized compiled loops.

---

# 7. Performance

Consider:

```python
numbers = list(range(1_000_000))
```

Python:

```python
result = [x * 2 for x in numbers]
```

NumPy:

```python
arr = np.arange(1_000_000)
result = arr * 2
```

Both express similar mathematical work, but their execution models are different.

---

# 8. Why NumPy Can Be Faster

Several ideas contribute to NumPy's performance.

### 8.1 Homogeneous Data

An ndarray has a defined `dtype`.

```python
a.dtype
```

NumPy therefore knows how each element should be interpreted.

---

### 8.2 Compact Memory Representation

NumPy arrays can store homogeneous numerical values compactly.

This differs from ordinary Python containers that hold references to Python objects.

---

### 8.3 Compiled Numerical Loops

Operations such as:

```python
a + b
```

can dispatch into NumPy's compiled implementation rather than repeatedly executing the arithmetic operation through a Python `for` loop.

---

### 8.4 Memory Layout

Array layout can affect performance.

Important properties include:

```python
a.shape
a.strides
a.flags
```

Contiguous and predictable memory access is often advantageous for CPU caches and optimized numerical kernels.

---

### 8.5 Hardware Optimization

Depending on the NumPy build, CPU architecture, operation, dtype, and memory layout, lower-level implementations may take advantage of hardware optimizations such as SIMD/vector instructions.

Do not assume every NumPy operation is automatically SIMD-accelerated.

---

# 9. Performance Mental Model

```text
Python loop

Python interpreter
      ↓
 process element
      ↓
 process element
      ↓
 process element
      ↓
      ...


Vectorized NumPy

Python
  ↓
request array operation
  ↓
NumPy compiled implementation
  ↓
optimized loop over array data
  ↓
result ndarray
```

---

# 10. AI/ML Connection

Vectorized numerical computation appears throughout machine learning.

Instead of manually calculating:

```text
x₁w₁ + x₂w₂ + x₃w₃ + ...
```

numerical libraries express computations using arrays and matrix operations.

For example:

```python
y = X @ w
```

This style forms the computational foundation used by libraries such as:

* NumPy
* pandas
* scikit-learn
* PyTorch
* TensorFlow
* JAX

Understanding NumPy vectorization therefore helps build the mental model required for later ML and deep-learning computation.

