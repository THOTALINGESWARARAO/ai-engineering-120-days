# Day 28 - XGBoost, LightGBM and CatBoost

## Overview

Today I studied three popular gradient boosting frameworks used for machine learning on structured and tabular data:

* XGBoost
* LightGBM
* CatBoost

The main goal was to understand how these frameworks work, how they differ, and how to implement them using Python.

## Topics Covered

* Gradient Boosting
* XGBoost
* LightGBM
* Histogram-based learning
* Leaf-wise tree growth
* CatBoost
* Categorical feature handling
* Ordered boosting
* Target leakage
* Model comparison
* Feature importance

## Gradient Boosting

Gradient Boosting builds decision trees sequentially.

Each new tree attempts to improve the existing model by reducing the remaining loss.

```text
Dataset
   ↓
Tree 1
   ↓
Current errors
   ↓
Tree 2
   ↓
Remaining errors
   ↓
Tree 3
   ↓
Final prediction
```

This is different from Random Forest, where the trees are trained largely independently.

## XGBoost

XGBoost stands for Extreme Gradient Boosting.

It is an optimized gradient boosting framework based on decision trees.

Important concepts:

* Sequential tree building
* Learning rate
* Number of estimators
* Maximum tree depth
* Regularization
* Subsampling
* Early stopping
* Missing-value handling

Example:

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Important parameters:

### `n_estimators`

Controls the number of boosting iterations or trees.

### `learning_rate`

Controls the contribution of each tree.

### `max_depth`

Controls the depth and complexity of each tree.

### `reg_alpha`

L1 regularization.

### `reg_lambda`

L2 regularization.

### Early stopping

Stops training when the validation metric stops improving for a specified number of iterations.

## LightGBM

LightGBM is a gradient boosting framework designed for efficient training, particularly on large tabular datasets.

Two important concepts are:

* Histogram-based learning
* Leaf-wise tree growth

## Histogram-Based Learning

Instead of considering every possible continuous feature value individually, LightGBM groups feature values into bins.

```text
Continuous values
       ↓
     Binning
       ↓
   Histograms
       ↓
 Efficient split finding
```

This can reduce computational and memory requirements.

## Leaf-Wise Tree Growth

LightGBM chooses the leaf that provides the largest loss reduction and splits that leaf.

```text
             Root
            /    \
           A      B
          / \
         C   D

Choose the leaf
with the largest
loss reduction
```

This differs from level-wise tree growth, where nodes are expanded level by level.

Leaf-wise growth can produce highly asymmetric trees and may increase the risk of overfitting.

Important parameters include:

* `num_leaves`
* `learning_rate`
* `n_estimators`
* `max_depth`
* `min_child_samples`

Example:

```python
from lightgbm import LGBMClassifier

model = LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

## CatBoost

CatBoost is a gradient boosting framework with strong support for categorical features.

The name comes from:

```text
Categorical + Boosting
```

Important concepts:

* Native categorical feature handling
* Ordered boosting
* Target leakage reduction
* High-cardinality categorical features
* Symmetric/oblivious trees

## Categorical Features

Consider:

```text
City
Education
Device
Occupation
```

Traditional machine learning algorithms often require these values to be encoded into numerical representations.

One-hot encoding can create a large number of columns when a feature has many unique categories.

CatBoost can process categorical features directly as part of its training process.

Example:

```python
from catboost import CatBoostClassifier

model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    verbose=False
)

model.fit(
    X_train,
    y_train,
    cat_features=["Sex", "Embarked"]
)
```

## Ordered Boosting

Target-based statistics can introduce target leakage if the target information of an observation is used improperly when constructing its features.

CatBoost uses ordered approaches to reduce this problem.

Conceptually:

```text
Previous observations
        ↓
Category statistics
        ↓
Current observation
```

Rather than allowing the current observation's target to directly influence its own target-derived statistic.

## XGBoost vs LightGBM vs CatBoost

| Feature                      | XGBoost                                    | LightGBM                         | CatBoost                   |
| ---------------------------- | ------------------------------------------ | -------------------------------- | -------------------------- |
| Gradient boosting            | Yes                                        | Yes                              | Yes                        |
| Decision trees               | Yes                                        | Yes                              | Yes                        |
| Regularization               | Yes                                        | Yes                              | Yes                        |
| Histogram-based learning     | Yes                                        | Core design                      | Yes                        |
| Leaf-wise growth             | No, traditionally level-wise               | Yes                              | No                         |
| Categorical feature handling | Requires preprocessing in common workflows | Supported                        | Strong native support      |
| Ordered boosting             | No                                         | No                               | Yes                        |
| Typical strength             | General-purpose tabular ML                 | Efficient large-scale tabular ML | Categorical-heavy datasets |

These frameworks should not be considered universally superior to one another. Model performance depends on the dataset, feature types, preprocessing, hyperparameters, validation strategy, and computational constraints.

## Practical Implementation

For this day's implementation, the Titanic dataset was used.

Features:

```text
Pclass
Sex
Age
SibSp
Parch
Fare
Embarked
```

Target:

```text
Survived
```

XGBoost and LightGBM were trained using encoded categorical features.

CatBoost was trained with categorical features specified directly.

The implementation also compares:

* Accuracy
* Feature importance
* Predictions

## Feature Scaling

Feature scaling is generally not required for these models because they are tree-based algorithms.

Tree models make decisions using feature split thresholds rather than distance calculations.

This differs from algorithms such as:

* KNN
* SVM
* Logistic Regression
* Neural Networks

where feature scaling can be important.

## How This Connects With Day 27

Day 27 covered:

* Cross-validation
* Hyperparameter tuning
* Pipelines

These concepts can be combined with the models learned today.

```text
Dataset
   ↓
Preprocessing
   ↓
Cross-validation
   ↓
XGBoost / LightGBM / CatBoost
   ↓
Hyperparameter tuning
   ↓
Evaluation
   ↓
Deployment
```

## Key Takeaways

### XGBoost

```text
Optimized gradient boosting
+
Regularization
+
Efficient tree construction
```

### LightGBM

```text
Gradient boosting
+
Histogram-based learning
+
Leaf-wise tree growth
```

### CatBoost

```text
Gradient boosting
+
Categorical feature handling
+
Ordered boosting
```

## Mental Model

```text
Gradient Boosting
       |
       |-------------------|-------------------|
       ↓                   ↓                   ↓
    XGBoost             LightGBM            CatBoost
       |                   |                   |
 Regularization      Histogram +         Categorical +
                     Leaf-wise           Ordered boosting
```

## Practical Relevance

These frameworks are widely useful for structured machine learning problems such as:

* Fraud detection
* Customer churn prediction
* Credit risk
* Classification
* Regression
* Ranking
* Recommendation systems
* Sales prediction
* Demand prediction

