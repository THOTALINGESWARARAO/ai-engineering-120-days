
# Day 6 — Linear Algebra Foundations

## Part 1: Introduction to Linear Algebra & Scalars


# Chapter 1 — Introduction to Linear Algebra

---

# 1.1 Why Should an AI Engineer Learn Linear Algebra?

Suppose you build an AI system that recognizes cats.

The computer never sees:

```
🐱
```

Instead it sees millions of numbers.

An image becomes

```
[120, 125, 140, 255, 13, 52, ...]
```

A sentence becomes

```
[-0.25, 0.91, 0.33, ...]
```

A song becomes

```
[0.21, -0.11, 0.88, ...]
```

Everything in AI eventually becomes **numbers**.

Linear Algebra is the mathematics that teaches us how to represent, organize, and manipulate those numbers.

---

# 1.2 Where Is Linear Algebra Used?

| Domain                 | Uses Linear Algebra? | Example                    |
| ---------------------- | -------------------: | -------------------------- |
| Machine Learning       |                    ✅ | Feature vectors            |
| Deep Learning          |                    ✅ | Weight matrices            |
| Computer Vision        |                    ✅ | Images as matrices         |
| NLP                    |                    ✅ | Word embeddings            |
| Transformers           |                    ✅ | Attention                  |
| Recommendation Systems |                    ✅ | Similarity search          |
| Robotics               |                    ✅ | Coordinate transformations |
| Graphics               |                    ✅ | 3D transformations         |

If you remove linear algebra from AI, modern AI systems cannot function.

---

# 1.3 The Big Picture

Imagine a complete ML pipeline.

```
Real World

↓

Collect Data

↓

Convert into Numbers

↓

Linear Algebra

↓

Machine Learning

↓

Prediction
```

Notice something important:

Everything passes through **Linear Algebra**.

---

# 1.4 The Building Blocks

Linear Algebra has four fundamental mathematical objects.

```
Scalar

↓

Vector

↓

Matrix

↓

Tensor
```

Think of them as increasing levels of organization.

---

## Scalar

One number.

```
5
```

---

## Vector

Collection of numbers.

```
[5, 7, 9]
```

---

## Matrix

Collection of vectors.

```
[
 [1,2],
 [3,4]
]
```

---

## Tensor

Collection of matrices.

```
[
 Matrix 1,
 Matrix 2,
 Matrix 3
]
```

We'll study tensors later.

---

# 1.5 Mental Model

Think of these like containers.

```
Scalar

┌───┐
│ 7 │
└───┘

↓

Vector

┌───┐
│ 2 │
├───┤
│ 4 │
├───┤
│ 8 │
└───┘

↓

Matrix

┌─────────┐
│2 4 8    │
│5 1 7    │
│9 2 6    │
└─────────┘

↓

Tensor

┌──────────────┐

Matrix

Matrix

Matrix

└──────────────┘
```

---

# 1.6 AI Interpretation

Imagine a classroom.

One student's marks:

```
95
```

Scalar.

---

One student's complete information:

```
[95, 90, 92]
```

Vector.

---

Entire classroom:

```
[
 [95,90,92],
 [88,77,91],
 [65,82,80]
]
```

Matrix.

---

Entire school (many classrooms):

Tensor.

---

# 1.7 Why Not Use Ordinary Variables?

Instead of

```python
math = 95
science = 90
english = 92
```

we use

```python
marks = [95,90,92]
```

Why?

Because mathematics becomes much simpler.

Imagine adding 100 subjects manually.

Vectors make it one operation.

---

# 1.8 AI Examples

### Face Recognition

One face

↓

```
512 numbers
```

↓

One vector.

---

### ChatGPT

One sentence

↓

```
3072 numbers
```

↓

Embedding vector.

---

### Image Classification

One image

↓

```
Millions of numbers
```

↓

Matrices and tensors.

---

# 1.9 Common Misconceptions

### ❌ Mathematics is only for researchers.

No.

Every NumPy operation is linear algebra.

---

### ❌ Libraries hide mathematics.

Libraries implement mathematics.

Understanding the math helps you understand what the library is doing.

---

### ❌ Linear algebra is separate from programming.

No.

NumPy, PyTorch, TensorFlow, JAX, and scikit-learn are built around linear algebra.

---

# Chapter Summary

Linear Algebra is the language used to represent and manipulate numerical data in AI.

It begins with four mathematical objects:

* Scalar
* Vector
* Matrix
* Tensor

Everything you'll study later builds on these.

---

# Chapter 2 — Scalars

---

# 2.1 Need

Suppose we only want to store one value.

Temperature:

```
35
```

Age:

```
20
```

Learning rate:

```
0.001
```

Accuracy:

```
98.2
```

These are all **scalars**.

---

# 2.2 Definition

A scalar is a **single numerical value**.

Examples:

```
7

-12

3.14

0

1000
```

Unlike vectors, scalars have **no components**.

---

# 2.3 Mental Model

Imagine a box.

```
┌─────┐
│  42 │
└─────┘
```

Only one value.

Nothing else.

---

# 2.4 Scalar Properties

A scalar has:

* one value
* no direction
* no dimension in the vector-space sense
* no components

---

# 2.5 Scalars in AI

Learning rate

```
0.001
```

Batch size

```
32
```

Epochs

```
100
```

Loss

```
0.254
```

Accuracy

```
97.5
```

All are scalars.

---

# 2.6 Python Representation

```python
age = 20

temperature = 35.7

learning_rate = 0.001
```

These are ordinary Python numbers.

---

# 2.7 NumPy Representation

Later we'll use

```python
import numpy as np

x = np.array(5)
```

Notice:

Even though it is stored inside NumPy,

it is still mathematically a scalar.

---

# 2.8 Scalar Operations

Addition

```
5 + 7 = 12
```

Subtraction

```
8 - 3 = 5
```

Multiplication

```
4 × 6 = 24
```

Division

```
10 / 2 = 5
```

Nothing new here.

---

# 2.9 Scalars vs Vectors

Scalar

```
5
```

Vector

```
[5]
```

These are **not** the same object.

One is

```
Number
```

The other is

```
Collection containing one number.
```

This distinction becomes important when using NumPy.

---

# 2.10 AI Example

Suppose a neural network predicts

```
Loss = 0.12
```

That loss is a scalar.

The gradient computation may involve vectors and matrices, but the final loss is often a single scalar value.

---

# Common Misconceptions

### ❌ `[5]` is a scalar.

No.

It is a one-dimensional vector with one component.

---

### ❌ Scalars cannot be floats.

They absolutely can.

```
3.14
```

is a scalar.

---

### ❌ Scalars are only integers.

No.

Integers, floating-point numbers, and other numeric values can all be scalars.

---

# Revision Sheet

## Linear Algebra Objects

```
Scalar

↓

Vector

↓

Matrix

↓

Tensor
```

---

## Scalar

```
5
```

One value.

---

## Vector

```
[5,7]
```

Multiple values.

---

## Matrix

```
[
 [1,2],
 [3,4]
]
```

Collection of vectors.

---

# Interview Questions

1. What is Linear Algebra?
2. Why is Linear Algebra important for AI?
3. Differentiate scalar and vector.
4. Is `[5]` a scalar?
5. Why are images represented using matrices?
6. Give three examples of scalars in deep learning.

---

# Practice Questions

1. Classify each as scalar, vector, matrix, or tensor:

```
42

[4,5]

[[1,2],[3,4]]

10

[7]
```

2. Give five examples of scalars used in machine learning.

3. Explain why a scalar and a one-element vector are mathematically different.

---

---

# Chapter 3 — Vectors

---

# 3.1 Why Do We Need Vectors?

Suppose you are building an AI model to predict whether a student will get placed.

Each student has multiple attributes.

| Feature             | Value |
| ------------------- | ----: |
| Age                 |    20 |
| CGPA                |   9.1 |
| DSA Problems Solved |   450 |
| Attendance          |    92 |

Instead of storing four independent variables,

```python
age = 20
cgpa = 9.1
dsa = 450
attendance = 92
```

AI groups them into **one mathematical object**:

```text
[20, 9.1, 450, 92]
```

This object is called a **vector**.

---

# Why is this better?

Imagine a dataset with

* 10 features
* 100 features
* 1000 features
* 10,000 features

Creating separate variables becomes impossible.

Vectors allow us to treat **all features as one object**.

---

# 3.2 Official Definition

A **vector** is an ordered collection of numbers.

Mathematically,

[
\mathbf{v} =
\begin{bmatrix}
v_1\
v_2\
v_3\
\vdots\
v_n
\end{bmatrix}
]

or

[
(v_1,v_2,\ldots,v_n)
]

Each number is called a **component** (or element) of the vector.

---

# 3.3 Mental Model

Think of a vector as a **feature container**.

Instead of

```text
Student

Age = 20
CGPA = 9.1
Attendance = 92
```

we package everything into one object.

```text
Student

↓

Vector

[20, 9.1, 92]
```

The vector is simply the numerical representation of one object.

---

# 3.4 Components

Example

```text
v = [3, 7, 2]
```

Components:

```text
Component 1 = 3

Component 2 = 7

Component 3 = 2
```

Diagram

```text
      Vector

┌─────────────────────┐
│   3    7     2      │
└─────────────────────┘
    ↑    ↑     ↑

   v₁   v₂    v₃
```

---

# 3.5 Dimension

The **dimension** of a vector is the number of components it contains.

Examples

```text
[5]
```

Dimension = **1**

---

```text
[5,7]
```

Dimension = **2**

---

```text
[5,7,9]
```

Dimension = **3**

---

```text
[1,2,3,4,5]
```

Dimension = **5**

---

Suppose an ML dataset has

256 features.

Every training example becomes a

```text
256-dimensional vector
```

---

# Important

Dimension is **not** physical dimensions.

A 768-dimensional embedding does **not** mean 768 spatial directions.

It simply means

```text
768 numbers.
```

---

# 3.6 Order Matters

Consider

```text
[20, 9.1, 92]
```

Suppose it means

```text
Age

CGPA

Attendance
```

Now reorder it.

```text
[92,20,9.1]
```

Now it means

```text
Attendance

Age

CGPA
```

The meaning changes completely.

Vectors are **ordered**.

Unlike a set,

```text
{1,2,3}
```

the order is significant.

---

# 3.7 Row Vector vs Column Vector

A vector can be written in two ways.

## Row Vector

[
[1\quad2\quad3]
]

Diagram

```text
┌─────────────┐
│1   2   3    │
└─────────────┘
```

Shape

```text
1 × 3
```

---

## Column Vector

[
\begin{bmatrix}
1\
2\
3
\end{bmatrix}
]

Diagram

