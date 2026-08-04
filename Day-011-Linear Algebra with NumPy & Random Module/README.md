# Day 011 - Linear Algebra with NumPy & Random Module

---

# What is Linear Algebra?

Linear Algebra is the branch of mathematics that deals with vectors, matrices, and linear transformations.

In Artificial Intelligence and Machine Learning, almost every dataset and model is represented using matrices.

Examples:

- Images → Matrix
- Dataset → Matrix
- Word Embeddings → Vector
- Neural Network Weights → Matrix

Without Linear Algebra, modern Machine Learning would not exist.

---

# NumPy and Linear Algebra

NumPy provides a powerful N-dimensional array object (`ndarray`) and an extensive collection of mathematical operations.

Advantages:

- Fast computation
- Optimized memory usage
- Vectorized operations
- Scientific computing support
- Foundation for Pandas, Scikit-Learn, TensorFlow and PyTorch

---

# Scalars, Vectors and Matrices

## Scalar

A single numerical value.

Example

```python
5
```

---

## Vector

A one-dimensional collection of values.

```python
[1, 2, 3]
```

Created using

```python
np.array([1,2,3])
```

---

## Matrix

A two-dimensional collection of numbers arranged in rows and columns.

```python
[[1,2],
 [3,4]]
```

Created using

```python
np.array([[1,2],[3,4]])
```

---

# Common NumPy Array Properties

| Property | Description |
|-----------|-------------|
| shape | Size of each dimension |
| ndim | Number of dimensions |
| size | Total number of elements |
| dtype | Data type of array |

---

# Frequently Used Functions

```python
np.array()

np.zeros()

np.ones()

np.eye()

np.full()

reshape()

transpose()

flatten()

ravel()
```

---

# Matrix Operations

- Addition
- Subtraction
- Element-wise Multiplication
- Matrix Multiplication
- Transpose

Common operators

```python
+

-

*

@

np.dot()
```

---

# numpy.linalg Module

Used for advanced Linear Algebra operations.

Important functions

```python
det()

inv()

eig()

solve()

norm()

matrix_rank()
```

---

# Python Random Module

The `random` module is used to generate pseudo-random values.

Common functions

```python
random()

randint()

uniform()

choice()

sample()

shuffle()

seed()
```

---

# NumPy Random Module

NumPy provides faster and more powerful random number generation.

Important functions

```python
np.random.rand()

np.random.randn()

np.random.randint()

np.random.uniform()

np.random.normal()

np.random.choice()

np.random.shuffle()

np.random.default_rng()
```

---

# Random Seed

Setting a seed allows experiments to produce the same random values every time.

Example

```python
import numpy as np

np.random.seed(42)
```

Modern approach

```python
rng = np.random.default_rng(42)
```

---

# Applications in Machine Learning

Linear Algebra

- Feature matrices
- Image processing
- Neural networks
- Word embeddings
- PCA
- Recommendation systems

Random Module

- Weight initialization
- Data shuffling
- Train-test split
- Data augmentation
- Random sampling
- Simulation

---

# Key Takeaways

- NumPy is the standard library for numerical computing.
- Linear Algebra is the mathematical foundation of Machine Learning.
- Vectors and matrices represent almost every AI dataset.
- NumPy provides efficient matrix operations.
- Random number generation is essential for training and testing Machine Learning models.
- Reproducibility is achieved using random seeds.

---

