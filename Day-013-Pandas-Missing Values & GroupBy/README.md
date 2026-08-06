# Day 13/120 — Pandas: Missing Values & GroupBy

---

# Chapter 1 — Missing Values ✅

## 1. Why Missing Values Matter

Real-world datasets are often incomplete. Before using data for analysis or machine learning, we need to detect missing values and decide whether to remove, replace, propagate, or estimate them.

Mental model:

```text
Raw Data
   ↓
Detect Missing Values
   ↓
Understand Missingness
   ↓
Choose a Strategy
   ↓
Clean / Impute
   ↓
ML-ready Data
```

## 2. Missing-Value Representations

Common pandas/Python representations:

```python
np.nan
None
pd.NA
pd.NaT
```

- `np.nan` — commonly used for floating-point missing values.
- `None` — Python's absence-of-value object.
- `pd.NA` — pandas nullable missing-value scalar.
- `pd.NaT` / `NaT` — missing datetime/timedelta value.

Example of nullable integer data:

```python
import pandas as pd

s = pd.Series([10, pd.NA, 30], dtype="Int64")
print(s)
```

## 3. Detecting Missing Values

```python
df.isna()
df.notna()
```

Mental model:

```text
isna():
missing     → True
non-missing → False

notna():
missing     → False
non-missing → True
```

Count missing values per column:

```python
df.isna().sum()
```

For a single value:

```python
pd.isna(value)
```

Do not rely on:

```python
x == np.nan
```

Use `isna()` / `pd.isna()` instead.

## 4. Removing Missing Data — `dropna()`

Basic usage:

```python
df.dropna()
```

By default, rows containing missing values are removed.

### Rows vs Columns

```python
df.dropna(axis=0)  # drop rows
df.dropna(axis=1)  # drop columns
```

### `how`

```python
df.dropna(how="any")
df.dropna(how="all")
```

- `any` — drop when at least one checked value is missing.
- `all` — drop only when all checked values are missing.

### `subset`

Check only selected columns:

```python
df.dropna(subset=["cgpa"])
```

Multiple columns:

```python
df.dropna(subset=["cgpa", "salary"])
```

### `thresh`

Require a minimum number of non-missing values:

```python
df.dropna(thresh=2)
```

### Important ML Consideration

Blindly dropping rows can remove a large amount of training data or change the population distribution.

```text
Original Dataset
      ↓
Blind dropna()
      ↓
Potentially Biased Subset
      ↓
Model learns altered distribution
```

## 5. Filling Missing Values — `fillna()`

Fill with a constant:

```python
df["skill"] = df["skill"].fillna("Unknown")
```

Numerical example:

```python
df["age"] = df["age"].fillna(0)
```

A constant should only be used when it makes semantic sense.

### Mean Imputation

```python
mean_cgpa = df["cgpa"].mean()
df["cgpa"] = df["cgpa"].fillna(mean_cgpa)
```

pandas `mean()` skips missing values by default.

### Median Imputation

```python
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)
```

Median is generally more robust to extreme outliers than mean.

### Mode Imputation

Useful for categorical features:

```python
mode_city = df["city"].mode()[0]
df["city"] = df["city"].fillna(mode_city)
```

## 6. Forward and Backward Fill

### Forward Fill

```python
df["temperature"] = df["temperature"].ffill()
```

Mental model:

```text
previous valid value
        ↓
      missing
```

### Backward Fill

```python
df["temperature"] = df["temperature"].bfill()
```

Mental model:

```text
missing
   ↑
next valid value
```

These are especially relevant for ordered/time-series data when propagation is valid for the domain.

## 7. Interpolation

Estimate intermediate missing values:

```python
df["temperature"] = df["temperature"].interpolate()
```

Example:

```text
20
NaN  → 22
24
```

Interpolation should only be used when the underlying variable/process supports such estimation.

## 8. ML Connection — Data Leakage

Avoid calculating imputation statistics using the entire dataset before splitting.

Incorrect conceptual flow:

```text
Entire Dataset
     ↓
Calculate Mean
     ↓
Impute
     ↓
Train/Test Split
```

Preferred ML flow:

```text
Dataset
   ↓
Train/Test Split
   ↓
Fit imputation on TRAIN data
   ↓
Apply learned transformation
   ├── Train
   └── Test
```

Later this connects to scikit-learn:

```python
from sklearn.impute import SimpleImputer
```

