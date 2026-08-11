# Day 18 — Regression & Linear Regression

## 🎯 Objective

Understand regression as a supervised learning problem and learn how Linear Regression learns parameters by minimizing squared prediction errors.

By the end of this day, the goal is to understand Linear Regression mathematically and implement it using scikit-learn rather than treating `LinearRegression()` as a black box.

---

# 1. Regression

## What is Regression?

Regression is a supervised learning task where the target variable is a **continuous numerical value**.

Examples:

* House price prediction
* Salary prediction
* Temperature prediction
* Sales forecasting
* Exam score prediction

### Mental Model

```text
Features
   ↓
Regression Model
   ↓
Continuous numerical prediction
```

Example:

```text
Hours Studied → Exam Score
House Features → House Price
```

## Regression vs Classification

| Regression                 | Classification            |
| -------------------------- | ------------------------- |
| Predicts continuous values | Predicts discrete classes |
| Price = ₹75,000            | Spam / Not Spam           |
| Temperature = 32.5°C       | Cat / Dog                 |
| Score = 87.4               | Pass / Fail               |

---

# 2. Linear Regression

Linear Regression models the relationship between input features and a numerical target using a linear function.

For one feature:

[
\hat{y}=b_0+b_1x
]

Where:

* (x) → input feature
* (\hat{y}) → predicted value
* (b_0) → intercept
* (b_1) → coefficient/slope

### Example

[
\hat{y}=35+7.5x
]

If:

[
x=4
]

then:

[
\hat{y}=35+7.5(4)=65
]

---

# 3. Intercept and Coefficient

## Intercept

The intercept (b_0) is the predicted target value when the feature is zero.

[
\hat{y}=b_0+b_1x
]

If:

[
b_0=40
]

then the model predicts 40 when (x=0).

### Mental Model

```text
Intercept → starting point of the line
```

---

## Coefficient / Slope

The coefficient (b_1) represents the change in the predicted target for a one-unit increase in the feature.

Example:

[
\hat{y}=40+6x
]

The coefficient is:

[
b_1=6
]

Therefore, increasing (x) by 1 increases the predicted value by 6.

### Mental Model

```text
Coefficient → rate of change / steepness of the line
```

---

# 4. Prediction

A Linear Regression model uses the learned parameters to make predictions.

[
\hat{y}=b_0+b_1x
]

Example:

[
b_0=0.667
]

[
b_1=1.5
]

For:

[
x=4
]

the prediction is:

[
\hat{y}=0.667+1.5(4)
]

[
\hat{y}\approx6.67
]

---

# 5. Residuals

A residual measures the difference between the actual target and the predicted target.

[
e_i=y_i-\hat{y}_i
]

Where:

* (y_i) → actual value
* (\hat{y}_i) → predicted value
* (e_i) → residual

### Example

```text
Actual     = 80
Predicted  = 75
```

[
e=80-75=5
]

Therefore, the residual is positive.

### Interpretation

```text
Positive residual → model underpredicted
Negative residual → model overpredicted
Zero residual     → perfect prediction
```

---

# 6. Absolute and Squared Errors

Residuals can be transformed in different ways.

### Absolute Error

[
|y-\hat{y}|
]

This prevents positive and negative residuals from cancelling.

### Squared Error

[
(y-\hat{y})^2
]

This also prevents cancellation and gives larger errors a stronger penalty.

Example:

```text
Error = 2  → Squared error = 4
Error = 10 → Squared error = 100
```

A large error receives a disproportionately larger penalty.

---

# 7. Least Squares

Linear Regression uses the **least-squares principle**.

The objective is to find parameters that minimize the sum of squared residuals:

[
RSS=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
]

Substituting the Linear Regression equation:

[
RSS=
\sum_{i=1}^{n}
(y_i-b_0-b_1x_i)^2
]

The model finds the values of (b_0) and (b_1) that minimize this objective.

### Mental Model

```text
Choose parameters
      ↓
Make predictions
      ↓
Calculate residuals
      ↓
Square residuals
      ↓
Add squared residuals
      ↓
Minimize the total
      ↓
Best-fit line
```

scikit-learn's `LinearRegression` implements Ordinary Least Squares and minimizes the residual sum of squares.

---

# 8. Finding the Parameters

The optimization problem is:

[
\min_{b_0,b_1}
\sum_{i=1}^{n}
(y_i-b_0-b_1x_i)^2
]

Taking partial derivatives and setting them to zero produces the **normal equations**.

For the intercept:

[
b_0=\bar{y}-b_1\bar{x}
]

For the slope:

