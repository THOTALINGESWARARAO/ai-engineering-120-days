"""
Day 10/120
NumPy — Universal Functions, Vectorization & Performance
"""

import timeit

import numpy as np


# ============================================================
# 1. Unary Universal Function
# ============================================================

a = np.array([1.0, 4.0, 9.0, 16.0])

result = np.sqrt(a)

print("Original:")
print(a)

print("\nSquare root:")
print(result)


# ============================================================
# 2. Binary Universal Function
# ============================================================

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

result = np.add(a, b)

print("\nBinary ufunc:")
print(result)


# ============================================================
# 3. Operator vs ufunc
# ============================================================

operator_result = a + b
ufunc_result = np.add(a, b)

print("\nOperator:")
print(operator_result)

print("ufunc:")
print(ufunc_result)

print(
    "Same values:",
    np.array_equal(operator_result, ufunc_result),
)


# ============================================================
# 4. reduce()
# ============================================================

a = np.array([1, 2, 3, 4])

result = np.add.reduce(a)

print("\nReduce:")
print(result)

# Predict before running:
#
# 1 + 2 + 3 + 4 = ?


# ============================================================
# 5. accumulate()
# ============================================================

result = np.add.accumulate(a)

print("\nAccumulate:")
print(result)

# Predict:
#
# [
#   1,
#   1 + 2,
#   1 + 2 + 3,
#   1 + 2 + 3 + 4
# ]


# ============================================================
# 6. outer()
# ============================================================

a = np.array([1, 2, 3])
b = np.array([10, 20])

result = np.multiply.outer(a, b)

print("\nOuter:")
print(result)

print("Shape:", result.shape)


# ============================================================
# 7. Python Loop
# ============================================================

numbers = list(range(10))

python_result = []

for x in numbers:
    python_result.append(x * 2)

print("\nPython loop:")
print(python_result)


# ============================================================
# 8. NumPy Vectorization
# ============================================================

arr = np.arange(10)

numpy_result = arr * 2

print("\nNumPy vectorization:")
print(numpy_result)


# ============================================================
# 9. Performance Experiment
# ============================================================

N = 1_000_000

python_numbers = list(range(N))
numpy_numbers = np.arange(N)


def python_version():
    return [x * 2 for x in python_numbers]


def numpy_version():
    return numpy_numbers * 2


python_time = timeit.timeit(
    python_version,
    number=10,
)

numpy_time = timeit.timeit(
    numpy_version,
    number=10,
)

print("\nPerformance")

print("Python:", python_time)
print("NumPy :", numpy_time)

print(
    "Speed ratio:",
    python_time / numpy_time,
)


# ============================================================
# 10. dtype
# ============================================================

a = np.arange(10, dtype=np.int32)

print("\nArray:")
print(a)

print("dtype:")
print(a.dtype)

print("itemsize:")
print(a.itemsize)

print("nbytes:")
print(a.nbytes)


# ============================================================
# 11. Memory Layout
# ============================================================

a = np.arange(12).reshape(3, 4)

print("\nArray:")
print(a)

print("Shape:")
print(a.shape)

print("Strides:")
print(a.strides)

print("C contiguous:")
print(a.flags.c_contiguous)


# ============================================================
# 12. Transpose and Memory Layout
# ============================================================

b = a.T

print("\nTransposed:")
print(b)

print("Shape:")
print(b.shape)

print("Strides:")
print(b.strides)

print("C contiguous:")
print(b.flags.c_contiguous)


# ============================================================
# 13. ML-style Vectorized Computation
# ============================================================

X = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
])

weights = np.array([0.5, 2.0])

predictions = X @ weights

print("\nML-style computation:")
print(predictions)

print("Prediction shape:")
print(predictions.shape)


# ============================================================
# Questions
# ============================================================

"""
After completing Day 10, answer:

1. What is a ufunc?

2. What is the difference between:
       a + b
   and:
       np.add(a, b)?

3. What does vectorization mean?

4. Does vectorization mean there are no loops?

5. Why are Python loops often slower for numerical workloads?

6. Why can NumPy execute numerical operations efficiently?

7. What role does dtype play?

8. How can memory layout affect performance?

9. Why might vectorization allocate temporary arrays?

10. How does this relate to ML computations?
"""