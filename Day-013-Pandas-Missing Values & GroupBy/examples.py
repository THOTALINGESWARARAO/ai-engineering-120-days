"""
Day 13/120 — Pandas
"""

import numpy as np
import pandas as pd


# Missing value representations

df = pd.DataFrame({
    "name": ["Arun", "Ravi", None, "Kiran"],
    "cgpa": [8.5, np.nan, 9.1, 7.8],
    "joining_date": pd.to_datetime([
        "2026-08-01",
        "2026-08-02",
        None,
        "2026-08-04"
    ])
})

print("\nMissing value representations")
print(df)

nullable_scores = pd.Series(
    [90, pd.NA, 75],
    dtype="Int64"
)

print("\npd.NA with nullable integer")
print(nullable_scores)


# Detecting missing values

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [90, np.nan, 75, np.nan]
})

print("\nisna()")
print(df.isna())

print("\nnotna()")
print(df.notna())


# Counting missing values

print("\nCounting missing values")
print(df.isna().sum())

print("\nCounting missing values in score")
print(df["score"].isna().sum())


# Filtering non-missing values

available_scores = df[df["score"].notna()]

print("\nFiltering non-missing values")
print(available_scores)


# Correct way to check a missing value

value = np.nan

print("\nComparing with np.nan")
print(value == np.nan)

print("\npd.isna()")
print(pd.isna(value))


# dropna()

df = pd.DataFrame({
    "name": ["Arun", "Ravi", "Priya", "Kiran"],
    "cgpa": [8.5, np.nan, 9.1, 7.8],
    "salary": [600000, 550000, 700000, np.nan]
})

clean_df = df.dropna()

print("\ndropna()")
print(clean_df)


# dropna() does not modify original DataFrame

print("\nOriginal DataFrame after dropna()")
print(df)


# Drop rows containing missing values

print("\ndropna(axis=0)")
print(df.dropna(axis=0))


# Drop columns containing missing values

print("\ndropna(axis=1)")
print(df.dropna(axis=1))


# how="any"

example = pd.DataFrame({
    "A": [10, np.nan, np.nan],
    "B": [20, 30, np.nan]
})

print('\ndropna(how="any")')
print(example.dropna(how="any"))


# how="all"

print('\ndropna(how="all")')
print(example.dropna(how="all"))


# subset

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "cgpa": [8.5, np.nan, 9.0],
    "salary": [np.nan, 500000, 700000]
})

print("\ndropna() with subset=['cgpa']")
print(df.dropna(subset=["cgpa"]))

print("\ndropna() with subset=['cgpa', 'salary']")
print(df.dropna(subset=["cgpa", "salary"]))


# thresh

df = pd.DataFrame({
    "A": [1, 4, np.nan, np.nan],
    "B": [2, np.nan, np.nan, np.nan],
    "C": [3, 6, 9, np.nan]
})

print("\ndropna(thresh=2)")
print(df.dropna(thresh=2))


# fillna() with a constant

df = pd.DataFrame({
    "skill": ["Python", None, "Java", None]
})

df["skill"] = df["skill"].fillna("Unknown")

print("\nfillna() with constant")
print(df)


# Mean imputation

df = pd.DataFrame({
    "cgpa": [8.0, 9.0, np.nan, 7.0]
})

mean_cgpa = df["cgpa"].mean()
df["cgpa"] = df["cgpa"].fillna(mean_cgpa)

print("\nMean imputation")
print("Mean:", mean_cgpa)
print(df)


# Median imputation

df = pd.DataFrame({
    "salary": [
        30000,
        32000,
        35000,
        40000,
        1000000,
        np.nan
    ]
})

median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

print("\nMedian imputation")
print("Median:", median_salary)
print(df)


# Mode imputation

df = pd.DataFrame({
    "city": [
        "Hyderabad",
        "Bangalore",
        "Hyderabad",
        None,
        "Hyderabad"
    ]
})

mode_city = df["city"].mode()[0]
df["city"] = df["city"].fillna(mode_city)

print("\nMode imputation")
print("Mode:", mode_city)
print(df)


