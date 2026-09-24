# Day 29 - End-to-End ML Project: Credit Card Fraud Detection

## Objective

Build an end-to-end machine learning classification project for detecting fraudulent credit card transactions.

The project covers the complete machine learning workflow:

```text
Data
↓
Data Understanding
↓
Data Cleaning
↓
Train/Test Split
↓
Preprocessing
↓
Model Training
↓
Prediction
↓
Evaluation
↓
Model Comparison
```

## Problem Statement

Credit card fraud detection is a binary classification problem.

The goal is to classify each transaction as:

* `0` - Legitimate transaction
* `1` - Fraudulent transaction

The major challenge is class imbalance because fraudulent transactions represent a very small portion of all transactions.

Therefore, accuracy alone is not a sufficient evaluation metric.

## Dataset

Dataset:

**Credit Card Fraud Detection**

Source:

Kaggle - `mlg-ulb/creditcardfraud`

The dataset contains anonymized transaction features along with:

* `Time`
* `Amount`
* `V1` to `V28`
* `Class`

`Class` is the target variable.

## Why This Project Matters

End-to-end ML projects are important because real-world machine learning is not only about training a model.

A production ML workflow requires:

* Understanding the data
* Cleaning the data
* Preventing data leakage
* Selecting appropriate preprocessing
* Training models
* Evaluating multiple metrics
* Understanding business requirements
* Comparing model behavior

Fraud detection is a good example because the cost of different types of errors is not equal.

Missing a fraudulent transaction and incorrectly flagging a legitimate transaction have different consequences.

## Concepts Learned

### 1. Data Cleaning

Duplicate transactions were identified and removed.

```python
df = df.drop_duplicates()
```

### 2. Feature and Target Separation

```python
X = df.drop("Class", axis=1)
y = df["Class"]
```

`X` contains the input features.

`y` contains the target labels.

### 3. Stratified Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

`stratify=y` preserves the class distribution between training and testing data.

Mental model:

```text
Training Data → Learn
Testing Data  → Evaluate
```

The test set must remain unseen during model training.

### 4. Feature Scaling

`StandardScaler` was applied to:

* `Time`
* `Amount`

```python
scaler = StandardScaler()

X_train_scaled[["Time", "Amount"]] = scaler.fit_transform(
    X_train[["Time", "Amount"]]
)

X_test_scaled[["Time", "Amount"]] = scaler.transform(
    X_test[["Time", "Amount"]]
)
```

The scaler is fitted only on the training data.

```text
Training Data
     ↓
fit + transform
     ↓
Scaled Training Data

Test Data
     ↓
transform only
     ↓
Scaled Test Data
```

This prevents data leakage.

### 5. Class Imbalance

Fraud detection contains significantly fewer fraudulent transactions than legitimate transactions.

Therefore, the models were configured with:

```python
class_weight="balanced"
```

This gives greater importance to the minority class during training.

### 6. Logistic Regression

The first model was Logistic Regression.

```python
LogisticRegression(
    class_weight="balanced",
    random_state=42,
    max_iter=1000
)
```

Logistic Regression provides a strong baseline for binary classification.

### 7. Random Forest

The second model was Random Forest.

```python
RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)
```

Random Forest combines multiple decision trees to make predictions.

### 8. Confusion Matrix

The confusion matrix contains:

```text
                 Predicted
              Legit    Fraud

Actual Legit    TN       FP

Actual Fraud    FN       TP
```

Where:

* TN = True Negative
* FP = False Positive
* FN = False Negative
* TP = True Positive

For fraud detection:

* FN means a fraud transaction was missed.
* FP means a legitimate transaction was flagged as fraud.

### 9. Precision

Precision answers:

> Of all transactions predicted as fraud, how many were actually fraud?

```text
Precision = TP / (TP + FP)
```

High precision means fewer false fraud alerts.

### 10. Recall

Recall answers:

> Of all actual fraud transactions, how many did the model detect?

```text
Recall = TP / (TP + FN)
```

High recall means fewer fraudulent transactions are missed.

### 11. F1 Score

F1 Score combines precision and recall.

```text
F1 = 2 × (Precision × Recall)
     --------------------------
       Precision + Recall
```

It is useful when both precision and recall are important.

### 12. ROC-AUC

ROC-AUC evaluates how well the model separates the positive and negative classes across different classification thresholds.

The models were evaluated using predicted probabilities:

```python
model.predict_proba(X_test)[:, 1]
```

### 13. Precision-Recall Curve

The Precision-Recall curve shows the relationship between:

* Precision
* Recall

at different classification thresholds.

This is particularly useful for highly imbalanced classification problems.

## Model Results

