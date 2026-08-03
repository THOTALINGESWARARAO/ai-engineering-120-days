"""
===============================================================================
Day 8/120 — NumPy Foundations
Arrays • Data Types • Memory Layout
===============================================================================

AI Engineering in 120 Days

Purpose
-------
This file is the executable companion to the Day 8 README.

The goal is NOT simply to memorize NumPy syntax.

The goal is to experimentally understand:

1. ndarray
2. ndim, shape and size
3. Array creation
4. Indexing and slicing
5. Integer indexing vs slicing
6. Reshaping
7. Vectorized operations
8. NumPy dtypes
9. Fixed-width integers
10. itemsize and nbytes
11. Type inference
12. Type promotion
13. astype()
14. Integer overflow
15. Floating-point precision
16. Data buffers
17. Contiguous memory
18. Strides
19. Views vs copies
20. Memory sharing
21. Basic slicing vs advanced indexing
22. C-order
23. Fortran-order
24. Contiguity flags
25. Non-contiguous views
26. Memory offsets
27. Performance implications
28. AI/ML connections

Recommended learning method
---------------------------

For every experiment:

    1. Read the code.
    2. Predict the output.
    3. Run the code.
    4. Compare your prediction.
    5. Explain WHY NumPy behaved that way.
    6. Modify the experiment.
    7. Run it again.

===============================================================================
"""

import numpy as np
import time


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def subsection(title):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)


# =============================================================================
# 1. PYTHON LIST VS NUMPY ARRAY
# =============================================================================

section("1. Python List vs NumPy ndarray")

python_list = [10, 20, 30]

numpy_array = np.array([10, 20, 30])

print("Python list:")
print(python_list)
print("type:", type(python_list))

print("\nNumPy array:")
print(numpy_array)
print("type:", type(numpy_array))


# -----------------------------------------------------------------------------
# Mental model
# -----------------------------------------------------------------------------

"""
Python list:

    [ref] [ref] [ref]
      |     |     |
      v     v     v
     10    20    30

The list stores references to Python objects.


Numerical ndarray:

    ndarray metadata
          |
          v

    [10][20][30]

The values are represented using a common dtype in an array data buffer.
"""


# -----------------------------------------------------------------------------
# Python lists can hold heterogeneous objects
# -----------------------------------------------------------------------------

mixed_list = [10, "NumPy", True, 3.14]

print("\nMixed Python list:")
print(mixed_list)

for value in mixed_list:
    print(value, "->", type(value))


# -----------------------------------------------------------------------------
# NumPy normally chooses one common dtype
# -----------------------------------------------------------------------------

mixed_array = np.array([1, 2.5, 3])

print("\nMixed numerical ndarray:")
print(mixed_array)
print("dtype:", mixed_array.dtype)


# =============================================================================
# 2. NDARRAY PROPERTIES
# =============================================================================

section("2. ndarray Properties")

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(a)

print("\ntype     :", type(a))
print("ndim     :", a.ndim)
print("shape    :", a.shape)
print("size     :", a.size)
print("dtype    :", a.dtype)
print("itemsize :", a.itemsize)
print("nbytes   :", a.nbytes)
print("strides  :", a.strides)


# -----------------------------------------------------------------------------
# Prediction experiment
# -----------------------------------------------------------------------------

"""
PREDICT BEFORE RUNNING:

b = np.zeros((3, 4, 5))

What are:

    b.ndim  = ?
    b.shape = ?
    b.size  = ?
"""

b = np.zeros((3, 4, 5))

print("\n3D array:")
print("ndim :", b.ndim)
print("shape:", b.shape)
print("size :", b.size)

assert b.ndim == 3
assert b.shape == (3, 4, 5)
assert b.size == 60


# =============================================================================
# 3. ARRAY CREATION
# =============================================================================

section("3. Array Creation")


# -----------------------------------------------------------------------------
# np.array()
# -----------------------------------------------------------------------------

subsection("3.1 np.array()")

a = np.array([1, 2, 3, 4])

print(a)
print(a.dtype)


# -----------------------------------------------------------------------------
# np.zeros()
# -----------------------------------------------------------------------------

subsection("3.2 np.zeros()")

a = np.zeros((2, 3))

print(a)
print("shape:", a.shape)
print("dtype:", a.dtype)


# -----------------------------------------------------------------------------
# np.ones()
# -----------------------------------------------------------------------------

subsection("3.3 np.ones()")

a = np.ones((2, 4))

print(a)


# -----------------------------------------------------------------------------
# np.empty()
# -----------------------------------------------------------------------------

subsection("3.4 np.empty()")

a = np.empty((2, 3))

print(a)

"""
IMPORTANT:

np.empty() does NOT mean:

    create an array with no elements

It means:

    allocate storage without initializing every element
    to a chosen value such as zero.

Never depend on the initial values.
"""


# -----------------------------------------------------------------------------
# np.arange()
# -----------------------------------------------------------------------------

subsection("3.5 np.arange()")

a = np.arange(0, 12, 2)

print(a)

"""
Mental model:

arange(start, stop, step)

We control the STEP.
"""


# -----------------------------------------------------------------------------
# np.linspace()
# -----------------------------------------------------------------------------

subsection("3.6 np.linspace()")

a = np.linspace(0, 10, 5)

print(a)

"""
Mental model:

linspace(start, stop, number_of_samples)

We control the NUMBER OF SAMPLES.
"""


# =============================================================================
# 4. INDEXING
# =============================================================================

section("4. Indexing")


# -----------------------------------------------------------------------------
# 1D indexing
# -----------------------------------------------------------------------------

subsection("4.1 1D Indexing")

a = np.array([10, 20, 30, 40, 50])

print("a:", a)