```text
┌───┐
│1  │
├───┤
│2  │
├───┤
│3  │
└───┘
```

Shape

```text
3 × 1
```

---

# Important Rule

Both contain the same numbers.

Only the orientation changes.

Later, in matrix multiplication,

this difference becomes extremely important.

---

# 3.8 Geometry of Vectors

A vector can represent a point.

---

## One Dimension

```text
[4]
```

Number line

```text
----------------●---------
                4
```

---

## Two Dimensions

```text
[3,4]
```

```text
y

5 |

4 |          ●

3 |

2 |

1 |

0 +-------------------

   0 1 2 3 4

         x
```

---

## Three Dimensions

```text
[3,4,5]
```

Represents one point in 3D.

---

Higher dimensions

cannot be visualized,

but mathematically

nothing changes.

---

# 3.9 Object Representation

Suppose

```text
Car

Speed = 180

Mileage = 18

Price = 1200000
```

Object

↓

Vector

```text
[180,18,1200000]
```

Diagram

```text
Car

      │

      ▼

+-----------------------+

Speed

Mileage

Price

+-----------------------+

      │

      ▼

[180,18,1200000]
```

One vector now completely represents the car.

---

# 3.10 Python Representation

Python has no dedicated vector object.

We often begin with

```python
v = [3,4,5]
```

or

```python
v = (3,4,5)
```

But mathematically,

those are simply containers representing the vector.

---

# 3.11 NumPy Representation

In AI,

vectors are usually stored using NumPy.

```python
import numpy as np

v = np.array([3,4,5])
```

This is still the same mathematical vector,

but NumPy allows efficient mathematical operations.

---

# 3.12 Feature Vectors

Suppose an employee has

```text
Experience

Salary

Performance

Projects
```

AI converts it into

```text
[5,90000,9.4,12]
```

This is called a

**feature vector**.

Every ML model receives feature vectors as input.

---

# 3.13 Embedding Vectors

LLMs do not understand words.

Suppose we have

```text
"Cat"
```

The model converts it into

```text
[-0.82,
0.11,
...
1.45]
```

Maybe

1536 numbers.

This vector is called an

**embedding**.

Embeddings are vectors representing meaning.

---

# 3.14 Images

A grayscale image

28 × 28

↓

784 pixels

↓

One vector

```text
[0,
255,
132,
...
41]
```

784-dimensional vector.

---

# 3.15 Audio

One second of audio

↓

Thousands of amplitudes

↓

Vector.

---

# 3.16 Why AI Loves Vectors

Everything becomes

```text
Object

↓

Numbers

↓

Vector
```

Once everything becomes vectors,

the same mathematical operations work for

* Images
* Audio
* Text
* Videos
* Sensor data

---

# Common Misconceptions

## ❌ A vector is just a Python list.

No.

A Python list is a programming data structure.

A vector is a mathematical concept.

A list, tuple, or NumPy array can **represent** a vector.

---

## ❌ Dimension means physical space.

No.

Dimension means

```text
Number of components.
```

---

## ❌ A row vector and column vector are identical.

They contain the same numbers,

but they have different shapes.

This matters in matrix multiplication.

---

## ❌ Two vectors with the same numbers but different order are equal.

Example

```text
[1,2,3]
```

and

```text
[3,2,1]
```

They are different vectors.

Order is part of the definition.

---

## ❌ Vectors always represent arrows.

In physics, vectors often represent magnitude and direction.

In AI, vectors usually represent **data**, **features**, or **embeddings**.

---

# AI Connections

| AI Area                | Vector Represents |
| ---------------------- | ----------------- |
| Machine Learning       | Feature vector    |
| NLP                    | Word embedding    |
| LLMs                   | Token embedding   |
| Computer Vision        | Pixel values      |
| Recommendation Systems | User embedding    |
| Face Recognition       | Face embedding    |
| Speech Recognition     | Audio features    |

---

# Summary

A vector is:

* An ordered collection of numbers.
* A mathematical object.
* A representation of one entity.
* Defined by its dimension.
* The primary data structure used throughout AI.

---

# Revision Sheet

```text
Scalar

↓

One number

↓

Vector

↓

One ordered collection of numbers

↓

Matrix

↓

Collection of vectors

↓

Tensor

↓

Collection of matrices
```

---

# Interview Questions

1. What is a vector?
2. Difference between scalar and vector.
3. What is the dimension of a vector?
4. Why does order matter in vectors?
5. Difference between a row vector and a column vector.
6. What is a feature vector?
7. What is an embedding vector?
8. Why are vectors fundamental in AI?
9. Is a Python list a vector?
10. Explain why a 768-dimensional embedding does not mean 768 physical dimensions.

---

# Practice Questions

### Basic

1. Find the dimension:

```text
[3,7]
```

2. Find the dimension:

```text
[5,2,9,1]
```

3. Is

```text
[7]
```

a scalar or a vector?

---

### Intermediate

1. Explain why

```text
[1,2,3]
```

and

```text
[3,2,1]
```

represent different vectors.

2. Convert the following into a feature vector:

```text
Student

Age = 21

CGPA = 8.8

Attendance = 90

Projects = 5
```

---

### Advanced

A dataset contains

* Height
* Weight
* Age
* Income
* Experience
* Credit Score

How many dimensions does each sample vector have?

---

# Mind Map

```text
                 VECTOR
                    │
      ┌─────────────┼─────────────┐
      │             │             │
 Components     Dimension     Ordered
      │             │             │
      ├─────────────┼─────────────┤
      │             │             │
 Row Vector   Column Vector   Geometry
      │
      ├─────────────┬─────────────┐
      │             │             │
 Feature      Embedding      Image
 Vector         Vector        Vector
```

---

---

# Chapter 4 — Vector Operations

---

# 4.1 Why Do We Need Vector Operations?

In the previous chapter, we learned that a vector represents an object.

For example:

```text
Student A

[20, 9.1, 450, 92]
```

Suppose we have another student.

```text
Student B

[21, 8.8, 420, 88]
```

If vectors only stored information, they wouldn't be very useful.

The real power of vectors comes from performing **mathematical operations** on them.

These operations allow us to:

* Compare objects
* Measure similarity
* Transform data
* Train machine learning models
* Compute predictions
* Optimize neural networks

Every AI model performs millions or billions of vector operations every second.

---

# The Big Picture

```text
Objects

↓

Vectors

↓

Vector Operations

↓

Machine Learning

↓

Predictions
```

---

# Types of Vector Operations

In this chapter, we'll study:

1. Vector Addition
2. Vector Subtraction
3. Scalar Multiplication
4. Magnitude (Norm)
5. Unit Vector
6. Distance Between Vectors
7. Cosine Similarity (Intuition)

---

# 4.2 Vector Addition

---

## Why Do We Need It?

Imagine you're tracking sales over two weeks.

Week 1:

```text
[10, 20, 30]
```

Week 2:

```text
[5, 8, 10]
```

To find the total sales:

```text
Week1 + Week2
```

We add corresponding components.

---

## Definition

If

[
\mathbf{A}=[a_1,a_2,\dots,a_n]
]

and

[
\mathbf{B}=[b_1,b_2,\dots,b_n]
]

then

[
\mathbf{A+B}
============

[a_1+b_1,;
a_2+b_2,;
\dots,;
a_n+b_n]
]

---

## Example

```text
A = [2,4,6]

B = [1,3,5]
```

Add component-wise.

```text
[2+1,

4+3,

6+5]
```

Result

```text
[3,7,11]
```

---

## Visualization

```text
A

[2 4 6]

+

B

[1 3 5]

↓

[3 7 11]
```

Each position is added independently.

---

## Python

```python
A = [2,4,6]
B = [1,3,5]

result = []

for i in range(len(A)):
    result.append(A[i] + B[i])

print(result)
```

Output

```text
[3,7,11]
```

---

## NumPy Preview

```python
import numpy as np

A = np.array([2,4,6])
B = np.array([1,3,5])

print(A + B)
```

Output

```text
[3 7 11]
```

---

## AI Example

Suppose

Feature Vector

```text
[Age,
Experience,
Projects]
```

Two employees

```text
[20,2,5]

+

[21,3,6]
```

Adding vectors combines corresponding features mathematically.

Although simple addition is not always meaningful for raw features, vector addition is widely used in optimization algorithms, embedding arithmetic, and accumulated updates during training.

---

# Properties

Vector addition is:

✅ Commutative

```text
A+B=B+A
```

---

✅ Associative

```text
(A+B)+C

=

A+(B+C)
```

---

# Common Mistake

You cannot add vectors with different dimensions.

Example

```text
[1,2]

+

[3,4,5]
```

❌ Invalid

Dimensions must match.

---

# 4.3 Vector Subtraction

---

## Need

Suppose you want to know how much sales changed.

Yesterday

```text
[20,30,15]
```

Today

```text
[22,35,17]
```

Difference

```text
Today − Yesterday
```

---

## Definition

Subtract each component.

---

Example

```text
[5,8,10]

-

[2,3,5]

=

[3,5,5]
```

---

Visualization

```text
5−2=3

8−3=5

10−5=5
```

---

Python

```python
A = [5,8,10]
B = [2,3,5]

result = []

for i in range(len(A)):
    result.append(A[i]-B[i])

print(result)
```

---

NumPy

```python
A - B
```

---

## AI Example

Gradient Descent

During training

```text
New Weights

=

Old Weights

−

Learning Rate × Gradient
```

Subtraction is one of the most important operations in optimization.

---

# 4.4 Scalar Multiplication

---

## Why?

Suppose a teacher decides to award double marks.

Original

```text
[40,45,38]
```

Multiply by

```text
2
```

Result

```text
[80,90,76]
```

---

## Definition

Multiply every component by the scalar.

---

Example

```text
3 × [2,4,6]

↓

[6,12,18]
```

---

Visualization

```text
2

↓

6

4

↓

12

6

↓

18
```

---

Python

```python
A = [2,4,6]

result = []

for x in A:
    result.append(3*x)

print(result)
```

---

NumPy

```python
3 * A
```

---

## AI Example

Learning Rate

Gradient

```text
[0.2,0.8,0.5]
```

Learning rate

```text
0.01
```

Scaled Gradient

```text
0.01

×

Gradient
```

Every gradient update uses scalar multiplication.

---

# Common Mistake

Scalar multiplication

```text
3 × [2,4]
```

means

```text
[6,12]
```

It does **not** mean

```text
[2,4,2,4,2,4]
```

---

# 4.5 Magnitude (Norm)

---

## Why?

Suppose two students walked.

Student A

5 km

Student B

12 km

We want to know

**How long is the vector?**

This length is called the **magnitude** or **Euclidean norm**.

---

## Definition

For

[
\mathbf{v}
==========

[v_1,v_2,\dots,v_n]
]

