# Day 16/120 --- Matplotlib: Scatter Plots, Subplots, Styling & Saving Figures

## Progress

  Chapter   Topic                                                Status
  --------- ---------------------------------------------------- --------------
  1         Scatter Plots                                        ✅ Completed
  2         Subplots                                             ✅ Completed
  3         Styling                                              ✅ Completed
  4         Saving Figures                                       ✅ Completed
  5         Mini Project --- Student Performance EDA Dashboard   ✅ Completed

> **Day 16 is complete.** All planned concepts were learned, tested
> through prediction exercises, implemented, and combined into an EDA
> dashboard.

------------------------------------------------------------------------

# Chapter 1 --- Scatter Plots ✅

## 1. Why Scatter Plots Matter

A scatter plot is used to visualize the relationship between two
numerical variables.

Each observation becomes one point:

``` text
One row of data
      ↓
   (x, y)
      ↓
One point on the plot
```

Example:

``` python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [35, 42, 50, 61, 70]

plt.scatter(hours, scores)

plt.show()
```

Conceptually:

``` text
x → Hours Studied
y → Exam Score

(1, 35)
(2, 42)
(3, 50)
(4, 61)
(5, 70)
```

The fundamental mental model is:

> **Each observation `(x, y)` becomes one visual point.**

------------------------------------------------------------------------

## 2. When to Use a Scatter Plot

Scatter plots are useful when both variables are numerical and we want
to inspect their relationship.

Typical questions:

-   Does one variable increase when another increases?
-   Does one variable decrease when another increases?
-   Is there little or no visible relationship?
-   Are there clusters?
-   Are there unusual observations?
-   Does the relationship look approximately linear or nonlinear?

Examples:

``` text
Hours Studied ↔ Exam Score
Age           ↔ Salary
Height        ↔ Weight
Ad Spend      ↔ Revenue
Feature 1     ↔ Feature 2
```

------------------------------------------------------------------------

## 3. Positive Relationship

A positive relationship means that as one variable generally increases,
the other also tends to increase.

Example:

``` text
Hours ↑
   ↓
Score ↑
```

A scatter plot may visually trend upward from left to right.

Important:

> A positive relationship does not automatically mean that one variable
> causes the other.

------------------------------------------------------------------------

## 4. Negative Relationship

A negative relationship means that as one variable generally increases,
the other tends to decrease.

Example:

``` text
X ↑
  ↓
Y ↓
```

The points may visually trend downward from left to right.

------------------------------------------------------------------------

## 5. Weak or No Visible Relationship

If the points do not show a clear pattern, the two variables may have a
weak linear relationship or no useful relationship of the type being
inspected.

Important:

> A scatter plot is a visual diagnostic. It does not prove that two
> variables are mathematically independent.

------------------------------------------------------------------------

## 6. Correlation vs Causation

Suppose a scatter plot shows:

``` text
Study Hours ↑
      ↓
Exam Score ↑
```

We can describe this as a positive association.

We cannot automatically conclude:

``` text
Study Hours cause Exam Score to increase.
```

Other variables may also influence the target:

``` text
Study Hours ───────┐
                   │
Sleep ─────────────┤
                   ├──→ Exam Score
Prior Knowledge ───┤
                   │
Teaching Quality ──┘
```

Mental model:

``` text
Scatter Plot
     ↓
Observe association
     ↓
Investigate possible explanations
     ↓
Do not automatically claim causation
```

This distinction becomes important later in statistics, regression, and
machine learning.

------------------------------------------------------------------------

## 7. Marker Size --- `s`

The `s` parameter controls marker size.

``` python
plt.scatter(
    hours,
    scores,
    s=100
)
```

Mental model:

``` text
x, y
 ↓
Where the point is

s
 ↓
How large the point looks
```

Changing `s` does not change:

-   x values
-   y values
-   point positions
-   correlation
-   the underlying dataset

Example:

``` python
plt.scatter(hours, scores, s=20)
plt.scatter(hours, scores, s=300)
```

The same observations are plotted; only their visual size changes.

------------------------------------------------------------------------

## 8. Transparency --- `alpha`