print("a[0] :", a[0])
print("a[2] :", a[2])
print("a[-1]:", a[-1])


# -----------------------------------------------------------------------------
# 2D indexing
# -----------------------------------------------------------------------------

subsection("4.2 2D Indexing")

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a)

print("\na[0, 0]:", a[0, 0])
print("a[1, 2]:", a[1, 2])
print("a[2, 1]:", a[2, 1])


"""
Mental model:

a[axis0_index, axis1_index]

For a conventional 2D matrix:

a[row, column]
"""


# =============================================================================
# 5. SLICING
# =============================================================================

section("5. Slicing")

a = np.array([10, 20, 30, 40, 50, 60])

print("Original:")
print(a)

print("\na[1:4]")
print(a[1:4])

print("\na[:3]")
print(a[:3])

print("\na[3:]")
print(a[3:])

print("\na[::2]")
print(a[::2])

print("\na[::-1]")
print(a[::-1])


# -----------------------------------------------------------------------------
# 2D slicing
# -----------------------------------------------------------------------------

subsection("5.1 2D Slicing")

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original:")
print(a)

print("\na[0:2, 1:3]")
print(a[0:2, 1:3])


# =============================================================================
# 6. INTEGER INDEXING VS SLICING
# =============================================================================

section("6. Integer Indexing vs Slicing")

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

integer_index = a[0]
slice_result = a[0:1]

print("Original shape:")
print(a.shape)

print("\na[0]:")
print(integer_index)
print("shape:", integer_index.shape)
print("ndim :", integer_index.ndim)

print("\na[0:1]:")
print(slice_result)
print("shape:", slice_result.shape)
print("ndim :", slice_result.ndim)


"""
IMPORTANT:

a[0]

    removes the indexed axis

shape:

    (3,)


a[0:1]

    preserves the axis

shape:

    (1, 3)
"""


assert integer_index.shape == (3,)
assert slice_result.shape == (1, 3)


# =============================================================================
# 7. RESHAPING
# =============================================================================

section("7. Reshaping")

a = np.arange(12)

print("Original:")
print(a)

print("shape:", a.shape)
print("size :", a.size)


# -----------------------------------------------------------------------------
# reshape(3, 4)
# -----------------------------------------------------------------------------

b = a.reshape(3, 4)

print("\nreshape(3, 4):")
print(b)
print("shape:", b.shape)


# -----------------------------------------------------------------------------
# reshape(2, 6)
# -----------------------------------------------------------------------------

c = a.reshape(2, 6)

print("\nreshape(2, 6):")
print(c)


# -----------------------------------------------------------------------------
# reshape using -1
# -----------------------------------------------------------------------------

d = a.reshape(3, -1)

print("\nreshape(3, -1):")
print(d)
print("shape:", d.shape)


"""
NumPy solves:

3 * ? = 12

? = 4
"""


# -----------------------------------------------------------------------------
# Invalid reshape
# -----------------------------------------------------------------------------

subsection("7.1 Invalid Reshape")

try:
    a.reshape(5, 3)
except ValueError as error:
    print("Expected error:")
    print(error)


"""
RULE:

old number of elements
=
new number of elements
"""


# =============================================================================
# 8. VECTORIZED OPERATIONS
# =============================================================================

section("8. Vectorized Operations")

a = np.array([1, 2, 3, 4])

print("a:")
print(a)

print("\na + 10")
print(a + 10)

print("\na * 2")
print(a * 2)

print("\na ** 2")
print(a ** 2)


# -----------------------------------------------------------------------------
# Element-wise array operations
# -----------------------------------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("\na:")
print(a)

print("b:")
print(b)

print("\na + b:")
print(a + b)

print("\na * b:")
print(a * b)


"""
IMPORTANT:

a * b

means ELEMENT-WISE multiplication.

It is not automatically matrix multiplication.
"""


# =============================================================================
# 9. NDARRAY MUTABILITY
# =============================================================================

section("9. ndarray Mutability")

a = np.array([10, 20, 30])

print("Before:")
print(a)

a[1] = 999

print("After:")
print(a)


"""
ndarray objects are mutable.

Their elements can be changed after creation.
"""


# =============================================================================
# 10. NUMPY DTYPES
# =============================================================================

section("10. NumPy Data Types")


dtype_examples = [
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.float16,
    np.float32,
    np.float64,
    np.bool_
]


for dtype in dtype_examples:

    a = np.array([1], dtype=dtype)

    print(
        f"{str(dtype):25} "
        f"dtype={str(a.dtype):10} "
        f"itemsize={a.itemsize}"
    )


# =============================================================================
# 11. SIGNED VS UNSIGNED INTEGERS
# =============================================================================

section("11. Signed vs Unsigned Integers")


for dtype in [np.int8, np.uint8, np.int16, np.uint16]:

    info = np.iinfo(dtype)

    print(
        dtype,
        "min =", info.min,
        "max =", info.max
    )


"""
Important examples:

int8

    -128 ... 127


uint8

       0 ... 255


Both use:

    8 bits
    1 byte

The difference is how the bit patterns are interpreted.
"""


# =============================================================================
# 12. ITEMSIZE AND NBYTES
# =============================================================================

section("12. itemsize and nbytes")

a = np.array(
    [10, 20, 30, 40],
    dtype=np.int16
)

print("Array:")
print(a)

print("size     :", a.size)
print("itemsize :", a.itemsize)
print("nbytes   :", a.nbytes)


expected_nbytes = a.size * a.itemsize

print("\nsize * itemsize:")
print(expected_nbytes)

assert a.nbytes == a.size * a.itemsize


# -----------------------------------------------------------------------------
# Larger example
# -----------------------------------------------------------------------------

a = np.zeros(5000, dtype=np.float32)

print("\n5000 float32 values")

