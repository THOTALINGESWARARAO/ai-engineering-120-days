# Day 12 — Pandas Fundamentals


# Introduction

Data rarely comes in perfect mathematical arrays.

Instead, real-world datasets look like this:

| Name | Age | Salary | City |
|------|------|---------|------|
| Alice | 25 | 50000 | Delhi |
| Bob | 30 | 65000 | Mumbai |
| Charlie | 28 | 72000 | Hyderabad |

Unlike NumPy arrays, every column has meaning.

Each row represents one observation.

Each column represents one feature.

This is exactly the type of data pandas was designed to handle.

Today, pandas is the standard library used for:

- Data Analysis
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning preprocessing

Almost every ML project begins with pandas.

---

# Why Pandas?

Imagine we only have NumPy.

```python
import numpy as np

data = np.array([
    [25,50000],
    [30,65000],
    [28,72000]
])
```

Looking at this array:

```
[[25 50000]
 [30 65000]
 [28 72000]]
```

Questions immediately arise:

- Which column is Age?
- Which column is Salary?
- Which row belongs to Alice?

NumPy stores values efficiently but does not provide labels.

Now consider pandas:

```python
import pandas as pd

df = pd.DataFrame({
    "Age":[25,30,28],
    "Salary":[50000,65000,72000]
})
```

Output

```
   Age  Salary
0   25   50000
1   30   65000
2   28   72000
```

The data now has structure.

Columns have names.

Rows have labels.

Data becomes self-descriptive.

---

# Mental Model

Think of NumPy as mathematics.

```
Numbers
↓

Efficient Computation
```

Think of pandas as spreadsheets.

```
Rows
Columns
Labels
Missing Values
Data Cleaning
```

---

# Where Pandas Fits in Machine Learning

Typical ML Pipeline

```
CSV / Database
        │
        ▼
     pandas
        │
        ▼
Cleaning Missing Values
        │
        ▼
Feature Engineering
        │
        ▼
Encoding
Scaling
        │
        ▼
NumPy
        │
        ▼
scikit-learn / PyTorch
        │
        ▼
Model Training
```

Pandas is rarely the library that trains models.

Instead, it prepares data for model training.

You can think of pandas as the bridge between raw data and Machine Learning algorithms.

---

# Core Data Structures

Pandas has two primary data structures.

```
pandas
│
├── Series
│
└── DataFrame
```

Everything you learn in pandas is built around these two objects.

---

# Understanding Series

Official Definition

> A one-dimensional labeled array capable of holding data of any type.

The important words are:

- One-dimensional
- Labeled
- Array

Unlike a Python list, a Series stores labels along with values.

```
Series

Index          Value

A  ─────────► 10
B  ─────────► 20
C  ─────────► 30
```

Think of a Series as

```
NumPy Array
        +
Labels
```

rather than

```
Python List
```

---

# Creating a Series

From a list

```python
import pandas as pd

s = pd.Series([10,20,30])
```

Output

```
0    10
1    20
2    30
dtype: int64
```

Pandas automatically creates an index.

```
Index

0
1
2
```

called the Default Index.

---

From a custom index

```python
s = pd.Series(
    [10,20,30],
    index=["A","B","C"]
)
```

Output

```
A    10
B    20
C    30
```

Now the labels become meaningful.

Instead of

```
Position 1
```

we can write

```python
s["B"]
```

which makes the code easier to read.

---

# Series Attributes

Every Series consists of two fundamental components.

```
             Series
                │
      ┌─────────┴─────────┐
      │                   │
   Index (Labels)      Values
```

Example

```python
import pandas as pd

s = pd.Series(
    [85,92,78],
    index=["Alice","Bob","Charlie"],
    name="Marks"
)
```

Output

```
Alice      85
Bob        92
Charlie    78
Name: Marks
dtype: int64
```

---

## 1. Index

```python
s.index
```

Output

```
Index(['Alice', 'Bob', 'Charlie'], dtype='object')
```

The Index stores labels.

```
Index

Alice
Bob
Charlie
```

Unlike Python lists, labels do not have to be integers.

Example

```
Student ID

S101
S102
S103
```

or

```
Date

2025-01-01
2025-01-02
2025-01-03
```

