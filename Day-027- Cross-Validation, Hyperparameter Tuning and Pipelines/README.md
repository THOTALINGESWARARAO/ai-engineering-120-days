# Day 27 - Cross-Validation, Hyperparameter Tuning and Pipelines

## Overview

Day 27 focuses on three important concepts in machine learning model development:

* Cross-Validation
* Hyperparameter Tuning
* Pipelines

These concepts help build machine learning workflows that are more reliable, reproducible, and less prone to data leakage.

The examples in this folder use **Scikit-learn** and the **Iris dataset**.

## Learning Objectives

By the end of this day, the goal is to understand:

* Why a single train-test split may not be sufficient
* How K-Fold Cross-Validation works
* How Stratified K-Fold is used for classification
* The difference between parameters and hyperparameters
* How Grid Search works
* How Randomized Search works
* How Scikit-learn Pipelines work
* How Pipelines help prevent data leakage
* How to combine preprocessing, cross-validation, and hyperparameter tuning

## 1. Cross-Validation

Cross-Validation is a model evaluation technique where the training data is divided into multiple folds.

For 5-Fold Cross-Validation:

```text
Dataset
   |
   +---- Fold 1
   +---- Fold 2
   +---- Fold 3
   +---- Fold 4
   +---- Fold 5
```

The model is trained and validated multiple times.

```text
Round 1 -> Train: F2 F3 F4 F5 | Validation: F1
Round 2 -> Train: F1 F3 F4 F5 | Validation: F2
Round 3 -> Train: F1 F2 F4 F5 | Validation: F3
Round 4 -> Train: F1 F2 F3 F5 | Validation: F4
Round 5 -> Train: F1 F2 F3 F4 | Validation: F5
```

The final CV score is generally summarized using the mean of the individual scores.

## 2. `cross_val_score()`

Scikit-learn provides `cross_val_score()` for evaluating an estimator using cross-validation.

Example:

```python
scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)
```

The result contains one score for each fold.

```python
print(scores)
print(scores.mean())
print(scores.std())
```

## 3. Mean Cross-Validation Score

The mean provides an overall estimate of model performance across the folds.

For example:

```text
Fold 1 -> 96.67%
Fold 2 -> 100.00%
Fold 3 -> 93.33%
Fold 4 -> 96.67%
Fold 5 -> 100.00%

Mean -> 97.33%
```

A higher mean score generally indicates better performance for the selected metric, but model evaluation should also consider variance, the dataset, the metric, and the real-world objective.

## 4. Standard Deviation

The standard deviation indicates how much the validation scores vary across folds.

A smaller standard deviation means the model's performance is more consistent across the folds.

For the initial experiment:

```text
Mean CV Score: 97.33%
Standard Deviation: 2.49%
```

## 5. Stratified K-Fold

For classification problems, maintaining a similar class distribution across folds is important.

`StratifiedKFold` attempts to preserve the percentage of samples for each class in every fold.

Example:

```python
skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

It can then be passed to `cross_val_score()`:

```python
scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=skf,
    scoring="accuracy"
)
```

## 6. Parameters vs Hyperparameters

### Parameters

Parameters are values learned by the model during training.

Examples include:

```text
Linear Regression -> coefficients
Logistic Regression -> coefficients
Neural Network -> weights and biases
```

### Hyperparameters

Hyperparameters are configuration values selected before or during the training process.

For KNN:

```text
n_neighbors
weights
metric
```

For Random Forest:

```text
n_estimators
max_depth
min_samples_split
```

## 7. Pipelines

A Pipeline combines multiple machine learning steps into a single workflow.

Example:

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])
```

The workflow becomes:

```text
Raw Data
    |
    v
StandardScaler
    |
    v
KNN
    |
    v
Prediction
```

Instead of manually performing preprocessing and model training, the Pipeline manages the sequence.

## 8. Why Pipelines Matter

Pipelines are especially important when preprocessing is required.

They help:

* Keep preprocessing and modeling together
* Reduce repetitive code
* Make workflows reproducible
* Prevent preprocessing mistakes
* Reduce the risk of data leakage during cross-validation
* Make hyperparameter tuning easier

## 9. Data Leakage

Data leakage occurs when information from outside the training data improperly influences the model during training.

For example, fitting a scaler on the complete dataset before cross-validation can allow information from validation folds to influence the preprocessing.

A Pipeline avoids this problem by making preprocessing part of the model workflow.