print("size     :", a.size)
print("itemsize :", a.itemsize)
print("nbytes   :", a.nbytes)

assert a.nbytes == 20_000


# =============================================================================
# 13. TYPE INFERENCE
# =============================================================================

section("13. Type Inference")


examples = [

    np.array([1, 2, 3]),

    np.array([1.0, 2.0, 3.0]),

    np.array([True, False, True]),

    np.array([1, 2.5, 3]),

    np.array([True, 2, 3.5])
]


for array in examples:

    print("\nArray:")
    print(array)

    print("dtype:")
    print(array.dtype)


# =============================================================================
# 14. EXPLICIT DTYPE
# =============================================================================

section("14. Explicit dtype")

a = np.array(
    [1, 2, 3],
    dtype=np.float32
)

print(a)
print(a.dtype)


# =============================================================================
# 15. TYPE CONVERSION WITH astype()
# =============================================================================

section("15. astype()")

a = np.array([1, 2, 3])

b = a.astype(np.float32)

print("a:")
print(a)
print("dtype:", a.dtype)

print("\nb:")
print(b)
print("dtype:", b.dtype)

print("\na is b:")
print(a is b)

print("\nshares memory:")
print(np.shares_memory(a, b))


# -----------------------------------------------------------------------------
# Float -> Integer
# -----------------------------------------------------------------------------

subsection("15.1 Float to Integer")

a = np.array([1.9, 2.8, 3.7])

b = a.astype(np.int32)

print("Original:")
print(a)

print("Converted:")
print(b)


"""
Notice:

1.9 -> 1
2.8 -> 2
3.7 -> 3

astype(int) is NOT the same thing as rounding.
"""


# =============================================================================
# 16. TYPE PROMOTION
# =============================================================================

section("16. Type Promotion")

a = np.array(
    [1, 2, 3],
    dtype=np.int16
)

b = np.array(
    [10.5, 20.5, 30.5],
    dtype=np.float32
)

c = a + b

print("a dtype:", a.dtype)
print("b dtype:", b.dtype)

print("\nc:")
print(c)

print("c dtype:")
print(c.dtype)


# -----------------------------------------------------------------------------
# Inspect promotion directly
# -----------------------------------------------------------------------------

print("\nnp.result_type(np.int16, np.float32):")
print(np.result_type(np.int16, np.float32))


# =============================================================================
# 17. INTEGER OVERFLOW
# =============================================================================

section("17. Integer Overflow")


"""
Fixed-width integers have limited ranges.

int8:

    -128 ... 127
"""


# -----------------------------------------------------------------------------
# Positive overflow
# -----------------------------------------------------------------------------

a = np.array([120], dtype=np.int8)

print("Starting value:")
print(a)

# Performing the arithmetic using two int8 arrays keeps the operation
# clearly inside fixed-width int8 arithmetic.
increment = np.array([10], dtype=np.int8)

result = a + increment

print("\n120 + 10 using int8:")
print(result)

print("dtype:")
print(result.dtype)


# -----------------------------------------------------------------------------
# Negative overflow
# -----------------------------------------------------------------------------

a = np.array([-128], dtype=np.int8)

one = np.array([1], dtype=np.int8)

result = a - one

print("\n-128 - 1 using int8:")
print(result)


"""
Expected wrap-around:

127 + 1
    ->
-128


-128 - 1
    ->
127
"""


# -----------------------------------------------------------------------------
# Compare with Python int
# -----------------------------------------------------------------------------

python_value = 120

print("\nPython int:")
print(python_value + 10)

huge_integer = 10 ** 100

print("\nPython arbitrary precision:")
print(huge_integer)


# =============================================================================
# 18. FLOATING-POINT PRECISION
# =============================================================================

section("18. Floating-Point Precision")

print("0.1 + 0.2:")
print(0.1 + 0.2)

print("\n0.1 + 0.2 == 0.3:")
print(0.1 + 0.2 == 0.3)


# -----------------------------------------------------------------------------
# float32 vs float64
# -----------------------------------------------------------------------------

x32 = np.float32(1 / 3)

x64 = np.float64(1 / 3)

print("\nfloat32:")
print(x32)

print("float64:")
print(x64)

print("\nfloat32 itemsize:")
print(x32.itemsize)

print("float64 itemsize:")
print(x64.itemsize)


# -----------------------------------------------------------------------------
# Proper approximate comparison
# -----------------------------------------------------------------------------

print("\nnp.isclose(0.1 + 0.2, 0.3):")
print(np.isclose(0.1 + 0.2, 0.3))


# =============================================================================
# 19. WHY FLOAT32 MATTERS IN ML
# =============================================================================

section("19. Why float32 Matters in ML")

number_of_parameters = 100_000_000

float32_memory = number_of_parameters * 4
float64_memory = number_of_parameters * 8

print("100 million parameters")

print("\nfloat32 bytes:")
print(float32_memory)

print("float64 bytes:")
print(float64_memory)

print("\nfloat32 MB:")
print(float32_memory / 1_000_000)

print("float64 MB:")
print(float64_memory / 1_000_000)


# -----------------------------------------------------------------------------
# Verify using NumPy
# -----------------------------------------------------------------------------

small32 = np.zeros(1_000_000, dtype=np.float32)
small64 = np.zeros(1_000_000, dtype=np.float64)

print("\n1 million float32 values:")
print(small32.nbytes / 1_000_000, "MB")

print("1 million float64 values:")
print(small64.nbytes / 1_000_000, "MB")


# =============================================================================
# 20. DATA BUFFER
# =============================================================================

section("20. Data Buffer")

a = np.array(
    [10, 20, 30],
    dtype=np.int32
)

print("Array:")
print(a)

print("\ndtype:")
print(a.dtype)

