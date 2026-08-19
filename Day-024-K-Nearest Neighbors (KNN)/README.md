# Day 24 — K-Nearest Neighbors (KNN)

## Status

**Completed ✅**

Today focused only on K-Nearest Neighbors (KNN), from the core intuition and distance calculations to a complete scikit-learn workflow with feature scaling, cross-validation, hyperparameter tuning, and final evaluation.

---

## 1. What is KNN?

K-Nearest Neighbors (KNN) is an instance-based supervised learning algorithm.

Instead of learning an explicit mathematical decision function, KNN predicts a new sample based on the labels of nearby training samples.

The basic idea is:

```text
New data point
      ↓
Calculate distances
      ↓
Find K nearest training points
      ↓
Use their labels
      ↓
Majority vote / aggregation
      ↓
Prediction
```

scikit-learn describes nearest-neighbor methods as finding a predefined number of training samples closest to a new point and predicting from those neighbors.

---

## 2. Why do we need KNN?

Suppose we have labeled observations:

```text
Feature 1    Feature 2    Class

1            1            Red
2            2            Red
3            2            Blue
4            4            Blue
```

For a new point:

```text
X = (2, 3)
```

KNN asks:

> Which existing observations are most similar to this point?

If most of its nearest neighbors belong to the Red class, KNN predicts Red.

---

## 3. Mental Model

The easiest way to remember KNN is:

> **Tell me who your closest neighbors are, and I'll tell you what you probably are.**

For classification:

```text
New point
   ↓
Find nearby points
   ↓
Select K neighbors
   ↓
Majority vote
   ↓
Class prediction
```

For regression:

```text
New point
   ↓
Find nearby points
   ↓
Select K neighbors
   ↓
Aggregate their target values
   ↓
Numerical prediction
```

---

## 4. Instance-Based / Lazy Learning

KNN is commonly described as an instance-based or non-generalizing learning method.

Unlike a Decision Tree, KNN does not learn a set of explicit rules such as:

```text
if feature_1 > 2.5:
    Blue
else:
    Red
```

Instead, the training examples remain important when making predictions.

Mental model:

```text
Decision Tree
Training → Learn rules → Predict

Random Forest
Training → Build trees → Predict

KNN
Training → Store/prepare training examples
Prediction → Find neighbors → Predict
```

KNN still performs work during `fit()`, including preparing the data structures needed for neighbor queries.

---

## 5. Distance

KNN needs a way to measure how close two observations are.

The most common distance to understand is Euclidean distance.

For two points:

```text
A = (x₁, y₁)
B = (x₂, y₂)
```

Euclidean distance is:

[
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
]

Example:

```text
A = (2, 3)
B = (5, 7)
```

[
d=\sqrt{(5-2)^2+(7-3)^2}
]

[
=\sqrt{9+16}
]

[
=5
]

---

## 6. Manual KNN Example

Training data:

| Point | Feature 1 | Feature 2 | Class |
| ----- | --------: | --------: | ----- |
| A     |         1 |         1 | Red   |
| B     |         2 |         2 | Red   |
| C     |         3 |         2 | Blue  |
| D     |         4 |         4 | Blue  |

New point:

```text
X = (2, 3)
```

Distances:

```text
X → A = √5 ≈ 2.24
X → B = 1
X → C = √2 ≈ 1.41
X → D = √5 ≈ 2.24
```

For:

```text
K = 3
```

the nearest neighbors are:

```text
B → Red
C → Blue
A → Red
```

Votes:

```text
Red  → 2
Blue → 1
```

Prediction:

```text
Red
```

---

## 7. What does K mean?

`K` is the number of nearest neighbors considered for prediction.

Examples:

```text
K = 1
→ use 1 nearest neighbor

K = 3
→ use 3 nearest neighbors

K = 5
→ use 5 nearest neighbors
```

Important:

> **K controls how many neighbors participate in the prediction. It does not mean only K distances are calculated.**

For a new point, KNN may need to compare that point with many or all training samples before identifying the K nearest ones.

---

## 8. Small K vs Large K

### Small K

Example:

```text
K = 1
```

Only the closest observation determines the prediction.

