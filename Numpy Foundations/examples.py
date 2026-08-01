"""
Day 8/120 - NumPy Foundations
Examples covered so far
"""

import numpy as np


# ============================================================
# 1. Python List vs NumPy Array
# ============================================================

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print("Python list * 2:", python_list * 2)
print("NumPy array * 2:", numpy_array * 2)


# ============================================================
# 2. Creating an ndarray
# ============================================================

a = np.array([10, 20, 30])

print("\nArray:", a)
print("Type:", type(a))


# ============================================================
# 3. Element-wise Operations
# ============================================================

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("\na + b:", a + b)
print("a * 2:", a * 2)
print("a + 5:", a + 5)
print("a ** 2:", a ** 2)


# ============================================================
# 4. ndim - Number of Axes
# ============================================================

a = np.array([10, 20, 30])

b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n1D array ndim:", a.ndim)
print("2D array ndim:", b.ndim)


# ============================================================
# 5. shape - Size Along Each Axis
# ============================================================

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nArray:")
print(a)

print("Shape:", a.shape)
print("Dimensions:", a.ndim)


# ============================================================
# 6. 1D Shape vs 2D Shape
# ============================================================

one_dimensional = np.array([10, 20, 30])
two_dimensional = np.array([[10, 20, 30]])

print("\n1D array:")
print(one_dimensional)
print("ndim:", one_dimensional.ndim)
print("shape:", one_dimensional.shape)

print("\n2D array:")
print(two_dimensional)
print("ndim:", two_dimensional.ndim)
print("shape:", two_dimensional.shape)


# ============================================================
# 7. size - Total Number of Elements
# ============================================================

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print("\nArray:")
print(a)

print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)


# ============================================================
# 8. 3D Array Example
# ============================================================

x = np.zeros((3, 4, 5))

print("\n3D array:")
print(x)

print("ndim:", x.ndim)
print("shape:", x.shape)
print("size:", x.size)


# ============================================================
# 9. np.zeros()
# ============================================================

zeros = np.zeros((2, 3))

print("\nZeros:")
print(zeros)

print("shape:", zeros.shape)
print("size:", zeros.size)


# ============================================================
# 10. np.ones()
# ============================================================

ones = np.ones((2, 3))

print("\nOnes:")
print(ones)

print("shape:", ones.shape)
print("size:", ones.size)


# ============================================================
# 11. np.arange()
# ============================================================

a = np.arange(2, 12, 3)

print("\nnp.arange(2, 12, 3):")
print(a)

print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)


# ============================================================
# 12. np.linspace()
# ============================================================

# We stopped at this example.
# linspace creates a specified number of evenly spaced values.

a = np.linspace(0, 10, 5)

print("\nnp.linspace(0, 10, 5):")
print(a)
