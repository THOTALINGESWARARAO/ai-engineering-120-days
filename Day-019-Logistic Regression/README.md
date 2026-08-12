# Day 19 — Logistic Regression

## Overview

Logistic Regression is a supervised machine learning algorithm used primarily for **classification problems**.

Although its name contains "Regression", Logistic Regression is generally used to predict the probability of a class and then convert that probability into a class prediction using a decision threshold.

### Learning Goal

By the end of Day 19, the following concepts were covered:

* Why linear regression is not suitable for binary classification
* Logistic Regression intuition
* Linear score
* Sigmoid function
* Probability prediction
* Classification threshold
* Decision boundary
* Log-odds / logit
* Logistic Regression coefficients
* Log Loss / Binary Cross-Entropy
* `predict()` vs `predict_proba()`
* Model evaluation
* Regularization
* Logistic Regression implementation using scikit-learn

---

# 1. What is Logistic Regression?

Logistic Regression is a supervised learning algorithm used to model the probability of a categorical outcome.

For binary classification:

```text
0 → Negative class
1 → Positive class
```

Examples:

```text
Spam / Not Spam
Pass / Fail
Fraud / Not Fraud
Disease / No Disease
Customer Churn / No Churn
```

The model does not directly produce `0` or `1` initially.

Instead, it estimates:

```text
P(y = 1 | X)
```

which is the probability that an observation belongs to class `1`.

---

# 2. Why Not Use Linear Regression?

Linear Regression produces a continuous numerical output:

```text
y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ
```

Its output is not restricted to `[0, 1]`.

For example:

```text
-0.7
0.3
0.8
1.4
2.2
```

These values cannot all represent probabilities.

For classification, we need:

```text
0 ≤ probability ≤ 1
```

Logistic Regression solves this by transforming the linear score through the **sigmoid function**.

---

# 3. Logistic Regression Mental Model

The complete flow is:

```text
Input Features
      ↓
Linear Score
      ↓
z = wᵀx + b
      ↓
Sigmoid Function
      ↓
Probability
      ↓
Decision Threshold
      ↓
Class Prediction
```

Example:

```text
Study Hours = 7
Attendance = 85%
       ↓
Linear Score
       ↓
z = 2.1
       ↓
Sigmoid
       ↓
P(Pass) = 0.89
       ↓
Threshold = 0.5
       ↓
Prediction = 1
```

### Core Mental Model

> Logistic Regression is a linear model whose output is transformed into a probability using the sigmoid function.

---

# 4. Linear Score

Logistic Regression first calculates a linear combination of the input features.

```text
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

or:

```text
z = wᵀx + b
```

Where:

* `x` → input features
* `w` → model coefficients
* `b` → intercept
* `z` → linear score

The score itself is not a probability.

It is passed to the sigmoid function.

---

# 5. Sigmoid Function

The sigmoid function converts the linear score into a value between `0` and `1`.

```text
σ(z) = 1 / (1 + e⁻ᶻ)
```

Behavior:

```text
z → -∞   → sigmoid(z) → 0
z = 0    → sigmoid(z) = 0.5
z → +∞   → sigmoid(z) → 1
```

Therefore:

```text
Negative score → probability closer to 0
Zero score      → probability = 0.5
Positive score → probability closer to 1
```

### Tiny Python Experiment

```python
from math import exp


def sigmoid(z):
    return 1 / (1 + exp(-z))


print(sigmoid(-5))
print(sigmoid(0))
print(sigmoid(5))
```

Approximate result:

```text
0.0067
0.5
0.9933
```

---

# 6. Probability Prediction

After applying the sigmoid function:

```text
z
↓
sigmoid(z)
↓
P(y = 1 | X)
```

For example:

```text
P(y = 1) = 0.83
```

means the model estimates an `83%` probability of class `1`.

Important:

> A probability prediction is not automatically the final class prediction.

The model still needs a decision threshold.

---

# 7. Classification Threshold

The threshold converts the predicted probability into a class.

With the standard threshold:

```text
threshold = 0.5
```

The decision rule is:

```text
probability >= 0.5 → class 1
probability <  0.5 → class 0
```

Examples:

```text
0.83 → 1
0.71 → 1
0.52 → 1
0.49 → 0
0.20 → 0
```

The threshold can be changed depending on the application.

Example:

```python
predictions = (probabilities >= 0.7).astype(int)
```

A threshold of `0.7` makes the model more conservative when predicting class `1`.

---

# 8. Decision Boundary

The standard threshold is `0.5`.

The sigmoid produces `0.5` when:

```text
z = 0
```

Since:

```text
z = wᵀx + b
```

the decision boundary is:

```text
wᵀx + b = 0
```

For two features:

```text
w₁x₁ + w₂x₂ + b = 0
```

This means Logistic Regression produces a **linear decision boundary**.

### Important

Logistic Regression can produce nonlinear probability values, but its standard decision boundary in feature space is linear.

---

# 9. Log-Odds / Logit

Logistic Regression can also be understood through **log-odds**.

First, define odds:

```text
odds = p / (1 - p)
```

Then:

```text
log-odds = log(p / (1 - p))
```

This is called the **logit**.

Logistic Regression models the log-odds as a linear function:

```text
log(p / (1 - p)) = wᵀx + b
```

This provides the mathematical connection between the linear model and the probability output.

### Mental Model

```text
Linear combination
       ↓