[
b_1=
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
]

Therefore, the fitted regression line passes through:

[
(\bar{x},\bar{y})
]

### Important intuition

The slope can be viewed as:

[
b_1=
\frac{\text{how X and Y vary together}}
{\text{how much X varies}}
]

This connects Linear Regression with covariance and variance.

---

# 9. Simple Linear Regression

Simple Linear Regression uses one feature.

[
\hat{y}=b_0+b_1x
]

Example:

```text
Hours Studied → Exam Score
```

---

# 10. Multiple Linear Regression

Multiple Linear Regression uses multiple features.

[
\hat{y}
=======

b_0+b_1x_1+b_2x_2+\cdots+b_nx_n
]

Example:

```text
Hours Studied
Practice Tests
Attendance
       ↓
Exam Score
```

For example:

[
\hat{y}=20+3x_1+5x_2
]

Each coefficient represents the change in predicted target for a one-unit increase in that feature **while holding the other features constant**.

### Matrix Form

Multiple Linear Regression can be represented as:

[
\hat{\mathbf{y}}=X\boldsymbol{\beta}
]

with the least-squares objective:

[
\min_{\beta}|y-X\beta|^2
]

---

# 11. scikit-learn Implementation

```python
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3]]
y = [2, 4, 5]

model = LinearRegression()

model.fit(X, y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

prediction = model.predict([[4]])

print("Prediction:", prediction)
```

For this example, the learned model is approximately:

[
\hat{y}=0.667+1.5x
]

For (x=4):

[
\hat{y}\approx6.67
]

---

# 12. Important scikit-learn Attributes and Methods

## `fit()`

```python
model.fit(X, y)
```

Learns the model parameters from the training data.

Conceptually:

```text
X + y
 ↓
Least Squares Optimization
 ↓
Learn coefficients and intercept
```

## `coef_`

```python
model.coef_
```

Contains the learned coefficient(s).

For multiple features:

```text
[b1, b2, b3, ...]
```

## `intercept_`

```python
model.intercept_
```

Contains the learned intercept (b_0).

## `predict()`

```python
model.predict(X_new)
```

Uses the learned parameters to generate predictions.

The scikit-learn API defines `coef_` as the learned coefficients and `intercept_` as the intercept of the linear model.

---

# 13. Feature and Sample Shape

scikit-learn generally represents feature data as:

[
X.shape=(n_samples,n_features)
]

Example:

```python
X.shape = (100, 5)
```

means:

```text
100 samples
5 features
```

This convention is fundamental throughout the scikit-learn API.

---

# 14. Regression Evaluation Metrics

After training a model, we need to measure prediction quality.

The main metrics studied today were:

* MAE
* MSE
* RMSE
* R²

---

## Mean Absolute Error — MAE

[
MAE=
\frac{1}{n}
\sum_{i=1}^{n}|y_i-\hat{y}_i|
]

### Intuition

> Average absolute distance between actual and predicted values.

Example:

```text
Actual:     [10, 20, 30]
Predicted:  [12, 18, 25]
```

Residuals:

```text
[-2, +2, +5]
```

Absolute errors:

```text
[2, 2, 5]
```

Therefore:

[
MAE=\frac{2+2+5}{3}=3
]

MAE is expressed in the same units as the target.

---

# 15. Mean Squared Error — MSE

[
MSE=
\frac{1}{n}
\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
]

### Intuition

> Average squared prediction error.

MSE penalizes large errors more strongly than MAE.

Example:

```text
Error = 2  → 4
Error = 10 → 100
```

The large error receives a much larger penalty.

scikit-learn provides `mean_squared_error` for regression evaluation.

---

# 16. Root Mean Squared Error — RMSE

[
RMSE=\sqrt{MSE}
]

RMSE retains the original target units while preserving the squared-error sensitivity of MSE.

Example:

[
MSE=16
]

Therefore:

[
RMSE=\sqrt{16}=4
]

---

# 17. R² — Coefficient of Determination

R² measures model performance relative to predicting the mean of the target.

[
R^2=
1-\frac{SS_{res}}{SS_{tot}}
]

where:

[
SS_{res}=
\sum(y_i-\hat{y}_i)^2
]

and:

[
SS_{tot}=
\sum(y_i-\bar{y})^2
]

### Interpretation

```text
R² = 1
→ Perfect fit

R² = 0
→ Equivalent to mean-prediction baseline

R² < 0
→ Worse than the mean baseline
```

R² is **not accuracy** and should not be interpreted as "the model is X% accurate."

scikit-learn defines R² as the coefficient of determination and notes that it can be negative when the model performs worse than the constant mean baseline.

