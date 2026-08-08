import matplotlib.pyplot as plt

# 1. Line Plot

# Mental model:
# Line plot -> ordered progression / trend

# ML example:
# Epoch -> Training Loss

epochs = [1, 2, 3, 4, 5]
training_loss = [0.90, 0.70, 0.55, 0.42, 0.35]

plt.plot(
    epochs,
    training_loss,
    marker="o",
    linestyle="-",
    label="Training Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.grid()
plt.legend()
plt.show()


# 2. Multiple Line Plots

# Comparing training and validation loss.
#
# ML connection:
# Training loss decreasing while validation loss starts increasing
# can be a warning sign of potential overfitting.

epochs = [1, 2, 3, 4]

training_loss = [0.80, 0.60, 0.40, 0.30]
validation_loss = [0.90, 0.70, 0.65, 0.68]

plt.plot(
    epochs,
    training_loss,
    marker="o",
    label="Training Loss"
)

plt.plot(
    epochs,
    validation_loss,
    marker="o",
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid()

plt.show()


# 3. Bar Chart

# Mental model:
# Bar chart -> categorical comparison

subjects = ["Python", "Math", "ML", "DBMS"]
marks = [85, 72, 90, 78]

plt.bar(
    subjects,
    marks
)

plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Subject-wise Marks")

plt.show()


# 4. Bar Chart with Width

# width controls the visual thickness of the bars.
# It does not change the underlying values.

models = ["A", "B", "C"]
accuracy = [60, 80, 70]

plt.bar(
    models,
    accuracy,
    width=0.5
)

plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")

plt.show()


# 5. Horizontal Bar Chart

# barh() changes the orientation of the bars.
# Useful when category names are long.

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest"
]

accuracy = [82, 78, 91]

plt.barh(
    models,
    accuracy
)

plt.xlabel("Accuracy (%)")
plt.ylabel("Model")
plt.title("Model Accuracy Comparison")

plt.show()


# 6. Class Distribution

# ML / EDA connection:
# Bar charts can reveal class imbalance.

classes = ["Cat", "Dog", "Horse", "Elephant"]
samples = [1000, 950, 200, 50]

plt.bar(
    classes,
    samples
)

plt.xlabel("Class")
plt.ylabel("Number of Samples")
plt.title("Class Distribution")

plt.show()


# 7. Histogram

# Mental model:
# Histogram -> numerical distribution
#
# Each bar represents a numerical interval (bin).
# Height represents the number of observations in that bin.

scores = [
    45, 50, 52, 55, 55,
    60, 62, 65, 67, 70,
    72, 72, 75, 78, 80, 85, 90
]

plt.hist(
    scores,
    bins=5
)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution")

plt.show()


# 8. Histogram with Different Number of Bins

# The underlying data does not change.
# Only the grouping/resolution changes.

scores = [
    45, 50, 52, 55, 55,
    60, 62, 65, 67, 70,
    72, 72, 75, 78, 80, 85, 90
]

plt.hist(
    scores,
    bins=10
)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution - 10 Bins")

plt.show()


# 9. Histogram with Potential Skewness / Outlier

# Values are concentrated around the lower range,
# while 25 and 30 are far from the main group.

data = [
    10, 11, 11, 12, 12, 12,
    13, 13, 14, 14, 15,
    16, 17, 18, 25, 30
]

plt.hist(
    data,
    bins=5
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution with Potential Outliers")

plt.show()


# 10. Line Plot - Model Accuracy

# ML connection:
# Line plots can show how model accuracy changes
# across training epochs.

epochs = [1, 2, 3, 4, 5]
accuracy = [0.60, 0.68, 0.75, 0.82, 0.88]

plt.plot(
    epochs,
    accuracy,
    marker="o"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Over Epochs")
plt.grid()

plt.show()


# Day 15 Summary

# Line plot -> Ordered progression / Trend
# Bar chart -> Categories / Comparison
# Histogram -> Numerical values / Distribution
#
# ML / EDA:
# Line plot -> Training and validation behavior
# Bar chart -> Class distribution and class imbalance
# Histogram -> Feature distribution, skewness, potential outliers