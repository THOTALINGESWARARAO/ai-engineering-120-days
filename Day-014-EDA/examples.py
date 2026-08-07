import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset/titanic.csv")

# Display dataset
print(df.head())
print(df.tail())
print(df.sample(5))

# Dataset information
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()

# Descriptive statistics
print(df.describe())
print(df.describe(include="str"))

# Missing values
print(df.isnull().sum())
print((df.isnull().sum() / len(df)) * 100)

# Duplicate rows
print(df.duplicated().sum())

# Unique values
print(df.nunique())

# Value counts
print(df["pclass"].value_counts())
print(df["sex"].value_counts())
print(df["embarked"].value_counts())
print(df["survived"].value_counts())

# Numerical analysis
print(df["age"].mean())
print(df["age"].median())
print(df["fare"].min())
print(df["fare"].max())

# GroupBy analysis
print(df.groupby("sex")["survived"].mean())
print(df.groupby("pclass")["fare"].mean())
print(df.groupby("pclass")["survived"].mean())

# Filtering
print(df[df["age"] > 50])
print(df[df["fare"] > 100])
print(df[(df["sex"] == "female") & (df["age"] > 30)])

# Sorting
print(df.sort_values(by="fare", ascending=False))

# Feature engineering
df["FamilySize"] = df["sibsp"] + df["parch"] + 1
print(df[["sibsp", "parch", "FamilySize"]].head())

# Correlation
print(df.corr(numeric_only=True))