The Index gives semantic meaning to data.

---

## 2. Values

```python
s.values
```

Output

```
array([85,92,78])
```

The values contain the actual stored data.

Think of the Series as

```
Series

Index
 │
 ▼

Alice
Bob
Charlie

Values
 │
 ▼

85
92
78
```

The labels identify the values.

---

## 3. dtype

```python
s.dtype
```

Output

```
int64
```

The dtype represents the data type of the values.

Examples

```
[1,2,3]
↓

int64
```

```
[1.5,2.5]
↓

float64
```

```
["Alice","Bob"]
↓

object
```

Unlike DataFrames, a Series has only one dtype because it stores one type of data.

---

## 4. name

```python
s.name
```

Output

```
Marks
```

The name becomes important when a Series is placed inside a DataFrame.

```
DataFrame

Marks
Age
Salary
```

Each column is a named Series.

---

# Creating Series

There are multiple ways to construct a Series.

## From List

```python
s = pd.Series([10,20,30])
```

---

## From List with Custom Index

```python
s = pd.Series(
    [10,20,30],
    index=["A","B","C"]
)
```

---

## From Dictionary

```python
marks = {
    "Alice":85,
    "Bob":92,
    "Charlie":78
}

s = pd.Series(marks)
```

Output

```
Alice      85
Bob        92
Charlie    78
```

Dictionary Keys

↓

Series Index

Dictionary Values

↓

Series Values

---

# Accessing Elements

A Series supports two different ways of accessing data.

```
Series

Position
Label
```

These are different concepts.

---

## Label Access

```python
s.loc["Bob"]
```

or

```python
s["Bob"]
```

Returns

```
92
```

The lookup happens using the Index.

---

## Position Access

```python
s.iloc[1]
```

Returns

```
92
```

The lookup happens using the integer position.

---

# Label vs Position

This distinction is one of the most important concepts in pandas.

Suppose

```
Position

0
1
2
```

```
Index

Alice
Bob
Charlie
```

```
Value

85
92
78
```

Then

```
.loc["Bob"]

↓

Find label Bob

↓

92
```

Whereas

```
.iloc[1]

↓

Find position 1

↓

92
```

Although both return the same value, they use completely different lookup mechanisms.

---

# Common Confusion

Suppose

```python
s = pd.Series(
    [10,20,30],
    index=[100,200,300]
)
```

Then

```python
s.loc[200]
```

returns

```
20
```

because 200 is an Index label.

However,

```python
s.iloc[200]
```

raises

```
IndexError
```

because there is no position 200.

Remember

```
.loc

↓

LABEL
```

```
.iloc

↓

POSITION
```

Never mix them.

---

# Series Operations

One of the biggest advantages of pandas is vectorized computation.

Suppose

```python
s = pd.Series([10,20,30])
```

Adding five

```python
s + 5
```

Result

```
15
25
35
```

Every value is updated automatically.

No loop is required.

---

Multiplication

```python
s * 2
```

Result

```
20
40
60
```

---

Comparison

```python
s > 15
```

Result

```
False
True
True
```

Notice that comparison also returns another Series.

---

# Automatic Index Alignment

This is the feature that makes pandas fundamentally different from NumPy.

Suppose

```python
s1 = pd.Series(
    [10,20,30],
    index=["A","B","C"]
)

s2 = pd.Series(
    [1,2,3],
    index=["C","A","B"]
)
```

Most beginners expect

```
10+1

20+2

30+3
```

But pandas performs

```
A

10+2

↓

12
```

```
B

20+3

↓

23
```

```
C

30+1

↓

31
```

because Series are aligned using labels.

The computation happens after matching Index labels.

---

# Missing Labels

Suppose

```
s1

A
B
C
```

```
s2

B
C
D
```

Now

```python
s1+s2
```

Result

```
A    NaN
B     21
C     32
D    NaN
```

Whenever a matching label does not exist, pandas cannot perform the operation.

Instead, it produces

```
NaN
```

which represents a missing value.

---

# Mental Model

Never think

```
Series + Series

↓

Position + Position
```

Instead think

```
Series + Series

↓

Match Labels

↓

Align Data

↓

Perform Operation
```

This idea appears repeatedly throughout pandas.


