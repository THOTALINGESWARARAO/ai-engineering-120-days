"""
Day 28 - XGBoost, LightGBM and CatBoost

Topics:
- XGBoost
- LightGBM
- CatBoost
- Gradient Boosting
- Histogram-based learning
- Leaf-wise tree growth
- Categorical feature handling
- Model comparison
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


# Load dataset

URL = (
    "https://raw.githubusercontent.com/"
    "datasciencedojo/datasets/master/titanic.csv"
)

df = pd.read_csv(URL)

print("Dataset shape:", df.shape)
print(df.head())


# Select features and target

features = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked"
]

X = df[features].copy()
y = df["Survived"]


# Handle missing values

X["Age"] = X["Age"].fillna(X["Age"].median())
X["Embarked"] = X["Embarked"].fillna(X["Embarked"].mode()[0])


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Preprocessing for XGBoost and LightGBM

categorical_features = [
    "Sex",
    "Embarked"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)


# XGBoost

xgb_model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42,
    eval_metric="logloss"
)

xgb_model.fit(
    X_train_encoded,
    y_train
)

xgb_predictions = xgb_model.predict(X_test_encoded)

xgb_accuracy = accuracy_score(
    y_test,
    xgb_predictions
)

print("XGBoost Accuracy:", xgb_accuracy)


# LightGBM

lgb_model = LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=31,
    random_state=42,
    verbosity=-1
)

lgb_model.fit(
    X_train_encoded,
    y_train
)

lgb_predictions = lgb_model.predict(X_test_encoded)

lgb_accuracy = accuracy_score(
    y_test,
    lgb_predictions
)

print("LightGBM Accuracy:", lgb_accuracy)


# CatBoost

cat_features = [
    "Sex",
    "Embarked"
]

cat_model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    loss_function="Logloss",
    random_seed=42,
    verbose=False
)

cat_model.fit(
    X_train,
    y_train,
    cat_features=cat_features
)

cat_predictions = cat_model.predict(X_test)

cat_accuracy = accuracy_score(
    y_test,
    cat_predictions
)

print("CatBoost Accuracy:", cat_accuracy)


# Model comparison

results = pd.DataFrame({
    "Model": [
        "XGBoost",
        "LightGBM",
        "CatBoost"
    ],
    "Accuracy": [
        xgb_accuracy,
        lgb_accuracy,
        cat_accuracy
    ]
})

print("\nModel Comparison:")
print(results.to_string(index=False))


# Feature importance

feature_names = preprocessor.get_feature_names_out()

xgb_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": xgb_model.feature_importances_
})

xgb_importance = xgb_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nXGBoost Feature Importance:")
print(xgb_importance.to_string(index=False))


lgb_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": lgb_model.feature_importances_
})

lgb_importance = lgb_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nLightGBM Feature Importance:")
print(lgb_importance.to_string(index=False))


cat_importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": cat_model.feature_importances_
})

cat_importance = cat_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nCatBoost Feature Importance:")
print(cat_importance.to_string(index=False))
