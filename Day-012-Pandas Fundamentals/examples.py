"""
Day 12 - Pandas Fundamentals
"""

import pandas as pd

# 1. Creating Series

s = pd.Series([10, 20, 30])
print(s)

# 2. Series with Custom Index

marks = pd.Series(
    [85, 92, 78],
    index=["Alice", "Bob", "Charlie"],
    name="Marks"
)

print(marks)

# 3. Series Attributes

print(marks.index)
print(marks.values)
print(marks.dtype)
print(marks.name)

# 4. Series from Dictionary

student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

series_dict = pd.Series(student_marks)

print(series_dict)

# 5. Label vs Position

print(marks.loc["Bob"])
print(marks.iloc[1])

# 6. Series Operations

numbers = pd.Series([10, 20, 30])

print(numbers + 5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 2)
print(numbers > 15)

# 7. Automatic Index Alignment

s1 = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

s2 = pd.Series(
    [1, 2, 3],
    index=["C", "A", "B"]
)

print(s1 + s2)

# 8. Missing Labels

s3 = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

s4 = pd.Series(
    [1, 2, 3],
    index=["B", "C", "D"]
)

print(s3 + s4)

# 9. Creating DataFrame

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "Salary": [50000, 65000, 72000]
})

print(df)

# 10. DataFrame with Custom Index

df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 28],
        "Salary": [50000, 65000, 72000]
    },
    index=["A", "B", "C"]
)

print(df)

# 11. DataFrame Attributes

print(df.shape)
print(df.index)
print(df.columns)
print(df.dtypes)

# 12. Column Selection

print(df["Age"])

print(df[["Name"]])

print(df[["Name", "Age"]])

# 13. loc

print(df.loc["A"])
print(df.loc["B"])
print(df.loc["C"])

print(df.loc["A", "Age"])
print(df.loc["B", "Salary"])

print(df.loc["A":"B"])

# 14. iloc

print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

print(df.iloc[0, 1])
print(df.iloc[1, 2])

print(df.iloc[0:2])

# 15. at

print(df.at["A", "Name"])
print(df.at["C", "Age"])

# 16. iat

print(df.iat[0, 0])
print(df.iat[2, 1])

# 17. Boolean Indexing

print(df[df["Age"] > 25])

print(df[df["Salary"] > 60000])

print(df[df["Age"] >= 28])

# 18. Multiple Conditions

print(
    df[
        (df["Age"] > 25) &
        (df["Salary"] > 60000)
    ]
)

print(
    df[
        (df["Age"] < 26) |
        (df["Salary"] > 70000)
    ]
)

print(
    df[
        ~(df["Age"] > 25)
    ]
)