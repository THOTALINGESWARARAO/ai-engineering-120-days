# Day 15/120 — Matplotlib: Data Visualization 📊

> **Phase 4 — Matplotlib & Data Visualization**

Day 15 focuses on the fundamentals of **Matplotlib** and three essential visualization techniques:

* Line plots
* Bar charts
* Histograms

The goal is not just to memorize plotting syntax, but to understand **which visualization answers which data question** and how these visualizations are used in **AI/ML Exploratory Data Analysis (EDA)**.

---

## 🎯 Learning Objectives

By the end of Day 15, I can:

* Understand why visualization is important in data analysis and ML.
* Use `matplotlib.pyplot` for basic visualization.
* Create and interpret line plots.
* Create and interpret bar charts.
* Create and interpret histograms.
* Understand the difference between a bar chart and a histogram.
* Choose an appropriate visualization based on the question being asked.
* Interpret basic ML training curves.
* Identify potential class imbalance using bar charts.
* Identify distribution, skewness, and potential outliers using histograms.

---

# 1. Why Visualization?

Raw data is often difficult to interpret directly.

For example:

```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 115, 150, 180]
```

The values are understandable, but visualization makes patterns such as **trends, comparisons, and distributions** much easier to recognize.

### Mental Model

```text
Raw Data
   ↓
Choose appropriate visualization
   ↓
Matplotlib
   ↓
Visual pattern
   ↓
Human interpretation
```

Visualization is especially useful during **Exploratory Data Analysis (EDA)** before building an ML model.

---

# 2. Matplotlib Fundamentals

Matplotlib is a Python library used for creating visualizations.

The interface used throughout this day is:

```python
import matplotlib.pyplot as plt
```

`pyplot` provides functions such as:

```python
plt.plot()
plt.bar()
plt.barh()
plt.hist()

plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
plt.grid()
plt.show()
```

---

## 2.1 Basic Plotting Workflow

A simple plotting workflow is:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 1, 5]

plt.plot(x, y)
plt.show()
```

The important idea is that the values of `x` and `y` correspond by position:

```text
x = [1, 2, 3, 4]
y = [2, 4, 1, 5]

        ↓

(1, 2)
(2, 4)
(3, 1)
(4, 5)
```

### Important Rule

For a simple `plt.plot(x, y)`, the X and Y sequences need compatible lengths.

For example:

```python
x = [1, 2, 3]
y = [10, 20]
```

does not provide a complete X-Y pairing.

---

# 3. Line Plots 📈

## 3.1 Need

A line plot is useful when the **order of observations matters** and we want to understand a trend or progression.

Examples:

* Temperature over days
* Revenue over months
* Accuracy over epochs
* Loss over epochs
* Measurements over time

---

## 3.2 Mental Model

```text
Ordered observations
        ↓
Connect observations
        ↓
Observe progression / trend
```

### Key Rule

> **Line plot → ordered progression / trend**

It does not have to represent literal time.

For example:

```text
Epoch → Accuracy
Iteration → Loss
Month → Revenue
Day → Temperature
```

All have an ordered progression.

---

## 3.3 Basic Line Plot

```python
import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5]
loss = [0.9, 0.7, 0.55, 0.42, 0.35]

plt.plot(epochs, loss)
plt.show()
```

The points are:

```text
(1, 0.90)
(2, 0.70)
(3, 0.55)
(4, 0.42)
(5, 0.35)
```

The line shows that the loss is generally decreasing.

---

# 4. Line Plot Customization

## 4.1 Markers

Markers show individual observations.

```python
plt.plot(epochs, loss, marker="o")
```

Mental model:

```text
marker
   ↓
individual observation
```

For five observations, five markers will appear.

---

## 4.2 Line Styles

The `linestyle` controls how observations are connected.

```python
plt.plot(
    epochs,
    loss,
    marker="o",
    linestyle="-"
)
```

Common styles:

```python
linestyle="-"
linestyle="--"
linestyle=":"
linestyle="-."
```

Mental model:

```text
marker
   ↓
individual point

linestyle
   ↓
connection between points
```

---

## 4.3 Labels

A label gives a plotted dataset a meaningful name.

```python
plt.plot(
    epochs,
    loss,
    marker="o",
    label="Training Loss"
)
```

The label becomes useful when combined with `plt.legend()`.

---

## 4.4 Legend

```python
plt.legend()
```

A legend displays the labels associated with plotted datasets.

Example:

```python
plt.plot(
    epochs,
    train_loss,
    label="Training Loss"
)

plt.plot(
    epochs,
    val_loss,
    label="Validation Loss"
)

plt.legend()
```

Mental model:

```text
label
  ↓
Name attached to dataset

legend()
  ↓