Advantages:

* Very local decisions
* Can capture detailed structure

Disadvantages:

* Highly sensitive to noise
* High variance
* Greater risk of overfitting

Mental model:

```text
Small K
   ↓
Very local
   ↓
Sensitive to individual points
   ↓
High variance
   ↓
Possible overfitting
```

### Large K

A larger neighborhood smooths the predictions.

Advantages:

* Less sensitive to individual noisy points
* Lower variance

Disadvantages:

* Can ignore local patterns
* Higher bias
* Greater risk of underfitting

Mental model:

```text
Large K
   ↓
Broader neighborhood
   ↓
Smoother decisions
   ↓
Higher bias
   ↓
Possible underfitting
```

scikit-learn also notes that larger K generally suppresses noise effects but makes classification boundaries less distinct.

---

## 9. Feature Scaling

KNN is distance-based, so feature scale matters.

Suppose:

```text
Age       → 18–60
Salary    → 20,000–2,00,000
```

Without scaling, the numerical magnitude of Salary can dominate the distance calculation.

This can cause KNN to consider points similar or different mainly because of their units rather than their actual relative position in feature space.

Therefore, feature scaling is generally important for KNN when features have different scales.

---

## 10. StandardScaler

A common approach is:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

`StandardScaler` standardizes features using statistics learned from the training data.

Conceptually:

```text
Original features
       ↓
StandardScaler
       ↓
Comparable numerical scale
       ↓
KNN distance calculation
```

Important:

```python
scaler.fit_transform(X_train)
```

but:

```python
scaler.transform(X_test)
```

Do not independently fit the scaler on the test set.

---

## 11. Data Leakage

If preprocessing learns information from validation or test data, that information can leak into the model-development process.

Incorrect:

```python
scaler.fit_transform(X_test)
```

The test set should remain unseen until final evaluation.

Correct principle:

> **Learn preprocessing parameters only from the training portion of the current evaluation split.**

This becomes especially important during cross-validation.

---

## 12. KNN Classification in scikit-learn

