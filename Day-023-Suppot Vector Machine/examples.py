"""
Day 23 - Support Vector Machine (SVM)

Concepts covered:
- Linear SVM
- RBF Kernel
- Soft Margin
- C parameter
- Gamma parameter
- Feature Scaling
- Pipeline
- Model Evaluation
- Support Vectors
"""

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# Create a non-linear dataset

X, y = make_moons(
    n_samples=300,
    noise=0.2,
    random_state=42
)


# Split the data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Linear SVM

linear_model = make_pipeline(
    StandardScaler(),
    SVC(kernel="linear")
)

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

linear_accuracy = accuracy_score(
    y_test,
    linear_predictions
)

print("Linear SVM Accuracy:", linear_accuracy)


# RBF SVM

rbf_model = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        C=1.0,
        gamma="scale"
    )
)

rbf_model.fit(X_train, y_train)

rbf_predictions = rbf_model.predict(X_test)

rbf_accuracy = accuracy_score(
    y_test,
    rbf_predictions
)

print("RBF SVM Accuracy:", rbf_accuracy)


# Compare Linear and RBF SVM

print("\nKernel Comparison")
print("Linear SVM:", linear_accuracy)
print("RBF SVM:", rbf_accuracy)


# C experiment

small_c_model = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        C=0.1,
        gamma="scale"
    )
)

large_c_model = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        C=100,
        gamma="scale"
    )
)

small_c_model.fit(X_train, y_train)
large_c_model.fit(X_train, y_train)

small_c_train_accuracy = small_c_model.score(
    X_train,
    y_train
)

large_c_train_accuracy = large_c_model.score(
    X_train,
    y_train
)

print("\nC Experiment")
print("C = 0.1:", small_c_train_accuracy)
print("C = 100:", large_c_train_accuracy)


# Gamma experiment

small_gamma_model = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        C=1.0,
        gamma=0.01
    )
)

large_gamma_model = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        C=1.0,
        gamma=10
    )
)

small_gamma_model.fit(X_train, y_train)
large_gamma_model.fit(X_train, y_train)

small_gamma_train_accuracy = small_gamma_model.score(
    X_train,
    y_train
)

large_gamma_train_accuracy = large_gamma_model.score(
    X_train,
    y_train
)

print("\nGamma Experiment")
print("Gamma = 0.01:", small_gamma_train_accuracy)
print("Gamma = 10:", large_gamma_train_accuracy)


# Inspect support vectors

svm = rbf_model.named_steps["svc"]

print("\nSupport Vector Information")

print("Support Vector Indices:")
print(svm.support_)

print("\nSupport Vectors:")
print(svm.support_vectors_)

print("\nNumber of Support Vectors per Class:")
print(svm.n_support_)


# Display final model information

print("\nFinal Model")
print("Kernel:", svm.kernel)
print("C:", svm.C)
print("Gamma:", svm.gamma)
print("Test Accuracy:", rbf_accuracy)