print("itemsize:")
print(a.itemsize)

print("nbytes:")
print(a.nbytes)


"""
Mental model:

                ndarray
                   |
        +----------+----------+
        |                     |
     metadata              data buffer

    shape=(3,)             [10][20][30]
    dtype=int32
    strides=(4,)
"""


# -----------------------------------------------------------------------------
# Inspect raw bytes
# -----------------------------------------------------------------------------

print("\nRaw bytes:")
print(a.tobytes())

print("\nNumber of raw bytes:")
print(len(a.tobytes()))

assert len(a.tobytes()) == a.nbytes


# =============================================================================
# 21. LOGICAL ARRAY VS PHYSICAL MEMORY
# =============================================================================

section("21. Logical Array vs Physical Memory")

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
], dtype=np.int32)

print("Logical array:")
print(a)

print("\nShape:")
print(a.shape)

print("Strides:")
print(a.strides)

print("\nFlattened C-order traversal:")
print(a.ravel(order="C"))


"""
Logical:

    [[10 20 30]
     [40 50 60]]


Typical C-contiguous traversal:

    [10][20][30][40][50][60]
"""


# =============================================================================
# 22. STRIDES
# =============================================================================

section("22. Strides")

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
], dtype=np.int32)

print("Array:")
print(a)

print("\nshape:")
print(a.shape)

print("itemsize:")
print(a.itemsize)

print("strides:")
print(a.strides)


"""
shape:

    (3, 4)

itemsize:

    4 bytes


C-order:

axis 1:

    1 -> 2

    move 4 bytes


axis 0:

    1
    |
    v
    5

    move 4 elements

    4 * 4 bytes

    = 16 bytes


Therefore:

    strides = (16, 4)
"""


assert a.strides == (16, 4)


# =============================================================================
# 23. STRIDES WITH SLICING
# =============================================================================

section("23. Strides with Slicing")

a = np.array(
    [10, 20, 30, 40, 50, 60],
    dtype=np.int32
)

b = a[::2]

print("a:")
print(a)

print("a.strides:")
print(a.strides)

print("\nb:")
print(b)

print("b.strides:")
print(b.strides)


"""
a:

[10][20][30][40][50][60]

stride:

4 bytes


b = a[::2]

[10]    [30]    [50]
 ^       ^       ^

stride:

8 bytes
"""


assert a.strides == (4,)
assert b.strides == (8,)


# =============================================================================
# 24. VIEWS
# =============================================================================

section("24. Views")

a = np.array([10, 20, 30, 40, 50])

b = a[1:4]

print("a:")
print(a)

print("\nb:")
print(b)

print("\na is b:")
print(a is b)

print("\nshares memory:")
print(np.shares_memory(a, b))


# -----------------------------------------------------------------------------
# Modify the view
# -----------------------------------------------------------------------------

print("\nChanging b[0] to 999...")

b[0] = 999

print("\na:")
print(a)

print("\nb:")
print(b)


"""
Because b is a view:

a and b are different ndarray objects,

BUT

their memory overlaps.
"""


# =============================================================================
# 25. COPIES
# =============================================================================

section("25. Copies")

a = np.array([10, 20, 30, 40, 50])

b = a[1:4].copy()

print("a:")
print(a)

print("\nb:")
print(b)

print("\nshares memory:")
print(np.shares_memory(a, b))

print("\nChanging b[0] to 999...")

b[0] = 999

print("\na:")
print(a)

print("\nb:")
print(b)


assert np.shares_memory(a, b) is False


# =============================================================================
# 26. VIEW VS COPY — FULL EXPERIMENT
# =============================================================================

section("26. View vs Copy — Full Experiment")

a = np.array([10, 20, 30, 40, 50])

view = a[1:4]

copy = a[1:4].copy()

print("Initial state")

print("a   :", a)
print("view:", view)
print("copy:", copy)


print("\nChanging view[0] = 100")

view[0] = 100

print("a   :", a)
print("view:", view)
print("copy:", copy)


print("\nChanging copy[1] = 200")

copy[1] = 200

print("a   :", a)
print("view:", view)
print("copy:", copy)


"""
Expected final state:

a:

    [10, 100, 30, 40, 50]

view:

    [100, 30, 40]

copy:

    [20, 200, 40]
"""


# =============================================================================
# 27. .base
# =============================================================================

section("27. The .base Attribute")

a = np.array([10, 20, 30, 40])

b = a[1:3]

c = a[1:3].copy()

print("b.base:")
print(b.base)

print("\nb.base is a:")
print(b.base is a)

print("\nc.base:")
print(c.base)


"""
.base can help inspect backing relationships.

However:

    b.base is a

is NOT a universal test for memory sharing.

Use:

    np.shares_memory()

when memory sharing is the actual question.
"""


# =============================================================================
# 28. BASIC SLICING VS ADVANCED INDEXING
# =============================================================================

section("28. Basic Slicing vs Advanced Indexing")

a = np.array([10, 20, 30, 40, 50])


# -----------------------------------------------------------------------------
# Basic slicing
# -----------------------------------------------------------------------------

basic = a[1:4]

print("Basic slice:")
print(basic)

print("shares memory:")
print(np.shares_memory(a, basic))


# -----------------------------------------------------------------------------
# Advanced integer indexing
# -----------------------------------------------------------------------------

advanced = a[[1, 2, 3]]

print("\nAdvanced indexing:")
print(advanced)

print("shares memory:")
print(np.shares_memory(a, advanced))


# -----------------------------------------------------------------------------
# Boolean indexing
# -----------------------------------------------------------------------------

boolean_result = a[a > 20]

print("\nBoolean indexing:")
print(boolean_result)

print("shares memory:")
print(np.shares_memory(a, boolean_result))