Display those names
```

---

## 4.5 Axis Labels

```python
plt.xlabel("Epoch")
plt.ylabel("Loss")
```

Axis labels explain what the axes represent.

---

## 4.6 Title

```python
plt.title("Training Loss Over Epochs")
```

The title provides context for the visualization.

---

## 4.7 Grid

```python
plt.grid()
```

A grid can make values and positions easier to estimate visually.

---

# 5. Multiple Lines

Multiple related datasets can be plotted on the same axes.

```python
import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4]

train_loss = [0.8, 0.6, 0.4, 0.3]
val_loss = [0.9, 0.7, 0.65, 0.68]

plt.plot(
    epochs,
    train_loss,
    marker="o",
    label="Training Loss"
)

plt.plot(
    epochs,
    val_loss,
    marker="o",
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")

plt.legend()
plt.grid()

plt.show()
```

---

# 6. ML Connection — Training Curves

Line plots are extremely useful in machine learning.

For example:

```text
Epoch
  ↓
Training Loss
Validation Loss
Training Accuracy
Validation Accuracy
```

A model's training behavior can be visualized using line plots.

### Example

```text
Training Loss     ↓↓↓
Validation Loss   ↓↓↓
```

This generally indicates that both training and validation performance are improving.

However:

```text
Training Loss     ↓↓↓
Validation Loss   ↑
```

can be a warning sign of **potential overfitting**.

The model is improving on training data while performing worse on validation data.

### Important Nuance

A rising validation loss does not automatically prove overfitting from a few observations. It is a **warning sign that requires further investigation**.

---

# 7. Accuracy Line Plot

Example:

```python
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

plt.show()
```

The accuracy increases:

```text
60% → 68% → 75% → 82% → 88%
```

This indicates that model accuracy is improving as training progresses.

---

# 8. Bar Charts 📊

## 8.1 Need

A bar chart is useful when we want to compare **numerical values across discrete categories**.

Example:

```text
Python      █████████
Java        ██████
C++         ████
JavaScript  ███████
```

---

## 8.2 Mental Model

```text
Category
   ↓
Numerical magnitude
   ↓
Bar height / length
   ↓
Comparison
```

### Key Rule

> **Bar chart → categorical comparison**

Unlike a line plot, the categories do not need to represent a progression.

---

# 9. Basic Bar Chart

```python
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [80, 50, 35, 65]

plt.bar(languages, students)
plt.show()
```

The mapping is:

```text
Python      → 80
Java        → 50
C++         → 35
JavaScript  → 65
```

The bar height represents the corresponding numerical value.

---

# 10. `plt.bar(x, height)`

The basic structure is:

```python
plt.bar(x, height)
```

For example:

```python
models = ["A", "B", "C"]
accuracy = [60, 80, 70]

plt.bar(models, accuracy)
```

Mental model:

```text
x       → categories
height  → numerical magnitude
```

The values correspond by position.

---

# 11. Bar Width

The width of a bar can be changed using `width`.

```python
plt.bar(
    models,
    accuracy,
    width=0.5
)
```

A smaller width produces narrower bars.

```python
width=0.3
```

produces narrower bars than:

```python
width=0.8
```

### Important Distinction

```text
height
   ↓
data magnitude

width
   ↓
visual thickness
```

Changing `width` does not change the underlying data.

---

# 12. Horizontal Bar Charts

Matplotlib provides `barh()` for horizontal bars.

```python
plt.barh(models, accuracy)
```

Mental model:

```text
plt.bar()
    ↓
vertical bars

plt.barh()
    ↓
horizontal bars
```

The underlying data does not change; only the orientation changes.

---

## When is `barh()` useful?

Horizontal bars are particularly useful when category names are long.

Example:

```text
Logistic Regression Model       ███████████
Decision Tree Classifier        █████████
Random Forest Classifier        ████████████
Support Vector Machine          ██████████
```

The category names are easier to read.

---

# 13. ML Connection — Model Comparison

Bar charts can compare model performance.

```python
models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest"
]

accuracy = [82, 78, 91]

plt.bar(models, accuracy)
```

Interpretation:

```text
Logistic Regression → 82%
Decision Tree       → 78%
Random Forest       → 91%
```

Random Forest has the highest accuracy in this example.

The key question is:

> **Which category has the larger value?**

---

# 14. ML Connection — Class Imbalance

A bar chart can be used to inspect the number of samples in different classes.

Example:

```python
classes = ["Cat", "Dog", "Horse", "Elephant"]
samples = [1000, 950, 200, 50]

