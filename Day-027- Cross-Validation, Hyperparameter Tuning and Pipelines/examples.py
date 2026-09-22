"""
Day 27 - Cross-Validation, Hyperparameter Tuning and Pipelines

Topics:
- Train/Test Split
- K-Fold Cross-Validation
- Stratified K-Fold Cross-Validation
- cross_val_score
- StandardScaler
- Pipelines
- GridSearchCV
- RandomizedSearchCV
- Model Evaluation

Library:
- scikit-learn
"""

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    StratifiedKFold,
    GridSearchCV,
    RandomizedSearchCV,
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. Load Dataset
# ============================================================

X, y = load_iris(return_X_y=True)

print("=" * 60)
print("Dataset")
print("=" * 60)

print("Features shape:", X.shape)
print("Target shape:", y.shape)


# ============================================================
# 2. Train/Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("Train/Test Split")
print("=" * 60)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# ============================================================
# 3. Basic K-Fold Cross-Validation
# ============================================================

model = KNeighborsClassifier(n_neighbors=5)

scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("\n" + "=" * 60)
print("5-Fold Cross-Validation")
print("=" * 60)

print("CV Scores:", scores)
print("Mean CV Score:", scores.mean())
print("Standard Deviation:", scores.std())


# ============================================================
# 4. Stratified K-Fold Cross-Validation
# ============================================================

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

stratified_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=skf,
    scoring="accuracy"
)

print("\n" + "=" * 60)
print("Stratified K-Fold Cross-Validation")
print("=" * 60)

print("Scores:", stratified_scores)
print("Mean:", stratified_scores.mean())
print("Standard Deviation:", stratified_scores.std())


# ============================================================
# 5. Pipeline
# ============================================================

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

pipeline_accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("Pipeline")
print("=" * 60)

print("Test Accuracy:", pipeline_accuracy)


# ============================================================
# 6. Pipeline + Cross-Validation
# ============================================================

pipeline_cv_scores = cross_val_score(
    pipeline,
    X_train,
    y_train,
    cv=skf,
    scoring="accuracy"
)

print("\n" + "=" * 60)
print("Pipeline + Cross-Validation")
print("=" * 60)

print("Scores:", pipeline_cv_scores)
print("Mean CV Score:", pipeline_cv_scores.mean())
print("Standard Deviation:", pipeline_cv_scores.std())


# ============================================================
# 7. GridSearchCV
# ============================================================

param_grid = {
    "knn__n_neighbors": [3, 5, 7, 9, 11],
    "knn__weights": ["uniform", "distance"],
    "knn__metric": ["euclidean", "manhattan"]
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\n" + "=" * 60)
print("GridSearchCV")
print("=" * 60)

print("Best Parameters:")
print(grid_search.best_params_)

print("Best CV Score:")
print(grid_search.best_score_)


# ============================================================
# 8. Evaluate Best Grid Search Model
# ============================================================

best_grid_model = grid_search.best_estimator_

grid_predictions = best_grid_model.predict(X_test)

grid_accuracy = accuracy_score(
    y_test,
    grid_predictions
)

print("\n" + "=" * 60)
print("Grid Search Final Evaluation")
print("=" * 60)

print("Test Accuracy:", grid_accuracy)

print("\nClassification Report:")
print(classification_report(y_test, grid_predictions))


# ============================================================
# 9. RandomizedSearchCV
# ============================================================

param_distributions = {
    "knn__n_neighbors": np.arange(1, 21),
    "knn__weights": ["uniform", "distance"],
    "knn__metric": ["euclidean", "manhattan", "minkowski"]
}

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=param_distributions,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("\n" + "=" * 60)
print("RandomizedSearchCV")
print("=" * 60)

print("Best Parameters:")
print(random_search.best_params_)

print("Best CV Score:")
print(random_search.best_score_)


# ============================================================
# 10. Final Random Search Evaluation
# ============================================================

best_random_model = random_search.best_estimator_

random_predictions = best_random_model.predict(X_test)

random_accuracy = accuracy_score(
    y_test,
    random_predictions
)

print("\n" + "=" * 60)
print("Random Search Final Evaluation")
print("=" * 60)

print("Test Accuracy:", random_accuracy)

print("\nClassification Report:")
print(classification_report(y_test, random_predictions))


# ============================================================
# 11. Final Summary
# ============================================================

print("\n" + "=" * 60)
print("Final Summary")
print("=" * 60)

print("Basic CV Mean:",
      round(scores.mean(), 4))

print("Pipeline CV Mean:",
      round(pipeline_cv_scores.mean(), 4))

print("Best GridSearch CV:",
      round(grid_search.best_score_, 4))

print("Best RandomizedSearch CV:",
      round(random_search.best_score_, 4))

print("GridSearch Test Accuracy:",
      round(grid_accuracy, 4))

print("RandomizedSearch Test Accuracy:",
      round(random_accuracy, 4))