---

# 18. Train/Test Split

A model should not be evaluated only on the same data used for training.

We divide the dataset into:

```text
Dataset
   ↓
 ┌─────────────┐
 ↓             ↓
Training      Test
   ↓             ↓
fit()         predict()
```

### Training Data

Used to learn the model parameters.

### Test Data

Used to evaluate performance on unseen samples.

---

## Implementation

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

`train_test_split` creates random train/test subsets, and `test_size=0.2` means 20% of the samples are assigned to the test split. `random_state` makes the randomized split reproducible.

---

# 19. Complete Regression Workflow

```text
Data
 ↓
Train/Test Split
 ↓
Training Data
 ↓
Model.fit()
 ↓
Learn Parameters
 ↓
Test Data
 ↓
Model.predict()
 ↓
Compare y_test and predictions
 ↓
MAE / MSE / RMSE / R²
```

This workflow is the basic foundation for supervised machine learning.

---

# 20. Generalization

A model should perform well not only on training data but also on unseen data.

Example:

```text
Training R² = 0.95
Test R²     = 0.93
```

The small difference suggests reasonable generalization.

Example:

```text
Training R² = 0.98
Test R²     = 0.52
```

The large gap can be a warning sign of **overfitting**.

Overfitting will be studied more deeply in later model-selection topics.

---

# 21. Correlation vs Regression

Correlation and regression are related but answer different questions.

### Correlation

> How strongly and in what direction are two variables linearly related?

### Regression

> What relationship can be used to predict a target from one or more features?

Correlation does not automatically establish causation.

---

# 22. AI/ML Connection

Linear Regression introduces a general machine learning pattern:

```text
Data
 ↓
Model with Parameters
 ↓
Prediction
 ↓
Loss / Error
 ↓
Optimization
 ↓
Learned Parameters
 ↓
Prediction on New Data
```

For Linear Regression:

```text
Model:
ŷ = b₀ + b₁x

Objective:
Minimize Σ(y - ŷ)²

Parameters:
b₀, b₁
```

This pattern extends to more advanced models:

```text
Linear Regression
       ↓
Logistic Regression
       ↓
Neural Networks
       ↓
Deep Learning
       ↓
LLMs
```

The model, loss function, and optimization mechanism become more sophisticated, but the fundamental learning structure remains.

---

# 23. How This Concept Can Be Leveraged in Modern AI

Linear Regression is still useful for:

* Baseline models
* Interpretable predictive modeling
* Forecasting simple numerical relationships
* Establishing a benchmark before using complex models
* Understanding feature-target relationships
* Understanding optimization and loss functions
* Learning the mathematical foundations of machine learning

In modern AI systems, a simple model is often valuable as a **baseline**. A complex model should demonstrate that it provides meaningful improvement over a simpler baseline.

---

# 24. Key Takeaways

```text
Regression
→ Predict continuous numerical targets

Linear Regression
→ Models a target as a linear combination of features

Residual
→ Actual - Predicted

Least Squares
→ Minimize the sum of squared residuals

b₀
→ Intercept

b₁
→ Coefficient / slope

MAE
→ Average absolute error

MSE
→ Average squared error

RMSE
→ Square root of MSE

R²
→ Performance relative to mean-prediction baseline

Train/Test Split
→ Evaluate generalization on unseen data
```

---

# 25. Official Documentation

Primary library used today: **scikit-learn**

* [Linear Models / Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html)
* [LinearRegression API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [train_test_split API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
* [Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
* [Mean Absolute Error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
* [Mean Squared Error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
* [R² / Coefficient of Determination](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)

---

# 26. Completion Status

## Regression & Linear Regression

* [x] Regression
* [x] Regression vs Classification
* [x] Continuous targets
* [x] Linear Regression
* [x] Linear Regression equation
* [x] Intercept
* [x] Coefficient / slope
* [x] Prediction
* [x] Residuals
* [x] Absolute error
* [x] Squared error
* [x] Least Squares
* [x] RSS / SSE
* [x] Normal equations
* [x] Closed-form solution
* [x] Simple Linear Regression
* [x] Multiple Linear Regression
* [x] scikit-learn `LinearRegression`
* [x] `fit()`
* [x] `coef_`
* [x] `intercept_`
* [x] `predict()`
* [x] Feature/sample shapes
* [x] MAE
* [x] MSE
* [x] RMSE
* [x] R²
* [x] Train/Test Split
* [x] Generalization
* [x] Basic overfitting intuition
* [x] Correlation vs Regression
* [x] AI/ML connection