plt.bar(classes, samples)
```

The visualization can reveal that some classes have substantially fewer observations.

```text
Cat        → 1000
Dog        → 950
Horse      → 200
Elephant   → 50
```

This suggests potential **class imbalance**.

### Important distinction

Class imbalance is associated with **categorical classes**.

A bar chart is appropriate because we are comparing:

```text
Class → Number of samples
```

---

# 15. Histograms 📊

## 15.1 Need

A histogram is used to understand the **distribution of numerical data**.

Suppose we have many numerical observations:

```text
18, 19, 19, 20, 21, 21, 22, 23, ...
```

Looking at every individual value isn't very useful.

We want to know:

* Where are most values concentrated?
* How spread out are the values?
* Is the distribution symmetric?
* Is it skewed?
* Are there unusual values?

A histogram helps answer these questions.

---

# 16. Histogram Mental Model

```text
Raw numerical values
        ↓
Divide numerical range into bins
        ↓
Count observations in each bin
        ↓
Visualize frequency
```

### Key Rule

> **Histogram → numerical distribution**

---

# 17. Histogram vs Bar Chart

This is one of the most important distinctions from Day 15.

## Bar Chart

```text
Category → Value

Python      █████████
Java        ██████
C++         ████
```

Used for:

> **Comparing discrete categories**

---

## Histogram

```text
Numerical range → Frequency

40–49     ███
50–59     █████
60–69     ████████
70–79     █████
80–89     ███
```

Used for:

> **Understanding the distribution of numerical values**

### Core distinction

```text
BAR
Category → magnitude
Comparison

HISTOGRAM
Numerical interval → frequency
Distribution
```

---

# 18. Basic Histogram

```python
import matplotlib.pyplot as plt

scores = [
    45, 50, 52, 55, 55,
    60, 62, 65, 67, 70,
    72, 72, 75, 78, 80, 85, 90
]

plt.hist(scores)
plt.show()
```

The `hist()` function groups the numerical observations into bins and counts how many observations fall into each bin.

---

# 19. Bins

The `bins` parameter controls how the numerical range is divided.

```python
plt.hist(scores, bins=5)
```

Conceptually:

```text
Numerical range
       ↓
┌────┬────┬────┬────┬────┐
│ B1 │ B2 │ B3 │ B4 │ B5 │
└────┴────┴────┴────┴────┘
```

Each bin represents an interval of numerical values.

The height of the bar represents the number of observations in that interval when using the default `density=False`.

---

# 20. Changing the Number of Bins

The same data can be visualized with different numbers of bins:

```python
plt.hist(scores, bins=3)
```

or:

```python
plt.hist(scores, bins=5)
```

or:

```python
plt.hist(scores, bins=10)
```

The data does not change.

Only the grouping changes.

### Mental Model

```text
Same data
   │
   ├── bins=3  → coarser view
   ├── bins=5  → moderate view
   └── bins=10 → finer view
```

More bins do **not** mean more data.

Fewer bins do **not** mean less data.

---

# 21. Distribution Shape

Histograms allow us to inspect the overall shape of numerical data.

Example:

```python
data = [
    10, 11, 11, 12, 12, 12,
    13, 13, 14, 14, 15,
    16, 17, 18, 25, 30
]

plt.hist(data, bins=5)
```

Most observations are concentrated around the lower values, while values such as `25` and `30` are far from the main concentration.

---

# 22. Potential Outliers

An **outlier** is an observation that appears unusually far from the general pattern of the data.

In the previous example:

```text
10–18 → main concentration

25
30
```

The values `25` and `30` may be **potential outliers**.

### Important

A histogram can help identify unusual observations, but it does not by itself prove that a value is statistically an outlier.

Further analysis may be required.

---

# 23. Skewness

A distribution is **skewed** when it is not symmetric.

For example, if most observations are concentrated toward smaller values and a tail extends toward larger values:

```text
██████████████
████████████
████████
████
██
             █
                 █
────────────────────→
              larger values
```

This is commonly called:

> **Right-skewed / positively skewed**

Histograms are useful for visually identifying such distributions.

---

# 24. ML/EDA Connection

Histograms are particularly useful for inspecting numerical features before ML modeling.

For example:

```text
Dataset
   ↓
Numerical feature
   ↓
Histogram
   ↓
Inspect distribution
   ├── Concentration
   ├── Spread
   ├── Skewness
   └── Potential outliers
```

This can inform later decisions about:

* Data preprocessing
* Feature engineering
* Transformations
* Outlier investigation
* Model assumptions

The appropriate next step depends on the dataset and model; visualization itself does not automatically dictate a preprocessing action.

---

# 25. Class Imbalance vs Skewness

These two concepts must not be confused.

## Class Imbalance

Usually involves a **categorical target/class**:

```text
Cat       1000
Dog        950
Horse      200
Elephant    50
```

Visualized using a:

> **Bar chart**

---

## Skewed Distribution

Usually involves a **numerical feature**:

```text
Age
Income
Salary
Temperature
```

Visualized using a:

> **Histogram**

### Mental Model

```text
Categorical classes
       ↓
