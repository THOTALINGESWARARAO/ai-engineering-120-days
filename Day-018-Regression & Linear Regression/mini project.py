import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

X = np.array([
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4],
    [2200, 4],
    [2500, 4],
    [2800, 5],
    [3000, 5],
    [3500, 5],
])

y = np.array([
    40,
    48,
    60,
    70,
    82,
    90,
    100,
    115,
    125,
    145,
])

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(x_test)

print("Actual prices:", y_test)
print("Predicted prices:", y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

new_house = np.array([[2300, 4]])
predicted_price = model.predict(new_house)
print("Predicted price:", predicted_price[0])