Magnitude

[
||v||
=====

\sqrt{
v_1^2+
v_2^2+
\cdots+
v_n^2
}
]

---

## Example

```text
[3,4]
```

Magnitude

```text
√(3²+4²)

=

√25

=

5
```

---

Visualization

```text
        ● (3,4)

       /

      /

5

    /

   /

●-----------

     3
```

The vector's magnitude is the length of the hypotenuse.

---

## Python

```python
import math

v = [3,4]

length = math.sqrt(v[0]**2 + v[1]**2)

print(length)
```

Output

```text
5.0
```

---

## NumPy

```python
np.linalg.norm(v)
```

---

## AI Example

Embedding vectors often have different lengths.

Before comparing them, we frequently normalize them so that only their direction (semantic meaning) influences the comparison.

---

# 4.6 Unit Vector

---

## Need

Suppose two arrows point in exactly the same direction.

One is

10 meters.

Another is

100 meters.

Sometimes

we only care about the **direction**, not the length.

A **unit vector** keeps the direction but has a magnitude of **1**.

---

## Definition

For a non-zero vector (\mathbf{v}),

[
\hat{v}
=======

\frac{v}{||v||}
]

where (||v||) is the magnitude.

---

## Example

For

```text
v = [3,4]
```

Magnitude

```text
5
```

Unit vector

```text
[3/5,

4/5]

=

[0.6,

0.8]
```

Check its magnitude:

```text
√(0.6²+0.8²)

=

1
```

---

## AI Example

Embedding vectors are often normalized before similarity search.

This prevents larger vectors from appearing more important simply because of their length.

---

# Common Mistake

A unit vector is **not** any vector with small numbers.

The defining property is:

```text
Magnitude = 1
```

---

# 4.7 Distance Between Two Vectors

---

## Need

Suppose two customers have feature vectors.

Customer A

```text
[2,4]
```

Customer B

```text
[5,8]
```

How similar are they?

One basic measure is the straight-line distance.

---

## Formula

[
\text{Distance}
===============

\sqrt{
(x_1-y_1)^2
+
(x_2-y_2)^2
+
\cdots
}
]

---

## Example

Distance between

```text
[1,2]

and

[4,6]
```

```text
√((4−1)²+(6−2)²)

=

√(9+16)

=

5
```

---

## AI Example

Algorithms like **K-Nearest Neighbors (KNN)** compare feature vectors using distance.

Smaller distance usually indicates greater similarity.

---

# 4.8 Cosine Similarity (Intuition)

> **Note:** We'll study the mathematical details later. Here we'll focus on the intuition.

---

## Problem

Imagine two vectors.

```text
A

→

B

→
```

Both point in nearly the same direction.

They likely represent similar objects.

Now imagine

```text
A →

B ↓
```

Their directions differ greatly.

They are less similar.

---

Cosine similarity measures **how aligned two vectors are**, rather than how far apart they are.

---

## Example

Suppose we have word embeddings.

```text
King

↓

[0.5,0.2,0.9,...]
```

Queen

↓

```text
[0.48,0.21,0.88,...]
```

Their vectors point in similar directions.

Therefore, cosine similarity is high.

---

## AI Applications

Cosine similarity is widely used in:

* Semantic search
* Recommendation systems
* Sentence embeddings
* Document retrieval
* Vector databases
* Large Language Models

---

# Documentation Box

> **📖 NumPy Documentation Note**
> NumPy provides efficient vectorized operations for addition, subtraction, scaling, and norms through `numpy.ndarray` and functions such as `numpy.linalg.norm`. These operations are implemented in optimized C code, making them much faster than manual Python loops for large arrays.

> **📖 PyTorch Documentation Note**
> In PyTorch, vectors are represented as 1-dimensional tensors. Operations like addition, subtraction, multiplication, normalization, and similarity are performed directly on tensors, and PyTorch can compute gradients for these operations automatically using Autograd.

---

# Chapter Summary

In this chapter, we learned the fundamental operations performed on vectors:

* **Addition:** Combine corresponding components.
* **Subtraction:** Compute differences between vectors.
* **Scalar Multiplication:** Scale every component by the same number.
* **Magnitude (Norm):** Measure the length of a vector.
* **Unit Vector:** Preserve direction while setting length to 1.
* **Distance:** Measure how far apart two vectors are.
* **Cosine Similarity (Intuition):** Compare vectors based on direction.

These operations are the mathematical building blocks behind optimization algorithms, similarity search, recommendation systems, embeddings, and deep learning.

---

# Revision Sheet

```text
Vector Addition:
A + B

Vector Subtraction:
A - B

Scalar Multiplication:
k × A

Magnitude:
||A||

Unit Vector:
A / ||A||

Distance:
||A - B||

Cosine Similarity:
Measures directional similarity
```

---

# Interview Questions

1. Why can only vectors of the same dimension be added?
2. Explain vector addition with an example.
3. What is scalar multiplication?
4. What is the magnitude (norm) of a vector?
5. What is a unit vector and why is it useful?
6. How is Euclidean distance used in machine learning?
7. Why is cosine similarity preferred over Euclidean distance for many embedding-based applications?
8. How does gradient descent use vector subtraction and scalar multiplication?

---

# Practice Questions

### Basic

1. Compute:

```text
[2, 5] + [3, 1]
```

2. Compute:

```text
[8, 6] - [2, 4]
```

3. Compute:

```text
4 × [1, 3, 5]
```

---

### Intermediate

1. Find the magnitude of:

```text
[6, 8]
```

2. Convert the vector:

```text
[6, 8]
```

into a unit vector.

3. Find the Euclidean distance between:

```text
[2, 3]

and

[5, 7]
```

---

### Challenge

A recommendation system represents two movies as embedding vectors. Explain why cosine similarity may be a better measure than Euclidean distance when comparing their semantic similarity.

---

# Chapter 5 — Matrices

---

# 5.1 Why Were Matrices Invented?

In the previous chapter, we learned that a **vector** represents **one object**.

Example:

```text
Student A

[20, 9.1, 450, 92]
```

But what if we have **1000 students**?

Can we create 1000 separate vectors?

Yes.

But analyzing them individually becomes inefficient.

Instead, we organize all vectors into one mathematical object called a **matrix**.

---

## The Need

Suppose we have three students.

| Student | Age | CGPA | DSA Solved |
| ------- | --: | ---: | ---------: |
| A       |  20 |  9.1 |        450 |
| B       |  21 |  8.7 |        380 |
| C       |  19 |  9.4 |        520 |

Instead of storing

```text
Student A → [20,9.1,450]

Student B → [21,8.7,380]

Student C → [19,9.4,520]
```

We combine them into

```text
[
 [20,9.1,450],
 [21,8.7,380],
 [19,9.4,520]
]
```

This collection is called a **matrix**.

---

# Mental Model

Think of a matrix as a **container of vectors**.

```text
Vector

↓

Vector

↓

Vector

↓

Matrix
```

Every row is one vector.

---

# 5.2 Official Definition

A **matrix** is a rectangular arrangement of numbers organized into **rows** and **columns**.

Mathematically,

[
A=
\begin{bmatrix}
1&2&3\
4&5&6\
7&8&9
\end{bmatrix}
]

Each element has a unique position.

---

# 5.3 Rows and Columns

Consider

[
A=
\begin{bmatrix}
1&2&3\
4&5&6\
7&8&9
\end{bmatrix}
]

---

Rows

```text
Row 1

1 2 3

Row 2

4 5 6

Row 3

7 8 9
```

---

Columns

```text
Column 1

1

4

7
```

```text
Column 2

2

5

8
```

```text
Column 3

3

6

9
```

---

Visualization

```text
          Columns

        C1  C2  C3

      ┌──────────────┐

R1    │1   2   3     │

R2    │4   5   6     │

R3    │7   8   9     │

      └──────────────┘
```

---

# 5.4 Matrix Dimensions (Shape)

The size of a matrix is written as

```text
Rows × Columns
```

Example

```text
[
 [1,2,3],
 [4,5,6]
]
```

Rows

```text
2
```

Columns

```text
3
```

Shape

```text
2 × 3
```

---

Another example

```text
[
 [1],
 [2],
 [3],
 [4]
]
```

Rows

```text
4
```

Columns

```text
1
```

Shape

```text
4 × 1
```

---

# Common Shapes

```text
1×1

Scalar-like matrix
```

---

```text
1×5

Row vector
```

---

```text
5×1

Column vector
```

---

```text
3×3

Square matrix
```

---

```text
200×100

Typical dataset matrix
```

---

# Important

The shape determines

* valid operations
* memory layout
* compatibility with other matrices

---

# 5.5 Matrix Notation

Matrices are usually written using capital letters.

Example

[
A
]

[
B
]

[
W
]

Elements use subscripts.

Example

[
A_{12}
]

means

Row

```text
1
```

Column

```text
2
```

---

Example

[
A=
\begin{bmatrix}
5&8\
2&4
\end{bmatrix}
]

Then

```text
A11 = 5

A12 = 8

A21 = 2

A22 = 4
```

---

# 5.6 Matrix as Multiple Vectors

Consider

```text
[
 [2,4],
 [6,8],
 [1,3]
]
```

Each row is one vector.

```text
Vector 1

↓

[2,4]

Vector 2

↓

[6,8]

Vector 3

↓

[1,3]
```

A matrix is therefore a collection of vectors with the same dimension.

---

# 5.7 Matrix as a Dataset

Suppose we have customer data.

| Age | Income | Purchases |
| --: | -----: | --------: |
|  25 |  40000 |         6 |
|  31 |  60000 |         8 |
|  22 |  35000 |         3 |

The matrix representation is

```text
[
 [25,40000,6],
 [31,60000,8],
 [22,35000,3]
]
```

Interpretation

Rows

↓

Customers

Columns

↓

Features

---

Visualization

```text
             Features

        Age Income Purchases

Customer1

Customer2

Customer3
```

This is exactly how most machine learning datasets are organized.

---

# 5.8 Matrix as an Image

A grayscale image is also a matrix.

Example

```text
[
 [10,20,30],
 [50,80,90],
 [70,60,40]
]
```

Every number is a pixel intensity.

```text
0

↓

Black
```

```text
255

↓

White
```

Visualization

```text
10 20 30

50 80 90

70 60 40
```

Each position corresponds to one pixel.

---

# AI Example

MNIST digits

28 × 28

↓

Matrix

```text
28 rows

28 columns
```

Before feeding into some models, this matrix may be flattened into a 784-dimensional vector.

---

# 5.9 Matrix as a Table

Think of a spreadsheet.

```text
Student

Math

Science

English
```

This is simply

a matrix.

Rows

↓

Students

