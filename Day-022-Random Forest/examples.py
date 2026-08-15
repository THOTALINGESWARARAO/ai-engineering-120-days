"""
Day 22 — Random Forest
AI Engineering in 120 Days

This file demonstrates the core Random Forest concepts learned today:
1. Creating a Random Forest classifier
2. Training and prediction
3. Model evaluation
4. Important hyperparameters
5. Feature importance
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


# ============================================================
# 2. LOAD DATASET
# ============================================================

# Load the built-in Iris classification dataset.
iris = load_iris()

# X contains the input features.
X = iris.data

# y contains the target labels.
y = iris.target

# Feature names help us understand the columns in X.
feature_names = iris.feature_names

print("Feature names:")
print(feature_names)

print("\nDataset shape:")
print(X.shape)


# ============================================================
# 3. SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

# The training set is used to learn patterns.
# The test set is used to evaluate how well the model
# generalizes to unseen data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)


# ============================================================
# 4. CREATE THE RANDOM FOREST MODEL
# ============================================================

# n_estimators=100 means the forest contains 100 decision trees.
#
# random_state=42 makes the experiment reproducible.
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)


# ============================================================
# 5. TRAIN THE MODEL
# ============================================================

# The Random Forest learns patterns from the training data.
model.fit(X_train, y_train)


# ============================================================
# 6. MAKE PREDICTIONS
# ============================================================

# Predict the class of each sample in the test set.
y_pred = model.predict(X_test)


# ============================================================
# 7. EVALUATE THE MODEL
# ============================================================

# Accuracy measures the proportion of correct predictions.
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# Classification report provides precision, recall,
# F1-score, and support for each class.
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion matrix shows actual classes versus predicted classes.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ============================================================
# 8. FEATURE IMPORTANCE
# ============================================================

# Random Forest can estimate how useful each feature was
# for making predictions.
importances = model.feature_importances_

print("\nFeature Importance:")

for feature_name, importance in zip(feature_names, importances):
    print(f"{feature_name}: {importance:.4f}")


# ============================================================
# 9. UNDERSTANDING IMPORTANT HYPERPARAMETERS
# ============================================================

# n_estimators:
# Controls the number of trees in the forest.
#
# max_depth:
# Controls the maximum depth of each tree.
#
# max_features:
# Controls how many features are considered when looking
# for the best split.
#
# min_samples_split:
# Minimum number of samples required to split an internal node.
#
# min_samples_leaf:
# Minimum number of samples required at a leaf node.

experiment_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    max_features="sqrt",
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42,
)

experiment_model.fit(X_train, y_train)

experiment_predictions = experiment_model.predict(X_test)

print("\nExperiment Model Accuracy:")
print(accuracy_score(y_test, experiment_predictions))


# ============================================================
# 10. CONCEPTUAL MODEL OF RANDOM FOREST
# ============================================================

"""
A Random Forest can be understood conceptually as:

                 Training Data
                       |
          +------------+------------+
          |            |            |
     Bootstrap     Bootstrap    Bootstrap
      Sample 1      Sample 2      Sample 3
          |            |            |
        Tree 1       Tree 2       Tree 3
          |            |            |
          +------------+------------+
                       |
                Combine Predictions
                       |
                 Final Prediction

Randomness comes from:
1. Bootstrap samples
2. Random feature selection at splits

The goal is to create diverse trees whose combined prediction
is generally more robust than the prediction of one tree.
"""


# ============================================================
# 11. QUICK REFERENCE
# ============================================================

print("\nRandom Forest Summary:")
print("- Many Decision Trees")
print("- Bootstrap sampling")
print("- Random feature selection")
print("- Classification: combine tree predictions")
print("- Regression: average tree predictions")
print("- Main benefit: reduced variance and better generalization")