Log-odds
       ↓
Sigmoid transformation
       ↓
Probability
```

---

# 10. Interpreting Coefficients

Logistic Regression coefficients describe the effect of features on the **log-odds** of the positive class.

Suppose:

```python
model.coef_
```

returns:

```text
[[0.8, -1.2]]
```

Then:

```text
Feature 1 → positive coefficient
Feature 2 → negative coefficient
```

Interpretation:

### Positive coefficient

Increasing the feature tends to increase the log-odds of class `1`.

### Negative coefficient

Increasing the feature tends to decrease the log-odds of class `1`.

### Important

A coefficient is **not directly a change in probability**.

The relationship between a feature and probability is nonlinear because of the sigmoid function.

---

# 11. Log Loss

Logistic Regression commonly uses **Log Loss**, also known as **Binary Cross-Entropy**, for binary classification.

The loss function evaluates how well the predicted probabilities match the actual classes.

Conceptually:

```text
Correct + confident prediction
        ↓
Small loss

Wrong + confident prediction
        ↓
Large loss
```

Example:

```text
Actual = 1

Prediction = 0.99
→ Very good

Prediction = 0.60
→ Less confident

Prediction = 0.01
→ Very bad
```

This encourages the model to produce meaningful probabilities rather than only correct class labels.

---

# 12. Logistic Regression with scikit-learn

The main implementation uses:

```python
from sklearn.linear_model import LogisticRegression
```

Example:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)
```

---

# 13. `fit()`

```python
model.fit(X_train, y_train)
```

The model learns the parameters:

```text
w₁, w₂, ..., wₙ
b
```

from the training data.

The learned parameters define the relationship between the input features and the probability of the target class.

---

# 14. `predict()`

```python
predictions = model.predict(X_test)
```

`predict()` returns the final class labels.

Example:

```text
[0, 1, 1, 0, 1]
```

The prediction already applies the model's classification decision rule.

---

# 15. `predict_proba()`

```python
probabilities = model.predict_proba(X_test)
```

This returns class probabilities.

Example:

```text
[
    [0.92, 0.08],
    [0.12, 0.88],
    [0.25, 0.75]
]
```

Each row represents:

```text
[class 0 probability, class 1 probability]
```

For:

```text
[0.12, 0.88]
```

we have:

```text
P(class 0) = 0.12
P(class 1) = 0.88
```

### Key Difference

```text
predict()
    ↓
Final class

predict_proba()
    ↓
Probability for each class
```

---

# 16. Custom Classification Threshold

The probability of class `1` can be extracted using:

```python
probabilities = model.predict_proba(X_test)[:, 1]
```

A custom threshold can then be applied:

```python
predictions = (probabilities >= 0.7).astype(int)
```

Different thresholds produce different trade-offs between false positives and false negatives.

Therefore:

> The model's probability estimation and the classification decision are separate stages.

---

# 17. Model Coefficients and Intercept

The learned coefficients can be inspected using:

```python
print(model.coef_)
```

The intercept can be inspected using:

```python
print(model.intercept_)
```

For a model with `n` features:

```text
coef_
    ↓
weights for features

intercept_
    ↓
bias term
```

These parameters define the linear score:

```text
z = wᵀx + b
```

---

# 18. Model Evaluation

Common classification metrics include:

```text
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
```

Example:

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1:", f1_score(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
```

### What Each Metric Answers

| Metric           | Main Question                                              |
| ---------------- | ---------------------------------------------------------- |
| Accuracy         | How many predictions were correct overall?                 |
| Precision        | When the model predicts positive, how often is it correct? |
| Recall           | How many actual positives did the model find?              |
| F1               | How well are precision and recall balanced?                |
| Confusion Matrix | How are correct and incorrect predictions distributed?     |

---

# 19. Regularization

Logistic Regression in scikit-learn uses regularization by default.

Regularization helps control model complexity and reduce overfitting.

The `C` parameter controls the inverse of regularization strength.

```python
LogisticRegression(C=0.1)
```

means stronger regularization than:

```python
LogisticRegression(C=10)
```

Mental model:

```text
C small
→ stronger regularization

