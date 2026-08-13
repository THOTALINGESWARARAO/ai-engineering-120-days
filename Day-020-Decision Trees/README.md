# Day 20 — Decision Trees

## Overview

A Decision Tree is a supervised machine learning algorithm that makes predictions by recursively splitting data based on feature conditions.

It can be used for both:

* Classification
* Regression

The model represents decisions as a tree structure, where internal nodes contain conditions and leaf nodes contain predictions.

## 1. Decision Tree Structure

A decision tree contains:

* Root node — the first decision in the tree.
* Internal node — a decision/split based on a feature.
* Branch — the path resulting from a decision.
* Leaf node — the final prediction.

Mental model:

```text
Feature condition
       |
   Split data
    /       \
Group A    Group B
   |          |
Split       Split
   |          |
Prediction  Prediction
```

## 2. How a Decision Tree Works

The basic process is:

1. Start with the complete training dataset.
2. Evaluate possible feature-based splits.
3. Select a split that produces better-separated groups.
4. Divide the data.
5. Repeat the process for the resulting groups.
6. Stop according to the tree's stopping conditions.
7. Use the reached leaf node to make a prediction.

The tree therefore learns a sequence of simple decision rules from the training data.

## 3. Splitting

A split divides the samples at a node according to a feature condition.

For example:

```text
Age <= 30
```

Samples satisfying the condition go to one branch, while the remaining samples go to another branch.

The algorithm evaluates candidate splits and selects one according to the chosen criterion.

## 4. Gini Impurity

Gini impurity measures how mixed the classes are inside a node.

The formula is:

```text
Gini = 1 - Σ pᵢ²
```

where `pᵢ` is the proportion of samples belonging to class `i`.

Interpretation:

* Gini = 0 → completely pure node.
* Higher Gini → more mixed classes.

For classification, `gini` is the default criterion in scikit-learn's `DecisionTreeClassifier`.

## 5. Entropy

Entropy measures the uncertainty or disorder of the classes in a node.

```text
Entropy = -Σ pᵢ log₂(pᵢ)
```

Interpretation:

* Entropy = 0 → completely pure node.
* Higher entropy → greater class uncertainty.

scikit-learn supports entropy as a classification splitting criterion.

## 6. Information Gain

Information Gain measures how much uncertainty is reduced after a split.

```text
Information Gain
= Parent Entropy - Weighted Child Entropy
```

A good split produces a large reduction in impurity.

Therefore, the decision tree searches for splits that improve the quality of the resulting nodes.

## 7. Gini vs Entropy

Both are impurity measures used for classification.

| Criterion        | Main idea                            |
| ---------------- | ------------------------------------ |
| Gini             | Measures class impurity              |
| Entropy          | Measures class uncertainty           |
| Information Gain | Reduction in entropy after splitting |

In scikit-learn, `DecisionTreeClassifier` supports `gini`, `entropy`, and `log_loss` in current versions.

## 8. Classification Trees

`DecisionTreeClassifier` is used when the target is categorical.

Example:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Typical applications:

* Spam detection
* Customer churn classification
* Disease classification
* Fraud classification
* Loan approval classification

## 9. Regression Trees

`DecisionTreeRegressor` is used when the target is a continuous numerical value.

Example:

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Examples:

* House price prediction
* Sales prediction
* Demand prediction
* Temperature prediction

## 10. Overfitting

Decision Trees can easily overfit the training data.

A very deep tree can continue splitting until it creates highly specific rules for the training samples.

This can result in:

```text
Training performance → very high
Test performance     → poor
```

Therefore, controlling tree complexity is important.

## 11. Controlling Tree Complexity

Important hyperparameters include:

### `max_depth`

Controls the maximum depth of the tree.

```python
DecisionTreeClassifier(max_depth=3)
```

A smaller depth generally produces a simpler model.

### `min_samples_split`

Controls the minimum number of samples required to split an internal node.

```python
DecisionTreeClassifier(min_samples_split=10)
```

### `min_samples_leaf`

Controls the minimum number of samples that must remain in each leaf.

```python
DecisionTreeClassifier(min_samples_leaf=5)
```

### `max_leaf_nodes`

Limits the number of leaf nodes.

### `ccp_alpha`

Controls cost-complexity pruning.

These parameters can be used to reduce unnecessary tree complexity and overfitting.

## 12. Feature Scaling

Decision Trees generally do not require feature scaling.

Unlike algorithms based on distances or gradient optimization, tree splits are based on feature thresholds.

Therefore, standardization is usually unnecessary for a Decision Tree.

## 13. Feature Importance

Decision Trees can provide feature importance through:

```python
model.feature_importances_
```

This represents the normalized total reduction in the splitting criterion attributed to each feature.

Example:

```python
for feature, importance in zip(feature_names, model.feature_importances_):
    print(feature, importance)
```

Feature importance can help identify which features contributed most to the learned tree.

## 14. Inspecting the Learned Tree

scikit-learn provides tools for inspecting tree structure.

For example:

```python
from sklearn.tree import export_text

print(export_text(model, feature_names=feature_names))
```

This produces a text representation of the decision rules learned by the tree.

## 15. Advantages

Decision Trees:

* Are easy to understand.
* Can model nonlinear relationships.
* Can capture feature interactions.
* Do not generally require feature scaling.
* Can be used for classification and regression.
* Produce human-readable decision rules.

## 16. Limitations

Decision Trees:

* Can overfit easily.
* Can become very large.
* Can be unstable because small changes in training data may produce a different tree.
* A single tree may have weaker generalization than ensemble methods such as Random Forests.

## 17. Decision Trees in AI/ML

Decision Trees are an important foundation for ensemble learning.

The concept of combining multiple trees leads to algorithms such as:

```text
Decision Tree
     ↓
Multiple Trees
     ↓
Random Forest
     ↓
Ensemble Learning
```

Decision Trees also provide the basic intuition needed to understand more advanced tree-based models such as Random Forests and Gradient Boosting.

## 18. Scikit-learn Implementation

Basic classification workflow:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

Basic regression workflow:

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

## 19. Key Takeaways

* A Decision Tree learns a sequence of feature-based decision rules.
* Data is recursively divided through splits.
* Internal nodes represent decisions.
* Leaf nodes produce predictions.
* Gini impurity and entropy are commonly used to evaluate classification splits.
* Information Gain measures the reduction in entropy.
* Decision Trees support both classification and regression.
* Deep trees can overfit.
* `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_leaf_nodes`, and `ccp_alpha` can control complexity.
* Feature scaling is generally unnecessary.
* Decision Trees form the foundation of important ensemble algorithms.

## Official Documentation

* [scikit-learn Decision Trees User Guide](https://scikit-learn.org/stable/modules/tree.html)
* [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
* [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
* [Understanding Decision Tree Structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)


