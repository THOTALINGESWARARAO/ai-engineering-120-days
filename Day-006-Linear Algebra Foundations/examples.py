"""
Day 6 — Linear Algebra Foundations
"""

import numpy as np

# ============================================================
# PART 1 — SCALARS
# ============================================================

# 1. Creating Python Scalars

integer = 10
floating = 3.14
complex_number = 2 + 3j
boolean = True

print("Integer:", integer)
print("Float:", floating)
print("Complex:", complex_number)
print("Boolean:", boolean)

# ------------------------------------------------------------

# 2. NumPy Scalar

scalar = np.array(100)

print("Scalar:", scalar)
print("Type:", type(scalar))
print("Shape:", scalar.shape)
print("Dimensions:", scalar.ndim)
print("Data Type:", scalar.dtype)
print("Item Size:", scalar.itemsize)

# ------------------------------------------------------------

# 3. Scalar Arithmetic

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Power:", a ** b)

# ------------------------------------------------------------

# 4. Scalar Comparison

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# ------------------------------------------------------------

# 5. Scalar Functions

print(abs(-25))
print(round(3.14159, 2))
print(pow(2, 5))
print(min(10, 20))
print(max(10, 20))

# ============================================================
# PART 2 — VECTORS
# ============================================================

# 6. Creating Vectors

vector = np.array([10, 20, 30])

print(vector)

# ------------------------------------------------------------

# 7. Row Vector and Column Vector

row_vector = np.array([[1, 2, 3]])
column_vector = np.array([[1],
                          [2],
                          [3]])

print(row_vector)
print(column_vector)

# ------------------------------------------------------------

# 8. Vector Properties

vector = np.array([2, 4, 6, 8])

print("Shape:", vector.shape)
print("Size:", vector.size)
print("Dimensions:", vector.ndim)
print("Data Type:", vector.dtype)
print("Item Size:", vector.itemsize)

# ------------------------------------------------------------

# 9. Vector Indexing

vector = np.array([100, 200, 300, 400])

print(vector[0])
print(vector[1])
print(vector[-1])

# ------------------------------------------------------------

# 10. Vector Slicing

vector = np.array([10, 20, 30, 40, 50, 60])

print(vector[:3])
print(vector[2:])
print(vector[1:5])
print(vector[::2])
print(vector[::-1])

# ------------------------------------------------------------

# 11. Vector Addition

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(A + B)

# ------------------------------------------------------------

# 12. Vector Subtraction

print(A - B)

# ------------------------------------------------------------

# 13. Scalar Multiplication

print(5 * A)

# ------------------------------------------------------------

# 14. Scalar Division

print(A / 2)

# ------------------------------------------------------------

# 15. Element-wise Multiplication

print(A * B)

# ------------------------------------------------------------

# 16. Vector Magnitude

vector = np.array([3, 4])

print(np.linalg.norm(vector))

# ------------------------------------------------------------

# 17. Unit Vector

unit_vector = vector / np.linalg.norm(vector)

print(unit_vector)

# ------------------------------------------------------------

# 18. Dot Product

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.dot(A, B))
print(A @ B)

# ------------------------------------------------------------

# 19. Cross Product

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.cross(A, B))

# ------------------------------------------------------------

# 20. Euclidean Distance

A = np.array([1, 2])
B = np.array([4, 6])

print(np.linalg.norm(A - B))

# ------------------------------------------------------------

# 21. Vector Statistics

vector = np.array([10, 20, 30, 40, 50])

print(np.sum(vector))
print(np.mean(vector))
print(np.min(vector))
print(np.max(vector))
print(np.std(vector))
print(np.var(vector))

# ============================================================
# PART 3 — MATRICES
# ============================================================

# 22. Creating Matrices

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)

# ------------------------------------------------------------

# 23. Matrix Properties

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)
print("Item Size:", matrix.itemsize)

# ------------------------------------------------------------

# 24. Matrix Indexing

print(matrix[0, 0])
print(matrix[0, 2])
print(matrix[1, 1])
print(matrix[-1, -1])

# ------------------------------------------------------------

# 25. Row Access

print(matrix[0])
print(matrix[1])

# ------------------------------------------------------------

# 26. Column Access

print(matrix[:, 0])
print(matrix[:, 1])
print(matrix[:, 2])

# ------------------------------------------------------------

# 27. Matrix Slicing

print(matrix[:1])
print(matrix[:, 1:])
print(matrix[0:2, 1:3])

# ------------------------------------------------------------

# 28. Matrix Addition

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A + B)

# ------------------------------------------------------------

# 29. Matrix Subtraction

print(A - B)

# ------------------------------------------------------------

