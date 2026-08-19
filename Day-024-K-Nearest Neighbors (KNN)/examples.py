# Day 24 - K-Nearest Neighbors (KNN)

from sklearn.datasets import load_iris
from sklearn.model_selection import (train_test_split,cross_val_score,GridSearchCV)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import (KNeighborsClassifier,KNeighborsRegressor)
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)


# Load the Iris dataset

iris = load_iris()

X = iris.data
y = iris.target

print("Dataset shape:", X.shape)
print("Target classes:", iris.target_names)


# Train-Test Split

X_dev, X_test, y_dev, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

print("\nDevelopment samples:", len(X_dev))
print("Test samples:", len(X_test))


# KNN Without Scaling

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_dev, y_dev)

predictions = knn.predict(X_test)

print("\nKNN Accuracy without scaling:")
print(accuracy_score(y_test, predictions))


# KNN With Feature Scaling

scaler = StandardScaler()

X_dev_scaled = scaler.fit_transform(X_dev)
X_test_scaled = scaler.transform(X_test)

knn_scaled = KNeighborsClassifier(n_neighbors=5)

knn_scaled.fit(X_dev_scaled, y_dev)

scaled_predictions = knn_scaled.predict(X_test_scaled)

print("\nKNN Accuracy with scaling:")
print(accuracy_score(y_test, scaled_predictions))


# Different K Values

k_values = [1, 3, 5, 7, 9]

print("\nAccuracy for different K values:")

for k in k_values:

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_dev_scaled,y_dev)

    predictions = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test,predictions)

    print(f"K={k}: {accuracy:.3f}")


# Different Weighting Strategies

uniform_model = KNeighborsClassifier(n_neighbors=5,weights="uniform")

distance_model = KNeighborsClassifier(n_neighbors=5,weights="distance")

uniform_model.fit(X_dev_scaled,y_dev)

distance_model.fit(X_dev_scaled,y_dev)

uniform_predictions = uniform_model.predict(X_test_scaled)

distance_predictions = distance_model.predict(X_test_scaled)

print("\nUniform weighting accuracy:")
print(accuracy_score(y_test,uniform_predictions))

print("\nDistance weighting accuracy:")
print(accuracy_score(y_test,distance_predictions))


# Different Distance Metrics

euclidean_model = KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)

manhattan_model = KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=1)

euclidean_model.fit(X_dev_scaled,y_dev)

manhattan_model.fit(X_dev_scaled,y_dev)

euclidean_predictions = euclidean_model.predict(X_test_scaled)

manhattan_predictions = manhattan_model.predict(X_test_scaled)

print("\nEuclidean distance accuracy:")
print(accuracy_score(y_test,euclidean_predictions))

print("\nManhattan distance accuracy:")
print(accuracy_score(y_test,manhattan_predictions))


# Pipeline

pipeline = Pipeline([("scaler", StandardScaler()),("knn",KNeighborsClassifier())])

pipeline.fit(X_dev,y_dev)

pipeline_predictions = pipeline.predict(X_test)

print("\nPipeline accuracy:")
print(accuracy_score(y_test,pipeline_predictions))


# Cross-Validation

print("\n4-Fold Cross-Validation:")

for k in k_values:
    pipeline = Pipeline([("scaler", StandardScaler()),("knn",KNeighborsClassifier(n_neighbors=k))])

    scores = cross_val_score(pipeline,X_dev,y_dev,cv=4,scoring="accuracy")

    print(f"K={k}: "f"Mean CV Accuracy={scores.mean():.3f}")


# Hyperparameter Tuning with GridSearchCV

pipeline = Pipeline([("scaler", StandardScaler()),("knn",KNeighborsClassifier())])

param_grid = {
    "knn__n_neighbors": [1,3,5,7,9,11,13,15]}

grid_search = GridSearchCV(pipeline,param_grid,cv=4,scoring="accuracy")

grid_search.fit(X_dev,y_dev)

print("\nBest parameters:")
print(grid_search.best_params_)

print("\nBest cross-validation accuracy:")
print(grid_search.best_score_)


# Final Model Evaluation

final_model = grid_search.best_estimator_

test_predictions = final_model.predict(X_test)

test_accuracy = accuracy_score(y_test,test_predictions)

print("\nFinal Test Accuracy:")
print(test_accuracy)


# Confusion Matrix

confusion = confusion_matrix(y_test,test_predictions)

print("\nConfusion Matrix:")
print(confusion)


# Classification Report

report = classification_report(y_test,test_predictions,target_names=iris.target_names)

print("\nClassification Report:")
print(report)


# KNN Regression

regressor = KNeighborsRegressor(n_neighbors=5)

regressor.fit(X_dev_scaled,y_dev)

regression_predictions = regressor.predict(X_test_scaled)

print("\nKNN Regression predictions:")
print(regression_predictions[:5])