`alpha` controls marker transparency.

``` python
plt.scatter(
    hours,
    scores,
    alpha=0.5
)
```

Common interpretation:

``` text
alpha = 1.0 → opaque
alpha = 0.7 → slightly transparent
alpha = 0.5 → moderately transparent
alpha = 0.2 → highly transparent
```

Why is this useful?

When many observations overlap, fully opaque markers can hide the
density of observations.

``` text
Many overlapping points
          ↓
    Visual confusion
          ↓
Use transparency
          ↓
Dense regions become easier to see
```

Important:

> `alpha` changes the rendering, not the underlying data.

------------------------------------------------------------------------

## 9. Marker Shape --- `marker`

The `marker` parameter controls the shape used to display each
observation.

``` python
plt.scatter(
    hours,
    scores,
    marker="^"
)
```

Common markers:

``` text
"o" → circle
"^" → triangle
"s" → square
"x" → x
"*" → star
```

Mental model:

``` text
marker
   ↓
shape of observation
```

Changing the marker does not change the data or correlation.

------------------------------------------------------------------------

## 10. Color --- `c`

The `c` parameter controls color and can also be used to encode another
variable.

Example:

``` python
group = [0, 0, 0, 1, 1, 1]

plt.scatter(
    hours[:6],
    scores[:6],
    c=group
)
```

Mental model:

``` text
x → variable 1
y → variable 2
c → another visual encoding
```

This can allow one scatter plot to communicate information about groups
or classes.

Example:

``` text
Group 0 → one visual color
Group 1 → another visual color
```

Important distinction:

``` text
c=group
    ↓
data-driven visual encoding

color="red"
    ↓
pure styling
```

------------------------------------------------------------------------

## 11. Outliers

A scatter plot can reveal observations that are far from the general
pattern.

Example:

``` python
hours = [1, 2, 3, 4, 5, 6, 7]
scores = [35, 42, 50, 58, 65, 72, 20]
```

The observation:

``` text
(7, 20)
```

is unusual relative to the general increasing pattern.

Mental model:

``` text
General pattern
       ↓
Detect unusual observation
       ↓
Investigate it
       ↓
Decide how to handle it
```

### Outlier does not mean bad data

An outlier may be:

1.  A measurement error
2.  A data-entry error
3.  A genuine rare observation
4.  An important edge case

Therefore:

> **Do not automatically remove an outlier simply because it looks
> unusual.**

------------------------------------------------------------------------

## 12. Scatter Plot for EDA

Scatter plots are an important part of Exploratory Data Analysis.

They can help inspect:

``` text
Feature ↔ Feature
Feature ↔ Target
Class    ↔ Features
```

Before machine learning, this can help us understand:

-   feature relationships
-   possible outliers
-   possible clusters
-   class separation
-   potential nonlinear patterns
-   whether transformations may be worth investigating

------------------------------------------------------------------------

# Chapter 2 --- Subplots ✅

## 13. Why Subplots?

Suppose an EDA task requires:

``` text
1. Hours vs Score
2. Attendance vs Score
3. Score distribution
4. Attendance distribution
```

Creating four separate figures is possible, but comparison is easier
when the plots are placed together.

A subplot layout might look like:

``` text
┌───────────────────┬───────────────────┐
│ Hours vs Score    │ Attendance Score  │
│                   │                   │
├───────────────────┼───────────────────┤
│ Score Distribution│ Attendance Dist.  │
│                   │                   │
└───────────────────┴───────────────────┘
```

Mental model:

``` text
One Figure
    ↓
Multiple Axes
    ↓
Multiple related visualizations
```

------------------------------------------------------------------------

## 14. Figure vs Axes

This is one of the most important Matplotlib concepts from Day 16.

``` python
fig, ax = plt.subplots()
```

returns:

``` text
fig → Figure
ax  → Axes
```

### Figure

The Figure is the overall canvas/container.

``` text
Figure
┌──────────────────────────────┐
│                              │
│       plotting area(s)       │
│                              │
└──────────────────────────────┘
```

### Axes

An Axes is an individual plotting area.

An Axes contains things such as:

