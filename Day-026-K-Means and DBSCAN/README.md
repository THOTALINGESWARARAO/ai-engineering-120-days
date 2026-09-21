# Day 26 — K-Means and DBSCAN

## Overview

Day 26 focuses on **unsupervised learning**, specifically clustering algorithms.

The two algorithms covered are:

* K-Means Clustering
* DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

The goal is to understand how these algorithms discover groups in unlabeled data, how they work internally, when to use them, and how to implement them using **scikit-learn**.

---

## Learning Objectives

By the end of Day 26, you should be able to:

* Explain unsupervised learning and clustering.
* Explain how K-Means works.
* Understand centroids and Euclidean distance.
* Explain the assignment and update steps.
* Understand inertia and the Elbow Method.
* Explain why feature scaling is important for distance-based algorithms.
* Understand the limitations of K-Means.
* Explain how DBSCAN works.
* Understand `eps` and `min_samples`.
* Distinguish between core, border, and noise points.
* Implement K-Means and DBSCAN using scikit-learn.
* Compare K-Means and DBSCAN.
* Evaluate clustering using the Silhouette Score.

---

# 1. Unsupervised Learning

In supervised learning, the training data contains both input features and target labels.

```text
Features + Labels
       ↓
   ML Algorithm
       ↓
    Prediction
```

In unsupervised learning, the data does not contain a target label.

```text
Features
   ↓
ML Algorithm
   ↓
Discover hidden structure
```

Clustering is one of the major applications of unsupervised learning.

---

# 2. Clustering

Clustering is the process of grouping similar data points together.

For example, customer data could be grouped into different segments based on characteristics such as:

* Age
* Income
* Spending behavior
* Purchase frequency

The algorithm attempts to discover these groups without being explicitly told which group each customer belongs to.

---

# 3. K-Means Clustering

K-Means is a **centroid-based unsupervised clustering algorithm**.

Its objective is to divide the data into `K` clusters.

The algorithm represents each cluster using a **centroid**.

A centroid is the mean position of the points belonging to that cluster.

---

## 3.1 How K-Means Works

K-Means follows an iterative process.

### Step 1 — Choose K

Choose the number of clusters.

```text
K = 3
```

means that the algorithm will attempt to create three clusters.

### Step 2 — Initialize Centroids

Initial centroid positions are selected.

### Step 3 — Assignment

Each data point is assigned to the nearest centroid.

Euclidean distance is commonly used:

$$
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$

### Step 4 — Update

After assigning points to clusters, the centroid of each cluster is recalculated using the mean of its feature values.

For a two-dimensional cluster:

$$
C = (\bar{x},\bar{y})
$$

where:

$$
\bar{x}=\frac{\sum x_i}{n}
$$

and

$$
\bar{y}=\frac{\sum y_i}{n}
$$

### Step 5 — Repeat

The assignment and update steps are repeated until the centroids converge.

```text
Choose K
   ↓
Initialize centroids
   ↓
Assign points
   ↓
Calculate new centroids
   ↓
Check convergence
   ↓
Repeat if necessary
```

---

# 4. K-Means in Scikit-Learn

Scikit-learn provides the `KMeans` class.

```python
from sklearn.cluster import KMeans

model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init="auto"
)

model.fit(X)
```

### Cluster assignments

```python
model.labels_
```

This tells us which cluster each data point belongs to.

### Cluster centers

```python
model.cluster_centers_
```

This contains the coordinates of the learned centroids.

### Inertia

```python
model.inertia_
```

This measures the sum of squared distances between data points and their assigned centroids.

---

# 5. Inertia

Inertia measures how compact the clusters are.

Conceptually:

$$
\text{Inertia}
=
\sum_{i=1}^{n}
d(x_i,c_i)^2
$$

where:

* \(x_i\) is a data point.
* \(c_i\) is its assigned centroid.
* \(d\) is the distance between them.

Lower inertia generally means the points are closer to their respective centroids.

However, inertia **always tends to decrease as K increases**.

Therefore, the lowest inertia alone should not be used to determine the optimal number of clusters.

---

# 6. Elbow Method

The Elbow Method is a heuristic for selecting a suitable value of `K`.

We calculate inertia for different values of `K` and plot the results.

```text
Inertia
   |
   |\
   | \
   |  \
   |   \__
   |      \____
   |
   +----------------
       K
```

The point where the decrease in inertia becomes significantly smaller is called the **elbow**.

That value can be considered as a candidate for `K`.

The Elbow Method is a heuristic and should be combined with other considerations such as domain knowledge and clustering metrics.

---

# 7. Feature Scaling

K-Means is distance-based.

If features have very different numerical ranges, a feature with a large magnitude can dominate the distance calculation.

For example:

```text
Age       → 18–60
Height    → 150–190
Salary    → 20,000–200,000
```

Salary has a much larger numerical range than age or height.

Therefore, scaling can be important before applying K-Means.