The main classifier is:

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(
    n_neighbors=5
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Important parameter:

```python
n_neighbors
```

represents K.

The current scikit-learn documentation defines `KNeighborsClassifier` as a classifier implementing the k-nearest-neighbors vote.

---

## 13. Important KNN Parameters

### `n_neighbors`

Number of neighbors used.

```python
KNeighborsClassifier(n_neighbors=5)
```

### `weights`

Controls how neighbors contribute.

```python
weights="uniform"
```

Every neighbor has equal weight.

```python
weights="distance"
```

Closer neighbors receive greater influence.

### `metric`

Controls the distance calculation.

```python
metric="minkowski"
```

is the default metric.

With:

```python
p=2
```

Minkowski distance becomes Euclidean distance.

With:

```python
p=1
```

it corresponds to Manhattan distance.

### `algorithm`

Controls the neighbor-search strategy:

```text
auto
ball_tree
kd_tree
brute
```

The default is:

```python
algorithm="auto"
```

scikit-learn chooses an appropriate approach based on the data and configuration.

---

## 14. KNN Regression

KNN can also solve regression problems.

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(
    n_neighbors=5
)
```

For regression, neighboring target values are aggregated rather than using a class majority vote.

Example:

```text
Nearest house prices:

40
45
50
55
60
```

With uniform weighting:

[
\frac{40+45+50+55+60}{5}=50
]

Prediction:

```text
50
```

---

## 15. Decision Boundary

KNN can produce highly irregular decision boundaries because predictions depend on local neighborhoods.

To visualize a decision boundary, we can:

1. Create many hypothetical points across the feature space.
2. Ask KNN to predict each point.
3. Plot the predictions as regions.
4. Observe where predicted classes change.

Conceptually:

```text
Feature space
      ↓
Create grid points
      ↓
KNN predicts every grid point
      ↓
Classify each location
      ↓
Color prediction regions
      ↓
Decision boundary
```

### Important insight

KNN does not explicitly learn a decision boundary and store it as a separate object.

The boundary emerges from the local neighbor predictions.

---

## 16. Grid Visualization

Suppose we create:

```text
10,000 hypothetical grid points
```

Then:

```python
Z = model.predict(grid_points)
```

produces:

```text
10,000 individual predictions
```

Each grid point is treated as a separate query.

For each query:

```text
Grid point
   ↓
Find nearest training samples
   ↓
Select K
   ↓
Vote
   ↓
Prediction
```

Then the predictions are reshaped and visualized as regions.

---

## 17. Choosing K

We should not simply guess K.

Possible values:

```text
1, 3, 5, 7, 9, 11, ...
```

can be evaluated using validation or cross-validation.

Example:

|  K | Validation Accuracy |
| -: | ------------------: |
|  1 |                 88% |
|  3 |                 92% |
|  5 |                 95% |
|  7 |                 94% |
|  9 |                 90% |

Here:

```text
Best K = 5
```

But the best K is **dataset-dependent**.

---

## 18. Validation vs Test Data

Suppose we have 100 samples.

A simple approach is:

```text
100 samples
│
├── 80 Development
└── 20 Test
```

The 20 test samples remain untouched.

We can use the 80 development samples for cross-validation.

---

## 19. 4-Fold Cross-Validation

Suppose:

```text
80 development samples
```

and:

```text
cv = 4
```

Then:

```text
80 samples
│
├── Fold 1 → 20
├── Fold 2 → 20
├── Fold 3 → 20
└── Fold 4 → 20
```

Each round uses:

```text
60 → training
20 → validation
```

Example:

```text
Round 1:
60 training + 20 validation

Round 2:
60 training + 20 validation

Round 3:
60 training + 20 validation

Round 4:
60 training + 20 validation
```

Every sample gets a chance to be validation data.

The four validation scores are then averaged.

---

## 20. Cross-Validation and KNN K

There are two different meanings of K that must not be confused.

### KNN K

```text
n_neighbors
```

Number of neighbors used for prediction.

### Cross-validation K

```text
cv=4
```

Number of folds.

They are completely different concepts.

---

## 21. Pipeline

A proper KNN workflow can use a Pipeline:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])
```

Pipeline ensures preprocessing is performed as part of the model workflow.

This is particularly important during cross-validation because the scaler should be fitted independently inside each training fold.

---

## 22. GridSearchCV

Instead of manually testing every K:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "knn__n_neighbors": [1, 3, 5, 7, 9, 11]
}

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=4,
    scoring="accuracy"
)

grid_search.fit(X_dev, y_dev)
```

Then:

```python
grid_search.best_params_
```

returns the best parameter combination.

For example:

```text
{'knn__n_neighbors': 5}
```

And:

```python
grid_search.best_score_
```

returns the best cross-validation score.

`GridSearchCV` performs an exhaustive search over the specified parameter values using cross-validation.

---

## 23. Final Model Workflow

The complete workflow is:

```text
Dataset
   ↓
Train/Test Split
   ↓
Development data + untouched Test data
   ↓
Pipeline
   ├── StandardScaler
   └── KNN
   ↓
Cross-validation
   ↓
Try multiple K values
   ↓
Select best K
   ↓
Refit selected pipeline on all development data
   ↓
Evaluate once on Test data
```

The test set should not be used to select K.

---

## 24. Complete KNN Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split into development and test data
X_dev, X_test, y_dev, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create preprocessing + model pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

# K values to test
param_grid = {
    "knn__n_neighbors": [1, 3, 5, 7, 9, 11, 13, 15]
}

# Hyperparameter tuning using 4-fold CV
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=4,
    scoring="accuracy"
)

# Fit using development data
grid_search.fit(X_dev, y_dev)

# Best K
print("Best Parameters:")
print(grid_search.best_params_)

# Best cross-validation score
print("Best CV Accuracy:")
print(grid_search.best_score_)

# Final selected model
final_model = grid_search.best_estimator_

# Final test prediction
test_predictions = final_model.predict(X_test)

# Test accuracy
print("Test Accuracy:")
print(accuracy_score(y_test, test_predictions))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, test_predictions))

# Classification report
print("Classification Report:")
print(
    classification_report(
        y_test,
        test_predictions
    )
)
```