-   plotted data
-   x-axis
-   y-axis
-   title
-   axis labels
-   grid
-   legend

Important:

> In Matplotlib, an `Axes` object is not just the x-axis or y-axis.

Mental model:

``` text
Figure
   ↓
Axes
   ├── data
   ├── x-axis
   ├── y-axis
   ├── title
   ├── labels
   ├── grid
   └── legend
```

------------------------------------------------------------------------

## 15. `plt.subplots()`

Basic syntax:

``` python
fig, ax = plt.subplots()
```

For multiple subplots:

``` python
fig, axes = plt.subplots(1, 2)
```

This means:

``` text
1 row × 2 columns
```

Visual structure:

``` text
┌──────────────┬──────────────┐
│   axes[0]    │   axes[1]    │
│              │              │
└──────────────┴──────────────┘
```

------------------------------------------------------------------------

## 16. Subplot Indexing --- `1 × 2`

For:

``` python
fig, axes = plt.subplots(1, 2)
```

we access:

``` python
axes[0]
axes[1]
```

Conceptually:

``` text
axes[0] → first plotting area
axes[1] → second plotting area
```

Example:

``` python
axes[0].scatter(hours, scores)
axes[1].hist(scores)
```

------------------------------------------------------------------------

## 17. Subplot Indexing --- `2 × 2`

For:

``` python
fig, axes = plt.subplots(2, 2)
```

the layout is:

``` text
             Column
             0       1
          ┌───────┬───────┐
Row 0     │ [0,0] │ [0,1] │
          ├───────┼───────┤
Row 1     │ [1,0] │ [1,1] │
          └───────┴───────┘
```

Therefore:

``` python
axes[0, 0]
```

means:

``` text
first row, first column
```

``` python
axes[0, 1]
```

means:

``` text
first row, second column
```

``` python
axes[1, 0]
```

means:

``` text
second row, first column
```

``` python
axes[1, 1]
```

means:

``` text
second row, second column
```

Mental model:

``` text
axes[row, column]
```

Python indexing starts at zero.

------------------------------------------------------------------------

## 18. Plotting on a Specific Axes

Instead of:

``` python
plt.scatter(...)
```

we can explicitly select the Axes:

``` python
axes[0, 0].scatter(hours, scores)
```

Similarly:

``` python
axes[0, 0].set_title("Hours vs Score")
axes[0, 0].set_xlabel("Hours")
axes[0, 0].set_ylabel("Score")
```

This makes it explicit which subplot is being modified.

Mental model:

``` text
Figure
│
├── axes[0,0] → control this plot
├── axes[0,1] → control this plot
├── axes[1,0] → control this plot
└── axes[1,1] → control this plot
```

------------------------------------------------------------------------

## 19. `set_title()`, `set_xlabel()`, `set_ylabel()`

For an Axes object:

``` python
ax.set_title("Study Hours vs Exam Score")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Exam Score")
```

For subplots:

``` python
axes[0, 0].set_title("Hours vs Score")
axes[0, 0].set_xlabel("Hours")
axes[0, 0].set_ylabel("Score")
```

These methods apply to the specific Axes object.

### Why labels matter

A visualization can be visually correct but still misleading if its
labels are wrong.

Example:

``` text
Actual x variable → Hours Studied
Incorrect label   → Experience
```

The graph would visually render, but the viewer could draw the wrong
conclusion.

Therefore:

> **Labels are part of the meaning of a visualization, not decoration.**

------------------------------------------------------------------------

## 20. `tight_layout()`

When multiple subplots contain titles and labels, elements can become
crowded.

Use:

``` python
plt.tight_layout()
```

Mental model:

``` text
Multiple subplots
      ↓
Titles + labels + axes
      ↓
Possible overlap/crowding
      ↓
tight_layout()
      ↓
Improved spacing
```

A common workflow is:

``` python
plt.tight_layout()
plt.show()
```

When saving:

``` python
plt.tight_layout()

plt.savefig(
    "plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

------------------------------------------------------------------------

# Chapter 3 --- Styling ✅

## 21. Why Styling Matters

Styling should improve:

-   readability
-   interpretation
-   comparison
-   communication

Styling should not be added randomly.

Mental model:

``` text
Data
 ↓
