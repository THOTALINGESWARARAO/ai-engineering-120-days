
"""
Day 9/120 — NumPy Array Manipulation & Broadcasting
Topic: Multi-Dimensional Indexing

Covered:
1. Creating a 2-D array
2. Understanding axes
3. Indexing one axis
4. Indexing multiple axes
5. Integer indexing and dimension reduction
6. 0-D vs 1-D arrays
7. Integer indexing vs slicing preview
"""

import numpy as np


# ============================================================
# 1. CREATE A 2-D ARRAY
# ============================================================

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(a)

print("\nArray Information:")
print("ndim :", a.ndim)
print("shape:", a.shape)
print("size :", a.size)


# ============================================================
# 2. MULTI-DIMENSIONAL INDEXING
# ============================================================

# Mental model:
#
# a[i, j]
#
# i -> axis 0
# j -> axis 1

print("\n--- Multi-Dimensional Indexing ---")

value = a[1, 2]

print("a[1, 2] =", value)

# axis 0 -> index 1
# axis 1 -> index 2
#
# Result:
# 60


# ============================================================
# 3. INDEXING ONLY AXIS 0
# ============================================================

print("\n--- Indexing Axis 0 ---")

x = a[2]

print("a[2]:")
print(x)

print("ndim :", x.ndim)
print("shape:", x.shape)

# Output:
#
# [70 80 90]
# ndim  = 1
# shape = (3,)
#
# Integer indexing consumes axis 0.


# ============================================================
# 4. ZERO-BASED INDEXING
# ============================================================

print("\n--- Zero-Based Indexing ---")

print("a[0] =", a[0])
print("a[1] =", a[1])
print("a[2] =", a[2])

# Remember:
#
# index 0 -> first position
# index 1 -> second position
# index 2 -> third position


# ============================================================
# 5. INDEXING BOTH AXES
# ============================================================

print("\n--- Indexing Both Axes ---")

x = a[2, 1]

print("a[2, 1] =", x)
print("ndim     =", x.ndim)
print("shape    =", x.shape)

# Result:
#
# 80
#
# ndim  = 0
# shape = ()
#
# Both axes were indexed using integers.
# Therefore, both axes were consumed.


# ============================================================
# 6. DIMENSION REDUCTION
# ============================================================

print("\n--- Dimension Reduction ---")

print("Original:")
print("shape =", a.shape)
print("ndim  =", a.ndim)

one_axis = a[2]

print("\nAfter a[2]:")
print("value =", one_axis)
print("shape =", one_axis.shape)
print("ndim  =", one_axis.ndim)

two_axes = a[2, 1]

print("\nAfter a[2, 1]:")
print("value =", two_axes)
print("shape =", two_axes.shape)
print("ndim  =", two_axes.ndim)


# ============================================================
# 7. 0-D ARRAY/SCALAR-LIKE RESULT VS 1-D ARRAY
# ============================================================

print("\n--- 0-D vs 1-D ---")

scalar_like = a[2, 1]

one_d = np.array([80])

print("Scalar-like result:")
print("value =", scalar_like)
print("ndim  =", scalar_like.ndim)
print("shape =", scalar_like.shape)

print("\n1-D array:")
print("value =", one_d)
print("ndim  =", one_d.ndim)
print("shape =", one_d.shape)

# They may represent the same numerical value,
# but their dimensional structures are different.
#
# 80
# shape = ()
#
# [80]
# shape = (1,)


# ============================================================
# 8. INTEGER INDEXING VS SLICING — PREVIEW
# ============================================================

print("\n--- Integer Indexing vs Slicing ---")

integer_result = a[2, 1]

slice_result = a[2, 1:2]

print("Integer indexing:")
print(integer_result)
print("shape =", integer_result.shape)

print("\nSlicing:")
print(slice_result)
print("shape =", slice_result.shape)

# Important:
#
# a[2, 1]
#     -> integer index on both axes
#     -> shape ()
#
# a[2, 1:2]
#     -> integer on axis 0
#     -> slice on axis 1
#     -> shape (1,)
#
# Integer indexing can remove an axis.
# Slicing can preserve an axis.


# ============================================================
# 9. AXIS MENTAL MODEL
# ============================================================

print("\n--- Axis Mental Model ---")

print(a)

# For a 2-D array:
#
# a[i, j]
#
# i -> axis 0
# j -> axis 1
#
# Avoid thinking only:
#
# row, column
#
# Prefer:
#
# axis 0, axis 1, axis 2, ...
#
# because this model extends naturally to N-dimensional arrays.


# ============================================================
# 10. MINI EXPERIMENT
# ============================================================

print("\n--- Mini Experiment ---")

x = a[1]

print("a[1] =", x)
print("ndim =", x.ndim)
print("shape =", x.shape)

y = a[1, 0]

print("\na[1, 0] =", y)
print("ndim =", y.ndim)
print("shape =", y.shape)


# ============================================================
# DAY 9 — CURRENT TAKEAWAY
# ============================================================

"""
Core Mental Model

    a[i, j, k, ...]

    i -> axis 0
    j -> axis 1
    k -> axis 2


Integer indexing:

    a[2]

    shape:
        (3, 3)
           |
           v
          (3,)


Multiple integer indices:

    a[2, 1]

    shape:
        (3, 3)
           |
           v
           ()


Key Rule:

    Integer indexing consumes an axis.

Slicing:

    Can preserve the indexed axis.


NEXT:

    x = a[1:3]

Predict:

    x       = ?
    x.ndim  = ?
    x.shape = ?
"""
