"""
Day 26 - K-Means and DBSCAN

Topics:
- K-Means Clustering
- Centroids
- Inertia
- Elbow Method
- Feature Scaling
- DBSCAN
- Core, Border and Noise Points
- K-Means vs DBSCAN
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# 1. K-Means Clustering

X_blobs, y_blobs = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.0,
    random_state=42
)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init="auto"
)

kmeans.fit(X_blobs)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_

print("Cluster labels:")
print(labels)

print("\nCluster centers:")
print(centroids)

print("\nInertia:")
print(inertia)


# 2. K-Means Visualization

plt.figure(figsize=(8, 6))

plt.scatter(
    X_blobs[:, 0],
    X_blobs[:, 1],
    c=labels
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# 3. Elbow Method

inertias = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init="auto"
    )

    model.fit(X_blobs)

    inertias.append(model.inertia_)

print("Inertia values:")

for k, inertia_value in enumerate(inertias, start=1):
    print(f"K = {k}: Inertia = {inertia_value:.2f}")


plt.figure(figsize=(8, 6))

plt.plot(
    range(1, 11),
    inertias,
    marker="o"
)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.show()


# 4. Feature Scaling

X_scaled_example = np.array([
    [20, 25000],
    [25, 30000],
    [40, 80000],
    [45, 90000],
    [30, 40000],
    [50, 100000]
])

print("Original data:")
print(X_scaled_example)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_scaled_example)

print("\nScaled data:")
print(X_scaled)

print("\nScaled feature means:")
print(X_scaled.mean(axis=0))

print("\nScaled feature standard deviations:")
print(X_scaled.std(axis=0))


# 5. DBSCAN

X_moons, y_moons = make_moons(
    n_samples=300,
    noise=0.08,
    random_state=42
)

dbscan = DBSCAN(
    eps=0.2,
    min_samples=5
)

dbscan_labels = dbscan.fit_predict(X_moons)

print("\nDBSCAN labels:")
print(dbscan_labels)

unique_labels = np.unique(dbscan_labels)

print("\nUnique labels:")
print(unique_labels)

noise_count = np.sum(dbscan_labels == -1)

print("\nNumber of noise points:")
print(noise_count)


# 6. DBSCAN Visualization

plt.figure(figsize=(8, 6))

plt.scatter(
    X_moons[:, 0],
    X_moons[:, 1],
    c=dbscan_labels
)

plt.title("DBSCAN Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# 7. DBSCAN - EPS Experiment

eps_values = [0.1, 0.2, 0.5]

for eps in eps_values:

    model = DBSCAN(
        eps=eps,
        min_samples=5
    )

    labels = model.fit_predict(X_moons)

    clusters = set(labels)
    clusters.discard(-1)

    noise = np.sum(labels == -1)

    print(f"\neps = {eps}")
    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of noise points: {noise}")


# 8. DBSCAN - min_samples Experiment

min_samples_values = [3, 5, 10]

for min_samples in min_samples_values:

    model = DBSCAN(
        eps=0.2,
        min_samples=min_samples
    )

    labels = model.fit_predict(X_moons)

    clusters = set(labels)
    clusters.discard(-1)

    noise = np.sum(labels == -1)

    print(f"\nmin_samples = {min_samples}")
    print(f"Number of clusters: {len(clusters)}")
    print(f"Number of noise points: {noise}")


# 9. K-Means vs DBSCAN

kmeans_moons = KMeans(
    n_clusters=2,
    random_state=42,
    n_init="auto"
)

kmeans_moon_labels = kmeans_moons.fit_predict(X_moons)

dbscan_moons = DBSCAN(
    eps=0.2,
    min_samples=5
)

dbscan_moon_labels = dbscan_moons.fit_predict(X_moons)


# K-Means on non-linear data

plt.figure(figsize=(8, 6))

plt.scatter(
    X_moons[:, 0],
    X_moons[:, 1],
    c=kmeans_moon_labels
)

plt.title("K-Means on Non-Linear Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# DBSCAN on non-linear data

plt.figure(figsize=(8, 6))

plt.scatter(
    X_moons[:, 0],
    X_moons[:, 1],
    c=dbscan_moon_labels
)

plt.title("DBSCAN on Non-Linear Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# 10. Silhouette Score

kmeans_score = silhouette_score(
    X_blobs,
    kmeans.labels_
)

print(f"\nK-Means Silhouette Score: {kmeans_score:.4f}")


non_noise = dbscan_moon_labels != -1

if len(np.unique(dbscan_moon_labels[non_noise])) >= 2:

    dbscan_score = silhouette_score(
        X_moons[non_noise],
        dbscan_moon_labels[non_noise]
    )

    print(f"DBSCAN Silhouette Score: {dbscan_score:.4f}")

else:
    print("DBSCAN does not have enough clusters for Silhouette Score.")


# Final Summary

print("""
Day 26 Complete

K-Means:
- Centroid-based clustering
- Requires K
- Uses distance to centroids
- Uses mean to update centroids
- Inertia measures cluster compactness

DBSCAN:
- Density-based clustering
- Does not require K
- Uses eps and min_samples
- Identifies core, border and noise points
- Noise is represented by -1

Key difference:
K-Means -> centroid-based
DBSCAN -> density-based
""")