```text
Training Fold
     |
     v
Fit Scaler
     |
     v
Transform Training Fold
     |
     v
Train Model

Validation Fold
     |
     v
Use fitted Scaler
     |
     v
Transform Validation Fold
     |
     v
Evaluate Model
```

## 10. GridSearchCV

Grid Search evaluates all combinations of specified hyperparameter values.

Example:

```python
param_grid = {
    "knn__n_neighbors": [3, 5, 7, 9, 11],
    "knn__weights": ["uniform", "distance"],
    "knn__metric": ["euclidean", "manhattan"]
}
```

Then:

```python
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid_search.fit(X_train, y_train)
```

Important attributes:

```python
grid_search.best_params_
grid_search.best_score_
grid_search.best_estimator_
```

## 11. Pipeline Hyperparameter Syntax

When tuning a Pipeline, parameters are specified using:

```text
step_name__parameter_name
```

Example:

```python
"knn__n_neighbors"
```

Here:

```text
knn
 |
 +---- step name

n_neighbors
 |
 +---- hyperparameter
```

This syntax is important when using `GridSearchCV` or `RandomizedSearchCV` with Pipelines.

## 12. RandomizedSearchCV

Grid Search evaluates every specified combination.

Randomized Search samples a specified number of combinations from the parameter distributions.

Example:

```python
random_search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_distributions,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42
)
```

Randomized Search can be useful when the hyperparameter search space is large.

## 13. Grid Search vs Randomized Search

| Feature            | GridSearchCV               | RandomizedSearchCV            |
| ------------------ | -------------------------- | ----------------------------- |
| Search strategy    | All specified combinations | Randomly sampled combinations |
| Computational cost | Can become expensive       | Usually more controllable     |
| Search space       | Explicit grid              | Distributions/ranges          |
| Number of trials   | Determined by combinations | Controlled using `n_iter`     |
| Useful when        | Search space is small      | Search space is large         |

## 14. Complete Workflow

The complete workflow implemented in `examples.py` is:

```text
Dataset
   |
   v
Train/Test Split
   |
   v
Pipeline
   |
   +---- StandardScaler
   |
   +---- KNN
   |
   v
Cross-Validation
   |
   v
Hyperparameter Search
   |
   +---- GridSearchCV
   |
   +---- RandomizedSearchCV
   |
   v
Best Model
   |
   v
Final Test Evaluation
```

The test set is kept separate so it can be used for the final evaluation after model selection.

## 15. Practical Implementation

The implementation uses:

* Python
* NumPy
* Scikit-learn
* K-Nearest Neighbors
* StandardScaler
* Pipeline
* Cross-Validation
* GridSearchCV
* RandomizedSearchCV

Run the examples with:

```bash
python examples.py
```

## 16. Key Takeaways

1. Cross-Validation provides a more robust estimate than relying on a single validation split.
2. K-Fold Cross-Validation divides the training data into multiple folds.
3. Stratified K-Fold preserves class proportions for classification tasks.
4. Hyperparameters control how a model is configured.
5. GridSearchCV systematically searches a specified hyperparameter grid.
6. RandomizedSearchCV samples hyperparameter combinations.
7. Pipelines combine preprocessing and modeling into one workflow.
8. Pipelines help reduce the risk of preprocessing-related data leakage.
9. The test set should remain untouched during model selection.
10. A good ML workflow requires more than simply choosing an algorithm.

## 17. Why This Matters for AI Engineering

These concepts form the foundation of reliable machine learning experimentation.

The same principles become important later in:

```text
Classical Machine Learning
        |
        v
Deep Learning
        |
        v
Hyperparameter Optimization
        |
        v
Experiment Tracking
        |
        v
MLOps
        |
        v
Production ML Systems
```

The tools may change, but the fundamental goal remains the same:

> Build models that generalize well to unseen data and evaluate them using a reliable methodology.

## 18. Documentation

Primary documentation:

* Scikit-learn Cross-Validation
* Scikit-learn Model Selection
* Scikit-learn Pipeline
* Scikit-learn GridSearchCV
* Scikit-learn RandomizedSearchCV

## Day 27 Completion Checklist

* [x] Understand Cross-Validation
* [x] Implement K-Fold Cross-Validation
* [x] Use `cross_val_score()`
* [x] Understand mean CV score
* [x] Understand standard deviation
* [x] Understand Stratified K-Fold
* [x] Understand Pipelines
* [x] Understand data leakage
* [x] Implement GridSearchCV
* [x] Implement RandomizedSearchCV
* [x] Tune a Pipeline
* [x] Evaluate the final model on the test set
* [x] Document the concepts