Excellent. Here's **README.md – Part 3**.

````markdown
---

# Understanding DataFrame

The DataFrame is the most commonly used data structure in pandas.

Official Definition

> A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

This definition contains several important ideas.

- Two-dimensional
- Tabular
- Labeled rows
- Labeled columns
- Columns can have different data types
- Size can grow or shrink

Think of a DataFrame as an Excel spreadsheet.

```

```
          Name      Age      Salary
0         Alice      25      50000
1         Bob        30      65000
2         Charlie    28      72000
```

````

Unlike NumPy arrays, every column has meaning.

---

# Mental Model

Most beginners think

```
DataFrame

↓

2D Array
```

This is **not the best mental model**.

Instead think

```
              DataFrame
                   │
      ┌────────────┼────────────┐
      │            │            │
   Series       Series       Series
    Name         Age         Salary
```

Every column inside a DataFrame is actually a **Series**.

This single idea explains many pandas behaviors.

---

# Why DataFrame Exists

Suppose we only have a Series.

```python
marks = pd.Series([85,92,78])
```

A Series can represent only one variable.

```
Marks

85
92
78
```

But real datasets usually contain many variables.

```
Student

Marks
Age
City
Salary
Department
Experience
```

A DataFrame groups these related Series into one table.

---

# Creating a DataFrame

The most common method is using a dictionary.

```python
import pandas as pd

df = pd.DataFrame({
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,28],
    "Salary":[50000,65000,72000]
})
```

Output

```
      Name      Age    Salary
0     Alice      25     50000
1     Bob        30     65000
2     Charlie    28     72000
```

Dictionary keys become column names.

Dictionary values become column data.

---

# Creating Custom Row Labels

```python
df = pd.DataFrame(
{
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,28]
},
index=["A","B","C"]
)
```

Output

```
        Name     Age
A      Alice     25
B      Bob       30
C      Charlie   28
```

The row labels now become

```
A
B
C
```

instead of

```
0
1
2
```

---

# Internal Anatomy

```
                Columns

          Name      Age

Rows

A        Alice      25

B        Bob        30

C        Charlie    28
```

A DataFrame has three major components.

```
DataFrame

│

├── Row Index

├── Column Labels

└── Values
```

---

# DataFrame Attributes

Consider

```python
df = pd.DataFrame(
{
    "Marks":[80,90,70],
    "Age":[20,21,19]
},
index=["A","B","C"]
)
```

---

## shape

```python
df.shape
```

Output

```
(3,2)
```

Meaning

```
3 Rows

2 Columns
```

---

## index

```python
df.index
```

Output

```
Index(['A','B','C'])
```

These represent row labels.

---

## columns

```python
df.columns
```

Output

```
Index(['Marks','Age'])
```

These represent column labels.

---

## dtypes

```python
df.dtypes
```

Output

```
Marks    int64
Age      int64
dtype: object
```

Notice

Every column has its own dtype.

This is possible because each column is a separate Series.

---

# Why Different dtypes are Allowed

NumPy Array

```
Entire Array

↓

One dtype
```

```
int64

or

float64
```

DataFrame

```
Column 1

↓

object
```

```
Column 2

↓

int64
```

```
Column 3

↓

float64
```

Every Series controls its own dtype.

Therefore the DataFrame naturally supports heterogeneous data.

---

# Selecting Columns

Suppose

```
        Name      Age      Salary

0      Alice      25      50000

1      Bob        30      65000

2      Charlie    28      72000
```

Selecting one column

```python
df["Age"]
```

returns

```
0    25
1    30
2    28

Name: Age
```

Notice

This is **not** a DataFrame.

It is a **Series**.

---

# Why Does One Column Return a Series?

Remember our mental model.

```
              DataFrame

                    │

      ┌─────────────┼─────────────┐

      │             │             │

 Series(Name)  Series(Age)  Series(Salary)
```

When we write

```python
df["Age"]
```

we are simply asking pandas

> Give me the **Age Series**.

---

# Selecting Multiple Columns

Suppose

```python
df[["Name","Age"]]
```

Output

```
      Name      Age

0     Alice      25

1     Bob        30

