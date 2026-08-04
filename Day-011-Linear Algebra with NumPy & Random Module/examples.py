"""
=========================================================
Day 11
Linear Algebra with NumPy & Random Module
=========================================================

This file contains starter examples.

Topics:
- NumPy Arrays
- Vectors
- Matrices
- Matrix Operations
- Random Number Generation

The file will be updated with detailed implementations
after completing the official NumPy documentation.
"""

import numpy as np
import random

print("=" * 60)
print("LINEAR ALGEBRA WITH NUMPY")
print("=" * 60)

# ----------------------------------------------------
# Creating Arrays
# ----------------------------------------------------

vector = np.array([1, 2, 3, 4])
matrix = np.array([
    [1, 2],
    [3, 4]
])

print("\nVector")
print(vector)

print("\nMatrix")
print(matrix)

# ----------------------------------------------------
# Array Information
# ----------------------------------------------------

print("\nShape :", matrix.shape)
print("Size  :", matrix.size)
print("Dimensions :", matrix.ndim)
print("Data Type :", matrix.dtype)

# ----------------------------------------------------
# Basic Operations
# ----------------------------------------------------

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nAddition")
print(A + B)

print("\nSubtraction")
print(A - B)

print("\nElement-wise Multiplication")
print(A * B)

print("\nMatrix Multiplication")
print(A @ B)

print("\nTranspose")
print(A.T)

# ----------------------------------------------------
# Random Module
# ----------------------------------------------------

print("\n" + "=" * 60)
print("PYTHON RANDOM")
print("=" * 60)

print("Random Integer :", random.randint(1, 100))
print("Random Float   :", random.random())
print("Random Choice  :", random.choice(["Python", "NumPy", "AI", "ML"]))

# ----------------------------------------------------
# NumPy Random
# ----------------------------------------------------

print("\n" + "=" * 60)
print("NUMPY RANDOM")
print("=" * 60)

np.random.seed(42)

print("\nRandom Vector")
print(np.random.randint(0, 10, size=5))

print("\nRandom Matrix")
print(np.random.randint(0, 20, size=(3, 3)))

print("\nNormal Distribution")
print(np.random.normal(size=5))

print("\nUniform Distribution")
print(np.random.uniform(0, 1, size=5))

print("\nToday's implementation is an initial scaffold.")
print("Complete examples will be added after learning the official documentation.")