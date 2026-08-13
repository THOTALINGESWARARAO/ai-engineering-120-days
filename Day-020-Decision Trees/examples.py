#Day-20 Decision Trees: classification, regression, splitting, complexity control, and feature importance

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_text
from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np


# Classification

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

classifier = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)

print("Classification Accuracy:", accuracy_score(y_test, predictions))
print("Classification Predictions:", predictions[:5])


# Tree structure

tree_rules = export_text(
    classifier,
    feature_names=iris.feature_names
)

print("\nDecision Tree Rules:")
print(tree_rules)


# Feature importance

print("Feature Importance:")

for feature, importance in zip(
    iris.feature_names,
    classifier.feature_importances_
):
    print(feature, importance)


# Regression

X_reg = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

y_reg = np.array([
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
])

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.25,
    random_state=42
)

regressor = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

regressor.fit(X_train_reg, y_train_reg)

reg_predictions = regressor.predict(X_test_reg)

print("\nRegression Predictions:", reg_predictions)
print(
    "Regression Mean Squared Error:",
    mean_squared_error(y_test_reg, reg_predictions)
)


# Controlling tree complexity

simple_tree = DecisionTreeClassifier(
    max_depth=2,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

simple_tree.fit(X_train, y_train)

simple_predictions = simple_tree.predict(X_test)

print(
    "\nAccuracy with Controlled Tree:",
    accuracy_score(y_test, simple_predictions)
)