2     Charlie    28
```

The return type is now

```
DataFrame
```

---

# Why Double Square Brackets?

Single brackets

```python
df["Age"]
```

Python passes

```
"Age"
```

to pandas.

Double brackets

```python
df[["Age"]]
```

Python first creates

```
["Age"]
```

which is a **list**.

Pandas interprets this as

> Return a DataFrame containing these columns.

Similarly

```python
df[["Name","Age"]]
```

passes

```
["Name","Age"]
```

which is a list of column names.

---

# Common Confusion

```
df["Age"]
```

↓

Series

```
df[["Age"]]
```

↓

DataFrame

Even though both contain exactly the same values, their data types are different.

---

# Comparison

| Expression           | Returns   |
| -------------------- | --------- |
| `df["Age"]`          | Series    |
| `df[["Age"]]`        | DataFrame |
| `df[["Name","Age"]]` | DataFrame |

---

# Why This Matters in Machine Learning

Suppose

```python
X = df[["Age","Salary"]]
```

X becomes

```
DataFrame

Shape

(rows,2)
```

Target

```python
y = df["Salary"]
```

becomes

```
Series

Shape

(rows,)
```

Many Machine Learning libraries expect

Features

↓

DataFrame

Target

↓

Series

Understanding this distinction prevents many beginner mistakes when using scikit-learn.

---

# Summary

A DataFrame is **not simply a two-dimensional NumPy array**.

Instead, it is better understood as

```
DataFrame

↓

Collection of aligned Series
```

This mental model explains

* Different dtypes
* Column selection
* Index alignment
* Most DataFrame operations

```

---
---

# Indexing and Selection

Accessing data is one of the most frequently performed operations in pandas.

Pandas provides multiple indexing methods, each designed for a different purpose.

```
                    DataFrame
                         │
        ┌────────────────┼────────────────┐
        │                │                │
       []              .loc            .iloc
                                           │
                                   .at / .iat
```

Understanding when to use each method is essential.

---

# [] Operator

The square bracket operator is primarily used for **column selection**.

Single column

```python
df["Age"]
```

Returns

```
Series
```

Multiple columns

```python
df[["Name","Age"]]
```

Returns

```
DataFrame
```

Remember

```
[]

↓

Primarily selects columns
```

It is **not** the general method for selecting rows.

---

# .loc

Official meaning

> Label-based indexing.

Think

```
.loc

↓

LABEL
```

Example

```python
df.loc["A"]
```

returns

```
Entire row having label A
```

Selecting one value

```python
df.loc["A","Age"]
```

```
25
```

Selecting multiple rows

```python
df.loc["A":"C"]
```

Returns

```
A

B

C
```

Notice

`.loc` slicing is **inclusive**.

```
.loc["A":"C"]

↓

A
B
C
```

End label is included.

---

# .iloc

Official meaning

> Integer position based indexing.

Think

```
.iloc

↓

POSITION
```

Example

```python
df.iloc[0]
```

returns

```
First row
```

Selecting one value

```python
df.iloc[0,1]
```

```
25
```

Selecting multiple rows

```python
df.iloc[0:2]
```

Returns

```
Position 0

Position 1
```

Unlike `.loc`

```
.iloc

↓

Python slicing

↓

End excluded
```

---

# Label vs Position

Suppose

```
Position

0
1
2
```

```
Index

100
200
300
```

Then

```python
df.loc[200]
```

Finds

```
Label

200
```

Whereas

```python
df.iloc[200]
```

tries to access

```
Position

200
```

which raises

```
IndexError
```

This is one of the most common interview questions.

---

# .at

Used for accessing one scalar value using labels.

```python
df.at["B","Age"]
```

Returns

```
21
```

Think

```
.at

↓

One Value

+

Label
```

---

# .iat

Used for accessing one scalar value using positions.

```python
df.iat[1,1]
```

Returns

```
21
```

Think

```
.iat

↓

One Value

+

Position
```

---

# Indexing Summary

| Method | Uses |
|---------|------|
| [] | Column Selection |
| .loc | Labels |
| .iloc | Positions |
| .at | Single Value by Label |
| .iat | Single Value by Position |

---

# Boolean Indexing

Boolean indexing allows selecting rows based on conditions.

Example

```python
df[df["Age"]>25]
```

Step 1