Visualization
 ↓
Styling
 ↓
Better communication
```

> Every visual choice should have a communication purpose.

------------------------------------------------------------------------

## 22. Figure Size --- `figsize`

`figsize` controls the Figure dimensions.

``` python
fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)
```

The tuple is:

``` text
figsize = (width, height)
```

The units are inches.

For:

``` python
figsize=(12, 8)
```

think:

``` text
width  = 12 inches
height = 8 inches
```

Changing `figsize` changes the Figure's physical dimensions.

It does not change:

-   the dataset
-   x/y values
-   correlation
-   number of subplots

------------------------------------------------------------------------

## 23. Grid --- `grid()`

Use:

``` python
ax.grid(True)
```

A grid provides reference lines that make values and point positions
easier to estimate.

Mental model:

``` text
Data points
    ↓
Actual information

Grid
    ↓
Visual reference for reading that information
```

The grid does not change the data or move the points.

------------------------------------------------------------------------

## 24. Legends

A legend explains what different plotted groups represent.

Example:

``` python
ax.scatter(
    hours_a,
    scores_a,
    label="Group A"
)

ax.scatter(
    hours_b,
    scores_b,
    label="Group B"
)

ax.legend()
```

Mental model:

``` text
label="Group A"
       ↓
Name the plotted object

ax.legend()
       ↓
Display the names
```

Important:

``` python
label="Group A"
```

does not by itself guarantee that the legend is displayed.

You generally need:

``` python
ax.legend()
```

------------------------------------------------------------------------

## 25. Visual Encoding vs Decoration

Not every styling parameter has the same role.

### Visual encoding

A visual property can communicate data:

``` text
x       → variable
y       → variable
color   → group / variable
size    → variable
```

### Decoration / readability

Some properties primarily improve presentation:

``` text
grid
title
axis labels
figure size
```

This distinction matters because data-driven visual encodings carry
information, while purely decorative choices should improve readability
without creating misleading meaning.

------------------------------------------------------------------------

# Chapter 4 --- Saving Figures ✅

## 26. Why Save Figures?

`plt.show()` displays a visualization.

`savefig()` persists the visualization to a file.

Mental model:

``` text
Data
 ↓
Matplotlib
 ↓
Figure
 ↓
savefig()
 ↓
Persistent figure file
```

Useful for:

-   EDA reports
-   GitHub documentation
-   presentations
-   research
-   model evaluation reports
-   project artifacts

------------------------------------------------------------------------

## 27. Basic `savefig()`

``` python
plt.savefig("plot.png")
```

Here:

``` text
plot → filename
.png → file format
```

Examples:

``` python
plt.savefig("student_performance.png")
plt.savefig("results/day16.png")
```

------------------------------------------------------------------------

## 28. Relative Paths and Current Working Directory

A relative path is interpreted relative to the current working
directory.

Example:

``` python
plt.savefig("results/day16.png")
```

Conceptually:

``` text
Current Working Directory
│
└── results
      └── day16.png
```

The parent directory should already exist.

`savefig()` does not automatically create arbitrary missing parent
directories.

------------------------------------------------------------------------

## 29. DPI --- Resolution

For raster formats such as PNG:

``` python
plt.savefig(
    "plot.png",
    dpi=300
)
```

`dpi` means dots per inch.

Mental model:

``` text
figsize
   ↓
physical Figure dimensions

dpi
   ↓
density/resolution of raster rendering
```

Example:

``` text
dpi=100 → lower raster resolution
dpi=300 → higher raster resolution
dpi=600 → very high raster resolution
```

A higher DPI generally produces a more detailed raster image and can
also increase file size.

Important:

> DPI does not change the underlying x/y data.

It also does not change the conceptual data value represented by a
marker.

------------------------------------------------------------------------

## 30. `bbox_inches="tight"`

Use:

``` python
plt.savefig(
    "plot.png",
    dpi=300,
    bbox_inches="tight"
)
```

`bbox_inches="tight"` makes the saved bounding box fit the figure
content more closely.

This is useful when titles, labels, or other content is close to the
boundaries of the figure.

Mental model:

``` text
Figure content
      ↓