# 30. Scalar Multiplication

print(5 * A)

# ------------------------------------------------------------

# 31. Scalar Division

print(A / 2)

# ------------------------------------------------------------

# 32. Element-wise Multiplication

print(A * B)

# ------------------------------------------------------------

# 33. Matrix Transpose

print(A.T)
print(np.transpose(A))

# ------------------------------------------------------------

# 34. Matrix Reshape

matrix = np.arange(12)

print(matrix)

matrix = matrix.reshape(3, 4)

print(matrix)

# ------------------------------------------------------------

# 35. Matrix Flatten

print(matrix.flatten())
print(matrix.ravel())

# ------------------------------------------------------------

# 36. Matrix Statistics

print(np.sum(matrix))
print(np.mean(matrix))
print(np.min(matrix))
print(np.max(matrix))
print(np.std(matrix))
print(np.var(matrix))

# ============================================================
# PART 4 — SPECIAL MATRICES
# ============================================================

# 37. Zero Matrix

zero_matrix = np.zeros((3, 3))

print(zero_matrix)

# ------------------------------------------------------------

# 38. Ones Matrix

ones_matrix = np.ones((3, 3))

print(ones_matrix)

# ------------------------------------------------------------

# 39. Identity Matrix

identity = np.eye(4)

print(identity)

# ------------------------------------------------------------

# 40. Diagonal Matrix

diagonal = np.diag([2, 4, 6, 8])

print(diagonal)

# ------------------------------------------------------------

# 41. Full Matrix

full_matrix = np.full((3, 4), 100)

print(full_matrix)

# ------------------------------------------------------------

# 42. Random Matrix

random_matrix = np.random.rand(3, 3)

print(random_matrix)

# ------------------------------------------------------------

# 43. Integer Random Matrix

random_int = np.random.randint(1, 10, (3, 3))

print(random_int)

# ------------------------------------------------------------

# 44. Matrix Copy

A = np.array([
    [1, 2],
    [3, 4]
])

B = A.copy()

print(B)

# ------------------------------------------------------------

# 45. Matrix Shape Manipulation

matrix = np.arange(16)

matrix = matrix.reshape(4, 4)

print(matrix)

print(matrix.reshape(2, 8))
print(matrix.reshape(8, 2))
print(matrix.reshape(1, 16))

# ============================================================
# PART 5 — MATRIX MULTIPLICATION
# ============================================================

# 46. Matrix × Vector Multiplication

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 20, 30])

print(A @ v)

# ------------------------------------------------------------

# 47. Matrix × Matrix Multiplication

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A @ B)

# ------------------------------------------------------------

# 48. np.matmul()

print(np.matmul(A, B))

# ------------------------------------------------------------

# 49. np.dot()

print(np.dot(A, B))

# ------------------------------------------------------------

# 50. Matrix Power

A = np.array([
    [2, 0],
    [0, 2]
])

print(np.linalg.matrix_power(A, 2))
print(np.linalg.matrix_power(A, 3))

# ------------------------------------------------------------

# 51. Matrix Trace

A = np.array([
    [1, 2],
    [3, 4]
])

print(np.trace(A))

# ------------------------------------------------------------

# 52. Matrix Determinant

print(np.linalg.det(A))

# ------------------------------------------------------------

# 53. Matrix Inverse

print(np.linalg.inv(A))

# ------------------------------------------------------------

# 54. Matrix Rank

print(np.linalg.matrix_rank(A))

# ------------------------------------------------------------

# 55. Eigen Values and Eigen Vectors

eigen_values, eigen_vectors = np.linalg.eig(A)

print("Eigen Values")
print(eigen_values)

print()

print("Eigen Vectors")
print(eigen_vectors)

# ============================================================
# PART 6 — TENSORS
# ============================================================

# 56. Creating Rank-3 Tensor

tensor = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(tensor)

# ------------------------------------------------------------

# 57. Tensor Properties

print("Shape:", tensor.shape)
print("Dimensions:", tensor.ndim)
print("Size:", tensor.size)
print("Data Type:", tensor.dtype)
print("Item Size:", tensor.itemsize)

# ------------------------------------------------------------

# 58. Tensor Indexing

print(tensor[0])
print(tensor[1])

print(tensor[0, 0])
print(tensor[0, 1])

print(tensor[0, 0, 0])
print(tensor[1, 1, 1])

# ------------------------------------------------------------

# 59. Tensor Slicing

print(tensor[:, :, 0])
print(tensor[:, :, 1])

print(tensor[0, :, :])
print(tensor[1, :, :])

# ------------------------------------------------------------

# 60. Tensor Reshape