Columns

↓

Subjects

Many datasets begin life as spreadsheets before becoming matrices for machine learning.

---

# 5.10 Matrix as a Linear Transformation (Intuition)

So far, we've treated a matrix as a table of numbers.

There is another, deeper interpretation.

A matrix can represent a **transformation**.

Imagine a vector

```text
[2,3]
```

Multiplying it by a matrix can

* rotate it
* stretch it
* shrink it
* reflect it

This idea is fundamental in computer graphics, robotics, and neural networks.

We'll explore this in detail in the matrix multiplication chapter.

---

# 5.11 Python Representation

Nested lists are often used to represent matrices.

```python
A = [
    [1,2,3],
    [4,5,6]
]
```

However, Python lists are not optimized for matrix operations.

---

# 5.12 NumPy Representation

In AI, matrices are almost always stored using NumPy arrays.

```python
import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6]
])
```

Check the shape.

```python
print(A.shape)
```

Output

```text
(2, 3)
```

---

# 5.13 PyTorch Representation

```python
import torch

A = torch.tensor([
    [1,2,3],
    [4,5,6]
])
```

PyTorch stores the same mathematical object as a tensor.

A 2-dimensional tensor corresponds to a matrix.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> NumPy stores matrices as 2-dimensional `ndarray` objects. The `shape` attribute returns a tuple `(rows, columns)`, which determines how array operations are performed.

> **📖 PyTorch Documentation Note**
> PyTorch represents matrices as rank-2 tensors. Most neural network layers expect batched matrices or higher-dimensional tensors, making matrix operations central to deep learning.

---

# Common Misconceptions

### ❌ A matrix is just a table.

A table is one way to visualize a matrix.

A matrix is a mathematical object with well-defined operations and properties.

---

### ❌ Every matrix must be square.

No.

Examples:

```text
2×5

5×2

10×3
```

All are valid matrices.

---

### ❌ Every row can have a different number of columns.

No.

Every row must contain the same number of columns.

Otherwise, it is not a valid matrix.

---

### ❌ A matrix is different from a collection of vectors.

A matrix can be viewed as a collection of vectors arranged consistently.

---

# AI Connections

| AI Area                | Matrix Represents      |
| ---------------------- | ---------------------- |
| Machine Learning       | Dataset                |
| Deep Learning          | Weight matrix          |
| Computer Vision        | Image                  |
| NLP                    | Batch of embeddings    |
| Recommendation Systems | User-item interactions |
| Statistics             | Data matrix            |

---

# Chapter Summary

A matrix is:

* A rectangular arrangement of numbers.
* Organized into rows and columns.
* Often interpreted as a collection of vectors.
* Commonly used to represent datasets, images, weight matrices, and transformations.
* One of the most important mathematical structures in AI.

---

# Revision Sheet

```text
Scalar
   ↓
Vector
   ↓
Matrix
   ↓
Tensor
```

```text
Rows → Objects / Samples

Columns → Features
```

```text
Shape = Rows × Columns
```

---

# Interview Questions

1. What is a matrix?
2. What is the difference between a vector and a matrix?
3. What does the shape of a matrix represent?
4. Explain the difference between rows and columns.
5. Why are datasets represented as matrices?
6. How are grayscale images represented mathematically?
7. What does `A.shape` return in NumPy?
8. How does PyTorch represent matrices?

---

# Practice Questions

### Basic

1. Find the shape of:

```text
[
 [1,2],
 [3,4],
 [5,6]
]
```

2. Identify the number of rows and columns in:

```text
[
 [2,4,6,8]
]
```

3. What is the value of (A_{23}) in:

```text
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

---

### Intermediate

1. Represent the following dataset as a matrix:

| Height | Weight | Age |
| -----: | -----: | --: |
|    170 |     65 |  22 |
|    165 |     58 |  20 |
|    180 |     75 |  25 |

2. Explain why every row in a matrix must have the same number of columns.

---

### Challenge

A facial recognition system stores each face as a **512-dimensional embedding vector**. If there are **10,000 faces** in the database:

1. What is the shape of the matrix storing all face embeddings?
2. What does each row represent?
3. What does each column represent?

---

---

# Chapter 6 — Matrix Operations

In the previous chapter, we learned **what a matrix is**.

Now we'll answer a more important question:

> **What can we do with matrices?**

Just like numbers can be added, subtracted, and multiplied, matrices also support mathematical operations.

These operations form the mathematical backbone of:

* Machine Learning
* Deep Learning
* Computer Vision
* NLP
* Recommendation Systems
* Scientific Computing

Every neural network performs millions of matrix operations during training and inference.

---

# 6.1 Overview of Matrix Operations

In this chapter, we'll study:

1. Matrix Addition
2. Matrix Subtraction
3. Scalar Multiplication
4. Matrix Transpose
5. Zero Matrix
6. Identity Matrix
7. Diagonal Matrix
8. Matrix Multiplication (Introduction)

---

# 6.2 Matrix Addition

---

## Why Do We Need Matrix Addition?

Imagine two stores selling the same products.

### Store A Sales

| Laptop | Mouse | Keyboard |
| ------ | ----- | -------- |
| 20     | 35    | 15       |
| 18     | 42    | 19       |

Represented as

[
A=
\begin{bmatrix}
20&35&15\
18&42&19
\end{bmatrix}
]

---

### Store B Sales

[
B=
\begin{bmatrix}
5&10&4\
6&9&3
\end{bmatrix}
]

To find total sales,

we simply add corresponding entries.

---

## Definition

If

[
A=
[a_{ij}]
]

and

[
B=
[b_{ij}]
]

then

[
A+B
===

[a_{ij}+b_{ij}]
]

Every element is added with the element in the same position.

---

## Example

[
A=
\begin{bmatrix}
1&2\
3&4
\end{bmatrix}
]

[
B=
\begin{bmatrix}
5&6\
7&8
\end{bmatrix}
]

Addition

[
A+B=
\begin{bmatrix}
6&8\
10&12
\end{bmatrix}
]

---

## Visualization

```text
Matrix A

1  2
3  4

+

Matrix B

5  6
7  8

↓

6   8
10 12
```

Each position is processed independently.

---

## Python

```python
A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print(result)
```

Output

```text
[[6, 8], [10, 12]]
```

---

## NumPy

```python
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A + B)
```

---

## Important Rule

Both matrices **must have the same shape**.

Example

```text
2×3

+

2×3

✓ Valid
```

---

```text
2×3

+

3×2

✗ Invalid
```

---

## AI Example

During training,

two gradient matrices from different mini-batches might be accumulated before updating model parameters.

---

# Properties

Matrix addition is

✅ Commutative

[
A+B=B+A
]

---

✅ Associative

[
(A+B)+C=A+(B+C)
]

---

# Common Mistake

Students often think

```text
2×3

+

3×2
```

is possible.

It is **not**.

Shapes must be identical.

---

# 6.3 Matrix Subtraction

---

## Definition

Subtract corresponding elements.

---

Example

[
\begin{bmatrix}
7&8\
6&5
\end{bmatrix}
-------------

\begin{bmatrix}
1&2\
3&4
\end{bmatrix}
=============

\begin{bmatrix}
6&6\
3&1
\end{bmatrix}
]

---

Visualization

```text
7−1 = 6

8−2 = 6

6−3 = 3

5−4 = 1
```

---

Python

```python
A = [[7,8],[6,5]]
B = [[1,2],[3,4]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j]-B[i][j])
    result.append(row)

print(result)
```

---

NumPy

```python
A - B
```

---

## AI Example

Weight updates in gradient descent are fundamentally matrix subtraction operations.

---

# 6.4 Scalar Multiplication

---

## Definition

Multiply every element by the scalar.

---

Example

[
3
\begin{bmatrix}
1&2\
3&4
\end{bmatrix}
=============

\begin{bmatrix}
3&6\
9&12
\end{bmatrix}
]

---

Visualization

```text
1 → 3

2 → 6

3 → 9

4 → 12
```

---

Python

```python
A = [[1,2],[3,4]]

result = []

for row in A:
    new_row = []
    for value in row:
        new_row.append(3*value)
    result.append(new_row)

print(result)
```

---

NumPy

```python
3 * A
```

---

## AI Example

Learning rates scale gradient matrices before parameter updates.

---

# 6.5 Matrix Transpose

---

## Why Do We Need Transpose?

Sometimes

rows need to become columns.

Example

Dataset

```text
Students

↓

Rows
```

Sometimes algorithms require

```text
Features

↓

Rows
```

Transpose performs this conversion.

---

## Definition

Transpose swaps rows and columns.

Notation

[
A^T
]

---

Example

[
A=
\begin{bmatrix}
1&2&3\
4&5&6
\end{bmatrix}
]

Transpose

[
A^T=
\begin{bmatrix}
1&4\
2&5\
3&6
\end{bmatrix}
]

---

Visualization

```text
Original

1 2 3

4 5 6

↓

Transpose

1 4

2 5

3 6
```

---

## Shape Rule

If

```text
A

↓

m × n
```

then

```text
Aᵀ

↓

n × m
```

Example

```text
2×5

↓

5×2
```

---

## Python

```python
A = [
    [1,2,3],
    [4,5,6]
]

transpose = []

for j in range(len(A[0])):
    row = []
    for i in range(len(A)):
        row.append(A[i][j])
    transpose.append(row)

print(transpose)
```

---

## NumPy

```python
A.T
```

or

```python
np.transpose(A)
```

---

## AI Example

The transpose is used extensively in:

* Linear regression
* PCA
* Neural networks
* Attention mechanisms
* Covariance matrices

---

# Common Mistake

Transpose does **not** reverse numbers.

Example

Original

```text
1 2

3 4
```

Incorrect

```text
4 3

2 1
```

Correct

```text
1 3

2 4
```

Transpose swaps positions—it does not reverse order.

---

# 6.6 Zero Matrix

---

## Definition

A matrix whose every element is zero.

Example

[
\begin{bmatrix}
0&0\
0&0
\end{bmatrix}
]

---

## Properties

Adding a zero matrix changes nothing.

[
A+0=A
]

---

## NumPy

```python
np.zeros((3,4))
```

---

## AI Example

Zero matrices are commonly used to initialize arrays, buffers, masks, and accumulators.

---

# 6.7 Identity Matrix

---

## Need

The number

```text
1
```

has a special property.

[
5\times1=5
]

Matrices have an equivalent object.

It is called the **identity matrix**.

---

## Definition

Diagonal elements are

```text
1
```

All other elements

```text
0
```

Example

[
I=
\begin{bmatrix}
1&0&0\
0&1&0\
0&0&1
\end{bmatrix}
]

---

## Property

[
AI=IA=A
]

Multiplying by the identity matrix leaves the matrix unchanged.

---

## NumPy

```python
np.eye(3)
```

---

## AI Example

Identity matrices appear in:

* Linear algebra algorithms
* Matrix inversion
* Regularization
* Covariance computations

---

# Common Mistake

Identity matrix

≠

Matrix of all ones.

Correct

```text
1 0

