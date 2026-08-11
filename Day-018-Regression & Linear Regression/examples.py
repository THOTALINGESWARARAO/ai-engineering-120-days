import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


# Simple Linear Regression

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 5])

model = LinearRegression()
model.fit(X, y)

print("Simple Linear Regression")
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

prediction = model.predict([[4]])
print("Prediction for x=4:", prediction[0])


# Linear Regression Equation

b1 = model.coef_[0]
b0 = model.intercept_

x = 4
manual_prediction = b0 + b1 * x

print("\nLinear Regression Equation")
print("b0:", b0)
print("b1:", b1)
print("Manual prediction:", manual_prediction)
print("Model prediction:", model.predict([[x]])[0])


# Residuals

predictions = model.predict(X)
residuals = y - predictions

print("\nResiduals")
print("Actual:", y)
print("Predicted:", predictions)
print("Residuals:", residuals)


# Least Squares and RSS

squared_residuals = residuals ** 2
rss = np.sum(squared_residuals)

print("\nLeast Squares")
print("Squared residuals:", squared_residuals)
print("RSS:", rss)


# Mean Absolute Error

mae = np.mean(np.abs(residuals))

print("\nMean Absolute Error")
print("MAE:", mae)


# Mean Squared Error

mse = np.mean(residuals ** 2)

print("\nMean Squared Error")
print("MSE:", mse)


# Root Mean Squared Error

rmse = np.sqrt(mse)

print("\nRoot Mean Squared Error")
print("RMSE:", rmse)


# R2 Score

r2 = r2_score(y, predictions)

print("\nR2 Score")
print("R2:", r2)


# Multiple Linear Regression

X_multiple = np.array([
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 2],
    [5, 3],
])

y_multiple = np.array([50, 55, 65, 70, 80])

multiple_model = LinearRegression()
multiple_model.fit(X_multiple, y_multiple)

print("\nMultiple Linear Regression")
print("Coefficients:", multiple_model.coef_)
print("Intercept:", multiple_model.intercept_)

new_student = np.array([[6, 2]])
multiple_prediction = multiple_model.predict(new_student)

print("Prediction:", multiple_prediction[0])


# Features and Samples

print("\nFeature and Sample Shape")
print("X shape:", X_multiple.shape)
print("Number of samples:", X_multiple.shape[0])
print("Number of features:", X_multiple.shape[1])


# Train/Test Split

X_regression = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10],
])

y_regression = np.array([
    12,
    15,
    18,
    21,
    24,
    28,
    30,
    33,
    36,
    39,
])

X_train, X_test, y_train, y_test = train_test_split(
    X_regression,
    y_regression,
    test_size=0.2,
    random_state=42,
)

test_model = LinearRegression()
test_model.fit(X_train, y_train)

y_pred = test_model.predict(X_test)

print("\nTrain/Test Split")
print("Training samples:", len(X_train))
print("Test samples:", len(X_test))
print("Test predictions:", y_pred)
print("Test actual values:", y_test)


# Regression Evaluation on Test Data

test_mae = mean_absolute_error(y_test, y_pred)
test_mse = mean_squared_error(y_test, y_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_pred)

print("\nTest Set Evaluation")
print("MAE:", test_mae)
print("MSE:", test_mse)
print("RMSE:", test_rmse)
print("R2:", test_r2)