C large
→ weaker regularization
```

The exact optimization mathematics is not required for this stage.

---

# 20. Complete Example

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# Load dataset
X, y = load_breast_cancer(return_X_y=True)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LogisticRegression(
    max_iter=1000
)


# Train
model.fit(X_train, y_train)


# Class predictions
predictions = model.predict(X_test)


# Probability predictions
probabilities = model.predict_proba(X_test)


# Evaluation
print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1:", f1_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# Model parameters
print("\nCoefficients:")
print(model.coef_)

print("\nIntercept:")
print(model.intercept_)
```

---

# 21. Important Concepts to Distinguish

## Linear Regression vs Logistic Regression

```text
Linear Regression
    ↓
Continuous prediction

Logistic Regression
    ↓
Probability
    ↓
Classification
```

---

## `predict()` vs `predict_proba()`

```text
predict()
    ↓
Class label

predict_proba()
    ↓
Class probabilities
```

---

## Probability vs Classification

```text
Probability
    ↓
0.82

Threshold
    ↓
0.5

Class
    ↓
1
```

The probability and class label are not the same thing.

---

## Coefficient vs Probability

A coefficient represents the effect on **log-odds**, not a direct probability change.

---

# 22. Common Misconceptions

### Misconception 1

> Logistic Regression is a regression algorithm because it predicts numbers.

**Correction:**
It is primarily a classification algorithm that estimates class probabilities.

---

### Misconception 2

> The sigmoid directly gives the final class.

**Correction:**
The sigmoid gives a probability. A threshold converts that probability into a class.

---

### Misconception 3

> The threshold must always be 0.5.

**Correction:**
`0.5` is a common default, but the threshold can be changed depending on the application's cost of false positives and false negatives.

---

### Misconception 4

> A positive coefficient means probability increases by exactly that coefficient.

**Correction:**
The coefficient affects the **log-odds**. Probability changes nonlinearly through the sigmoid.

---

### Misconception 5

> Logistic Regression can only produce 0 or 1.

**Correction:**
The underlying model produces probabilities between `0` and `1`; the classification step converts them into class labels.

---

# 23. AI/ML Connection

Logistic Regression is important because it establishes several ideas that appear repeatedly in modern machine learning:

```text
Linear transformation
        ↓
Nonlinear transformation
        ↓
Probability
        ↓
Decision rule
        ↓
Evaluation
```

These concepts appear in more advanced models as well.

Logistic Regression is commonly useful when:

* The target is binary.
* Interpretability is important.
* A linear decision boundary is sufficient.
* A strong baseline model is needed.
* Probability estimates are useful.
* Training speed and simplicity matter.

It is often an excellent **baseline classifier** before moving to more complex models.

---

# 24. What I Learned Today

* [x] Classification vs regression
* [x] Why linear regression is unsuitable for binary classification
* [x] Logistic Regression
* [x] Linear score
* [x] Sigmoid function
* [x] Probability prediction
* [x] Classification threshold
* [x] Decision boundary
* [x] Log-odds / logit
* [x] Coefficient interpretation
* [x] Log Loss / Binary Cross-Entropy
* [x] `LogisticRegression`
* [x] `fit()`
* [x] `predict()`
* [x] `predict_proba()`
* [x] `coef_`
* [x] `intercept_`
* [x] Accuracy
* [x] Precision
* [x] Recall
* [x] F1 Score
* [x] Confusion Matrix
* [x] Classification threshold tuning
* [x] Regularization
* [x] `C` parameter

---

# 25. Official Documentation

### scikit-learn

* [LogisticRegression — scikit-learn API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* [Linear Models — scikit-learn User Guide](https://scikit-learn.org/stable/modules/linear_model.html)
* [Classification Metrics — scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Recommended Documentation Focus

---

# Day 19 Summary

The central idea of Logistic Regression is:

```text
Features
   ↓
Linear Score
   ↓
z = wᵀx + b
   ↓
Sigmoid
   ↓
Probability
   ↓
Threshold
   ↓
Class
```

The most important conceptual distinction is:

> **Logistic Regression estimates probabilities; the classification threshold converts those probabilities into class predictions.**

**Day 19 Status: COMPLETE ✅**