0 1
```

Incorrect

```text
1 1

1 1
```

---

# 6.8 Diagonal Matrix

---

## Definition

Only diagonal elements may be non-zero.

Example

[
\begin{bmatrix}
5&0&0\
0&3&0\
0&0&9
\end{bmatrix}
]

---

Identity matrix is a special case of a diagonal matrix where every diagonal element equals **1**.

---

## NumPy

```python
np.diag([5,3,9])
```

---

## AI Example

Diagonal matrices are used in scaling transformations, covariance approximations, and feature weighting.

---

# 6.9 Matrix Multiplication (Introduction)

Matrix multiplication is the **most important operation in Linear Algebra**.

Unlike addition or subtraction,

matrix multiplication is **not performed element by element**.

Instead,

rows from the first matrix interact with columns from the second matrix.

We'll study the complete algorithm in the next chapter.

For now, remember:

```text
Addition

↓

Element-wise
```

```text
Multiplication

↓

Row × Column
```

This distinction is fundamental.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> Element-wise operations (`+`, `-`, `*`) work on arrays of identical shape. Matrix multiplication is performed using the `@` operator or `numpy.matmul()` and follows linear algebra rules rather than element-wise multiplication.

> **📖 PyTorch Documentation Note**
> PyTorch tensors support the same operations. Element-wise arithmetic uses operators like `+`, `-`, and `*`, while matrix multiplication uses `@` or `torch.matmul()`. PyTorch automatically tracks gradients for these operations during training.

---

# Chapter Summary

In this chapter, we learned:

* **Addition:** Add corresponding elements.
* **Subtraction:** Subtract corresponding elements.
* **Scalar Multiplication:** Multiply every element by the same scalar.
* **Transpose:** Swap rows and columns.
* **Zero Matrix:** The additive identity.
* **Identity Matrix:** The multiplicative identity.
* **Diagonal Matrix:** Only diagonal elements can be non-zero.
* **Matrix Multiplication (Preview):** Combines rows and columns, not individual elements.

These operations are essential for data preprocessing, optimization, neural networks, and numerical computing.

---

# Revision Sheet

```text
Matrix Addition
A + B

Matrix Subtraction
A - B

Scalar Multiplication
kA

Transpose
Aᵀ

Zero Matrix
All elements = 0

Identity Matrix
Diagonal = 1
Others = 0

Diagonal Matrix
Only diagonal entries may be non-zero

Matrix Multiplication
(Row) × (Column)
```

---

# Interview Questions

1. What condition is required for matrix addition?
2. Why is matrix subtraction only defined for matrices of the same shape?
3. What does matrix transpose do?
4. How does the shape change after transpose?
5. What is a zero matrix?
6. What is an identity matrix?
7. How is an identity matrix different from a diagonal matrix?
8. Why is matrix multiplication different from element-wise multiplication?
9. How do NumPy and PyTorch distinguish between element-wise multiplication and matrix multiplication?

---

# Practice Questions

### Basic

1. Compute:

[
\begin{bmatrix}
2&3\
4&5
\end{bmatrix}
+
\begin{bmatrix}
1&1\
2&2
\end{bmatrix}
]

2. Find:

[
2
\begin{bmatrix}
3&4\
5&6
\end{bmatrix}
]

3. Transpose:

[
\begin{bmatrix}
1&2&3\
4&5&6
\end{bmatrix}
]

---

### Intermediate

1. Explain why a **2 × 3** matrix cannot be added to a **3 × 2** matrix.
2. Construct a **4 × 4** identity matrix.
3. Give an example of a **3 × 3** diagonal matrix that is not an identity matrix.

---

### Challenge

Suppose a machine learning dataset contains **1,000 samples** with **50 features**.

1. What is the shape of the dataset matrix?
2. What will be the shape after taking its transpose?
3. What does each row and each column represent before and after the transpose?

---

---

# Chapter 7 — Dot Product

> **This is one of the most important concepts in AI.**

The dot product appears everywhere:

* Machine Learning
* Deep Learning
* Neural Networks
* Transformers
* Large Language Models
* Semantic Search
* Recommendation Systems
* Computer Vision

If you understand the dot product deeply, many AI algorithms become much easier to understand.

---

# 7.1 Why Do We Need the Dot Product?

Imagine you have two students.

Student A

```text
[Math = 90,
 Science = 80,
 English = 70]
```

Student B

```text
[Math = 92,
 Science = 81,
 English = 72]
```

Looking at these values, we naturally think:

> "These students are quite similar."

Now consider Student C.

```text
[Math = 20,
 Science = 95,
 English = 10]
```

Clearly,

Student A and Student C are much less similar.

**Question:**

How can a computer measure this mathematically?

The answer is the **dot product**.

---

# Big Picture

```text
Objects

↓

Vectors

↓

Dot Product

↓

Similarity

↓

AI Decision
```

---

# 7.2 What is the Dot Product?

The dot product combines two vectors into **one scalar value**.

Unlike vector addition,

the result is **not another vector**.

Example

```text
[2,3]

·

[4,5]

↓

23
```

The output is a single number.

---

# 7.3 Official Definition

Suppose

[
A=[a_1,a_2,\ldots,a_n]
]

and

[
B=[b_1,b_2,\ldots,b_n]
]

Then

[
A\cdot B
========

a_1b_1+a_2b_2+\cdots+a_nb_n
]

We:

1. Multiply corresponding components.
2. Add the products.

---

# 7.4 Step-by-Step Example

Let

```text
A = [2,3]

B = [4,5]
```

Multiply corresponding components.

```text
2 × 4 = 8

3 × 5 = 15
```

Add them.

```text
8 + 15 = 23
```

Therefore,

```text
A · B = 23
```

---

# Visualization

```text
A

[2    3]

↓

Multiply

↓

B

[4    5]

↓

(2×4)

+

(3×5)

↓

23
```

---

# Another Example

```text
A = [1,2,3]

B = [4,5,6]
```

Multiply

```text
1×4 = 4

2×5 = 10

3×6 = 18
```

Add

```text
4+10+18=32
```

Answer

```text
32
```

---

# 7.5 Why Does It Work?

The dot product rewards vectors whose corresponding components point in similar directions.

Consider

```text
A

[5,5]

B

[5,5]
```

Dot product

```text
5×5

+

5×5

=

50
```

Large value.

---

Now

```text
A

[5,-5]

B

[-5,5]
```

Dot product

```text
-25

+

-25

=

-50
```

Negative value.

This tells us the vectors point in opposite directions.

---

# Mental Model

Think of each component as casting a vote.

If both vectors agree,

the vote is positive.

If they disagree,

the vote becomes negative.

The final score is the total agreement.

---

# 7.6 Geometric Interpretation

The dot product has another beautiful meaning.

Imagine two arrows.

```text
        B

       ↗

      /

     /

----→---------

     A
```

If they point in nearly the same direction,

the dot product is large.

---

If

```text
A →

B ↓
```

they are perpendicular.

The dot product becomes

```text
0
```

---

If

```text
A →

← B
```

they point in opposite directions.

The dot product becomes negative.

---

# 7.7 Relationship with Angle

The geometric formula is

[
A\cdot B
========

||A||
||B||
\cos\theta
]

where

* (||A||) is the magnitude of (A)
* (||B||) is the magnitude of (B)
* (\theta) is the angle between them

---

# Three Important Cases

### Case 1

Same direction

```text
θ = 0°
```

Since

```text
cos(0)=1
```

Dot product is maximum.

---

### Case 2

Perpendicular

```text
θ = 90°
```

Since

```text
cos(90)=0
```

Dot product becomes

```text
0
```

---

### Case 3

Opposite direction

```text
θ =180°
```

Since

```text
cos(180)=-1
```

Dot product is negative.

---

# Visualization

```text
Same Direction

→ →

Large Positive

---------------

Perpendicular

→

↓

Zero

---------------

Opposite

→ ←

Negative
```

---

# 7.8 Python Implementation

```python
A = [2,3]
B = [4,5]

dot = 0

for i in range(len(A)):
    dot += A[i] * B[i]

print(dot)
```

Output

```text
23
```

---

# NumPy

```python
import numpy as np

A = np.array([2,3])
B = np.array([4,5])

print(np.dot(A,B))
```

Output

```text
23
```

---

# PyTorch

```python
import torch

A = torch.tensor([2,3])
B = torch.tensor([4,5])

print(torch.dot(A,B))
```

---

# 7.9 Dot Product in Machine Learning

Suppose

Weights

```text
[0.2,0.5,0.3]
```

Input Features

```text
[100,80,90]
```

Prediction

```text
Weights

·

Input
```

This single dot product computes the weighted combination of features.

Almost every linear model starts this way.

---

# 7.10 Dot Product in Neural Networks

A neuron receives

```text
Inputs

↓

Weights

↓

Dot Product

↓

Bias

↓

Activation
```

Visualization

```text
x₁ ----\
         \
x₂ -------> ●

x₃ ----/

      ↓

Dot Product

↓

Activation
```

Every neuron in a neural network computes a dot product before applying an activation function.

---

# 7.11 Dot Product in Recommendation Systems

Suppose

User embedding

```text
[0.9,0.2,0.8]
```

Movie embedding

```text
[0.8,0.1,0.9]
```

Large dot product

↓

High similarity

↓

Recommend movie.

---

# 7.12 Dot Product in Semantic Search

Sentence

```text
"Artificial Intelligence"
```

↓

Embedding

```text
[...]
```

Document

↓

Embedding

```text
[...]
```

Dot product

↓

Similarity score.

Higher score

↓

Better search result.

---

# 7.13 Dot Product in Large Language Models

Transformers use three vectors:

* Query (Q)
* Key (K)
* Value (V)

The first step of attention is

```text
Q

·

K
```

This measures how relevant one token is to another.

Without the dot product,

the attention mechanism cannot determine which words should influence each other.

---

# 7.14 Common Misconceptions

### ❌ Dot product returns a vector.

No.

It always returns a **scalar**.

---

### ❌ Dot product is the same as element-wise multiplication.

Example

```text
[2,3]

×

[4,5]
```

Element-wise multiplication

```text
[8,15]
```

Dot product

```text
8+15

=