"""
General rule:

Basic slicing
    ->
usually view


Advanced indexing
    ->
usually copy
"""


# =============================================================================
# 29. C-ORDER
# =============================================================================

section("29. C-order")

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=np.int32, order="C")

print("Array:")
print(a)

print("\nshape:")
print(a.shape)

print("strides:")
print(a.strides)

print("\nC-order traversal:")
print(a.ravel(order="C"))


"""
Logical:

[1 2]
[3 4]
[5 6]


C-order traversal:

1 2 3 4 5 6


Mental model:

LAST axis changes fastest.
"""


# =============================================================================
# 30. FORTRAN ORDER
# =============================================================================

section("30. Fortran-order")

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=np.int32, order="F")

print("Array:")
print(a)

print("\nshape:")
print(a.shape)

print("strides:")
print(a.strides)

print("\nF-order traversal:")
print(a.ravel(order="F"))


"""
Logical array is STILL:

[1 2]
[3 4]
[5 6]


F-order traversal:

1 3 5 2 4 6


Mental model:

FIRST axis changes fastest.
"""


assert a.strides == (4, 12)


# =============================================================================
# 31. C-ORDER VS F-ORDER
# =============================================================================

section("31. C-order vs F-order")

c_array = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=np.int32, order="C")


f_array = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
], dtype=np.int32, order="F")


print("C array:")
print(c_array)

print("C strides:")
print(c_array.strides)


print("\nF array:")
print(f_array)

print("F strides:")
print(f_array.strides)


print("\nSame logical values?")
print(np.array_equal(c_array, f_array))


"""
Same:

    values
    shape
    dtype

Different:

    memory layout
    strides
"""


# =============================================================================
# 32. CONTIGUITY FLAGS
# =============================================================================

section("32. Contiguity Flags")

c_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
], order="C")


f_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
], order="F")


print("C array")

print("C_CONTIGUOUS:")
print(c_array.flags["C_CONTIGUOUS"])

print("F_CONTIGUOUS:")
print(c_array.flags["F_CONTIGUOUS"])


print("\nF array")

print("C_CONTIGUOUS:")
print(f_array.flags["C_CONTIGUOUS"])

print("F_CONTIGUOUS:")
print(f_array.flags["F_CONTIGUOUS"])


# =============================================================================
# 33. NON-CONTIGUOUS VIEW
# =============================================================================

section("33. Non-Contiguous View")

a = np.arange(10, dtype=np.int32)

b = a[::2]

print("a:")
print(a)

print("strides:")
print(a.strides)

print("C contiguous:")
print(a.flags["C_CONTIGUOUS"])


print("\nb:")
print(b)

print("strides:")
print(b.strides)

print("C contiguous:")
print(b.flags["C_CONTIGUOUS"])

print("shares memory:")
print(np.shares_memory(a, b))


"""
Important:

VIEW
does NOT imply
CONTIGUOUS.
"""


# =============================================================================
# 34. NEGATIVE STRIDES
# =============================================================================

section("34. Negative Strides")

a = np.array(
    [10, 20, 30, 40, 50],
    dtype=np.int32
)

reversed_view = a[::-1]

print("Original:")
print(a)

print("Original strides:")
print(a.strides)


print("\nReversed:")
print(reversed_view)

print("Reversed strides:")
print(reversed_view.strides)

print("shares memory:")
print(np.shares_memory(a, reversed_view))


"""
Why negative stride?

Original:

10 -> 20 -> 30 -> 40 -> 50


Reversed view:

50 -> 40 -> 30 -> 20 -> 10


NumPy moves BACKWARD through memory.

Therefore the stride can be negative.
"""


# =============================================================================
# 35. CALCULATING BYTE OFFSETS
# =============================================================================

section("35. Calculating Byte Offsets")

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
], dtype=np.int32)

print("Array:")
print(a)

print("\nshape:")
print(a.shape)

print("strides:")
print(a.strides)


row = 1
column = 2

offset = (
    row * a.strides[0]
    +
    column * a.strides[1]
)


print("\nIndex:")
print((row, column))

print("Byte offset:")
print(offset)

print("Value:")
print(a[row, column])


"""
For:

a[1, 2]

strides:

(16, 4)


offset:

1 * 16
+
2 * 4

=
24 bytes


value:

70
"""


assert offset == 24
assert a[1, 2] == 70


# =============================================================================
# 36. GENERAL STRIDE OFFSET FUNCTION
# =============================================================================

section("36. General Stride Offset Function")


def byte_offset(array, index):
    """
    Calculate the byte offset implied by an ndarray's strides.

    This assumes 'index' contains one integer index per array axis.

    Example:

        array.shape   = (2, 4)
        array.strides = (16, 4)
        index         = (1, 2)

        offset =
            1 * 16
            +
            2 * 4

            = 24 bytes
    """

    if len(index) != array.ndim:
        raise ValueError(
            "Index must contain exactly one integer per axis."
        )

    return sum(
        i * stride
        for i, stride in zip(index, array.strides)
    )


a = np.arange(
    24,
    dtype=np.int32
).reshape(2, 3, 4)


print("shape:")
print(a.shape)

print("strides:")
print(a.strides)


index = (1, 2, 3)

print("\nindex:")
print(index)

print("value:")
print(a[index])

print("byte offset:")
print(byte_offset(a, index))


# =============================================================================
# 37. RESHAPE AND MEMORY SHARING
# =============================================================================

section("37. Reshape and Memory Sharing")

a = np.arange(12)

b = a.reshape(3, 4)

print("a:")
print(a)

print("\nb:")
print(b)

print("\nshares memory:")
print(np.shares_memory(a, b))


