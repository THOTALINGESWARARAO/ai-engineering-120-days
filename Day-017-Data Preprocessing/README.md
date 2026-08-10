# Day 17 — Data Preprocessing

## 🎯 Objective

Understand how raw datasets are prepared for machine learning using **scikit-learn**, including:

* Train/test splitting
* Feature scaling
* Standardization
* Min-Max scaling
* Categorical encoding
* One-hot encoding
* Ordinal encoding
* Data leakage
* `ColumnTransformer`
* `Pipeline`

The goal is to understand **why preprocessing is required, when to use each technique, and how to build a reliable preprocessing workflow**.

---

## 📚 Concepts Covered

### 1. Data Preprocessing

Machine learning models generally cannot directly consume raw real-world data.

Typical preprocessing tasks include:

```text
Raw Data
   ↓
Train/Test Split
   ↓
Numerical Feature Processing
   ↓
Categorical Feature Encoding
   ↓
Processed Features
   ↓
ML Model
```

Common preprocessing operations include:

* Scaling numerical features
* Encoding categorical features
* Handling missing values
* Feature transformation
* Preparing consistent train/test representations

---

# 2. Train/Test Split

## Why?

The model needs data for learning and separate unseen data for evaluation.

```text
Dataset
   │
   ├── Training Set → Learn
   │
   └── Test Set → Evaluate
```

Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### `test_size`

`test_size=0.2` means approximately **20% of the samples** are assigned to the test set.

For 1000 samples:

```text
Training → 800 samples
Testing  → 200 samples
```

The number of features does not change.

For:

```text
X.shape = (1000, 20)
```

the split produces approximately:

```text
X_train → (800, 20)
X_test  → (200, 20)
```

### `random_state`

Controls the reproducibility of the random split.

```python
random_state=42
```

allows the same split to be reproduced.

> `random_state` controls reproducibility, not model quality.

---

# 3. Feature Scaling

## Why?

Different numerical features can have very different ranges.

Example:

```text
Age       → 20–60
Salary    → 20,000–100,000
```

Algorithms that depend on distances, magnitudes, or optimization can be affected by these differences.

Scaling puts numerical features onto a more comparable numerical scale.

Common techniques learned:

```text
MinMaxScaler
StandardScaler
```

---

# 4. Min-Max Scaling

`MinMaxScaler` transforms features into a specified range, commonly `[0, 1]`.

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Mental Model

> **Where does this value lie between the minimum and maximum?**

For:

```text
Age = [20, 30, 40]
```

Min-Max scaling produces:

```text
20 → 0.0
30 → 0.5
40 → 1.0
```

The important distinction:

```text
Min-Max Scaling
→ usually produces values between 0 and 1
```

It does **not** mean the mean becomes zero.

---

# 5. Standardization

Standardization centers each feature around zero and scales it according to its standard deviation.

The standard score is:

```text
z = (x - mean) / standard deviation
```

Example:

```text
Age = [20, 30, 40, 50, 60]
Mean = 40
```

After standardization, approximately:

```text
20 → -1.41
30 → -0.71
40 →  0.00
50 → +0.71
60 → +1.41
```

### Mental Model

> **How many standard deviations away from the mean is this value?**

For example:

```text
Mean = 50
Standard deviation = 10
Age = 70

z = (70 - 50) / 10
  = 2
```

Therefore:

```text
z = 2
```

means the value is **2 standard deviations above the mean**.

---

## `StandardScaler`

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

`StandardScaler` learns the mean and standard deviation from the training data and uses those learned statistics when transforming later data.

---

# 6. `fit()`, `transform()`, and `fit_transform()`

This is one of the most important preprocessing concepts.

### `fit()`

Learns preprocessing parameters from data.

For `StandardScaler`:

```text
fit()
 ↓
learn mean
learn standard deviation
```

For `MinMaxScaler`:

```text
fit()
 ↓
learn minimum
learn maximum
```

### `transform()`

Applies the already-learned parameters.

```python
scaler.transform(X_test)
```

### `fit_transform()`

Combines both operations:

```python
scaler.fit_transform(X_train)
```

Conceptually:

```text
fit
 ↓
learn parameters
 ↓
transform
 ↓
return transformed data
```

---

# 7. Data Leakage

Data leakage occurs when information that should be unavailable during training influences the training process.