23
```

Different operations.

---

### ❌ Dot product can be computed for vectors of different dimensions.

No.

The vectors must have the same number of components.

---

### ❌ A larger dot product always means the vectors are closer.

Not necessarily.

Longer vectors naturally produce larger dot products.

To compare **direction** rather than **length**, we often normalize vectors and use **cosine similarity**.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> `numpy.dot()` computes the dot product of two vectors. For higher-dimensional arrays, its behavior generalizes according to NumPy's array multiplication rules. For explicit matrix multiplication, prefer the `@` operator or `numpy.matmul()`.

> **📖 PyTorch Documentation Note**
> `torch.dot()` computes the dot product of two 1-dimensional tensors. During neural network training, PyTorch's Autograd automatically computes gradients through dot product operations.

---

# AI Connections

| AI Area                | Role of Dot Product      |
| ---------------------- | ------------------------ |
| Linear Regression      | Weighted sum of features |
| Logistic Regression    | Linear prediction        |
| Neural Networks        | Neuron computation       |
| Transformers           | Attention scores (Q·K)   |
| Semantic Search        | Similarity scoring       |
| Recommendation Systems | User-item similarity     |
| Embedding Models       | Vector comparison        |
| Computer Vision        | Feature matching         |

---

# Chapter Summary

The **dot product**:

* Combines two vectors into one scalar.
* Measures agreement between corresponding components.
* Has both an algebraic and geometric interpretation.
* Is fundamental to machine learning, neural networks, embeddings, recommendation systems, and transformers.
* Forms the basis for cosine similarity and attention mechanisms.

---

# Revision Sheet

```text
Dot Product

A · B

↓

Multiply corresponding components

↓

Add all products

↓

One Scalar
```

```text
Same Direction

↓

Large Positive

Perpendicular

↓

Zero

Opposite

↓

Negative
```

---

# Interview Questions

1. What is the dot product?
2. Why does the dot product return a scalar?
3. Explain the algebraic formula for the dot product.
4. What is the geometric interpretation of the dot product?
5. Why is the dot product zero for perpendicular vectors?
6. How is the dot product used in neural networks?
7. What role does the dot product play in transformers?
8. What is the difference between element-wise multiplication and the dot product?
9. Why are vectors often normalized before similarity comparisons?

---

# Practice Questions

### Basic

1. Compute:

```text
[2, 3] · [5, 4]
```

2. Compute:

```text
[1, 2, 3] · [4, 5, 6]
```

3. Explain why the result of a dot product is always a scalar.

---

### Intermediate

1. Explain why two perpendicular vectors have a dot product of zero.
2. Compare the results of element-wise multiplication and the dot product for the same pair of vectors.
3. Describe how a neuron uses the dot product to compute its output.

---

### Challenge

Suppose a search engine stores millions of document embeddings. A user query is converted into an embedding vector.

1. How can the dot product be used to rank documents?
2. Why might cosine similarity be preferred over the raw dot product?
3. How does this idea relate to semantic search in modern LLM-powered retrieval systems?

---

---

# Chapter 8 — Matrix × Vector Multiplication

> **This chapter is where Linear Algebra truly starts to power AI.**

Almost every machine learning model and every neural network layer performs **matrix × vector multiplication**.

If you understand this chapter, you'll understand the mathematical computation behind:

* Linear Regression
* Logistic Regression
* Neural Networks
* Computer Vision
* Transformers
* Large Language Models

---

# 8.1 Why Do We Need Matrix × Vector Multiplication?

Suppose a student has three features:

```text
Student

↓

[Age, CGPA, DSA Score]

↓

[20, 9.2, 450]
```

A machine learning model doesn't use these values directly.

It **transforms** them into a new representation.

How?

Using a matrix.

---

## Big Picture

```text
Input Features (Vector)

↓

Weight Matrix

↓

Matrix × Vector

↓

New Features

↓

Prediction
```

Every neural network layer follows this pipeline.

---

# 8.2 What is Matrix × Vector Multiplication?

A matrix transforms a vector into another vector.

Mathematically,

[
A \times x = y
]

where

* (A) → Matrix
* (x) → Input Vector
* (y) → Output Vector

Notice:

Input

↓

Vector

Output

↓

Vector

The matrix acts like a **machine** that transforms the input.

---

# 8.3 Why Must Dimensions Match?

Consider

[
A=
\begin{bmatrix}
1&2&3\
4&5&6
\end{bmatrix}
]

Shape

```text
2 × 3
```

Input vector

[
x=
\begin{bmatrix}
7\
8\
9
\end{bmatrix}
]

Shape

```text
3 × 1
```

The multiplication is valid because

```text
Columns of Matrix

↓

3

=

Rows of Vector

↓

3
```

General Rule

```text
(m × n)

×

(n × 1)

↓

(m × 1)
```

---

# Memory Trick

```text
Rows × Columns

↓

(2 × 3)

×

(3 × 1)

↓

Middle Numbers Match

✓ Valid
```

If the middle numbers don't match,

the multiplication is impossible.

---

# 8.4 Step-by-Step Example

Matrix

[
A=
\begin{bmatrix}
1&2&3\
4&5&6
\end{bmatrix}
]

Vector

[
x=
\begin{bmatrix}
7\
8\
9
\end{bmatrix}
]

---

## Step 1

Take the first row.

```text
1  2  3
```

Multiply with the vector.

```text
1×7

+

2×8

+

3×9
```

Compute.

```text
7

+

16

+

27

=

50
```

First output

```text
50
```

---

## Step 2

Take the second row.

```text
4 5 6
```

Multiply.

```text
4×7

+

5×8

+

6×9
```

Compute.

```text
28

+

40

+

54

=

122
```

Second output

```text
122
```

Final answer

[
\begin{bmatrix}
50\
122
\end{bmatrix}
]

---

# Visualization

```text
Matrix

1 2 3
4 5 6

×

Vector

7
8
9

↓

Output

50
122
```

Each row produces exactly one output value.

---

# 8.5 Mental Model

Think of every row as asking a question about the input vector.

Row 1

```text
How much of Feature1,

Feature2,

Feature3
should contribute?
```

Row 2 asks a different question.

Each row produces one answer.

Those answers become the new vector.

---

# 8.6 Why Does Each Row Produce One Output?

Suppose

Matrix

```text
3 rows
```

Each row computes one dot product.

```text
Row 1

·

Vector

↓

One Number
```

```text
Row 2

·

Vector

↓

One Number
```

```text
Row 3

·

Vector

↓

One Number
```

Therefore,

three rows produce

three output numbers.

---

# Key Insight

**Matrix × Vector multiplication is simply multiple dot products.**

If the matrix has (m) rows,

it performs (m) dot products,

one for each row.

---

# 8.7 Python Implementation

```python
A = [
    [1,2,3],
    [4,5,6]
]

x = [7,8,9]

result = []

for row in A:
    total = 0
    for i in range(len(x)):
        total += row[i] * x[i]
    result.append(total)

print(result)
```

Output

```text
[50, 122]
```

---

# NumPy Implementation

```python
import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6]
])

x = np.array([7,8,9])

print(A @ x)
```

Output

```text
[50 122]
```

---

# PyTorch Implementation

```python
import torch

A = torch.tensor([
    [1,2,3],
    [4,5,6]
])

x = torch.tensor([7,8,9])

print(A @ x)
```

---

# 8.8 Matrix as a Transformation

Previously,

the vector represented

```text
Student

↓

[20,9.2,450]
```

After multiplication

```text
↓

[18.4,

71.3]
```

The meaning has changed.

The matrix has transformed the original feature space into a new feature space.

This idea is called a **linear transformation**.

---

# Visualization

```text
Original Vector

↓

[20,9.2,450]

↓

Weight Matrix

↓

Transformation

↓

New Vector
```

The output vector is a new representation of the same object.

---

# 8.9 Matrix × Vector in Machine Learning

Linear Regression

Prediction

[
y = Wx + b
]

where

* (W) → Weight Matrix
* (x) → Feature Vector
* (b) → Bias

The multiplication (Wx) computes the weighted combination of features.

---

# 8.10 Matrix × Vector in Neural Networks

A neuron computes

```text
Input

↓

Weights

↓

Dot Product

↓

Bias

↓

Activation
```

A layer of many neurons computes

```text
Weight Matrix

×

Input Vector

↓

Output Vector
```

Instead of one neuron,

many neurons work simultaneously.

---

# Visualization

```text
Input Features

x₁
x₂
x₃

↓

Weight Matrix

↓

Hidden Layer Outputs

h₁
h₂
h₃
h₄
```

Each hidden neuron corresponds to one row of the weight matrix.

---

# 8.11 Why GPUs Love Matrix Operations

Suppose

1000 neurons

1000 input features

Instead of computing

```text
1000 separate dot products
```

the GPU performs one optimized matrix × vector multiplication.

This is why deep learning libraries rely heavily on highly optimized linear algebra libraries (such as BLAS and cuBLAS).

---

# 8.12 Common Misconceptions

### ❌ Matrix × Vector multiplication is element-wise multiplication.

No.

Element-wise multiplication:

```text
[2,3]

×

[4,5]

↓

[8,15]
```

Matrix × Vector multiplication:

```text
Dot Product

↓

One Output

↓

Repeat for every row
```

---

### ❌ The output has the same size as the input.

Not always.

Example

```text
(5 × 3)

×

(3 × 1)

↓

(5 × 1)
```

The output size depends on the **number of rows** in the matrix.

---

### ❌ Each matrix element becomes one output.

No.

Each **row** becomes one output value.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> The `@` operator (or `numpy.matmul()`) performs matrix multiplication following linear algebra rules. For a matrix of shape `(m, n)` and a vector of shape `(n,)`, the output has shape `(m,)`.

> **📖 PyTorch Documentation Note**
> `torch.matmul()` and the `@` operator perform matrix-vector multiplication efficiently on CPUs and GPUs. During training, Autograd computes gradients through these operations automatically.

---

# AI Connections

| AI Area                | Matrix × Vector Represents                            |
| ---------------------- | ----------------------------------------------------- |
| Linear Regression      | Feature transformation                                |
| Logistic Regression    | Weighted prediction                                   |
| Neural Networks        | One complete layer                                    |
| CNN                    | Convolution can be expressed as matrix multiplication |
| Recommendation Systems | User embedding transformation                         |
| NLP                    | Token embedding projection                            |
| Transformers           | Query, Key, and Value projections                     |

---

# Chapter Summary

Matrix × Vector multiplication:

* Transforms one vector into another vector.
* Is valid only when the matrix's columns equal the vector's dimensions.
* Computes one dot product per row of the matrix.
* Forms the mathematical foundation of machine learning models and neural network layers.
* Is highly optimized in libraries such as NumPy and PyTorch for efficient computation.

---

# Revision Sheet

```text
Matrix (m × n)

×

Vector (n × 1)

↓

Output (m × 1)
```

```text
Each Row