---

## 25. Evaluation Metrics

### Accuracy

[
Accuracy =
\frac{Correct\ Predictions}{Total\ Predictions}
]

Useful when class distributions are reasonably balanced.

### Confusion Matrix

Shows:

```text
Actual vs Predicted
```

The diagonal represents correct predictions.

### Classification Report

Provides:

```text
Precision
Recall
F1-score
Support
```

These metrics are especially useful when accuracy alone does not provide enough information.

---

## 26. KNN Limitations

### Computational cost

Prediction can become expensive as the training dataset grows because neighbor searches must be performed for query points.

### Feature scaling sensitivity

Different feature scales can distort distance.

### Irrelevant features

Irrelevant dimensions can distort the notion of similarity.

### Choice of K

Poor K selection can lead to overfitting or underfitting.

### High-dimensional data

Nearest-neighbor methods can become less effective in high-dimensional spaces because of the **curse of dimensionality**.

---

## 27. KNN vs Models Learned So Far

| Model         | Main idea                        |
| ------------- | -------------------------------- |
| Decision Tree | Learn decision rules             |
| Random Forest | Combine multiple decision trees  |
| KNN           | Find similar nearby observations |

Mental models:

```text
Decision Tree
"What rule separates these classes?"
```

```text
Random Forest
"What do many trees collectively decide?"
```

```text
KNN
"Which training examples are most similar to this point?"
```

---

## 28. AI/ML Connection

KNN is useful beyond classical classification.

Its most important modern connection is **similarity search**.

### Classical KNN

```text
Feature vectors
      ↓
Distance
      ↓
Nearest examples
      ↓
Prediction
```

### Modern embedding retrieval

```text
Query
  ↓
Embedding vector
  ↓
Vector similarity
  ↓
Nearest vectors
  ↓
Retrieve relevant information
```

This connects directly to concepts used in:

* Recommendation systems
* Image similarity
* Semantic search
* Vector databases
* Retrieval-Augmented Generation (RAG)

The algorithms and representations may differ, but the core intuition is:

> **Represent things as vectors and retrieve nearby/similar vectors.**

---

## 29. What I Need to Remember

The most important KNN mental model:

```text
New point
   ↓
Measure distance
   ↓
Find nearest neighbors
   ↓
Take K neighbors
   ↓
Vote / aggregate
   ↓
Prediction
```

And the most important practical model:

```text
Split
   ↓
Pipeline
   ↓
Scale
   ↓
Cross-validation
   ↓
Tune K
   ↓
Refit
   ↓
Final test evaluation
```

---

## 30. Key Takeaways

* KNN is an instance-based supervised learning algorithm.
* K represents the number of neighbors considered.
* Euclidean distance is a common distance metric.
* Classification uses neighbor voting.
* Regression aggregates neighboring target values.
* Small K can produce high variance and overfitting.
* Large K can produce high bias and underfitting.
* Feature scaling is important for distance-based models.
* `StandardScaler` should be fitted only on appropriate training folds.
* `Pipeline` helps prevent preprocessing leakage during cross-validation.
* Cross-validation helps select K without touching the final test set.
* `GridSearchCV` can automate K selection.
* The test set should be used only for final evaluation.
* KNN can produce highly irregular decision boundaries.
* KNN becomes less effective in high-dimensional spaces.
* Nearest-neighbor reasoning provides useful intuition for modern similarity search and vector retrieval.

---

## Official Documentation

* scikit-learn — Nearest Neighbors: https://scikit-learn.org/stable/modules/neighbors.html
* scikit-learn — `KNeighborsClassifier`: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
* scikit-learn — `GridSearchCV`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
* scikit-learn — Nearest Neighbors Classification example: https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html

---

## Day 24 Completion

**Topic:** K-Nearest Neighbors (KNN)

**Status:** ✅ Completed

**Conceptual understanding:** ✅

**Mathematical intuition:** ✅

**Visualization:** ✅

**scikit-learn implementation:** ✅

**Cross-validation:** ✅

**Hyperparameter tuning:** ✅

**Final evaluation workflow:** ✅

**AI/ML connection:** ✅