| Metric    | Logistic Regression | Random Forest |
| --------- | ------------------: | ------------: |
| Accuracy  |              97.52% |        99.95% |
| Precision |               5.62% |        97.10% |
| Recall    |              87.37% |        70.53% |
| F1 Score  |              10.57% |        81.71% |
| ROC-AUC   |              96.58% |        92.46% |

## Confusion Matrices

### Logistic Regression

```text
[[55258  1393]
 [   12    83]]
```

Therefore:

```text
TN = 55258
FP = 1393
FN = 12
TP = 83
```

The model detected a large proportion of fraud transactions, but it also produced many false positives.

### Random Forest

```text
[[56649     2]
 [   28    67]]
```

Therefore:

```text
TN = 56649
FP = 2
FN = 28
TP = 67
```

Random Forest produced very few false positives, but missed more fraudulent transactions than Logistic Regression.

## Precision-Recall Trade-off

The project demonstrates an important machine learning concept:

> There is no universally optimal metric for fraud detection.

Logistic Regression:

```text
Higher Recall
Lower Precision
```

Random Forest:

```text
Higher Precision
Lower Recall
```

The appropriate model depends on the operational cost of:

* False positives
* False negatives

For example, a financial institution may have different requirements depending on whether its priority is catching more fraud or reducing unnecessary transaction blocks.

## End-to-End Architecture

```text
Credit Card Dataset
        ↓
Data Understanding
        ↓
Duplicate Removal
        ↓
Feature / Target Separation
        ↓
Stratified Train/Test Split
        ↓
Feature Scaling
        ↓
Class Imbalance Handling
        ↓
        ┌──────────────────────┐
        │                      │
        ↓                      ↓
Logistic Regression      Random Forest
        │                      │
        ↓                      ↓
   Predictions            Predictions
        │                      │
        └──────────┬───────────┘
                   ↓
             Model Evaluation
                   ↓
       ┌───────────┼────────────┐
       ↓           ↓            ↓
  Confusion     Precision     Recall
   Matrix                      ↓
       └───────────┬────────────┘
                   ↓
               F1 / ROC-AUC
                   ↓
          Precision-Recall Curve
                   ↓
            Model Comparison
```

## Why This Needs to Be Learned

End-to-end ML workflow is one of the most important skills for an ML Engineer.

Individual algorithms are only one part of machine learning.

Real ML systems require the ability to move from:

```text
Problem
  ↓
Data
  ↓
Preprocessing
  ↓
Model
  ↓
Evaluation
  ↓
Decision
```

This workflow becomes the foundation for later topics such as:

* Model deployment
* MLOps
* Model monitoring
* Feature engineering
* Model serving
* Production ML pipelines

## How Modern Technology Uses This

The same workflow is used in systems such as:

* Credit card fraud detection
* Payment risk detection
* Account takeover detection
* Spam detection
* Recommendation systems
* Customer churn prediction
* Transaction risk scoring
* Anomaly detection

Modern production systems extend this workflow with:

```text
ML Model
   ↓
API / Model Server
   ↓
Real-Time Prediction
   ↓
Monitoring
   ↓
Retraining
```

This connects classical machine learning with the MLOps and AI Engineering topics that come later in the 120-day roadmap.

## Important Lessons

1. Accuracy can be misleading for imbalanced datasets.
2. Precision and recall must be interpreted together.
3. Stratified splitting is important for imbalanced classification.
4. Test data must remain unseen during training.
5. Preprocessing must avoid data leakage.
6. `class_weight="balanced"` can help address class imbalance.
7. Confusion matrices provide detailed error information.
8. Precision-Recall curves are useful for imbalanced classification.
9. Model selection depends on the problem requirements.
10. An ML project is more than just training a model.

## Official Documentation

Scikit-learn documentation:

* Logistic Regression
* Random Forest
* StandardScaler
* train_test_split
* Classification Metrics
* Precision-Recall Curve

Official documentation:

https://scikit-learn.org/stable/

## Project Files

```text
Day-029-End-to-End-ML-Project/
│
├── README.md
└── examples.py
```

## Completion Checklist

* [x] Understand the problem
* [x] Load the dataset
* [x] Perform data understanding
* [x] Remove duplicates
* [x] Separate features and target
* [x] Perform stratified train/test split
* [x] Apply feature scaling
* [x] Prevent data leakage
* [x] Handle class imbalance
* [x] Train Logistic Regression
* [x] Train Random Forest
* [x] Generate predictions
* [x] Evaluate confusion matrix
* [x] Calculate precision
* [x] Calculate recall
* [x] Calculate F1 score
* [x] Calculate ROC-AUC
* [x] Generate classification report
* [x] Plot Precision-Recall curve
* [x] Compare models
* [x] Complete an end-to-end ML project

## Status

**Day 29/120 — Completed**

The complete end-to-end machine learning workflow was implemented using a real-world credit card fraud detection problem.