Determine content bounds
      ↓
Save a tighter bounding box
```

It can reduce unnecessary whitespace and help avoid content near the
edges being clipped by an overly tight/default boundary.

------------------------------------------------------------------------

## 31. Save Before Show

A reliable workflow is:

``` python
plt.tight_layout()

plt.savefig(
    "plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

Mental model:

``` text
Create
  ↓
Style
  ↓
Adjust layout
  ↓
Save
  ↓
Display
```

This ensures the figure is saved after the intended layout and styling
have been applied.

------------------------------------------------------------------------

## 32. PNG vs SVG

### PNG

``` python
plt.savefig("plot.png", dpi=300)
```

PNG is a raster format.

Useful for:

-   general EDA
-   GitHub
-   reports
-   presentations
-   screenshots

### SVG

``` python
plt.savefig("plot.svg")
```

SVG is a vector format.

Useful when scalable vector graphics are preferred, such as diagrams or
publication-quality graphics.

Mental model:

``` text
PNG → raster
SVG → vector
```

------------------------------------------------------------------------

# Chapter 5 --- AI/ML Connection ✅

## 33. Scatter Plots in Machine Learning

Scatter plots are frequently used before model training to understand
relationships between features and targets.

Examples:

``` text
Feature 1 ↔ Feature 2
Feature 1 ↔ Target
Feature 2 ↔ Target
```

This can help answer questions such as:

``` text
Do these features appear related?

Are there obvious outliers?

Are classes visually separated?

Does the relationship appear linear?

Are there clusters?
```

This is part of EDA rather than a replacement for statistical analysis.

------------------------------------------------------------------------

## 34. Outliers and Machine Learning

An unusual observation should not automatically be removed.

Possible reasons:

``` text
Outlier
  │
  ├── Data-entry error
  ├── Measurement error
  ├── Genuine rare event
  └── Important edge case
```

The correct process is:

``` text
Detect
  ↓
Investigate
  ↓
Understand
  ↓
Choose a justified treatment
```

Blindly removing observations can change the training distribution.

------------------------------------------------------------------------

## 35. Color and Classification

Suppose:

``` python
group = [0, 0, 0, 1, 1, 1]
```

and color is used to represent the group.

Then a scatter plot can help visually inspect whether two classes are
separated.

Conceptually:

``` text
Features
   ↓
Scatter plot
   ↓
Color = class
   ↓
Visual class separation
```

This becomes relevant when later studying:

-   KNN
-   Logistic Regression
-   Decision Trees
-   SVM
-   Clustering

Visualization does not replace the model, but it helps us understand the
structure of the data.

------------------------------------------------------------------------

## 36. Subplots in ML/EDA

Subplots allow multiple diagnostic views to be compared in one Figure.

Example:

``` text
┌─────────────────────┬─────────────────────┐
│ Feature vs Target   │ Feature vs Target   │
├─────────────────────┼─────────────────────┤
│ Distribution         │ Distribution         │
└─────────────────────┴─────────────────────┘
```

This is useful for:

-   comparing feature relationships
-   examining distributions
-   checking possible outliers
-   comparing multiple preprocessing results
-   presenting model evaluation results

------------------------------------------------------------------------

# Chapter 6 --- Mini Project: Student Performance EDA Dashboard ✅

## 37. Dataset

``` python
hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

scores = [
    35, 40, 48, 52, 58,
    65, 70, 75, 82, 90
]

attendance = [
    60, 65, 68, 72, 75,
    80, 82, 88, 92, 95
]
```

------------------------------------------------------------------------

## 38. Dashboard Design

The dashboard contains four views:

``` text
┌──────────────────────────┬──────────────────────────┐
│ Hours vs Exam Score      │ Attendance vs Exam Score │
│ Scatter Plot             │ Scatter Plot             │
├──────────────────────────┼──────────────────────────┤
│ Score Distribution        │ Attendance Distribution  │
│ Histogram                 │ Histogram                │
└──────────────────────────┴──────────────────────────┘
```

Mapping:

``` text
axes[0,0] → Hours vs Score
axes[0,1] → Attendance vs Score
axes[1,0] → Score Distribution
axes[1,1] → Attendance Distribution
```

------------------------------------------------------------------------

## 39. Complete Mini Project

``` python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

scores = [35, 40, 48, 52, 58, 65, 70, 75, 82, 90]

attendance = [60, 65, 68, 72, 75, 80, 82, 88, 92, 95]


fig, axes = plt.subplots(
    2,
    2,
    figsize=(12, 8)
)


# 1. Hours vs Exam Score
axes[0, 0].scatter(
    hours,
    scores,
    s=80,
    alpha=0.7
)

axes[0, 0].set_title("Hours Studied vs Exam Score")
axes[0, 0].set_xlabel("Hours Studied")
axes[0, 0].set_ylabel("Exam Score")
axes[0, 0].grid(True)


# 2. Attendance vs Exam Score
axes[0, 1].scatter(
    attendance,
    scores,
    s=80,
    alpha=0.7
)

axes[0, 1].set_title("Attendance vs Exam Score")
axes[0, 1].set_xlabel("Attendance")
axes[0, 1].set_ylabel("Exam Score")
axes[0, 1].grid(True)


# 3. Score Distribution
axes[1, 0].hist(
    scores,
    bins=5
)

axes[1, 0].set_title("Score Distribution")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True)


# 4. Attendance Distribution
axes[1, 1].hist(
    attendance,
    bins=5
)

axes[1, 1].set_title("Attendance Distribution")
axes[1, 1].set_xlabel("Attendance")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(True)


plt.tight_layout()

plt.savefig(
    "Student Performance EDA dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

------------------------------------------------------------------------

# Chapter 7 --- Key Misconceptions to Eliminate

## "`s` changes the data."

No.

``` text
s → marker size
```

It changes the visual representation only.

------------------------------------------------------------------------

## "`alpha` changes the values of the points."

No.

``` text
alpha → transparency
```

It is a rendering property.

------------------------------------------------------------------------

## "`marker` changes the relationship."

No.

``` text
marker → shape
```

The data remains unchanged.

------------------------------------------------------------------------

## "An outlier should always be removed."

No.

Investigate the reason for the unusual observation first.

------------------------------------------------------------------------

## "A positive scatter-plot relationship proves causation."

No.

Correlation/association does not establish causation.

------------------------------------------------------------------------

## "`axes[0,0]` means the x-axis."

No.

It means the **Axes object at row 0, column 0**.

That Axes contains its x-axis, y-axis, plot, title, labels, grid, etc.

------------------------------------------------------------------------

## "`figsize` changes the data."

No.

``` text
figsize → Figure dimensions
```

------------------------------------------------------------------------

## "`dpi` changes the data."

No.

``` text
dpi → raster rendering resolution
```

------------------------------------------------------------------------

## "`savefig()` saves the raw dataset."

No.

``` text
savefig() → saves the visualization
```

It does not replace saving your data in CSV, Parquet, database, etc.

------------------------------------------------------------------------

## "`label=` automatically displays a legend."

Not by itself.

``` python
ax.scatter(..., label="Group A")
```

assigns the label.

``` python
ax.legend()
```

displays the legend.

------------------------------------------------------------------------

# Chapter 8 --- Unified Mental Model

## Scatter Plot

``` text
x, y
 ↓
point position

s
 ↓
marker size

alpha
 ↓
transparency

marker
 ↓
shape

c
 ↓
color / visual encoding
```

## Subplots

``` text
Figure
   ↓
Multiple Axes
   ↓
Each Axes is independently controlled
```

## Styling

``` text
figsize → Figure dimensions
title   → overall context
xlabel  → x variable meaning
ylabel  → y variable meaning
grid    → visual reference
legend  → group/series explanation
```

## Saving

``` text
Figure
  ↓
tight_layout()
  ↓
savefig()
  ├── filename
  ├── format
  ├── dpi
  └── bbox_inches
  ↓
Saved visualization
```

------------------------------------------------------------------------

# Chapter 9 --- Practice / Experiments Completed

During Day 16, the concepts were learned using prediction-first
experiments.

### Scatter Plot Experiments

-   Predicted number of points
-   Predicted point coordinates
-   Predicted positive and negative relationships
-   Swapped x/y variables and reasoned about correlation
-   Tested marker size
-   Tested transparency
-   Tested marker shapes
-   Tested color encoding
-   Identified outliers
-   Distinguished correlation from causation

### Subplot Experiments

-   Predicted `1 × 2` layouts
-   Predicted `2 × 2` layouts
-   Practiced `axes[row, column]`
-   Distinguished Figure from Axes
-   Applied titles and labels to individual Axes
-   Used `tight_layout()`

### Saving Experiments

-   Identified filenames and formats
-   Understood current working directory
-   Distinguished saved visualization from raw data
-   Understood DPI
-   Understood `bbox_inches="tight"`
-   Practiced the `savefig()` → `show()` workflow

------------------------------------------------------------------------

# Chapter 10 --- Day 16 Revision Map

``` text
Matplotlib Day 16
│
├── Scatter Plots
│   ├── scatter()
│   ├── x / y
│   ├── positive relationship
│   ├── negative relationship
│   ├── weak relationship
│   ├── clusters
│   ├── outliers
│   ├── s
│   ├── alpha
│   ├── marker
│   └── c
│
├── Subplots
│   ├── Figure
│   ├── Axes
│   ├── subplots()
│   ├── 1 × 2
│   ├── 2 × 2
│   ├── axes[row, column]
│   ├── set_title()
│   ├── set_xlabel()
│   ├── set_ylabel()
│   └── tight_layout()
│
├── Styling
│   ├── figsize
│   ├── grid()
│   ├── legend()
│   ├── marker styling
│   ├── transparency
│   └── readable labels
│
└── Saving
    ├── savefig()
    ├── relative paths
    ├── dpi
    ├── bbox_inches="tight"
    ├── PNG
    └── SVG
```

------------------------------------------------------------------------

# Official Documentation

Use the official Matplotlib documentation as the source of truth:

-   Matplotlib `scatter()`:
    https://matplotlib.org/stable/api/\_as_gen/matplotlib.pyplot.scatter.html
-   Matplotlib `subplots()`:
    https://matplotlib.org/stable/api/\_as_gen/matplotlib.pyplot.subplots.html
-   Matplotlib `savefig()`:
    https://matplotlib.org/stable/api/\_as_gen/matplotlib.pyplot.savefig.html
-   Matplotlib `Axes` API:
    https://matplotlib.org/stable/api/axes_api.html
-   Matplotlib `Figure` API:
    https://matplotlib.org/stable/api/figure_api.html

------------------------------------------------------------------------

# Day 16 Completion Checklist

-   [x] Understand why scatter plots are used
-   [x] Create scatter plots with `scatter()`
-   [x] Map observations to `(x, y)` points
-   [x] Interpret positive relationships
-   [x] Interpret negative relationships
-   [x] Recognize weak/no visible relationships
-   [x] Understand correlation vs causation
-   [x] Use marker size with `s`
-   [x] Use transparency with `alpha`
-   [x] Use marker shapes with `marker`
-   [x] Use color with `c`
-   [x] Understand outliers
-   [x] Understand scatter plots in EDA/ML
-   [x] Understand Figure vs Axes
-   [x] Create subplots with `plt.subplots()`
-   [x] Understand 1×2 subplot layouts
-   [x] Understand 2×2 subplot layouts
-   [x] Index subplots with `axes[row, column]`
-   [x] Use Axes-oriented plotting
-   [x] Set titles and axis labels
-   [x] Control Figure size with `figsize`
-   [x] Use legends
-   [x] Use grids
-   [x] Use `tight_layout()`
-   [x] Save figures with `savefig()`
-   [x] Understand relative save paths
-   [x] Understand `dpi`
-   [x] Understand `bbox_inches="tight"`
-   [x] Distinguish PNG and SVG
-   [x] Build the Student Performance EDA Dashboard

## Day 16 --- COMPLETE ✅
