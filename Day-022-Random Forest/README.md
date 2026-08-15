Day 22 — Random Forest

📌 Overview

Day 22 of the AI Engineering in 120 Days roadmap

Today's topic is:

Random Forest

Random Forest is an ensemble learning algorithm built from multiple Decision Trees. It is designed to improve generalization and reduce the variance/overfitting associated with individual decision trees.

Status: 🟡 In Progress

🎯 Learning Goal

Understand:

why a single Decision Tree can overfit

why multiple trees can produce a more robust model

how bootstrap sampling creates different training sets

how random feature selection creates diverse trees

how predictions from the trees are combined

how to implement Random Forest using scikit-learn

the most important Random Forest hyperparameters

how Random Forest connects to practical AI/ML systems

🧠 Mental Model

Think of a single Decision Tree as one expert making a decision.

A Random Forest is a committee of many Decision Trees.

Each tree is intentionally made somewhat different by introducing randomness in:

the training samples used by the tree

the features considered while splitting nodes

The forest then combines the individual tree predictions.

Core idea

Training Dataset
       │
       ├── Bootstrap Sample ──> Decision Tree 1
       │
       ├── Bootstrap Sample ──> Decision Tree 2
       │
       ├── Bootstrap Sample ──> Decision Tree 3
       │
       ├── Bootstrap Sample ──> Decision Tree 4
       │
       └── ...
                    │
                    ▼
            Combine Predictions
                    │
                    ▼
               Final Output

The key idea is:

Many diverse trees can make a more reliable prediction than one tree.

🌲 Why Random Forest?

A Decision Tree can become very deep and closely fit its training data.

This can lead to:

low training error

high variance

poor generalization

overfitting

Random Forest addresses this by creating many different trees and combining their predictions.

The randomness helps make the trees less correlated, so some individual errors can cancel when their predictions are combined.

🌱 Bootstrap Sampling

Random Forest uses bootstrap samples.

A bootstrap sample is created by repeatedly selecting training examples with replacement.

For example, suppose the original dataset contains:

[A, B, C, D, E]

A possible bootstrap sample could be:

[A, C, C, E, B]

Another tree may receive:

[D, A, E, A, C]

Therefore, different trees train on different versions of the original dataset.

🎲 Random Feature Selection

Random Forest also introduces randomness in feature selection.

At each split, a tree considers only a subset of the available features rather than necessarily considering every feature.

In scikit-learn, this behavior is controlled by:

max_features

This increases diversity among the trees.

🗳️ How Prediction Works

Classification

For classification, the trees produce class predictions/probabilities and the forest combines them to determine the final class.

Conceptually:

Tree 1 → Class A
Tree 2 → Class A
Tree 3 → Class B
Tree 4 → Class A
Tree 5 → Class B

Final → Class A

Regression

For regression, the predictions are combined by averaging.

Tree 1 → 20
Tree 2 → 24
Tree 3 → 22
Tree 4 → 26

Final → Average prediction

🧩 Random Forest in scikit-learn

The main classifier is:

from sklearn.ensemble import RandomForestClassifier

Basic structure:

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

⚙️ Important Parameters

n_estimators

Number of trees in the forest.

RandomForestClassifier(n_estimators=100)

More trees can generally make the estimate more stable, but increase computation.

max_depth

Controls the maximum depth of each decision tree.

RandomForestClassifier(max_depth=5)

It can be used to control tree complexity.

max_features

Controls how many features are considered when searching for a split.

RandomForestClassifier(max_features="sqrt")

This is an important source of randomness in Random Forest.

min_samples_split

Minimum number of samples required to split an internal node.

RandomForestClassifier(min_samples_split=5)

min_samples_leaf

Minimum number of samples required to be at a leaf node.

RandomForestClassifier(min_samples_leaf=2)

random_state

Controls the randomness used during fitting.

RandomForestClassifier(random_state=42)

Using a fixed value makes experiments reproducible.

🔍 Feature Importance

Random Forest models can expose feature importance through:

model.feature_importances_

Example:

importances = model.feature_importances_

print(importances)

Feature importance can help investigate which features contributed most to the model according to the model's importance calculation.

Feature importance should not automatically be interpreted as proof that a feature causes the target.

🆚 Decision Tree vs Random Forest

Aspect

Decision Tree

Random Forest

Number of trees

One

Many

Random sampling

No bootstrap forest

Yes

Feature randomness

Not a forest mechanism

Yes

Variance

Usually higher

Usually lower

Overfitting risk

Higher

Generally reduced

Interpretability

Easier

More difficult

Computation

Lower

Higher

Main idea

One tree

Ensemble of trees

🤖 AI/ML Connection

Random Forest is especially useful when working with structured/tabular data.

Typical applications include:

classification

regression

feature importance analysis

baseline ML models

datasets with nonlinear relationships

It is also an important example of ensemble learning, a major machine learning concept.

The broader principle is:

Combining diverse models can improve robustness and generalization.

🧪 Practical Experiment

The practical implementation for today should include:

Dataset
   ↓
Train/Test Split
   ↓
RandomForestClassifier
   ↓
Fit
   ↓
Predict
   ↓
Evaluate
   ↓
Inspect Feature Importance

Suggested evaluation tools:

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)



📚 Official Documentation

Primary source:

scikit-learn — RandomForestClassifier

scikit-learn — Ensemble Methods

scikit-learn — Ensemble Examples

🔑 Key Takeaway

Random Forest combines many diverse Decision Trees to reduce variance and improve generalization compared with relying on a single tree.

The important part is not memorizing the class name:

RandomForestClassifier()

The important part is understanding why randomness + multiple trees + aggregation works.