"""
reshape() can often return a view when the requested shape
is compatible with the existing memory layout.

But do NOT assume every reshape operation in every situation
must avoid copying.

Memory layout matters.
"""


# =============================================================================
# 38. TRANSPOSE AND STRIDES
# =============================================================================

section("38. Transpose and Strides")

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int32)

b = a.T

print("a:")
print(a)

print("a.shape:")
print(a.shape)

print("a.strides:")
print(a.strides)


print("\na.T:")
print(b)

print("b.shape:")
print(b.shape)

print("b.strides:")
print(b.strides)

print("\nshares memory:")
print(np.shares_memory(a, b))


"""
Original:

shape:

    (2, 3)

strides:

    (12, 4)


Transpose:

shape:

    (3, 2)

strides:

    (4, 12)


The data does not necessarily need to be physically rearranged.

Changing metadata can produce a transposed view.
"""


# =============================================================================
# 39. MAKE A CONTIGUOUS COPY
# =============================================================================

section("39. Making a Contiguous Copy")

a = np.arange(10, dtype=np.int32)

b = a[::2]

print("b:")
print(b)

print("b.strides:")
print(b.strides)

print("C contiguous:")
print(b.flags["C_CONTIGUOUS"])


c = np.ascontiguousarray(b)

print("\nAfter np.ascontiguousarray():")

print("c:")
print(c)

print("c.strides:")
print(c.strides)

print("C contiguous:")
print(c.flags["C_CONTIGUOUS"])

print("shares memory with b:")
print(np.shares_memory(b, c))


# =============================================================================
# 40. MEMORY ADDRESS EXPERIMENT
# =============================================================================

section("40. Memory Address Experiment")

a = np.array(
    [10, 20, 30, 40],
    dtype=np.int32
)

base_address = a.__array_interface__["data"][0]

print("Base memory address:")
print(base_address)

print("\nExpected addresses based on strides:")

for i in range(a.size):

    expected_address = (
        base_address
        +
        i * a.strides[0]
    )

    print(
        f"a[{i}] = {a[i]:2} "
        f"offset={i * a.strides[0]:2} bytes "
        f"expected_address={expected_address}"
    )


"""
Do NOT memorize actual memory addresses.

They change between runs.

The important relationship is:

address of element
=
base address
+
byte offset
"""


# =============================================================================
# 41. PERFORMANCE — PYTHON LOOP VS NUMPY
# =============================================================================

section("41. Performance — Python Loop vs NumPy")


N = 1_000_000


python_values = list(range(N))

start = time.perf_counter()

python_result = [
    x * 2
    for x in python_values
]

python_time = time.perf_counter() - start


numpy_values = np.arange(N)

start = time.perf_counter()

numpy_result = numpy_values * 2

numpy_time = time.perf_counter() - start


print("Python loop time:")
print(python_time)

print("\nNumPy vectorized time:")
print(numpy_time)


if numpy_time > 0:

    print("\nApproximate speed ratio:")
    print(python_time / numpy_time)


"""
IMPORTANT:

Do NOT conclude:

    NumPy is fast ONLY because of contiguous memory.

Performance comes from several factors:

    - native compiled loops
    - reduced Python interpreter overhead
    - compact numerical representation
    - optimized kernels
    - SIMD/vector instructions
    - cache-friendly access patterns
    - optimized numerical libraries

Also:

One benchmark is not a rigorous performance study.
"""


# =============================================================================
# 42. MEMORY LAYOUT PERFORMANCE EXPERIMENT
# =============================================================================

section("42. Memory Layout Performance Experiment")


"""
This experiment compares row-wise and column-wise traversal.

Python-level loop overhead can dominate this benchmark,
so treat it as an intuition experiment rather than a rigorous
measurement of hardware cache behavior.
"""


matrix = np.ones(
    (1000, 1000),
    dtype=np.float64
)


start = time.perf_counter()

row_sum = 0.0

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        row_sum += matrix[i, j]

row_time = time.perf_counter() - start


start = time.perf_counter()

column_sum = 0.0

for j in range(matrix.shape[1]):
    for i in range(matrix.shape[0]):
        column_sum += matrix[i, j]

column_time = time.perf_counter() - start


print("Row-major traversal time:")
print(row_time)

print("\nColumn-major traversal time:")
print(column_time)

print("\nSame mathematical result:")
print(row_sum == column_sum)


# =============================================================================
# 43. AI/ML EXAMPLE — FEATURE MATRIX
# =============================================================================

section("43. AI/ML Example — Feature Matrix")


"""
Suppose:

1000 samples
20 features per sample

Common ML shape:

(samples, features)
"""


X = np.random.rand(
    1000,
    20
).astype(np.float32)


print("Dataset shape:")
print(X.shape)

print("dtype:")
print(X.dtype)

print("ndim:")
print(X.ndim)

print("number of values:")
print(X.size)

print("memory:")
print(X.nbytes, "bytes")


# =============================================================================
# 44. AI/ML EXAMPLE — SINGLE SAMPLE SHAPE
# =============================================================================

section("44. AI/ML Example — Single Sample Shape")

X = np.random.rand(
    100,
    5
).astype(np.float32)


sample_1d = X[0]

sample_2d = X[0:1]


print("X shape:")
print(X.shape)


print("\nX[0] shape:")
print(sample_1d.shape)


print("\nX[0:1] shape:")
print(sample_2d.shape)


"""
Potential ML distinction:

X[0]

    shape = (5,)


X[0:1]

    shape = (1, 5)


Some model APIs expect:

    (batch_size, features)

rather than:

    (features,)
"""


# =============================================================================
# 45. AI/ML EXAMPLE — IMAGE ARRAY
# =============================================================================

section("45. AI/ML Example — Image Array")


image = np.zeros(
    (224, 224, 3),
    dtype=np.uint8
)