# Forward fill

df = pd.DataFrame({
    "temperature": [25, 26, np.nan, 27]
})

df["temperature"] = df["temperature"].ffill()

print("\nForward fill - ffill()")
print(df)


# Backward fill

df = pd.DataFrame({
    "temperature": [25, 26, np.nan, 27]
})

df["temperature"] = df["temperature"].bfill()

print("\nBackward fill - bfill()")
print(df)


# Interpolation

df = pd.DataFrame({
    "temperature": [20, np.nan, 24]
})

df["temperature"] = df["temperature"].interpolate()

print("\nInterpolation")
print(df)


# Missing-value practice example

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [80, np.nan, 90, 70]
})

mean_score = df["score"].mean()
df["score"] = df["score"].fillna(mean_score)

print("\nMissing-value practice example")
print("Mean score:", mean_score)
print(df)


# GroupBy

df = pd.DataFrame({
    "department": ["AI", "Web", "AI", "Web", "AI"],
    "salary": [60000, 40000, 80000, 50000, 70000]
})

result = df.groupby("department")["salary"].mean()

print("\nBasic GroupBy")
print(result)


# GroupBy object

grouped = df.groupby("department")

print("\nGroupBy object")
print(grouped)


# Inspect groups

print("\nInspect GroupBy groups")
print(grouped.groups)


# Get a specific group

print("\nget_group('AI')")
print(grouped.get_group("AI"))


# Sum aggregation

print("\nGroupBy sum()")
print(df.groupby("department")["salary"].sum())


# Mean aggregation

print("\nGroupBy mean()")
print(df.groupby("department")["salary"].mean())


# Minimum aggregation

print("\nGroupBy min()")
print(df.groupby("department")["salary"].min())


# Maximum aggregation

print("\nGroupBy max()")
print(df.groupby("department")["salary"].max())


# count() vs size()

df_missing = pd.DataFrame({
    "department": ["AI", "AI", "Web", "Web"],
    "salary": [60000, np.nan, 40000, 50000]
})

print("\nGroupBy count()")
print(
    df_missing.groupby("department")["salary"].count()
)

print("\nGroupBy size()")
print(
    df_missing.groupby("department").size()
)


# Aggregating multiple columns

df = pd.DataFrame({
    "department": ["AI", "Web", "AI", "Web"],
    "salary": [60000, 40000, 80000, 50000],
    "experience": [2, 1, 4, 3]
})

result = (
    df.groupby("department")[["salary", "experience"]]
    .mean()
)

print("\nGroupBy with multiple columns")
print(result)


# Multiple aggregations with agg()

result = (
    df.groupby("department")["salary"]
    .agg(["mean", "min", "max"])
)

print("\nMultiple aggregations with agg()")
print(result)


# Different aggregations for different columns

result = df.groupby("department").agg({
    "salary": "mean",
    "experience": "max"
})

print("\nDifferent aggregations for different columns")
print(result)


# Named aggregation

summary = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    max_experience=("experience", "max")
)

print("\nNamed aggregation")
print(summary)


# Grouping by multiple columns

df = pd.DataFrame({
    "department": ["AI", "AI", "AI", "Web", "Web"],
    "level": [
        "Junior",
        "Senior",
        "Junior",
        "Junior",
        "Senior"
    ],
    "salary": [40000, 80000, 50000, 35000, 70000]
})

result = (
    df.groupby(["department", "level"])["salary"]
    .mean()
)

print("\nGrouping by multiple columns")
print(result)


# as_index=False

result = (
    df.groupby("department", as_index=False)["salary"]
    .mean()
)

print("\nas_index=False")
print(result)


# ML feature engineering with GroupBy

transactions = pd.DataFrame({
    "user_id": [101, 101, 102, 101, 102],
    "amount": [500, 1000, 200, 700, 800]
})

features = transactions.groupby("user_id").agg(
    total_spending=("amount", "sum"),
    avg_transaction=("amount", "mean"),
    transaction_count=("amount", "count"),
    max_transaction=("amount", "max")
)

print("\nML feature engineering with GroupBy")
print(features)