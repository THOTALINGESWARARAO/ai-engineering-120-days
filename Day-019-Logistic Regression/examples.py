# Day 19 - Logistic Regression

from math import exp

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


# Sigmoid function
def sigmoid(z):
    return 1 / (1 + exp(-z))


print(sigmoid(-5))
print(sigmoid(0))
print(sigmoid(5))


# Logistic Regression model
X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# Class prediction
predictions = model.predict(X_test)

print(predictions[:10])


# Probability prediction
probabilities = model.predict_proba(X_test)

print(probabilities[:5])


# Class 1 probabilities
class_1_probabilities = probabilities[:, 1]

print(class_1_probabilities[:10])


# Classification threshold
threshold = 0.7

custom_predictions = (
    class_1_probabilities >= threshold
).astype(int)

print(custom_predictions[:10])


# Model coefficients and intercept
print(model.coef_)
print(model.intercept_)


# Classification metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:")
print(cm)


# Regularization
model_c_01 = LogisticRegression(
    C=0.1,
    max_iter=1000
)

model_c_10 = LogisticRegression(
    C=10,
    max_iter=1000
)

model_c_01.fit(X_train, y_train)
model_c_10.fit(X_train, y_train)

print(model_c_01.coef_)
print(model_c_10.coef_)