### ❌ Incorrect

```python
scaler.fit(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)
```

The scaler learned information from the entire dataset, including the future test data.

### ✅ Correct

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

The fundamental rule is:

> **Fit preprocessing only on training data. Transform both training and test data using the learned parameters.**

---

# 8. Categorical Encoding

Machine learning algorithms generally require numerical representations of categorical features.

Example:

```text
City
------
Guntur
Hyderabad
Vijayawada
```

We need to convert these categories into numerical features.

Two important categories were learned:

### Nominal

No meaningful ordering.

```text
Red
Blue
Green
```

### Ordinal

A meaningful ordering exists.

```text
Small < Medium < Large
```

The type of categorical variable determines the appropriate encoding strategy.

---

# 9. One-Hot Encoding

One-hot encoding creates a binary column for each category.

Example:

```text
City
------
Guntur
Hyderabad
Vijayawada
```

becomes conceptually:

```text
Guntur  Hyderabad  Vijayawada
1       0          0
0       1          0
0       0          1
```

Each row contains `1` for its category and `0` for the others.

### scikit-learn

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

X_encoded = encoder.fit_transform(X)
```

`OneHotEncoder` creates a binary column for each category by default.

### When to use

Best suited to **nominal categorical features** where categories have no natural ordering.

Example:

```text
City
Color
Country
Browser
```

---

# 10. Ordinal Encoding

Ordinal encoding represents categories using integer codes.

Example:

```text
Size

Small  → 0
Medium → 1
Large  → 2
```

This is appropriate when the categories have a meaningful order:

```text
Small < Medium < Large
```

### scikit-learn

```python
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()

X_encoded = encoder.fit_transform(X)
```

`OrdinalEncoder` transforms categorical features into ordinal integer codes.

### Important distinction

Do not assign arbitrary integers to nominal categories such as:

```text
Guntur      → 1
Hyderabad   → 2
Vijayawada  → 3
```

This can introduce a false numerical ordering.

For nominal categories, prefer:

```text
OneHotEncoder
```

---

# 11. `LabelEncoder` vs Feature Encoding

A common misconception is that `LabelEncoder` should be used for arbitrary categorical feature columns.

scikit-learn specifically documents `LabelEncoder` for encoding **target labels (`y`)**, not input features (`X`).

For categorical features:

```text
Nominal feature
      ↓
OneHotEncoder

Ordinal feature
      ↓
OrdinalEncoder
```

For target labels:

```text
Target y
   ↓
LabelEncoder
```

when label encoding is appropriate for the task.

---

# 12. ColumnTransformer

Real datasets often contain different feature types.

Example:

```text
Age       → Numerical
Salary    → Numerical
City      → Nominal
Size      → Ordinal
```

Different columns need different preprocessing.

`ColumnTransformer` allows different transformations to be applied to different column subsets.

Example:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(), categorical_features)
    ]
)
```

### Mental Model

> **ColumnTransformer = decide which transformation each group of columns receives.**

```text
                    Dataset
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
        Numerical            Categorical
             ↓                   ↓
      StandardScaler       OneHotEncoder
             │                   │
             └─────────┬─────────┘
                       ↓
                Processed Features
```

---

# 13. Pipeline

A `Pipeline` chains multiple preprocessing steps and/or an estimator into a single workflow.

scikit-learn describes a typical ML pipeline as preprocessing followed by a final predictor. A pipeline can then be fitted and used for prediction like a normal estimator.

Example:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])
```

The workflow becomes:

```text
Input
  ↓
StandardScaler
  ↓
LogisticRegression
  ↓
Prediction
```

### Mental Model

> **Pipeline = sequence of operations.**

---

# 14. ColumnTransformer vs Pipeline

These two concepts solve different problems.

| Concept             | Main purpose                                         |
| ------------------- | ---------------------------------------------------- |
| `Pipeline`          | Chain operations in sequence                         |
| `ColumnTransformer` | Apply different transformations to different columns |

### Pipeline

Answers:

> **What should happen first, second, third?**

```text
Scaling
   ↓
Model
```

### ColumnTransformer

Answers:

> **Which columns should receive which transformation?**

```text
Numerical → Scaling
Categorical → Encoding
```

---

# 15. Using Them Together

This is the common scikit-learn pattern.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])
```

The complete architecture becomes:

```text
                         Pipeline
                            │
                    ColumnTransformer
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
        Numerical Features          Categorical Features
              ↓                           ↓
       StandardScaler              OneHotEncoder
              │                           │
              └─────────────┬─────────────┘
                            ↓
                    LogisticRegression
                            ↓
                        Prediction
```

scikit-learn's own mixed-type example demonstrates this pattern: separate preprocessing pipelines for numerical and categorical features, combined through `ColumnTransformer`, then integrated with a predictive model using `Pipeline`.

---

# 16. Complete Workflow

The complete Day 17 workflow is:

```text
                    Raw Dataset
                         │
                         ↓
                  Train/Test Split
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
           X_train                X_test
              │                     │
              ↓                     │
      Fit preprocessing            │
              │                     │
              ↓                     ↓
       Transform train       Transform test
              │                     │
              └──────────┬──────────┘
                         ↓
                        Model
                         ↓
                    Evaluation
```

With a production-style scikit-learn implementation:

```text
                         Pipeline
                            │
                    ColumnTransformer
                       /          \
                      /            \
             Numerical          Categorical
                 ↓                    ↓
          StandardScaler        OneHotEncoder
                 \                    /
                  \                  /
                   └──────┬─────────┘
                          ↓
                        Model
```

---

# 🤖 AI/ML Connection

Data preprocessing is not merely a data-cleaning step.

It directly affects how ML algorithms interpret features.

### Scaling

Important for models affected by feature magnitude, distances, or optimization, including:

* KNN
* K-Means
* SVM
* Logistic Regression
* Regularized linear models
* Neural networks

### Encoding

Makes categorical information usable by ML algorithms.

### Pipeline

Makes preprocessing reproducible between:

```text
Training
   ↓
Validation/Test
   ↓
Production inference
```

This becomes particularly important when deploying ML models because the same preprocessing logic used during training must be applied consistently to incoming production data.

---

# 🧠 Key Mental Models

### Train/Test Split

> **Training data teaches; test data evaluates.**

### Min-Max Scaling

> **Where does this value sit between the minimum and maximum?**

### Standardization

> **How many standard deviations away from the mean is this value?**

### One-Hot Encoding

> **Turn categories into independent binary features.**

### Ordinal Encoding

> **Represent meaningful category order numerically.**

### ColumnTransformer

> **Different columns → different transformations.**

### Pipeline

> **Chain the entire ML workflow together.**

---

# 🧪 Practical Example

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Dataset
data = pd.DataFrame({
    "Age": [22, 25, 31, 35, 28, 40],
    "Salary": [30000, 45000, 60000, 80000, 50000, 90000],
    "City": [
        "Guntur",
        "Hyderabad",
        "Guntur",
        "Vijayawada",
        "Hyderabad",
        "Guntur"
    ],
    "Purchased": [0, 0, 1, 1, 1, 1]
})


# Features and target
X = data.drop("Purchased", axis=1)
y = data["Purchased"]


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Feature groups
numeric_features = ["Age", "Salary"]
categorical_features = ["City"]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# Complete ML Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])


# Train
model.fit(X_train, y_train)


# Predict
predictions = model.predict(X_test)


# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
```

---

# 📖 Official Documentation

All concepts in this day were based on the **scikit-learn documentation**:

* [scikit-learn — Getting Started: Transformers and Pipelines](https://scikit-learn.org/stable/getting_started.html)
* [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
* [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
* [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
* [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
* [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
* [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)
* [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
* [Pipelines and Composite Estimators](https://scikit-learn.org/stable/modules/compose.html)

---

# ✅ Day 17 Completion Status

### Completed

* [x] Data preprocessing fundamentals
* [x] Train/test split
* [x] `test_size`
* [x] `random_state`
* [x] Feature scaling
* [x] Min-Max scaling
* [x] Standardization
* [x] `MinMaxScaler`
* [x] `StandardScaler`
* [x] `fit()`
* [x] `transform()`
* [x] `fit_transform()`
* [x] Data leakage
* [x] Nominal vs ordinal features
* [x] One-hot encoding
* [x] Ordinal encoding
* [x] `OneHotEncoder`
* [x] `OrdinalEncoder`
* [x] `ColumnTransformer`
* [x] `Pipeline`
* [x] Complete preprocessing workflow

### Status

**Day 17 — COMPLETE ✅**