A common approach is `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Standardization uses:

$$
z=\frac{x-\mu}{\sigma}
$$

where:

* \(x\) = original value
* \(\mu\) = feature mean
* \(\sigma\) = feature standard deviation

---

# 8. Limitations of K-Means

K-Means has several limitations.

### 8.1 Requires K

The number of clusters must be specified beforehand.

### 8.2 Sensitive to Outliers

Because centroids are calculated using means, extreme values can influence the centroid.

### 8.3 Cluster Shape

K-Means works best when clusters are relatively compact and can be represented effectively by their centroids.

It may struggle with complex, irregularly shaped clusters.

### 8.4 Initialization

Different initial centroid positions can potentially produce different solutions.

Scikit-learn supports multiple initializations through `n_init`.

---

# 9. DBSCAN

DBSCAN stands for:

**Density-Based Spatial Clustering of Applications with Noise**

Unlike K-Means, DBSCAN is based on **density** rather than centroids.

It identifies areas containing sufficiently dense groups of points.

One of its major advantages is that it can identify noise and does not require the number of clusters to be specified beforehand.

---

# 10. DBSCAN Parameters

DBSCAN primarily uses two parameters:

```python
DBSCAN(
    eps=0.2,
    min_samples=5
)
```

## 10.1 `eps`

`eps` defines the neighborhood radius around a point.

Points within this distance are considered neighbors.

A very small `eps` can result in many points being classified as noise.

A very large `eps` can cause separate clusters to become connected.

---

## 10.2 `min_samples`

`min_samples` defines the minimum number of samples required within an `eps` neighborhood for a point to qualify as a core point.

In scikit-learn, the point itself is included when counting samples.

---

# 11. DBSCAN Point Types

DBSCAN identifies three types of points.

## Core Point

A point with enough neighboring samples within its `eps` neighborhood.

```text
Enough neighbors
       ↓
Core Point
```

## Border Point

A point that does not itself satisfy the core-point requirement but is reachable from a core point.

```text
Not enough neighbors itself
          +
Near a core point
          ↓
Border Point
```

## Noise Point

A point that is neither a core point nor reachable from a core point.

```text
Not core
   +
Not reachable from core
   ↓
Noise
```

Scikit-learn represents noise with:

```python
-1
```

---

# 12. DBSCAN in Scikit-Learn

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(
    eps=0.2,
    min_samples=5
)

labels = model.fit_predict(X)
```

The resulting labels may look like:

```text
[0, 0, 0, 1, 1, 1, -1, 0, 1]
```

where:

```text
0  → Cluster 0
1  → Cluster 1
-1 → Noise
```

Unlike K-Means, there is no `n_clusters` parameter.

---

# 13. K-Means vs DBSCAN

| Feature                     | K-Means         | DBSCAN               |
| --------------------------- | --------------- | -------------------- |
| Learning type               | Unsupervised    | Unsupervised         |
| Clustering approach         | Centroid-based  | Density-based        |
| Requires number of clusters | Yes             | No                   |
| Centroids                   | Yes             | No                   |
| Main parameters             | `n_clusters`    | `eps`, `min_samples` |
| Handles noise               | Not naturally   | Yes                  |
| Irregular cluster shapes    | Limited         | Better suited        |
| Distance-based              | Yes             | Yes                  |
| Feature scaling             | Often important | Often important      |

The key distinction is:

```text
K-Means
→ Which centroid is this point closest to?

DBSCAN
→ Is this point part of a sufficiently dense region?
```

---

# 14. Silhouette Score

The Silhouette Score is one way to evaluate clustering quality.

It measures how similar a point is to its own cluster compared with other clusters.

The score ranges approximately from:

```text
-1 → 1
```

Interpretation:

```text
Closer to +1
→ Better separated clusters

Around 0
→ Overlapping cluster boundaries

Below 0
→ Possible poor assignment
```

In scikit-learn:

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X, labels)
```

A higher score generally indicates better-defined and more separated clusters.

For DBSCAN, noise points should be handled appropriately when computing the metric.

---

# 15. Practical Applications

Clustering is useful when labeled data is unavailable or when the goal is to discover hidden structure.

### Customer Segmentation

Group customers based on:

* Spending behavior
* Income
* Purchase frequency

### Anomaly Detection

DBSCAN can identify isolated points as noise.

### Spatial Data

DBSCAN can be useful for geographical or location-based clustering.

### Exploratory Data Analysis

Clustering can reveal groups that are not immediately obvious from raw data.

### Recommendation Systems

Users or products can be grouped based on similarity.

---

# 16. Scikit-Learn Concepts Used

Day 26 uses the following scikit-learn APIs:

```python
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
```

Dataset generation:

```python
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
```

Feature scaling:

```python
from sklearn.preprocessing import StandardScaler
```

Evaluation:

```python
from sklearn.metrics import silhouette_score
```

---

# 17. Practical Implementation

The `examples.py` file demonstrates:

1. K-Means clustering using `make_blobs`.
2. Cluster assignment using `labels_`.
3. Centroid extraction using `cluster_centers_`.
4. Inertia calculation.
5. Elbow Method.
6. Feature scaling using `StandardScaler`.
7. DBSCAN using `make_moons`.
8. Core, border, and noise behavior.
9. Experiments with `eps`.
10. Experiments with `min_samples`.
11. K-Means vs DBSCAN on non-linear data.
12. Silhouette Score.

---

# 18. What I Learned

* Clustering is an unsupervised learning technique.
* K-Means creates clusters around centroids.
* `K` represents the number of clusters.
* K-Means alternates between assignment and centroid update steps.
* Inertia measures within-cluster compactness.
* The Elbow Method can help select K.
* Feature scaling is important for distance-based algorithms when features have different scales.
* DBSCAN is a density-based clustering algorithm.
* DBSCAN uses `eps` and `min_samples`.
* DBSCAN identifies core, border, and noise points.
* Noise points are represented by `-1` in scikit-learn.
* DBSCAN does not require the number of clusters beforehand.
* K-Means and DBSCAN make different assumptions about cluster structure.
* Silhouette Score can be used to evaluate clustering structure.

---

# 19. Key Takeaways

```text
K-Means
    ↓
Centroid-based
    ↓
Requires K
    ↓
Assignment + Update
    ↓
Mean-based centroids
```

```text
DBSCAN
    ↓
Density-based
    ↓
No K required
    ↓
eps + min_samples
    ↓
Core / Border / Noise
```

The most important distinction to remember:

> **K-Means finds groups around centroids, while DBSCAN finds groups based on density.**

---