BAR CHART
       ↓
Class imbalance


Numerical feature
       ↓
HISTOGRAM
       ↓
Distribution / skewness / potential outliers
```

---

# 26. Choosing the Right Plot

The most important takeaway from Day 15:

| Visualization | Mental Model | Main Question                         | ML/EDA Example            |
| ------------- | ------------ | ------------------------------------- | ------------------------- |
| **Line plot** | Trend        | How is it changing?                   | Training loss over epochs |
| **Bar chart** | Comparison   | How do categories compare?            | Class counts              |
| **Histogram** | Distribution | How are numerical values distributed? | Feature distribution      |

### Remember:

```text
LINE       → TREND
BAR        → COMPARISON
HISTOGRAM  → DISTRIBUTION
```

---

# 27. Complete Example

```python
import matplotlib.pyplot as plt

# Line plot
epochs = [1, 2, 3, 4, 5]
loss = [0.9, 0.7, 0.55, 0.42, 0.35]

plt.plot(
    epochs,
    loss,
    marker="o",
    label="Training Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.legend()
plt.grid()
plt.show()


# Bar chart
models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest"
]

accuracy = [82, 78, 91]

plt.bar(models, accuracy)

plt.xlabel("Model")
plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy Comparison")
plt.show()


# Histogram
scores = [
    45, 50, 52, 55, 55,
    60, 62, 65, 67, 70,
    72, 72, 75, 78, 80, 85, 90
]

plt.hist(scores, bins=5)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Score Distribution")
plt.show()
```

---

# 28. Common Misconceptions Corrected

### ❌ "Line plots are only for time."

✅ Line plots are appropriate for **ordered progression/trends**. Time is only one common example.

---

### ❌ "Bar charts are for strings."

✅ Bar charts are for **categorical comparisons**.

---

### ❌ "A histogram bar represents one value."

✅ A histogram bar represents a **range/bin of numerical values**.

---

### ❌ "More bins means more data."

✅ The underlying data stays the same. Only the grouping resolution changes.

---

### ❌ "Skewed numerical data means class imbalance."

✅ Class imbalance concerns categorical class frequencies. Skewness concerns the shape of a numerical distribution.

---

### ❌ "An unusual histogram value is automatically an outlier."

✅ It is a **potential outlier** that requires further investigation.

---

# 29. Official Documentation

Primary documentation used for Day 15:

* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
* [Matplotlib Pyplot API](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
* [Matplotlib `plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
* [Matplotlib `bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
* [Matplotlib `barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html)
* [Matplotlib `hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

---

# 30. Day 15 Completion Checklist

### Matplotlib Fundamentals

* [x] Understand why visualization is useful
* [x] Import `matplotlib.pyplot`
* [x] Understand X-Y pairing
* [x] Understand compatible X/Y lengths

### Line Plots

* [x] `plt.plot()`
* [x] Markers
* [x] Line styles
* [x] Labels
* [x] Legends
* [x] X/Y axis labels
* [x] Titles
* [x] Grid
* [x] Multiple lines
* [x] Training/validation curves
* [x] Potential overfitting interpretation

### Bar Charts

* [x] `plt.bar()`
* [x] Categories and numerical values
* [x] Bar height
* [x] Bar width
* [x] `plt.barh()`
* [x] Horizontal vs vertical bars
* [x] Model comparison
* [x] Class distribution
* [x] Class imbalance

### Histograms

* [x] `plt.hist()`
* [x] Numerical distributions
* [x] Bins
* [x] Frequency
* [x] Effect of changing bin count
* [x] Distribution shape
* [x] Skewness
* [x] Potential outliers
* [x] Histogram vs bar chart

---

# 📌 Day 15 Status

**Concept Learning:** ✅ Complete

**Implementation Practice:** ⏳ Pending

**Topics Covered:** 3/3

```text
Matplotlib Fundamentals  ██████████ 100%
Line Plots               ██████████ 100%
Bar Charts               ██████████ 100%
Histograms               ██████████ 100%
```

> **Day 15 Concept Completion: 100% ✅**

---

## 🚀 Key Takeaway

Visualization is not about making data look attractive.

It is about asking the right question and choosing the visual representation that makes the answer easier to see.

```text
What am I trying to understand?
             ↓
       Choose the plot
             ↓
       Visualize data
             ↓
       Interpret pattern
             ↓
       Make a data/ML decision
```

**Line → Trend | Bar → Comparison | Histogram → Distribution**
