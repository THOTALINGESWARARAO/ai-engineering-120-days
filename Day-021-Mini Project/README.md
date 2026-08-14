# Day 21 — Iris Flower Classification

## Overview

Built a complete machine learning classification project using the Iris dataset and a Decision Tree Classifier.

The project demonstrates the basic end-to-end supervised machine learning workflow:

```text
Dataset
   ↓
Features and Target
   ↓
Train/Test Split
   ↓
Model Creation
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
New Data Prediction
```

## Concepts Learned

* Iris dataset
* Features and target
* `X` and `y`
* Dataset shape
* Train/test split
* `test_size`
* `random_state`
* `stratify`
* Decision Tree Classification
* Model training with `fit()`
* Prediction with `predict()`
* Accuracy
* Classification report
* Precision
* Recall
* F1-score
* Support
* Confusion matrix
* Prediction on new data
* Complete supervised ML workflow

## 1. Iris Dataset

The Iris dataset contains 150 flower samples and 4 numerical features.

### Features

* Sepal length
* Sepal width
* Petal length
* Petal width

### Target Classes

```text
0 → setosa
1 → versicolor
2 → virginica
```

The feature matrix has the shape:

```python
X.shape
# (150, 4)
```

The target vector has the shape:

```python
y.shape
# (150,)
```

## 2. Features and Target

`X` contains the input features used by the model.

```python
X = iris.data
```

`y` contains the target classes the model needs to learn.

```python
y = iris.target
```

The model learns the relationship:

```text
X → y
```

## 3. Train/Test Split

The dataset is divided into training and testing data.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

With `test_size=0.2`:

```text
80% → Training data
20% → Testing data
```

For 150 samples:

```text
120 → Training
30  → Testing
```

`random_state=42` makes the split reproducible.

`stratify=y` keeps the class distribution balanced between training and testing data.

## 4. Decision Tree Classifier

A Decision Tree learns decision rules from the training data and uses those rules to classify new observations.

```python
model = DecisionTreeClassifier(random_state=42)
```

Conceptually:

```text
Flower measurements
        ↓
Decision rules
        ↓
Flower species
```

## 5. Model Training

The model learns from the training data using `fit()`.

```python
model.fit(X_train, y_train)
```

During training, the Decision Tree learns patterns that help distinguish the three flower classes.

## 6. Prediction

After training, the model predicts the classes of previously unseen test samples.

```python
y_pred = model.predict(X_test)
```

The predictions can then be compared with the actual values:

```text
y_test → Actual classes
y_pred → Predicted classes
```

## 7. Accuracy

Accuracy measures the proportion of correct predictions.

```python
accuracy = accuracy_score(y_test, y_pred)
```

For this project, the model achieved approximately:

```text
Accuracy = 0.93
```

or:

```text
93%
```

The test set contained 30 samples, and the model correctly classified 28 of them.

## 8. Classification Report

The classification report provides several evaluation metrics.

```python
classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)
```

It includes:

### Precision

Of the samples predicted as a particular class, how many were actually that class?

```text
Precision = Correct Positive Predictions / All Positive Predictions
```

### Recall

Of the samples that actually belong to a class, how many did the model correctly identify?

```text
Recall = Correct Positive Predictions / All Actual Positives
```

### F1-score

The harmonic mean of precision and recall.

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

### Support

The number of actual samples belonging to each class in the test set.

## 9. Confusion Matrix

The confusion matrix shows where the model's predictions were correct or incorrect.

```python
confusion_matrix(y_test, y_pred)
```

Example result:

```text
[[10  0  0]
 [ 0  9  1]
 [ 0  1  9]]
```

Interpretation:

```text
Setosa:
10 correctly classified

Versicolor:
9 correctly classified
1 classified as Virginica

Virginica:
9 correctly classified
1 classified as Versicolor
```

The model had difficulty distinguishing two samples between:

```text
Versicolor ↔ Virginica
```

## 10. Predicting New Data

A new flower can be passed to the trained model.

```python
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)
```

The predicted numerical class can be converted into its actual class name:

```python
iris.target_names[prediction[0]]
```

Output:

```text
setosa
```

## Complete Workflow

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("New Flower Prediction:")
print(iris.target_names[prediction[0]])
```

## AI/ML Connection

The same workflow is used in larger real-world machine learning systems:

```text
Real-world Dataset
       ↓
Feature Engineering
       ↓
Train/Test Split
       ↓
Model Selection
       ↓
Training
       ↓
Prediction
       ↓
Evaluation
       ↓
Deployment
```

The Iris project is a small example of the same fundamental pipeline used for tasks such as:

* Customer classification
* Fraud detection
* Spam detection
* Medical classification
* Image classification
* Recommendation systems

The dataset and model may change, but the core workflow remains similar.

## Need to Learn Next

The project intentionally does not cover advanced model optimization yet.

Topics for later:

* Cross-validation
* Hyperparameter tuning
* Decision Tree hyperparameters
* Overfitting and underfitting
* Feature importance
* Random Forest
* Model comparison
* Pipeline
* Feature preprocessing

## Official Documentation

The concepts in this project are based on the official scikit-learn documentation:

* `load_iris`
* `train_test_split`
* `DecisionTreeClassifier`
* `accuracy_score`
* `classification_report`
* `confusion_matrix`

## Project Status

* [x] Load Iris dataset
* [x] Understand features and target
* [x] Inspect dataset shape
* [x] Split dataset into training and testing data
* [x] Create Decision Tree classifier
* [x] Train the model
* [x] Generate predictions
* [x] Calculate accuracy
* [x] Generate classification report
* [x] Generate confusion matrix
* [x] Predict a new flower
* [x] Understand the complete supervised ML workflow

Day 21 — Completed.