tensor = np.arange(24)

tensor = tensor.reshape(2, 3, 4)

print(tensor)

print()

print(tensor.reshape(4, 6))

print()

print(tensor.reshape(6, 4))

# ------------------------------------------------------------

# 61. Tensor Transpose

tensor = np.arange(24).reshape(2, 3, 4)

print(np.transpose(tensor))

print()

print(np.transpose(tensor, (1, 0, 2)))

print()

print(np.transpose(tensor, (2, 1, 0)))

# ------------------------------------------------------------

# 62. Tensor Flatten

tensor = np.arange(24).reshape(2, 3, 4)

print(tensor.flatten())

# ------------------------------------------------------------

# 63. Tensor Statistics

print(np.sum(tensor))
print(np.mean(tensor))
print(np.min(tensor))
print(np.max(tensor))
print(np.std(tensor))
print(np.var(tensor))

# ============================================================
# PART 7 — NUMPY LINEAR ALGEBRA
# ============================================================

# 64. Vector Norm

vector = np.array([3, 4])

print(np.linalg.norm(vector))

# ------------------------------------------------------------

# 65. Matrix Norm

matrix = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.norm(matrix))

# ------------------------------------------------------------

# 66. Matrix Trace

matrix = np.array([
    [1, 2],
    [3, 4]
])

print(np.trace(matrix))

# ------------------------------------------------------------

# 67. Matrix Determinant

matrix = np.array([
    [4, 7],
    [2, 6]
])

print(np.linalg.det(matrix))

# ------------------------------------------------------------

# 68. Matrix Inverse

print(np.linalg.inv(matrix))

# ------------------------------------------------------------

# 69. Matrix Rank

matrix = np.array([
    [1, 2],
    [2, 4]
])

print(np.linalg.matrix_rank(matrix))

# ------------------------------------------------------------

# 70. Eigen Values and Eigen Vectors

matrix = np.array([
    [4, 2],
    [1, 3]
])

eigen_values, eigen_vectors = np.linalg.eig(matrix)

print("Eigen Values")
print(eigen_values)

print()

print("Eigen Vectors")
print(eigen_vectors)

# ------------------------------------------------------------

# 71. Singular Value Decomposition (SVD)

matrix = np.array([
    [1, 2],
    [3, 4]
])

U, S, VT = np.linalg.svd(matrix)

print("U")
print(U)

print()

print("Singular Values")
print(S)

print()

print("VT")
print(VT)

# ------------------------------------------------------------

# 72. Solve Linear Equations

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([8, 13])

solution = np.linalg.solve(A, B)

print(solution)

# ------------------------------------------------------------

# 73. Matrix Power

matrix = np.array([
    [2, 0],
    [0, 2]
])

print(np.linalg.matrix_power(matrix, 2))
print(np.linalg.matrix_power(matrix, 3))

# ------------------------------------------------------------

# 74. Matrix Condition Number

matrix = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.cond(matrix))

# ------------------------------------------------------------

# 75. Matrix Pseudo Inverse

matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(np.linalg.pinv(matrix))

# ============================================================
# DAY 6 CORE MODEL
# ============================================================

"""
Linear Algebra Foundations
==========================

Scalar
------
Single numerical value

Vector
------
One-dimensional collection of values

Matrix
------
Two-dimensional collection of values

Tensor
------
Multi-dimensional collection of values

Vector Operations
-----------------
+
-
*
/
Dot Product
Cross Product
Magnitude
Unit Vector
Distance

Matrix Operations
-----------------
+
-
*
/
Transpose
Reshape
Flatten
Matrix × Vector
Matrix × Matrix

Special Matrices
----------------
Zero Matrix
Ones Matrix
Identity Matrix
Diagonal Matrix
Full Matrix

NumPy Functions
---------------
np.array()
np.zeros()
np.ones()
np.eye()
np.diag()
np.full()

Properties
----------
shape
ndim
size
dtype
itemsize

Linear Algebra
--------------
np.dot()
np.matmul()
@
np.linalg.norm()
np.trace()
np.linalg.det()
np.linalg.inv()
np.linalg.matrix_rank()
np.linalg.eig()
np.linalg.svd()
np.linalg.solve()
np.linalg.matrix_power()
np.linalg.cond()
np.linalg.pinv()

Mental Model
------------

Real World Data
        │
        ▼
Numbers
        │
        ▼
Scalars
        │
        ▼
Vectors
        │
        ▼
Matrices
        │
        ▼
Tensors
        │
        ▼
Linear Algebra
        │
        ▼
Machine Learning
        │
        ▼
Deep Learning
        │
        ▼
Large Language Models
"""