```
Age

25
30
28
```

Evaluate

```
False

True

True
```

Step 2

Only rows corresponding to **True** are returned.

Result

```
Bob

Charlie
```

---

# Multiple Conditions

AND

```python
df[
    (df["Age"]>20) &
    (df["Salary"]>50000)
]
```

OR

```python
df[
    (df["Age"]<20) |
    (df["Salary"]>70000)
]
```

NOT

```python
df[
    ~(df["Age"]>25)
]
```

Always remember

```
AND

↓

&
```

```
OR

↓

|
```

```
NOT

↓

~
```

Never use

```python
and
or
```

with pandas Series.

---

# Common Beginner Mistakes

## Mixing .loc and .iloc

Wrong

Thinking

```
.loc

↓

Position
```

Correct

```
.loc

↓

Label
```

---

## Forgetting Double Brackets

Wrong

```python
df["Age"]
```

when a DataFrame is required.

Correct

```python
df[["Age"]]
```

---

## Assuming Series Arithmetic Uses Position

Wrong

```
Series

↓

Position Alignment
```

Correct

```
Series

↓

Label Alignment
```

---

## Using Python Logical Operators

Wrong

```python
(df["Age"]>20) and (df["Age"]<30)
```

Correct

```python
(df["Age"]>20) &
(df["Age"]<30)
```

---

# Pandas in Machine Learning

Pandas is the first library used in almost every Machine Learning project.

Typical workflow

```
CSV

↓

read_csv()

↓

Data Cleaning

↓

Missing Values

↓

Feature Engineering

↓

Encoding

↓

Scaling

↓

Train-Test Split

↓

Model Training
```

Without pandas, preparing real-world datasets becomes extremely difficult.

---

# Mental Map

```
pandas

│

├── Series

│      │

│      ├── Index

│      ├── Values

│      ├── dtype

│      └── name

│

└── DataFrame

       │

       ├── Collection of Series

       ├── index

       ├── columns

       ├── shape

       └── dtypes
```

---

# Revision Sheet

Remember

```
Series

↓

1D Labeled Array
```

```
DataFrame

↓

Collection of Series
```

```
.loc

↓

Label
```

```
.iloc

↓

Position
```

```
.at

↓

Label + Single Value
```

```
.iat

↓

Position + Single Value
```

```
Series + Series

↓

Align Labels

↓

Operate
```

```
.loc Slice

↓

End Included
```

```
.iloc Slice

↓

End Excluded
```

```
df["A"]

↓

Series
```

```
df[["A"]]

↓

DataFrame
```

---

# Interview Questions

1. What is the difference between Series and DataFrame?

2. Why is pandas preferred over NumPy for tabular data?

3. Explain `.loc` vs `.iloc`.

4. Why does `df["Age"]` return a Series?

5. Why does `df[["Age"]]` return a DataFrame?

6. Explain automatic index alignment.

7. Why does pandas produce `NaN` during Series arithmetic?

8. Explain `.at` and `.iat`.

9. Why are `&` and `|` used instead of `and` and `or`?

10. Explain the internal relationship between DataFrame and Series.

---

# Practice Problems

## Easy

- Create a Series using a list.
- Create a Series using a dictionary.
- Create a DataFrame with three columns.
- Print `shape`, `index`, `columns`, and `dtypes`.

---

## Medium

- Select a single column.
- Select multiple columns.
- Retrieve a row using `.loc`.
- Retrieve a row using `.iloc`.
- Access one value using `.at`.
- Access one value using `.iat`.

---

## Advanced

- Filter rows where Age > 25.
- Filter rows using two conditions.
- Add two Series with different indexes.
- Explain why `NaN` appears.
- Compare `.loc` slicing with `.iloc` slicing.

---

# Completion Checklist

✅ Understand why pandas exists

✅ Understand Series

✅ Understand DataFrame

✅ Create Series

✅ Create DataFrames

✅ Understand Index

✅ Understand DataFrame attributes

✅ Select columns

✅ Use `.loc`

✅ Use `.iloc`

✅ Use `.at`

✅ Use `.iat`

✅ Understand slicing

✅ Perform Boolean indexing

✅ Understand index alignment

✅ Connect pandas fundamentals to Machine Learning

---