print("Image shape:")
print(image.shape)

print("dtype:")
print(image.dtype)

print("itemsize:")
print(image.itemsize)

print("nbytes:")
print(image.nbytes)


"""
Common image representation:

(height, width, channels)

(224, 224, 3)

uint8:

0 ... 255
"""


# =============================================================================
# 46. IMAGE CONVERSION FOR ML
# =============================================================================

section("46. Image Conversion for ML")


image = np.random.randint(
    0,
    256,
    size=(224, 224, 3),
    dtype=np.uint8
)


print("Original image")

print("dtype:")
print(image.dtype)

print("nbytes:")
print(image.nbytes)


image_float = image.astype(np.float32) / 255.0


print("\nConverted image")

print("dtype:")
print(image_float.dtype)

print("minimum:")
print(image_float.min())

print("maximum:")
print(image_float.max())

print("nbytes:")
print(image_float.nbytes)


"""
This pattern appears frequently in ML preprocessing:

uint8 image

        |
        v

convert to float32

        |
        v

scale values

0 ... 255

to approximately

0.0 ... 1.0
"""


# =============================================================================
# 47. MISCONCEPTION EXPERIMENTS
# =============================================================================

section("47. Misconception Experiments")


# -----------------------------------------------------------------------------
# Misconception: (3,) == (1, 3)
# -----------------------------------------------------------------------------

a = np.array([1, 2, 3])

b = np.array([[1, 2, 3]])

print("(3,) vs (1,3)")

print("a.shape:")
print(a.shape)

print("b.shape:")
print(b.shape)

print("Same shape?")
print(a.shape == b.shape)


# -----------------------------------------------------------------------------
# Misconception: slicing always copies
# -----------------------------------------------------------------------------

a = np.arange(5)

b = a[1:4]

print("\nSlicing shares memory:")
print(np.shares_memory(a, b))


# -----------------------------------------------------------------------------
# Misconception: advanced indexing gives the same memory behavior
# -----------------------------------------------------------------------------

c = a[[1, 2, 3]]

print("\nAdvanced indexing shares memory:")
print(np.shares_memory(a, c))


# -----------------------------------------------------------------------------
# Misconception: view means same object
# -----------------------------------------------------------------------------

print("\na is b:")
print(a is b)

print("shares memory:")
print(np.shares_memory(a, b))


# -----------------------------------------------------------------------------
# Misconception: float equality is always safe
# -----------------------------------------------------------------------------

print("\n0.1 + 0.2 == 0.3")
print(0.1 + 0.2 == 0.3)

print("np.isclose:")
print(np.isclose(0.1 + 0.2, 0.3))


# =============================================================================
# 48. UNIFIED NDARRAY INSPECTOR
# =============================================================================

section("48. Unified ndarray Inspector")


def inspect_array(name, array):

    print("\n" + "-" * 60)

    print("Array:", name)

    print("-" * 60)

    print(array)

    print("\ntype:")
    print(type(array))

    print("\nndim:")
    print(array.ndim)

    print("\nshape:")
    print(array.shape)

    print("\nsize:")
    print(array.size)

    print("\ndtype:")
    print(array.dtype)

    print("\nitemsize:")
    print(array.itemsize)

    print("\nnbytes:")
    print(array.nbytes)

    print("\nstrides:")
    print(array.strides)

    print("\nC_CONTIGUOUS:")
    print(array.flags["C_CONTIGUOUS"])

    print("\nF_CONTIGUOUS:")
    print(array.flags["F_CONTIGUOUS"])

    print("\nbase:")
    print(array.base)


original = np.arange(
    12,
    dtype=np.int32
).reshape(3, 4)


slice_view = original[:, ::2]

transpose_view = original.T

independent_copy = original.copy()


inspect_array(
    "original",
    original
)

inspect_array(
    "slice_view",
    slice_view
)

inspect_array(
    "transpose_view",
    transpose_view
)

inspect_array(
    "independent_copy",
    independent_copy
)


print("\nMemory sharing")

print(
    "original <-> slice:",
    np.shares_memory(
        original,
        slice_view
    )
)

print(
    "original <-> transpose:",
    np.shares_memory(
        original,
        transpose_view
    )
)

print(
    "original <-> copy:",
    np.shares_memory(
        original,
        independent_copy
    )
)


# =============================================================================
# 49. FINAL PREDICTION CHALLENGE
# =============================================================================

section("49. Final Prediction Challenge")


"""
STOP HERE BEFORE RUNNING THIS SECTION.

Predict everything first.
"""


a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
], dtype=np.int32)


b = a[:, ::2]

c = b.copy()


print("a:")
print(a)

print("\na.shape:")
print(a.shape)

print("a.size:")
print(a.size)

print("a.itemsize:")
print(a.itemsize)

print("a.nbytes:")
print(a.nbytes)

print("a.strides:")
print(a.strides)


print("\nb:")
print(b)

print("b.shape:")
print(b.shape)

print("b.strides:")
print(b.strides)

print("b C_CONTIGUOUS:")
print(b.flags["C_CONTIGUOUS"])

print("a and b share memory:")
print(np.shares_memory(a, b))


print("\nc:")
print(c)

print("c.strides:")
print(c.strides)

print("a and c share memory:")
print(np.shares_memory(a, c))


# -----------------------------------------------------------------------------
# Mutation challenge
# -----------------------------------------------------------------------------

print("\nChanging b[0, 0] = 999")

b[0, 0] = 999


print("a:")
print(a)

print("b:")
print(b)

print("c:")
print(c)


# =============================================================================
# 50. FINAL BYTE-OFFSET CHALLENGE
# =============================================================================

section("50. Final Byte-Offset Challenge")


a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
], dtype=np.int32)