↓

One Dot Product

↓

One Output Value
```

```text
Matrix × Vector

=

Many Dot Products
```

---

# Interview Questions

1. What condition must hold for matrix × vector multiplication?
2. Why does each row produce one output value?
3. Explain matrix × vector multiplication using the dot product.
4. Why is matrix × vector multiplication called a linear transformation?
5. How is matrix × vector multiplication used in a neural network layer?
6. What is the output shape of an (m \times n) matrix multiplied by an (n \times 1) vector?
7. Why are GPUs optimized for matrix operations?

---

# Practice Questions

### Basic

1. Compute:

[
\begin{bmatrix}
2 & 1 \
3 & 4
\end{bmatrix}
\begin{bmatrix}
5 \
6
\end{bmatrix}
]

2. Determine whether the following multiplication is valid:

* Matrix: (3 \times 4)
* Vector: (4 \times 1)

3. Determine the output shape of:

* Matrix: (5 \times 2)
* Vector: (2 \times 1)

---

### Intermediate

1. Explain why a (2 \times 3) matrix cannot multiply a (2 \times 1) vector.
2. Show how matrix × vector multiplication is equivalent to computing multiple dot products.

---

### Challenge

A neural network layer has:

* **128 input features**
* **64 neurons**

1. What is the shape of the weight matrix?
2. If the input is a (128 \times 1) vector, what is the shape of the output?
3. Explain why each neuron corresponds to one row of the weight matrix.

---

---

# Chapter 9 — Matrix × Matrix Multiplication

> **Matrix × Matrix Multiplication is the single most important computation in modern AI.**

Every deep learning framework—NumPy, PyTorch, TensorFlow, JAX—spends most of its execution time performing matrix multiplication.

If you've heard terms like:

* GPU Acceleration
* CUDA
* Tensor Cores
* BLAS
* cuBLAS

they all exist primarily to make **matrix multiplication faster**.

---

# 9.1 Why Do We Need Matrix × Matrix Multiplication?

Suppose a neural network has two layers.

```text
Input Features

↓

Layer 1

↓

Hidden Features

↓

Layer 2

↓

Output
```

Layer 1 transforms the data.

Layer 2 transforms it again.

Instead of applying these transformations separately every time, mathematics allows us to combine them into one equivalent transformation using **matrix × matrix multiplication**.

---

# Big Picture

```text
Input

↓

Matrix A

↓

Intermediate Representation

↓

Matrix B

↓

Output
```

This is equivalent to:

```text
Input

↓

(B × A)

↓

Output
```

The combined matrix performs both transformations together.

---

# 9.2 What is Matrix × Matrix Multiplication?

Suppose

[
A
=

\begin{bmatrix}
1 & 2\
3 & 4
\end{bmatrix}
]

and

[
B
=

\begin{bmatrix}
5 & 6\
7 & 8
\end{bmatrix}
]

Their product

[
AB
]

is another matrix.

Unlike addition,

matrix multiplication is **not element-wise**.

Each output element is computed using a **row from the first matrix** and a **column from the second matrix**.

---

# 9.3 Dimension Rule

Suppose

```text
A

↓

m × n
```

and

```text
B

↓

n × p
```

Then

```text
AB

↓

m × p
```

---

## Memory Trick

```text
(m × n)

×

(n × p)

↓

(m × p)
```

The **middle numbers must match**.

---

## Examples

### Example 1

```text
2 × 3

×

3 × 4

↓

2 × 4

✓ Valid
```

---

### Example 2

```text
5 × 10

×

10 × 7

↓

5 × 7

✓ Valid
```

---

### Example 3

```text
3 × 4

×

2 × 5

✗ Invalid
```

Because

```text
4 ≠ 2
```

---

# 9.4 Why Must the Inner Dimensions Match?

Consider

```text
Matrix

↓

2 × 3
```

Each row contains

```text
3 numbers
```

Now suppose the second matrix has

```text
2 rows
```

A row with 3 numbers cannot compute a dot product with a column containing only 2 numbers.

A dot product requires vectors of equal length.

Therefore,

the inner dimensions must be identical.

---

# 9.5 Step-by-Step Example

Let

[
A=
\begin{bmatrix}
1&2\
3&4
\end{bmatrix}
]

[
B=
\begin{bmatrix}
5&6\
7&8
\end{bmatrix}
]

---

## Step 1

Compute first row × first column.

```text
1×5

+

2×7

=

5+14

=

19
```

---

## Step 2

First row × second column.

```text
1×6

+

2×8

=

6+16

=

22
```

---

## Step 3

Second row × first column.

```text
3×5

+

4×7

=

15+28

=

43
```

---

## Step 4

Second row × second column.

```text
3×6

+

4×8

=

18+32

=

50
```

---

Final Answer

[
AB=
\begin{bmatrix}
19&22\
43&50
\end{bmatrix}
]

---

# Visualization

```text
Row 1

↓

●

Column 1

↓

19

---------------

Row 1

↓

●

Column 2

↓

22

---------------

Row 2

↓

●

Column 1

↓

43

---------------

Row 2

↓

●

Column 2

↓

50
```

Every output element is one **dot product**.

---

# 9.6 General Algorithm

For every row in Matrix A:

* Visit every column in Matrix B.
* Compute their dot product.
* Store the result in the output matrix.

This process continues until every row-column pair has been processed.

---

# 9.7 Mental Model

Think of the first matrix as asking questions.

Think of the second matrix as providing answers.

Each row asks:

> "How should I combine the information in this column?"

Each row-column interaction produces one value in the result.

---

# 9.8 Matrix × Matrix = Many Dot Products

Suppose

```text
Matrix A

↓

3 rows
```

Matrix B

```text
↓

4 columns
```

Output

```text
3 × 4
```

How many dot products?

```text
3 × 4

=

12
```

General Rule

```text
Rows of A

×

Columns of B

=

Number of Dot Products
```

---

# 9.9 Python Implementation

```python
A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

