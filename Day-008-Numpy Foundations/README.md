# Day 8/120 — NumPy Foundations: Arrays, Data Types & Memory Layout

> **AI Engineering in 120 Days**

Day 8 focuses on understanding NumPy from the inside out.

The goal is not just to learn NumPy syntax such as `np.array()` or `reshape()`, but to build a correct mental model of:

* What an `ndarray` actually is
* How multidimensional arrays are represented
* How NumPy chooses and stores data types
* Why NumPy uses fixed-width numeric types
* How array data is stored in memory
* What strides represent
* Why slicing often creates views
* How views differ from copies
* How C-order and Fortran-order differ
* Why memory layout matters for numerical and AI/ML workloads

---

# Table of Contents

1. [Why NumPy?](#1-why-numpy)
2. [Python Lists vs NumPy Arrays](#2-python-lists-vs-numpy-arrays)
3. [The ndarray Object](#3-the-ndarray-object)
4. [Dimensions, Shape and Size](#4-dimensions-shape-and-size)
5. [Creating NumPy Arrays](#5-creating-numpy-arrays)
6. [Indexing](#6-indexing)
7. [Slicing](#7-slicing)
8. [Integer Indexing vs Slicing](#8-integer-indexing-vs-slicing)
9. [Reshaping Arrays](#9-reshaping-arrays)
10. [Vectorized Operations](#10-vectorized-operations)
11. [NumPy Data Types](#11-numpy-data-types)
12. [Signed and Unsigned Integers](#12-signed-and-unsigned-integers)
13. [itemsize and nbytes](#13-itemsize-and-nbytes)
14. [Type Inference](#14-type-inference)
15. [Type Promotion](#15-type-promotion)
16. [Type Conversion with astype](#16-type-conversion-with-astype)
17. [Integer Overflow](#17-integer-overflow)
18. [Floating-Point Precision](#18-floating-point-precision)
19. [Why ML Commonly Uses float32](#19-why-ml-commonly-uses-float32)
20. [The NumPy Data Buffer](#20-the-numpy-data-buffer)
21. [Logical Arrays vs Physical Memory](#21-logical-arrays-vs-physical-memory)
22. [Contiguous Memory](#22-contiguous-memory)
23. [Strides](#23-strides)
24. [How NumPy Finds an Element in Memory](#24-how-numpy-finds-an-element-in-memory)
25. [Views vs Copies](#25-views-vs-copies)
26. [Memory Sharing](#26-memory-sharing)
27. [Advanced Indexing vs Basic Slicing](#27-advanced-indexing-vs-basic-slicing)
28. [C-order](#28-c-order)
29. [Fortran-order](#29-fortran-order)
30. [Contiguity Flags](#30-contiguity-flags)
31. [Non-Contiguous Views](#31-non-contiguous-views)
32. [Why Memory Layout Matters for Performance](#32-why-memory-layout-matters-for-performance)
33. [Unified ndarray Mental Model](#33-unified-ndarray-mental-model)
34. [Common Misconceptions](#34-common-misconceptions)
35. [AI/ML Connections](#35-aiml-connections)
36. [Revision Sheet](#36-revision-sheet)
37. [Completion Checklist](#37-completion-checklist)

---

# 1. Why NumPy?

Python lists are flexible general-purpose containers.

```python
values = [10, 20, 30, 40]
```

They can even contain objects of different types:

```python
values = [10, "hello", True, 3.14]
```

That flexibility is useful for general Python programming.

Numerical computing, however, has different requirements.

Machine learning, scientific computing, computer vision, signal processing, statistics, and deep learning frequently operate on huge collections of numbers.

Examples include:

```text
Feature vectors

[0.5, 1.2, 3.8, 7.1]
```

```text
Dataset

[
 [feature1, feature2, feature3],
 [feature1, feature2, feature3],
 ...
]
```

```text
Image

height × width × channels
```

```text
Deep-learning batch

batch × channels × height × width
```

For these workloads we want:

* compact numerical storage
* predictable data representation
* multidimensional arrays
* efficient array-level operations
* interoperability with native numerical libraries

NumPy provides this through the `ndarray`.

```python
import numpy as np

a = np.array([10, 20, 30])
```

---

# 2. Python Lists vs NumPy Arrays

Consider:

```python
values = [1, 2, 3]
```

and:

```python
values = np.array([1, 2, 3])
```

They may look similar, but their behavior and internal representation are different.

## Python list

A Python list is conceptually a container of references to Python objects.

```text
list

┌─────┬─────┬─────┐
│ ref │ ref │ ref │
└──┬──┴──┬──┴──┬──┘
   │     │     │
   ▼     ▼     ▼
   1     2     3
```

Each value is a Python object.

---

## NumPy array

A numerical NumPy array generally stores homogeneous fixed-width values in a data buffer.

```text
ndarray
   │
   ▼

[1][2][3]
```

The array also stores metadata describing how that memory should be interpreted.

This design is one of the foundations of NumPy's memory efficiency and performance.

---

# 3. The `ndarray` Object

NumPy's main array type is:

```python
numpy.ndarray
```

Example:

```python
a = np.array([10, 20, 30])

print(type(a))
```

Output:

```text
<class 'numpy.ndarray'>
```

An `ndarray` should not be thought of as merely:

> a list with faster mathematics.

A better mental model is:

```text
ndarray
│
├── reference to data
├── dtype
├── shape
├── strides
└── other metadata
```

Conceptually:

```text
             ndarray
                │
      ┌─────────┴─────────┐
      │                   │
   metadata            data
      │                   │
      ▼                   ▼
 shape=(...)        raw memory buffer
 dtype=...
 strides=...
```

This mental model becomes extremely important when understanding views, slicing, reshaping, and memory layout.

---

# 4. Dimensions, Shape and Size

Consider:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

## `ndim`

```python
a.ndim
```

returns:

```text
2
```

`ndim` means:

> Number of axes.

It does **not** mean "number of rows".

---

## `shape`

```python
a.shape
```

returns:

```text
(2, 3)
```

Meaning:

```text
axis 0 → 2 positions
axis 1 → 3 positions
```

For a conventional matrix this corresponds to:

```text
2 rows
3 columns
```

But thinking in terms of **axes** is more general because NumPy arrays can have more than two dimensions.

---

## `size`

```python
a.size
```

returns:

```text
6
```

because:

```text
2 × 3 = 6
```

For:

```python
a = np.zeros((3, 4, 5))
```

we have:

```text
ndim  = 3

shape = (3, 4, 5)

size  = 3 × 4 × 5
      = 60
```

---

# 5. Creating NumPy Arrays

## `np.array()`

```python
a = np.array([1, 2, 3])
```

---

## `np.zeros()`

```python
a = np.zeros((2, 3))
```

Result:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

## `np.ones()`

```python
a = np.ones((2, 3))
```

---

## `np.empty()`

```python
a = np.empty((2, 3))
```

Important:

`empty()` does **not** mean:

> Create an array containing zero elements.

The array still has the requested shape and size.

Instead, NumPy allocates storage without initializing every entry to a specific value.

Therefore, never depend on the initial values returned by `empty()`.

Use it when the contents will immediately be overwritten.

---

## `np.arange()`

```python
a = np.arange(0, 10, 2)
```

Result:

```text
[0 2 4 6 8]
```

Mental model:

```text
start
stop
step
```

You control the **step size**.

---

## `np.linspace()`

```python
a = np.linspace(0, 10, 5)
```

Result:

```text
[ 0.   2.5  5.   7.5 10. ]
```

Mental model:

> Give me exactly N equally spaced samples over an interval.

```text
start ●────●────●────●────● stop
```

For:

```python
np.linspace(0, 10, 5)
```

there are five points but four intervals.

Therefore:

```text
step = (10 - 0) / (5 - 1)
     = 2.5
```

A useful distinction:

```text
arange()
→ control the step

linspace()
→ control the number of samples
```

---

# 6. Indexing

## 1D indexing

```python
a = np.array([10, 20, 30, 40])

a[0]
# 10

a[2]
# 30

a[-1]
# 40
```

---

## 2D indexing

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Use:

```python
a[axis0_index, axis1_index]
```

For a matrix:

```python
a[row, column]
```

Example:

```python
a[1, 2]
```

returns:

```text
60
```

because:

```text
axis 0 index = 1
axis 1 index = 2
```

---

# 7. Slicing

NumPy uses Python's slicing syntax:

```text
start:stop:step
```

Example:

```python
a = np.array([10, 20, 30, 40, 50])

a[1:4]
```

Result:

```text
[20 30 40]
```

Remember:

```text
start → included
stop  → excluded
```

Other examples:

```python
a[:3]
a[3:]
a[::2]
a[::-1]
```

---

## 2D slicing

```python
a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
```

```python
a[0:2, 1:3]
```

means:

```text
axis 0 → indices 0 and 1

axis 1 → indices 1 and 2
```

Result:

```text
[[20 30]
 [60 70]]
```

Think:

```text
a[axis0_slice, axis1_slice]
```

This mental model scales naturally to higher-dimensional arrays.

---

# 8. Integer Indexing vs Slicing

This distinction is extremely important.

Given:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Integer indexing:

```python
a[0]
```

returns:

```text
[10 20 30]
```

Shape:

```text
(3,)
```

Dimension:

```text
1
```

The indexed axis has been removed from the result.

---

Now compare:

```python
a[0:1]
```

Result:

```text
[[10 20 30]]
```

Shape:

```text
(1, 3)
```

Dimension:

```text
2
```

So:

```text
a[0]

shape = (3,)
ndim  = 1
```

while:

```text
a[0:1]

shape = (1,3)
ndim  = 2
```

This distinction becomes very important when preparing tensors and model inputs.

---

# 9. Reshaping Arrays

Consider:

```python
a = np.array([1, 2, 3, 4, 5, 6])
```

Shape:

```text
(6,)
```

We can reorganize it:

```python
b = a.reshape(2, 3)
```

Result:

```text
[[1 2 3]
 [4 5 6]]
```

The critical invariant is:

> Reshaping can change the shape but cannot change the total number of elements.

Therefore:

```text
old size = new size
```

For six elements:

```text
(6,)     → valid

(1,6)    → valid

(2,3)    → valid

(3,2)    → valid

(6,1)    → valid

(2,4)    → invalid
```

because:

```text
2 × 4 = 8
```

but only six elements exist.

---

## Using `-1`

NumPy can infer one dimension.

```python
a = np.arange(12)

b = a.reshape(3, -1)
```

NumPy solves:

```text
3 × ? = 12

? = 4
```

Therefore:

```text
shape = (3,4)
```

Another example:

```python
a.reshape(2, 3, -1)
```

for 24 elements gives:

```text
2 × 3 × ? = 24

? = 4
```

Resulting shape:

```text
(2,3,4)
```

Only one dimension can be inferred using `-1`.

---

# 10. Vectorized Operations

One of NumPy's major strengths is expressing operations over whole arrays.

Python approach:

```python
values = [1, 2, 3, 4]

result = []

for x in values:
    result.append(x ** 2)
```

NumPy:

```python
a = np.array([1, 2, 3, 4])

result = a ** 2
```

Result:

```text
[1 4 9 16]
```

---

## Scalar operations

```python
a + 10
a - 10
a * 10
a / 10
a ** 2
```

---

## Array operations

```python
a = np.array([1, 2, 3])

b = np.array([10, 20, 30])

a + b
```

Result:

```text
[11 22 33]
```

```python
a * b
```

Result:

```text
[10 40 90]
```

Important:

```text
*
```

means element-wise multiplication.

It is not matrix multiplication.

Matrix multiplication can be expressed using:

```python
a @ b
```

or appropriate NumPy linear algebra operations.

---

# 11. NumPy Data Types

NumPy arrays are generally **homogeneous**.

That means elements share a common `dtype`.

```python
a = np.array([1, 2, 3])

print(a.dtype)
```

NumPy provides fixed-width numerical types such as:

```text
Signed integers

int8
int16
int32
int64
```

```text
Unsigned integers

uint8
uint16
uint32
uint64
```

```text
Floating point

float16
float32
float64
```

```text
Boolean

bool
```

The number generally indicates the number of bits used.

```text
int8
→ 8 bits
→ 1 byte

int32
→ 32 bits
→ 4 bytes

float32
→ 32 bits
→ 4 bytes

float64
→ 64 bits
→ 8 bytes
```

---

# 12. Signed and Unsigned Integers

## Signed

Signed integers represent negative and non-negative values.

For an `n`-bit signed integer:

```text
-2^(n-1) to 2^(n-1)-1
```

For `int8`:

```text
-128 → 127
```

---

## Unsigned

Unsigned integers represent only non-negative values.

Range:

```text
0 → 2^n - 1
```

For `uint8`:

```text
0 → 255
```

Compare:

```text
int8

-128 ........ 127


uint8

0 ............ 255
```

Both use exactly:

```text
8 bits
```

The difference is how the available bit patterns are interpreted.

---

## Why 256 patterns?

Eight bits can represent:

```text
2^8 = 256
```

different bit patterns.

Examples:

```text
00000000
00000001
00000010
...
11111111
```

The bits themselves do not inherently mean a particular number.

The dtype determines how they should be interpreted.

For example:

```text
11111111
```

as:

```text
uint8 → 255

int8 → -1
```

Same bits.

Different interpretation.

This is one of the deepest reasons `dtype` is part of ndarray metadata.

---

# 13. `itemsize` and `nbytes`

Consider:

```python
a = np.array([10, 20, 30, 40], dtype=np.int16)
```

`int16` uses:

```text
16 bits
= 2 bytes
```

## `itemsize`

```python
a.itemsize
```

returns:

```text
2
```

Meaning:

> Number of bytes used by one element.

---

## `nbytes`

```python
a.nbytes
```

returns:

```text
8
```

because:

```text
size = 4

itemsize = 2

nbytes = size × itemsize

       = 4 × 2

       = 8 bytes
```

Important:

`nbytes` refers to the bytes occupied by the array elements, not necessarily the total memory footprint of the Python ndarray object and all metadata.

---

# 14. Type Inference

If we don't specify a dtype:

```python
a = np.array([1, 2, 3])
```

NumPy determines an appropriate dtype.

Examples:

```python
np.array([1, 2, 3])
```

→ integer dtype

```python
np.array([1.0, 2.0, 3.0])
```

→ floating-point dtype

```python
np.array([True, False])
```

→ boolean dtype

The exact default integer width may depend on the platform/environment.

---

## Mixed types

Consider:

```python
a = np.array([1, 2.5, 3])
```

NumPy arrays use one common dtype.

Therefore NumPy must choose a dtype capable of representing all the values.

Conceptually:

```text
1       → integer
2.5     → float
3       → integer

          ↓

common dtype

          ↓

float
```

Result:

```text
[1.0 2.5 3.0]
```

---

# 15. Type Promotion

When different numerical types participate in an operation, NumPy determines a common result dtype according to its promotion rules.

Example:

```python
a = np.array([1, 2, 3], dtype=np.int16)

b = np.array([10.5, 20.5, 30.5], dtype=np.float32)

c = a + b
```

Result:

```text
[11.5 22.5 33.5]
```

with an appropriate floating-point result dtype.

A simplified beginner mental model is:

```text
bool
 ↓
integer
 ↓
floating point
```

But NumPy's real promotion rules are more precise than a simple hierarchy and should be checked when exact dtype behavior matters.

---

# 16. Type Conversion with `astype()`

We can explicitly convert an array:

```python
a = np.array([1, 2, 3])

b = a.astype(np.float32)
```

Now:

```text
a → integer array

b → float32 array
```

Importantly:

```python
a is b
```

is normally:

```text
False
```

`astype()` normally creates a new array containing converted values.

---

## Float to integer

```python
a = np.array([1.9, 2.8, 3.7])

b = a.astype(np.int32)
```

Result:

```text
[1 2 3]
```

The fractional portion is discarded during this conversion.

Do not confuse this with mathematical rounding.

---

# 17. Integer Overflow

Fixed-width integer types have finite ranges.

For example:

```text
int8

-128 → 127
```

Suppose:

```python
a = np.array([120], dtype=np.int8)
```

Mathematically:

```text
120 + 10 = 130
```

But:

```text
130 > 127
```

so it cannot be represented by `int8`.

Fixed-width integer arithmetic can therefore overflow.

Conceptually:

```text
...
125
126
127
-128
-127
-126
...
```

The result wraps according to fixed-width arithmetic.

This is fundamentally different from Python's arbitrary-precision `int`, which can grow to represent much larger integers.

---

# 18. Floating-Point Precision

Floating-point numbers cannot represent every real number exactly.

For example:

```python
print(0.1 + 0.2)
```

may produce:

```text
0.30000000000000004
```

Why?

Computers represent floating-point numbers in binary.

Some decimal fractions require infinitely repeating binary representations.

This is analogous to:

```text
1 / 3
```

in decimal:

```text
0.333333333...
```

Therefore floating-point numbers should be understood as finite approximations to real values.

---

## Precision levels

Broadly:

```text
float16
→ less storage
→ lower precision

float32
→ moderate storage
→ useful precision

float64
→ more storage
→ higher precision
```

The exact precision and range come from the floating-point representation, not simply the number of decimal digits written in source code.

---

# 19. Why ML Commonly Uses `float32`

Suppose a model has:

```text
100,000,000 parameters
```

Using `float64`:

```text
100,000,000 × 8 bytes

≈ 800 MB
```

Using `float32`:

```text
100,000,000 × 4 bytes

≈ 400 MB
```

That is roughly half the parameter storage.

Modern accelerators are also highly optimized for formats such as:

```text
float32
float16
bfloat16
```

For many ML workloads, `float32` provides an effective balance between:

```text
precision
memory
compute throughput
```

Modern deep learning increasingly also uses mixed precision and lower-precision formats where appropriate.

---

# 20. The NumPy Data Buffer

This is the foundation of NumPy memory layout.

Consider:

```python
a = np.array([10, 20, 30], dtype=np.int32)
```

Conceptually:

```text
             ndarray
                │
                ▼

       ┌─────────────────┐
       │ shape = (3,)    │
       │ dtype = int32   │
       │ strides = (...) │
       │ pointer/reference│
       └────────┬────────┘
                │
                ▼

          DATA BUFFER

       [10][20][30]
```

The data buffer contains the underlying bytes.

The ndarray metadata describes how those bytes should be interpreted.

A useful mental model is:

> ndarray = data access + metadata

---

# 21. Logical Arrays vs Physical Memory

Consider:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
], dtype=np.int32)
```

Logically:

```text
[[10 20 30]
 [40 50 60]]
```

But memory itself is linear.

For a normal C-contiguous layout, think:

```text
[10][20][30][40][50][60]
```

The 2D structure comes from metadata such as:

```text
shape
dtype
strides
```

This is an extremely important mental model:

> A multidimensional array is a logical interpretation of data stored in memory.

---

# 22. Contiguous Memory

A contiguous layout allows elements to be traversed according to a standard memory order without gaps between the expected neighboring elements.

For example:

```text
[10][20][30][40][50][60]
```

Sequential access patterns can interact efficiently with CPU caches.

However, contiguous memory is only one part of NumPy's performance.

Other important factors include:

* native compiled loops
* reduced Python interpreter overhead
* optimized numerical kernels
* SIMD/vector instructions
* BLAS/LAPACK integrations for relevant operations

---

# 23. Strides

Strides are one of the most important NumPy concepts.

> A stride tells NumPy how many **bytes** to move in memory when advancing one position along an axis.

Consider:

```python
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
], dtype=np.int32)
```

We have:

```text
shape = (3,4)

itemsize = 4 bytes
```

For normal C-order storage:

```text
memory:

[1][2][3][4][5][6][7][8][9][10][11][12]
```

Moving along axis 1:

```text
1 → 2
```

requires:

```text
4 bytes
```

Moving along axis 0:

```text
1
↓
5
```

requires moving past four `int32` positions:

```text
4 × 4
= 16 bytes
```

Therefore:

```python
a.strides
```

is:

```text
(16, 4)
```

Interpretation:

```text
strides = (16, 4)
            │   │
            │   └── axis 1 step = 4 bytes
            │
            └────── axis 0 step = 16 bytes
```

---

# 24. How NumPy Finds an Element in Memory

Suppose:

```python
a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
], dtype=np.int32)
```

Then:

```text
shape = (2,4)

strides = (16,4)
```

We want:

```python
a[1,2]
```

Conceptually, the byte offset is:

```text
(index_axis0 × stride_axis0)
+
(index_axis1 × stride_axis1)
```

Therefore:

```text
(1 × 16) + (2 × 4)

= 16 + 8

= 24 bytes
```

Memory:

```text
value:    10   20   30   40   50   60   70   80

offset:    0    4    8   12   16   20   24   28
                                         ↑
                                       a[1,2]
```

Therefore:

```text
a[1,2] = 70
```

This is the deeper purpose of strides:

> Strides help map multidimensional indices to positions in the underlying memory.

---

# 25. Views vs Copies

Consider:

```python
a = np.array([10, 20, 30, 40, 50])

b = a[1:4]
```

Basic slicing generally produces a **view**.

Conceptually:

```text
              shared data

[10][20][30][40][50]
     ▲   ▲   ▲
     │   │   │
     └── b ──┘
```

`a` and `b` are different ndarray objects:

```python
a is b
```

→

```text
False
```

But they can access overlapping memory.

Therefore:

```python
b[0] = 999
```

can change `a`:

```text
a = [10 999 30 40 50]

b = [999 30 40]
```

---

## Copy

```python
c = a[1:4].copy()
```

Conceptually:

```text
a
│
▼
Buffer A


c
│
▼
Buffer B
```

Now changing `c` does not change `a`.

---

# 26. Memory Sharing

NumPy provides:

```python
np.shares_memory(a, b)
```

Example:

```python
a = np.array([10, 20, 30, 40])

b = a[1:3]

np.shares_memory(a, b)
```

returns:

```text
True
```

For:

```python
c = a[1:3].copy()
```

```python
np.shares_memory(a, c)
```

returns:

```text
False
```

---

## `.base`

A simple view may expose its backing object through:

```python
b.base
```

For some simple cases:

```python
b.base is a
```

may be `True`.

However, `.base is a` should not be treated as a universal memory-sharing test because view chains and other backing objects can exist.

Use appropriate memory-sharing checks when that is the actual question.

---

# 27. Advanced Indexing vs Basic Slicing

A critical distinction:

## Basic slicing

Examples:

```python
a[1:4]

a[::2]

a[:, 1:3]
```

generally produces **views**.

---

## Advanced indexing

Examples:

```python
a[[0, 2, 4]]
```

or:

```python
a[a > 20]
```

generally produces **copies**.

Therefore:

```text
basic slicing
      ↓
usually view


advanced indexing
      ↓
usually copy
```

This difference is important for both correctness and memory usage.

---

# 28. C-order

C-order is commonly described as **row-major order** for 2D arrays.

Consider:

```text
[1 2]
[3 4]
[5 6]
```

C-order traversal:

```text
1 → 2 → 3 → 4 → 5 → 6
```

For:

```text
shape = (3,2)

dtype = int32
```

we get:

```text
strides = (8,4)
```

because:

```text
axis 1

1 → 2

4 bytes
```

while:

```text
axis 0

1
↓
3

8 bytes
```

A stronger general mental model is:

> In C-order, the **last axis changes fastest**.

---

# 29. Fortran-order

Fortran-order is commonly described as **column-major order** for 2D arrays.

Same logical matrix:

```text
[1 2]
[3 4]
[5 6]
```

But F-order traversal is:

```text
1 → 3 → 5 → 2 → 4 → 6
```

For:

```text
shape = (3,2)

dtype = int32
```

strides are:

```text
(4,12)
```

because:

```text
axis 0

1
↓
3

4 bytes
```

while:

```text
axis 1

1 → 2

3 elements × 4 bytes
= 12 bytes
```

The stronger general mental model is:

> In Fortran-order, the **first axis changes fastest**.

---

## Comparison

```text
Same logical array:

[1 2]
[3 4]
[5 6]
```

C-order:

```text
memory traversal:

1 2 3 4 5 6

strides:

(8,4)
```

F-order:

```text
memory traversal:

1 3 5 2 4 6

strides:

(4,12)
```

The logical values and shape can remain the same while the memory layout differs.

---

# 30. Contiguity Flags

NumPy exposes memory-layout information through:

```python
a.flags
```

Important flags include:

```text
C_CONTIGUOUS

F_CONTIGUOUS
```

You can check:

```python
a.flags["C_CONTIGUOUS"]

a.flags["F_CONTIGUOUS"]
```

A typical C-contiguous 2D array may have:

```text
C_CONTIGUOUS = True

F_CONTIGUOUS = False
```

These flags describe whether the array satisfies the corresponding contiguous layout requirements.

---

# 31. Non-Contiguous Views

Consider:

```python
a = np.array(
    [10, 20, 30, 40, 50, 60],
    dtype=np.int32
)

b = a[::2]
```

Then:

```text
a = [10 20 30 40 50 60]

b = [10 30 50]
```

Original stride:

```text
a.strides = (4,)
```

because neighboring `int32` values are four bytes apart.

But:

```text
b.strides = (8,)
```

because `b` skips one element each time.

Conceptually:

```text
[10][20][30][40][50][60]
 ↑       ↑       ↑
 │       │       │
 └────── b ──────┘
```

Therefore:

> A view does not necessarily have to be contiguous.

It can interpret selected positions of an existing buffer using different strides.

---

# 32. Why Memory Layout Matters for Performance

Modern CPUs have caches.

Accessing nearby memory sequentially often improves **spatial locality**.

Consider:

```text
[10][20][30][40][50][60]
```

When the processor requests one value, nearby bytes may be brought into a cache line.

If subsequent operations need neighboring values, the CPU may already have them in cache.

This can reduce expensive memory traffic.

---

## C-order example

For a large C-contiguous matrix:

```python
a = np.zeros((1000, 1000))
```

traversing:

```text
a[0,0]
a[0,1]
a[0,2]
a[0,3]
...
```

follows the contiguous last axis.

Repeatedly traversing:

```text
a[0,0]
a[1,0]
a[2,0]
...
```

uses a larger stride.

For low-level loops over sufficiently large arrays, memory-access order can therefore influence performance.

NumPy operations themselves may use optimized implementations, so performance should ultimately be measured rather than guessed.

---

# 33. Unified `ndarray` Mental Model

This is the most important mental model from Day 8.

Consider:

```python
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
], dtype=np.int32)
```

Think:

```text
                    a
                    │
                    ▼
          ┌──────────────────┐
          │     ndarray      │
          ├──────────────────┤
          │ ndim      = 2    │
          │ shape   = (2,3)  │
          │ size      = 6    │
          │ dtype   = int32  │
          │ itemsize  = 4    │
          │ nbytes   = 24    │
          │ strides=(12,4)   │
          │ flags            │
          │ data reference   │
          └────────┬─────────┘
                   │
                   ▼

               DATA BUFFER

       [10][20][30][40][50][60]
```

This explains nearly everything we learned.

### `shape`

Tells NumPy:

> What is the logical multidimensional structure?

### `dtype`

Tells NumPy:

> How should each element's bytes be interpreted?

### `itemsize`

Tells us:

> How many bytes are used per element?

### `strides`

Tell NumPy:

> How many bytes should I move when advancing along each axis?

### data buffer

Contains:

> The underlying numerical bytes.

### views

Can create:

> New ndarray metadata accessing shared underlying memory.

---

# 34. Common Misconceptions

## Misconception 1

> `ndim = 2` means x-axis and y-axis.

Better:

```text
ndim = number of axes
```

For a matrix those axes commonly correspond to rows and columns, but NumPy's axis model generalizes to arbitrary dimensions.

---

## Misconception 2

> `(3,)` and `(1,3)` are the same.

False.

```text
(3,)
→ 1D

(1,3)
→ 2D
```

---

## Misconception 3

> `np.empty()` creates an array with no elements.

False.

It creates an array of the requested shape without initializing entries to a chosen value such as zero.

---

## Misconception 4

> `a * b` means matrix multiplication.

False.

For ordinary NumPy arrays:

```text
*
```

performs element-wise multiplication.

---

## Misconception 5

> Reshape can change the number of elements.

False.

```text
old size = new size
```

must hold.

---

## Misconception 6

> NumPy arrays can freely store different numerical dtypes per element.

Ordinary numeric ndarrays are homogeneous.

The array has a common dtype.

---

## Misconception 7

> `float` means mathematically exact decimal values.

False.

Floating-point values have finite binary representations and therefore finite precision.

---

## Misconception 8

> Slicing always copies the data.

False.

Basic NumPy slicing generally creates a view.

---

## Misconception 9

> A view is the same ndarray object.

False.

```text
different ndarray objects

but

shared/overlapping underlying memory
```

can exist.

---

## Misconception 10

> A view must be contiguous.

False.

Example:

```python
a[::2]
```

can create a non-contiguous strided view.

---

## Misconception 11

> C-order changes the mathematical matrix.

False.

C-order and F-order describe memory-layout/traversal conventions.

The logical array can remain unchanged.

---

## Misconception 12

> NumPy is fast only because arrays are contiguous.

False.

Contiguous storage is important, but NumPy performance also comes from compiled implementations, optimized numerical libraries, reduced Python-level looping, hardware-friendly kernels, and other factors.

---

# 35. AI/ML Connections

These NumPy foundations appear throughout AI engineering.

## Dataset representation

A tabular dataset often looks like:

```text
(samples, features)
```

Example:

```text
(10000, 50)
```

Understanding shape is essential for interpreting model inputs.

---

## Images

An image may be represented as:

```text
(height, width, channels)
```

Example:

```text
(224, 224, 3)
```

Image storage commonly uses `uint8` for channel values from `0` to `255`.

---

## Neural-network tensors

Deep-learning frameworks extend many NumPy-like concepts:

```text
shape
dtype
strides
views
memory layout
broadcasting
vectorized operations
```

Understanding NumPy therefore makes frameworks such as PyTorch significantly easier to reason about.

---

## Model parameters

Millions or billions of parameters make dtype choices important.

```text
float64 → 8 bytes

float32 → 4 bytes

float16 → 2 bytes
```

Lower-precision representations can significantly reduce memory and increase accelerator throughput, provided numerical stability and model quality remain acceptable.

---

## Preprocessing

Operations such as:

```python
x.astype(np.float32)
```

appear frequently when preparing data for ML models.

---

## Shape bugs

Many ML errors are ultimately shape errors:

```text
expected (batch, features)

received (features,)
```

Understanding:

```text
(3,)

vs

(1,3)
```

therefore matters far beyond NumPy itself.

---

# 36. Revision Sheet

## Core ndarray properties

```python
a.ndim
a.shape
a.size
a.dtype
a.itemsize
a.nbytes
a.strides
a.flags
```

---

## Array creation

```python
np.array()

np.zeros()

np.ones()

np.empty()

np.arange()

np.linspace()
```

---

## Indexing and slicing

```python
a[0]

a[1,2]

a[1:4]

a[:, 1:3]

a[::2]
```

---

## Reshape

```python
a.reshape(2,3)

a.reshape(3,-1)
```

Rule:

```text
product of new dimensions = size
```

---

## Dtype

```python
dtype=np.int32

dtype=np.float32
```

---

## Conversion

```python
a.astype(np.float32)
```

---

## Memory

```text
ndarray
=
data access/reference
+
metadata
```

Important metadata:

```text
shape
dtype
strides
flags
```

---

## Strides

```text
stride
=
bytes moved when advancing one position along an axis
```

---

## Views

```python
b = a[1:4]
```

Basic slicing:

```text
usually view
```

---

## Copies

```python
b = a[1:4].copy()
```

Independent data.

---

## Memory sharing

```python
np.shares_memory(a, b)
```

---

## C-order

```text
last axis changes fastest
```

For 2D:

```text
row-major
```

---

## Fortran-order

```text
first axis changes fastest
```

For 2D:

```text
column-major
```

---

# 37. Completion Checklist

## NumPy Arrays

* [x] Why NumPy?
* [x] Python lists vs NumPy arrays
* [x] `ndarray`
* [x] `ndim`
* [x] `shape`
* [x] `size`
* [x] `np.array()`
* [x] `np.zeros()`
* [x] `np.ones()`
* [x] `np.empty()`
* [x] `np.arange()`
* [x] `np.linspace()`
* [x] Indexing
* [x] Slicing
* [x] Integer indexing vs slicing
* [x] Reshaping
* [x] `reshape(-1)`
* [x] Vectorized operations
* [x] ndarray mutability

## Data Types

* [x] `dtype`
* [x] Homogeneous arrays
* [x] Fixed-width numerical types
* [x] Signed integers
* [x] Unsigned integers
* [x] Floating-point types
* [x] Boolean dtype
* [x] `itemsize`
* [x] `nbytes`
* [x] Type inference
* [x] Mixed-type inference
* [x] Type promotion
* [x] `astype()`
* [x] Integer overflow
* [x] Floating-point precision
* [x] Why `float32` matters in ML

## Memory Layout

* [x] Data buffer
* [x] ndarray metadata
* [x] Logical vs physical representation
* [x] Contiguous memory
* [x] Strides
* [x] Calculating strides
* [x] Strided slicing
* [x] Views
* [x] Copies
* [x] `.copy()`
* [x] `.base`
* [x] `np.shares_memory()`
* [x] Basic slicing vs advanced indexing
* [x] C-order
* [x] Fortran-order
* [x] Contiguity flags
* [x] Non-contiguous views
* [x] Memory locality and performance

---

# Final Mental Model

Do not leave Day 8 thinking:

```text
NumPy = library that gives faster Python lists
```

The stronger model is:

```text
                    ndarray
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼

     METADATA                     DATA BUFFER

     shape                        raw bytes
     dtype
     strides
     flags
        │                             │
        └──────────────┬──────────────┘
                       │
                       ▼

             Multidimensional Array
```

A NumPy array is therefore best understood as a **multidimensional view/interpretation of typed memory**.

Its:

```text
shape
```

describes the logical structure.

Its:

```text
dtype
```

describes how bytes represent elements.

Its:

```text
strides
```

describe how NumPy navigates through memory.

Its:

```text
data buffer
```

contains the underlying bytes.

And its ability to create different metadata over shared memory explains why operations such as slicing and reshaping can often be extremely memory-efficient.

---

# Day 8 Complete ✅

**Topics:** NumPy Arrays • Data Types • Memory Layout

The key outcome of Day 8 is not memorizing NumPy functions.

It is understanding the internal model:

> **Data Buffer + dtype + shape + strides + metadata → ndarray**

This foundation prepares the way for deeper NumPy concepts such as broadcasting, universal functions, reductions, advanced indexing, and performance-oriented numerical computation—and later for tensor systems used throughout modern AI engineering.