"""
PREDICT:

1. a.shape
2. a.size
3. a.itemsize
4. a.nbytes
5. a.strides

Then calculate the byte offset of:

    a[2, 1]

using:

    offset =
        index0 * stride0
        +
        index1 * stride1
"""


print("Array:")
print(a)

print("\nshape:")
print(a.shape)

print("size:")
print(a.size)

print("itemsize:")
print(a.itemsize)

print("nbytes:")
print(a.nbytes)

print("strides:")
print(a.strides)


index = (2, 1)

offset = byte_offset(
    a,
    index
)


print("\nindex:")
print(index)

print("byte offset:")
print(offset)

print("value:")
print(a[index])


# =============================================================================
# 51. PRACTICE CHALLENGES
# =============================================================================

section("51. Practice Challenges")


"""
Do these WITHOUT immediately looking at the answers.

-------------------------------------------------------------------------------
Challenge 1
-------------------------------------------------------------------------------

Create:

    shape = (4, 5)
    dtype = int16

Predict:

    ndim
    size
    itemsize
    nbytes
    strides


-------------------------------------------------------------------------------
Challenge 2
-------------------------------------------------------------------------------

Create:

    a = np.arange(20, dtype=np.int32)

    b = a[::4]

Predict:

    a.strides
    b.strides

Does b share memory with a?


-------------------------------------------------------------------------------
Challenge 3
-------------------------------------------------------------------------------

Create:

    a = np.arange(12).reshape(3, 4)

Compare:

    a[0]
    a[0:1]

Predict both shapes.


-------------------------------------------------------------------------------
Challenge 4
-------------------------------------------------------------------------------

Create:

    a = np.arange(12).reshape(3, 4)

    b = a[:, ::2]

Predict:

    b.shape
    b.strides
    whether b is C-contiguous
    whether b shares memory with a


-------------------------------------------------------------------------------
Challenge 5
-------------------------------------------------------------------------------

Create:

    a = np.arange(12).reshape(3, 4)

    b = a.T

Predict:

    b.shape
    b.strides

Does b share memory with a?


-------------------------------------------------------------------------------
Challenge 6
-------------------------------------------------------------------------------

Create the same logical matrix in:

    C-order
    F-order

Compare:

    shape
    values
    strides
    C_CONTIGUOUS
    F_CONTIGUOUS


-------------------------------------------------------------------------------
Challenge 7
-------------------------------------------------------------------------------

Create:

    a = np.array([1.9, 2.8, 3.7])

Convert to:

    int32

Predict the result before executing.


-------------------------------------------------------------------------------
Challenge 8
-------------------------------------------------------------------------------

Create:

    10 million float32 values

and:

    10 million float64 values

Calculate the memory usage BEFORE creating the arrays.

Then verify with:

    .nbytes


-------------------------------------------------------------------------------
Challenge 9
-------------------------------------------------------------------------------

Create:

    a = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ], dtype=np.int32)

Calculate the byte offset of:

    a[1, 2]

WITHOUT directly reading the element first.


-------------------------------------------------------------------------------
Challenge 10
-------------------------------------------------------------------------------

Explain in your own words:

    ndarray
    dtype
    itemsize
    nbytes
    data buffer
    stride
    view
    copy
    C-order
    F-order

If you can explain all ten without looking at the README,
Day 8 is genuinely understood.
"""


# =============================================================================
# 52. DAY 8 FINAL MENTAL MODEL
# =============================================================================

section("52. Day 8 Final Mental Model")


print(
    """
                          ndarray
                             |
          +------------------+------------------+
          |                                     |
          v                                     v

       METADATA                            DATA BUFFER

       ndim                                raw bytes
       shape
       size
       dtype
       itemsize
       strides
       flags
          |                                     |
          +------------------+------------------+
                             |
                             v

                  MULTIDIMENSIONAL ARRAY


shape
    ->
logical structure


dtype
    ->
how element bytes are interpreted


itemsize
    ->
bytes per element


strides
    ->
bytes moved when advancing along each axis


data buffer
    ->
underlying numerical storage


views
    ->
new ndarray interpretation that can share memory


copies
    ->
independent array data


C-order
    ->
last axis changes fastest


F-order
    ->
first axis changes fastest
"""
)


# =============================================================================
# 53. COMPLETION CHECKLIST
# =============================================================================

section("53. Day 8 Completion Checklist")


topics = [

    "ndarray",
    "ndim",
    "shape",
    "size",
    "array creation",
    "indexing",
    "slicing",
    "integer indexing vs slicing",
    "reshape",
    "vectorized operations",
    "mutability",
    "dtype",
    "signed integers",
    "unsigned integers",
    "itemsize",
    "nbytes",
    "type inference",
    "type promotion",
    "astype",
    "integer overflow",
    "floating-point precision",
    "float32 in ML",
    "data buffer",
    "logical vs physical memory",
    "contiguous memory",
    "strides",
    "views",
    "copies",
    "memory sharing",
    "basic vs advanced indexing",
    "C-order",
    "F-order",
    "contiguity flags",
    "non-contiguous views",
    "negative strides",
    "byte offsets",
    "reshape memory sharing",
    "transpose and strides",
    "memory layout performance",
    "AI/ML array examples"
]


for topic in topics:
    print("[x]", topic)


print(
    """

===============================================================================
DAY 8 COMPLETE
===============================================================================

Core mental model:

    ndarray
        =
    typed data buffer
        +
    multidimensional metadata


The goal was not to memorize NumPy functions.

The goal was to understand how NumPy represents and manipulates
numerical data efficiently.

Next NumPy concepts can now build on this foundation:

    broadcasting
    universal functions
    reductions
    advanced indexing
    vectorization
    numerical performance

===============================================================================
"""
)