result = [[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print(result)
```

Output

```text
[[19, 22], [43, 50]]
```

---

# NumPy Implementation

```python
import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A @ B)
```

Output

```text
[[19 22]
 [43 50]]
```

---

# PyTorch Implementation

```python
import torch

A = torch.tensor([
    [1,2],
    [3,4]
])

B = torch.tensor([
    [5,6],
    [7,8]
])

print(A @ B)
```

---

# 9.10 Matrix Multiplication as Composition of Transformations

Suppose

Matrix A

```text
Input

↓

Rotate
```

Matrix B

```text
↓

Scale
```

Applying both

```text
Rotate

↓

Scale
```

is equivalent to

```text
(B × A)
```

One matrix can represent both transformations together.

This idea is called **composition of linear transformations**.

---

# Visualization

```text
Input

↓

Rotate

↓

Scale

↓

Output

===================

Equivalent To

Input

↓

Combined Matrix

↓

Output
```

---

# 9.11 Matrix Multiplication in Neural Networks

Suppose a neural network layer has

* 128 input features
* 64 neurons

Weight matrix

```text
64 × 128
```

Input

```text
128 × 1
```

Output

```text
64 × 1
```

Now imagine

100 layers.

The network performs matrix multiplication repeatedly.

Training a modern AI model involves billions or trillions of these operations.

---

# 9.12 Matrix Multiplication in Transformers

Transformers repeatedly compute

```text
Q = XWQ

K = XWK

V = XWV
```

where

* (X) is the input embedding matrix.
* (W_Q), (W_K), and (W_V) are learned weight matrices.

Every one of these computations is a matrix multiplication.

---

# 9.13 Why GPUs Are So Fast

A CPU executes a small number of operations very quickly.

A GPU executes thousands of matrix multiplication operations simultaneously.

Modern GPUs include specialized hardware called **Tensor Cores**, designed specifically for high-throughput matrix multiplication used in deep learning.

This is why GPU acceleration dramatically speeds up AI workloads.

---

# 9.14 Matrix Multiplication is Not Commutative

For numbers,

```text
2 × 3 = 3 × 2
```

For matrices,

```text
AB

≠

BA
```

In many cases,

(BA) is either a different matrix or not defined at all.

---

## Example

Let

[
A=
\begin{bmatrix}
1&2\
3&4
\end{bmatrix},
\quad
B=
\begin{bmatrix}
2&0\
1&2
\end{bmatrix}
]

Then

[
AB=
\begin{bmatrix}
4&4\
10&8
\end{bmatrix}
]

while

[
BA=
\begin{bmatrix}
2&4\
7&10
\end{bmatrix}
]

Clearly,

[
AB \neq BA
]

---

# Common Misconceptions

### ❌ Matrix multiplication is element-wise multiplication.

False.

Each output element comes from a **row-column dot product**, not from multiplying elements in the same position.

---

### ❌ Matrix multiplication is commutative.

False.

Generally,

```text
AB ≠ BA
```

---

### ❌ The output has the same shape as the input matrices.

False.

The output shape is

```text
Rows of First Matrix

×

Columns of Second Matrix
```

---

### ❌ Any two matrices can be multiplied.

False.

The number of columns in the first matrix must equal the number of rows in the second matrix.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> Use the `@` operator or `numpy.matmul()` for matrix multiplication. NumPy follows standard linear algebra rules: if `A` has shape `(m, n)` and `B` has shape `(n, p)`, then `A @ B` has shape `(m, p)`.

> **📖 PyTorch Documentation Note**
> `torch.matmul()` supports matrix-matrix, matrix-vector, and batched matrix multiplication. These operations are heavily optimized and form the computational core of neural network training on CPUs and GPUs.

---

# AI Connections

| AI Area                | Matrix × Matrix Role                                  |
| ---------------------- | ----------------------------------------------------- |
| Deep Learning          | Layer-to-layer transformations                        |
| Transformers           | Q, K, V projections                                   |
| CNNs                   | Convolution can be expressed as matrix multiplication |
| PCA                    | Projection onto principal components                  |
| Recommendation Systems | Embedding transformations                             |
| Computer Vision        | Image feature transformations                         |
| Scientific Computing   | Solving systems of equations                          |

---

# Chapter Summary

Matrix × Matrix multiplication:

* Combines two linear transformations into one.
* Requires the inner dimensions to match.
* Produces an output whose shape is determined by the outer dimensions.
* Computes one dot product for every row-column pair.
* Is the dominant computation in modern AI systems and is highly optimized on GPUs.

---

# Revision Sheet

```text
Matrix A (m × n)

×

Matrix B (n × p)

↓

Output Matrix (m × p)
```

```text
Each Output Element

↓

Row of A

·

Column of B

↓

One Dot Product
```

```text
Matrix × Matrix

=

Many Matrix × Vector Operations

=

Many Dot Products
```

---

# Interview Questions

1. What condition must hold for matrix × matrix multiplication?
2. Why must the inner dimensions match?
3. Explain why each output element is a dot product.
4. Why is matrix multiplication not commutative?
5. What determines the shape of the output matrix?
6. How is matrix multiplication used in neural networks?
7. Why are GPUs optimized for matrix multiplication?
8. What role does matrix multiplication play in transformer models?

---

# Practice Questions

### Basic

1. Compute:

[
\begin{bmatrix}
1 & 2 \
3 & 4
\end{bmatrix}
\begin{bmatrix}
2 & 0 \
1 & 2
\end{bmatrix}
]

2. Determine whether the following multiplication is valid:

* (4 \times 5) × (5 \times 2)
* (3 \times 4) × (2 \times 6)

3. Find the output shape of:

* (6 \times 8) × (8 \times 10)

---

### Intermediate

1. Explain why the result of matrix multiplication is a new transformation.
2. Show how matrix × matrix multiplication can be viewed as repeated dot products.

---

### Challenge

A transformer layer receives an input embedding matrix of shape **(512 × 768)**. It multiplies this matrix by a weight matrix of shape **(768 × 1024)**.

1. Is the multiplication valid?
2. What is the shape of the output matrix?
3. Explain what this transformation represents in the context of a neural network.

---
---

# Chapter 10 — Tensors

> **Tensors are the universal data structure of modern AI.**

Everything processed by PyTorch, TensorFlow, and JAX is represented as a **tensor**.

If you understand scalars, vectors, and matrices, then tensors are simply the next logical step.

---

# 10.1 Why Do We Need Tensors?

So far we've learned:

```text
Scalar

↓

One Number
```

```text
Vector

↓

One List of Numbers
```

```text
Matrix

↓

Table of Numbers
```

But AI often deals with more complex data.

Examples:

* A color image
* A video
* A batch of images
* A batch of sentences
* Multiple batches during training

A matrix is no longer sufficient.

We need a more general mathematical object.

That object is called a **tensor**.

---

# Big Picture

```text
Scalar

↓

Vector

↓

Matrix

↓

Tensor
```

A tensor generalizes all previous objects.

---

# 10.2 Official Definition

A **tensor** is a mathematical object that generalizes:

* Scalars
* Vectors
* Matrices

to **any number of dimensions**.

Instead of stopping at two dimensions,

tensors can have

* 3 dimensions
* 4 dimensions
* 5 dimensions
* even 100 dimensions

---

# Mental Model

Imagine building with boxes.

```text
One Box

↓

Scalar
```

```text
Many Boxes in a Line

↓

Vector
```

```text
Many Lines

↓

Matrix
```

```text
Many Matrices

↓

Tensor
```

Every step adds one more dimension.

---

# 10.3 Tensor Hierarchy

```text
Rank 0

↓

Scalar

↓

Rank 1

↓

Vector

↓

Rank 2

↓

Matrix

↓

Rank 3+

↓

Tensor
```

---

# Important Terminology

In mathematics,

the word **tensor** technically includes scalars, vectors, and matrices.

In deep learning,

people usually say

> "tensor"

when they mean

**rank 3 or higher**

or simply

**any multidimensional array**.

---

# 10.4 Tensor Rank

The **rank** of a tensor is the number of axes (dimensions).

Examples

---

## Rank 0

```text
5
```

One value

↓

Scalar

---

## Rank 1

```text
[2,4,6]
```

One axis

↓

Vector

---

## Rank 2

```text
[
 [1,2],
 [3,4]
]
```

Two axes

↓

Matrix

---

## Rank 3

```text
[
 Matrix 1,

 Matrix 2
]
```

Three axes

↓

Tensor

---

## Rank 4

Imagine

```text
Batch

↓

Images

↓

Rows

↓

Columns
```

Four dimensions.

---

# Visualization

```text
Rank 0

●

↓

Rank 1

● ● ● ●

↓

Rank 2

● ● ●

● ● ●

↓

Rank 3

Matrix

Matrix

Matrix

↓

Rank 4

Tensor

Tensor

Tensor
```

---

# 10.5 Tensor Shape

Just like matrices have shapes,

tensors also have shapes.

Example

```text
Shape

↓

(3,)
```

Means

```text
Vector

↓

3 elements
```

---

```text
Shape

↓

(2,3)
```

Means

```text
2 rows

3 columns
```

---

```text
Shape

↓

(4,3,2)
```

Means

```text
4 matrices

Each matrix

↓

3 rows

↓

2 columns
```

---

# Reading Shapes

Example

```text
(5, 28, 28)
```

Interpretation

```text
5 Images

↓

Each image

↓

28 Rows

↓

28 Columns
```

---

Example

```text
(64, 3, 224, 224)
```

Interpretation

```text
64 Images

↓

3 Channels

↓

224 Rows

↓

224 Columns
```

This is a common shape used in computer vision.

---

# 10.6 Tensor Examples in AI

---

## Image

Grayscale image

```text
28 × 28
```

Shape

```text
(28,28)
```

Rank

```text
2
```

---

## Color Image

Three channels

* Red
* Green
* Blue

Shape

```text
(3,224,224)
```

Rank

```text
3
```

---

## Batch of Images

Suppose

32 images

Shape

```text
(32,3,224,224)
```

Rank

```text
4
```

---

## Video

Suppose

* 100 frames
* RGB
* Height
* Width

Shape

```text
(100,3,224,224)
```

Rank

```text
4
```

If we process multiple videos simultaneously:

```text
(Batch, Frames, Channels, Height, Width)
```

Example:

```text
(8,100,3,224,224)
```

Rank

```text
5
```

---

# 10.7 Tensor Dimensions

Consider

```text
Shape

↓

(8,100,3,224,224)
```

Interpretation

```text
Dimension 1

↓

8 Videos

Dimension 2

↓

100 Frames

Dimension 3

↓

RGB Channels

Dimension 4

↓

Height

Dimension 5

↓

Width
```

Each number represents the size along one axis.

---

# 10.8 NumPy Representation

```python
import numpy as np

tensor = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(tensor.shape)
```

Output

```text
(2,2,2)
```

Meaning

```text
2 Matrices

↓

2 Rows

↓

2 Columns
```

---

# 10.9 PyTorch Representation

```python
import torch

tensor = torch.tensor([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(tensor.shape)
```

Output

```text
torch.Size([2,2,2])
```

PyTorch uses tensors as its primary data structure.

---

# 10.10 Why Deep Learning Uses Tensors

Suppose we train a CNN.

Input

```text
32 Images

↓

RGB

↓

224 × 224
```

Shape

```text
(32,3,224,224)
```

A matrix cannot represent this.

Only a tensor can.

---

Suppose we train an LLM.

Input

```text
Batch

↓

Sentence

↓

Embedding
```

Shape

```text
(64,512,768)
```

Interpretation

```text
64 Sentences

↓

512 Tokens

↓

768 Features
```

Again,

only tensors can represent this efficiently.

---

# 10.11 Tensor Operations

Most operations we learned for vectors and matrices extend naturally to tensors.

Examples:

* Addition
* Subtraction
* Scalar multiplication
* Matrix multiplication (on the appropriate dimensions)
* Transpose (generalized as permutation of axes)
* Reshape
* Slicing
* Broadcasting

These are heavily optimized in AI libraries.

---

# 10.12 Common Misconceptions

### ❌ Tensor means only 3D.

No.

A tensor can have

* 0 dimensions
* 1 dimension
* 2 dimensions
* or many dimensions.

---

### ❌ Every tensor represents an image.

No.

Tensors can represent:

* Images
* Videos
* Audio
* Text embeddings
* Time-series
* Sensor readings
* Model parameters

---

### ❌ Tensor and NumPy array are the same.

Not exactly.

A NumPy array stores numerical data efficiently.

A PyTorch tensor is similar but also supports:

* Automatic differentiation (Autograd)
* GPU acceleration
* Deep learning operations

---

### ❌ Rank and shape are the same.

No.

Example

```text
Shape

↓

(64,512,768)
```

Rank

```text
3
```

Shape tells you the size of each dimension.

Rank tells you the number of dimensions.

---

# Documentation Box

> **📖 NumPy Documentation Note**
> NumPy stores multidimensional data using `ndarray`. Arrays can have any number of dimensions, described by their `shape` and `ndim` attributes.

> **📖 PyTorch Documentation Note**
> In PyTorch, every piece of data is stored as a `torch.Tensor`. Tensors support CPU/GPU computation, automatic differentiation, broadcasting, reshaping, and optimized mathematical operations.

---

# AI Connections

| AI Area                | Tensor Represents             |
| ---------------------- | ----------------------------- |
| Computer Vision        | Images, batches of images     |
| NLP                    | Token embeddings              |
| Transformers           | Attention tensors             |
| Speech Recognition     | Spectrograms                  |
| Reinforcement Learning | Environment states            |
| Deep Learning          | Model parameters              |
| LLMs                   | Hidden states and activations |

---

# Chapter Summary

A tensor:

* Generalizes scalars, vectors, and matrices.
* Can have any number of dimensions.
* Is described by its **rank** and **shape**.
* Is the fundamental data structure used by NumPy, PyTorch, TensorFlow, and JAX.
* Represents nearly all data used in modern AI systems.

---

# Revision Sheet

```text
Rank 0

↓

Scalar

↓

Rank 1

↓

Vector

↓

Rank 2

↓

Matrix

↓

Rank 3+

↓

Tensor
```

```text
Rank

↓

Number of Dimensions

Shape

↓

Size Along Each Dimension
```

```text
Examples

(3,)            → Vector
(2,3)           → Matrix
(3,224,224)     → Color Image
(32,3,224,224)  → Batch of Images
(64,512,768)    → Batch of Token Embeddings
```

---

# Interview Questions

1. What is a tensor?
2. How does a tensor generalize vectors and matrices?
3. What is the difference between rank and shape?
4. What is the shape of a batch of 32 RGB images of size 224 × 224?
5. Why are tensors essential for deep learning?
6. What advantages do PyTorch tensors have over NumPy arrays?
7. Give three real-world AI examples where tensors are used.

---

# Practice Questions

### Basic

1. What is the rank of a tensor with shape:

```text
(10,)
```

2. What is the rank of:

```text
(64,3,224,224)
```

3. Explain the difference between rank and shape.

---

### Intermediate

1. Interpret the tensor shape:

```text
(16,128,768)
```

2. Explain why a color image is naturally represented as a rank-3 tensor.

---

### Challenge

A transformer processes a batch of **32 sentences**.

Each sentence contains **128 tokens**.

Each token is represented by a **768-dimensional embedding**.

1. What is the shape of the input tensor?
2. What is its rank?
3. What does each dimension represent?

---