and preprocessing pipelines.

## 9. Missing Values — Revision Map

```text
Missing Values
│
├── Detect
│   ├── isna()
│   ├── notna()
│   └── isna().sum()
│
├── Remove
│   └── dropna()
│       ├── axis
│       ├── how
│       ├── subset
│       └── thresh
│
├── Replace
│   └── fillna()
│       ├── constant
│       ├── mean
│       ├── median
│       └── mode
│
├── Propagate
│   ├── ffill()
│   └── bfill()
│
└── Estimate
    └── interpolate()
```

---

# Chapter 2 — GroupBy ❌ Not Completed

## 10. Why `GroupBy`?

`GroupBy` lets us split rows into groups and calculate information for each group.

Example:

```python
df.groupby("department")["salary"].mean()
```

Question represented by the code:

> What is the average salary for each department?

## 11. Core Mental Model — Split → Apply → Combine

```text
Original Data
      ↓
    SPLIT
      ↓
Group A   Group B
   ↓         ↓
      APPLY
   mean()   mean()
      ↓
    COMBINE
      ↓
Final grouped result
```

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "department": ["AI", "Web", "AI", "Web", "AI"],
    "salary": [60000, 40000, 80000, 50000, 70000]
})

result = df.groupby("department")["salary"].mean()
```

Conceptually:

```text
AI  → 60000, 80000, 70000 → mean = 70000
Web → 40000, 50000        → mean = 45000
```

## 12. Basic Syntax

```python
df.groupby("group_column")["value_column"].aggregation()
```

Example:

```python
df.groupby("department")["salary"].sum()
```

Breakdown:

```text
groupby("department") → how rows are grouped
["salary"]            → values being analyzed
sum()                 → operation applied to each group
```

## 13. `DataFrameGroupBy` Object

```python
g = df.groupby("department")
```

`groupby()` creates a GroupBy object describing how rows are partitioned. An aggregation or other operation is then applied to produce a result.

Inspect groups:

```python
g.groups
```

Retrieve one group:

```python
g.get_group("AI")
```

## 14. Common Aggregations

```python
.sum()
.mean()
.count()
.min()
.max()
.median()
.std()
.size()
```

Examples:

```python
df.groupby("department")["salary"].sum()
df.groupby("department")["salary"].mean()
df.groupby("department")["salary"].max()
```

## 15. `count()` vs `size()`

`count()` counts non-missing values:

```python
df.groupby("department")["salary"].count()
```

`size()` counts rows in each group:

```python
df.groupby("department").size()
```

Mental model:

```text
count() → non-missing values
size()  → rows
```

## 16. Aggregating Multiple Columns

```python
df.groupby("department")[["salary", "experience"]].mean()
```

## 17. Multiple Aggregations — `agg()`

```python
df.groupby("department")["salary"].agg(
    ["mean", "min", "max"]
)
```

Different operations for different columns:

```python
df.groupby("department").agg({
    "salary": "mean",
    "experience": "max"
})
```

## 18. Named Aggregation

```python
summary = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    max_experience=("experience", "max")
)
```

Named aggregation produces clearer feature/summary names.

## 19. Grouping by Multiple Columns

```python
df.groupby(
    ["department", "level"]
)["salary"].mean()
```

Conceptually:

```text
Department
│
├── AI
│   ├── Junior
│   └── Senior
│
└── Web
    ├── Junior
    └── Senior
```

This commonly produces a MultiIndex result.

## 20. `as_index=False`

Keep grouping keys as regular columns:

```python
df.groupby(
    "department",
    as_index=False
)["salary"].mean()
```

This is convenient before later operations such as merges, visualization, feature engineering, or export.

## 21. AI/ML Connection — Aggregate Feature Engineering

Transaction data:

```text
user_id   amount
101       500
101       1000
102       200
101       700
102       800
```

Create user-level features:

```python
features = df.groupby("user_id").agg(
    total_spending=("amount", "sum"),
    avg_transaction=("amount", "mean"),
    transaction_count=("amount", "count"),
    max_transaction=("amount", "max")
)
```

Mental model:

```text
Raw Transactions
       ↓
     GroupBy
       ↓
Aggregate Behavior
       ↓
ML Features
```

Examples:

```text
E-commerce        → user purchase statistics
Banking           → account transaction statistics
Healthcare        → patient measurement summaries
IoT               → device sensor statistics
Recommendation    → user interaction statistics
```
