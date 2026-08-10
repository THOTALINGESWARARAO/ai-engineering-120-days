"""
Day 17/120 - Data Preprocessing

Topics:
1. Train/Test Split
2. Min-Max Scaling
3. Standardization
4. fit(), transform(), fit_transform()
5. Data Leakage
6. One-Hot Encoding
7. Ordinal Encoding
8. ColumnTransformer
9. Pipeline
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    OneHotEncoder,
    OrdinalEncoder,
)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Train/Test Split

X = pd.DataFrame({
    "Age": [22, 25, 31, 35, 28, 40, 24, 45, 29, 33],
    "Salary": [
        30000, 45000, 60000, 80000, 50000,
        90000, 35000, 100000, 55000, 70000
    ],
})

y = pd.Series([0, 0, 1, 1, 1, 1, 0, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("Original shape:", X.shape)
print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)


# 2. Min-Max Scaling

age = [[20], [30], [40]]

minmax_scaler = MinMaxScaler()

age_scaled = minmax_scaler.fit_transform(age)

print("Original age:")
print(age)

print("Min-Max scaled age:")
print(age_scaled)


# 3. Standardization

age = [[20], [30], [40], [50], [60]]

standard_scaler = StandardScaler()

age_standardized = standard_scaler.fit_transform(age)

print("Original age:")
print(age)

print("Standardized age:")
print(age_standardized)

print("Mean learned by scaler:")
print(standard_scaler.mean_)

print("Standard deviation learned by scaler:")
print(standard_scaler.scale_)


# 4. fit(), transform(), fit_transform()

train_data = [[10], [20], [30], [40]]
test_data = [[15], [25], [35]]

scaler = StandardScaler()

scaler.fit(train_data)

train_transformed = scaler.transform(train_data)
test_transformed = scaler.transform(test_data)

print("Training data:")
print(train_data)

print("Training transformed:")
print(train_transformed)

print("Test data:")
print(test_data)

print("Test transformed using training parameters:")
print(test_transformed)

# Equivalent:
# train_transformed = scaler.fit_transform(train_data)


# 5. Data Leakage

print("""
Data Leakage:

Wrong:
scaler.fit(X)

Correct:
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

The test data must not be used to learn preprocessing parameters.
""")


# 6. One-Hot Encoding

cities = [
    ["Guntur"],
    ["Hyderabad"],
    ["Vijayawada"],
    ["Guntur"],
]

one_hot_encoder = OneHotEncoder(sparse_output=False)

cities_encoded = one_hot_encoder.fit_transform(cities)

print("Original cities:")
print(cities)

print("Categories:")
print(one_hot_encoder.categories_)

print("One-Hot encoded cities:")
print(cities_encoded)


# 7. Ordinal Encoding

sizes = [
    ["Small"],
    ["Medium"],
    ["Large"],
    ["Medium"],
]

ordinal_encoder = OrdinalEncoder(
    categories=[
        ["Small", "Medium", "Large"]
    ]
)

sizes_encoded = ordinal_encoder.fit_transform(sizes)

print("Original sizes:")
print(sizes)

print("Ordinal encoded sizes:")
print(sizes_encoded)


# 8. ColumnTransformer

data = pd.DataFrame({
    "Age": [22, 25, 31, 35, 28],
    "Salary": [30000, 45000, 60000, 80000, 50000],
    "City": [
        "Guntur",
        "Hyderabad",
        "Guntur",
        "Vijayawada",
        "Hyderabad",
    ],
})

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            StandardScaler(),
            numeric_features,
        ),
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False,
            ),
            categorical_features,
        ),
    ]
)

processed_data = preprocessor.fit_transform(data)

print("Original data:")
print(data)

print("Processed data:")
print(processed_data)


# 9. Pipeline

data = pd.DataFrame({
    "Age": [22, 25, 31, 35, 28, 40, 24, 45, 29, 33],
    "Salary": [
        30000, 45000, 60000, 80000, 50000,
        90000, 35000, 100000, 55000, 70000
    ],
    "City": [
        "Guntur",
        "Hyderabad",
        "Guntur",
        "Vijayawada",
        "Hyderabad",
        "Guntur",
        "Vijayawada",
        "Hyderabad",
        "Guntur",
        "Vijayawada",
    ],
    "Purchased": [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
})

X = data.drop("Purchased", axis=1)
y = data["Purchased"]


# 10. Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)


# 11. Feature Groups

numeric_features = ["Age", "Salary"]
categorical_features = ["City"]


# 12. Preprocessing

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            StandardScaler(),
            numeric_features,
        ),
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False,
            ),
            categorical_features,
        ),
    ]
)


# 13. Complete Pipeline

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression()),
])


# 14. Train

model.fit(X_train, y_train)


# 15. Predict

predictions = model.predict(X_test)


# 16. Evaluate

accuracy = accuracy_score(y_test, predictions)

print("Test data:")
print(X_test)

print("Actual values:")
print(y_test.to_numpy())

print("Predictions:")
print(predictions)

print("Accuracy:", accuracy)