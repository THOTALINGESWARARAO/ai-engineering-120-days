## Day-25 Naive Bayes
````markdown
# Day 25 — Naive Bayes

## Overview

Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem.

The core idea is simple:

> Given a set of features, determine which class is most probable.

Naive Bayes is called "naive" because it assumes that features are conditionally independent given the class.

Despite this strong assumption, Naive Bayes can work very well in practice, especially for high-dimensional problems such as text classification.

---

## Why Learn Naive Bayes?

Naive Bayes is important because it introduces probabilistic thinking into machine learning and provides a fast and simple classification approach.

It is particularly useful when:

- The problem is a classification problem.
- The dataset contains many features.
- The features are sparse or high-dimensional.
- Fast training and prediction are important.
- The problem involves text classification.
- A strong baseline model is required.

Naive Bayes is also useful for understanding the progression from traditional machine learning to modern NLP systems.

Traditional NLP:

```text
Text
  ↓
Feature Extraction
  ↓
Naive Bayes
  ↓
Classification
````

Modern NLP:

```text
Text
  ↓
Tokenizer
  ↓
Transformer
  ↓
Learned Representation
  ↓
Prediction / Generation
```

The models are very different, but the overall machine-learning pipeline remains similar.

---

## 1. Naive Bayes Intuition

Suppose we want to classify an email:

```text
"free money offer"
```

into:

```text
Spam
Not Spam
```

Naive Bayes asks:

> Which class is more probable given the observed features?

Conceptually:

```text
Input features
      ↓
Calculate probability for each class
      ↓
Compare class probabilities
      ↓
Select the most probable class
```

For text, the features could be words such as:

```text
free
money
offer
meeting
project
```

---

## 2. Why Is It Called "Naive"?

The naive assumption is:

> Features are conditionally independent given the class.

For example, for:

```text
"free money offer"
```

the model treats the contribution of:

```text
free
money
offer
```

as independent when calculating the class probability.

This assumption is often not completely true in real-world data.

For example:

```text
"not good"
```

contains a relationship between `not` and `good` that a basic Naive Bayes model does not explicitly understand.

However, the simplified assumption makes the algorithm computationally efficient.

---

## 3. Core Algorithm

The general process is:

```text
Training Data
     ↓
Separate examples by class
     ↓
Estimate class probabilities
     ↓
Estimate feature probabilities
     ↓
For a new sample:
     ↓
Calculate the probability for each class
     ↓
Compare the class probabilities
     ↓
Choose the highest probability
```

The important idea is:

```text
Features + Class probabilities
              ↓
       Most probable class
```

Naive Bayes does not use majority voting like KNN.

It makes a probabilistic decision.

---

## 4. Zero-Frequency Problem

A problem can occur when a particular feature has never appeared in a particular class.

For example:

```text
P(word | class) = 0
```

Since Naive Bayes combines feature probabilities, a zero probability can cause the entire class probability to become zero.

This is called the:

> Zero-frequency problem

---

## 5. Laplace Smoothing

A common solution is **Laplace smoothing**.

Instead of allowing an unseen feature to have exactly zero probability, a small value is added to the counts.

Conceptually:

```text
Original count
      ↓
Add smoothing value
      ↓
Calculate probability
```

In scikit-learn, smoothing for `MultinomialNB` can be controlled using `alpha`.

Example:

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB(alpha=1.0)
```

`alpha=1.0` corresponds to the standard additive/Laplace smoothing approach.

---

# 6. Types of Naive Bayes

Scikit-learn provides different Naive Bayes classifiers for different types of feature distributions.

## GaussianNB

Used for continuous numerical features.

Examples:

```text
Age = 21.5
Height = 172.4
Temperature = 36.7
Salary = 45000
```

Example:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X, y)
```

Mental model:

```text
Continuous numerical data
          ↓
      GaussianNB
```

Typical applications:

* Numerical classification
* Scientific measurements
* Sensor data
* Medical measurements

---

## MultinomialNB

Used when features represent counts or frequencies.

This is particularly useful for text classification.

Example:

```text
"free free money"
```

can be represented as:

```text
free   money
  2      1
```

Example:

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X, y)
```

Mental model:

```text
Counts / frequencies
        ↓
  MultinomialNB
```

Typical applications:

* Spam detection
* Sentiment analysis
* Document classification
* News classification
* Text categorization

---

## BernoulliNB

Used when features represent binary values.

For example:

```text
1 → Feature is present
0 → Feature is absent
```

Example:

```text
free   money   offer
  1      1       0
```

In text classification, this means that the model cares about whether a word is present rather than how many times it occurs.

Example:

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()
model.fit(X, y)
```

With `CountVectorizer`:

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(binary=True)
```

Mental model:

```text
Binary 0/1 features
        ↓
   BernoulliNB
```

---

## 7. GaussianNB vs MultinomialNB vs BernoulliNB

| Model         | Feature Type         | Example                    |
| ------------- | -------------------- | -------------------------- |
| GaussianNB    | Continuous numerical | Age, height, temperature   |
| MultinomialNB | Counts/frequencies   | Number of word occurrences |
| BernoulliNB   | Binary               | Word present/absent        |

Easy memory trick:

```text
Gaussian    → Continuous
Multinomial → Counts
Bernoulli   → Binary
```

---

# 8. CountVectorizer

For text classification, machine-learning algorithms cannot directly process raw text.

`CountVectorizer` converts text into numerical feature vectors.

Example:

```python
from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "free money",
    "free offer",
    "project meeting",
    "team meeting"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)
```

The vocabulary can be inspected using:

```python
print(vectorizer.get_feature_names_out())
```

The resulting feature matrix can be viewed using:

```python
print(X.toarray())
```

Conceptually:

```text
Raw text
   ↓
CountVectorizer
   ↓
Word-count matrix
   ↓
Naive Bayes
```

---

# 9. fit_transform() vs transform()

This is an important practical concept.

During training:

```python
X_train = vectorizer.fit_transform(texts)
```

`fit_transform()`:

1. Learns the vocabulary.
2. Converts the text into numerical features.

For new text:

```python
X_new = vectorizer.transform(new_text)
```

Use `transform()` because the vocabulary should remain the same as the training vocabulary.

Do not create a new vocabulary from the test/new data.

---

# 10. predict() vs predict_proba()

### predict()

Returns the predicted class.

```python
prediction = model.predict(X_new)
```

Example:

```text
[1]
```

could represent:

```text
1 → Spam
```

### predict_proba()

Returns the probability estimates for each class.

```python
probabilities = model.predict_proba(X_new)
```

Example:

```text
[[0.10, 0.90]]
```

If the class ordering is:

```text
[0, 1]
```

then:

```text
Class 0 → 10%
Class 1 → 90%
```

Therefore:

```text
predict()      → predicted class
predict_proba() → probability estimates
```

---

# 11. GaussianNB Implementation

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([
    [1.0, 2.0],
    [1.2, 1.8],
    [1.1, 2.2],
    [5.0, 6.0],
    [5.2, 5.8],
    [4.8, 6.2]
])

y = np.array([
    0, 0, 0,
    1, 1, 1
])

model = GaussianNB()

model.fit(X, y)

x_new = [[1.1, 2.0]]

prediction = model.predict(x_new)
print(prediction)

probabilities = model.predict_proba(x_new)
print(probabilities)
```

Here:

```text
Class 0 → values around 1–2
Class 1 → values around 5–6
```

The new sample:

```text
[1.1, 2.0]
```

is close to the Class 0 examples, so the model predicts Class 0.

---

# 12. MultinomialNB Implementation

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "free money",
    "free offer",
    "project meeting",
    "team meeting"
]

y = [1, 1, 0, 0]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print(vectorizer.get_feature_names_out())
print(X.toarray())

model = MultinomialNB()

model.fit(X, y)

new_text = ["free money"]

X_new = vectorizer.transform(new_text)

prediction = model.predict(X_new)

print(prediction)

print(model.predict_proba(X_new))
```

Here:

```text
1 → Spam
0 → Not Spam
```

The model learns from the word-count representation.

---

# 13. BernoulliNB Implementation

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

texts = [
    "free money",
    "free offer",
    "project meeting",
    "team meeting"
]

y = [1, 1, 0, 0]

vectorizer = CountVectorizer(binary=True)

X = vectorizer.fit_transform(texts)

print(vectorizer.get_feature_names_out())
print(X.toarray())

model = BernoulliNB()

model.fit(X, y)

new_text = ["free money"]

X_new = vectorizer.transform(new_text)

prediction = model.predict(X_new)

print(prediction)

print(model.predict_proba(X_new))
```

The important difference is:

```python
CountVectorizer(binary=True)
```

This converts the features into binary presence/absence values.

---

# 14. Advantages of Naive Bayes

## Fast

Naive Bayes is computationally efficient.

It can train and predict quickly.

## Good for high-dimensional data

Text datasets can contain thousands or millions of possible features.

Naive Bayes can work efficiently with this type of feature space.

## Works well with relatively small datasets

A useful classifier can sometimes be built without requiring extremely large amounts of labeled data.

## Excellent baseline

Naive Bayes is useful for establishing a quick baseline before experimenting with more complex models.

## Strong text-classification use case

Naive Bayes is particularly useful for:

* Spam detection
* Sentiment classification
* Document classification
* Topic classification

---

# 15. Limitations of Naive Bayes

## Strong independence assumption

Features are assumed to be conditionally independent given the class.

Real-world features are often related.

## Limited context understanding

For example:

```text
"not good"
```

contains a relationship between the words.

Basic Bag-of-Words + Naive Bayes does not truly understand this context.

## Zero-frequency problem

Unseen features can produce zero probabilities.

Smoothing is used to reduce this problem.

## Not suitable for every problem

Naive Bayes may not be the best choice when the problem depends heavily on complex relationships between features.

---

# 16. When Should We Use Naive Bayes?

Naive Bayes is worth considering when:

* The problem is classification.
* The data is high-dimensional.
* The features are sparse.
* Text is involved.
* Fast training is important.
* A simple baseline is required.
* The assumptions are reasonably suitable for the problem.

A classic text classification pipeline is:

```text
Raw Text
   ↓
CountVectorizer / TF-IDF
   ↓
Numerical Features
   ↓
MultinomialNB
   ↓
Classification
```

---

# 17. Naive Bayes vs Other Algorithms

## Naive Bayes

```text
Probability-based
```

It asks:

> Which class is most probable given these features?

## KNN

```text
Similarity-based
```

It asks:

> Which training examples are closest to this new example?

## Logistic Regression

```text
Linear decision boundary
```

It learns feature weights and estimates class probabilities.

## SVM

```text
Margin-based
```

It searches for a decision boundary that separates classes with a large margin.

Comparison:

| Algorithm           | Core Idea           | Common Strength                 |
| ------------------- | ------------------- | ------------------------------- |
| Naive Bayes         | Probability         | Fast, high-dimensional text     |
| KNN                 | Distance/similarity | Local patterns                  |
| Logistic Regression | Linear boundary     | Strong classification baseline  |
| SVM                 | Maximum margin      | High-dimensional classification |

---

# 18. Real-World Applications

Naive Bayes can be used in:

## Spam Detection

```text
Email
 ↓
Text features
 ↓
Naive Bayes
 ↓
Spam / Not Spam
```

## Sentiment Analysis

```text
Review
 ↓
Text features
 ↓
Naive Bayes
 ↓
Positive / Negative
```

## Document Classification

```text
Article
 ↓
Word features
 ↓
Naive Bayes
 ↓
Technology / Business / Science / etc.
```

## Topic Classification

Classifying documents according to their subject.

## Intent Classification

For example:

```text
"How many casual leaves do I have?"
                ↓
          Naive Bayes
                ↓
          LEAVE_BALANCE
```

The predicted intent can then be passed to another system or tool.

---

# 19. Connection to Modern AI

Naive Bayes is not used to build modern LLMs.

Naive Bayes:

```text
Features
   ↓
Probabilistic classifier
   ↓
Class
```

Modern NLP:

```text
Text
   ↓
Tokenizer
   ↓
Transformer
   ↓
Learned representations
   ↓
Prediction / Generation
```

However, Naive Bayes teaches an important machine-learning concept:

> Transform data into useful representations and use a statistical model to make predictions.

This idea continues to exist in modern AI, even though the models and representations have become much more sophisticated.

---

# 20. Naive Bayes Mental Model

Remember this:

```text
                    NAIVE BAYES
                         |
               Probabilistic Classifier
                         |
              "Which class is likely?"
                         |
          +--------------+--------------+
          |              |              |
          ↓              ↓              ↓
     GaussianNB    MultinomialNB   BernoulliNB
          |              |              |
    Continuous         Counts         Binary
      values          /frequency       0/1
                         |
                         ↓
                 Especially useful
                    for text
```

---

# 21. Key Takeaways

1. Naive Bayes is a probabilistic classification algorithm.
2. It is based on Bayes' theorem.
3. Its "naive" assumption is conditional independence of features given the class.
4. GaussianNB is used for continuous numerical features.
5. MultinomialNB is useful for count/frequency features.
6. BernoulliNB is useful for binary features.
7. Laplace smoothing helps handle zero-frequency problems.
8. `predict()` returns the predicted class.
9. `predict_proba()` returns probability estimates.
10. `CountVectorizer` converts text into numerical count features.
11. Naive Bayes is particularly useful for text classification.
12. It is fast and works well with high-dimensional data.
13. It is useful as a simple and strong baseline.
14. It does not understand complex context like modern Transformer models.

---

# 22. Completion Checklist

* [x] Understand Bayes theorem concept
* [x] Understand Naive Bayes intuition
* [x] Understand the conditional independence assumption
* [x] Understand the core algorithm
* [x] Understand the zero-frequency problem
* [x] Understand Laplace smoothing
* [x] Learn GaussianNB
* [x] Learn MultinomialNB
* [x] Learn BernoulliNB
* [x] Understand CountVectorizer
* [x] Understand `fit_transform()` vs `transform()`
* [x] Understand `predict()`
* [x] Understand `predict_proba()`
* [x] Implement GaussianNB
* [x] Implement MultinomialNB
* [x] Implement BernoulliNB
* [x] Understand advantages
* [x] Understand limitations
* [x] Understand when to use Naive Bayes
* [x] Compare Naive Bayes with KNN, Logistic Regression and SVM
* [x] Understand real-world applications
* [x] Complete final knowledge checkpoint

---

# Day 25 Status

**Completed — Naive Bayes**

The three major Naive Bayes variants were implemented using scikit-learn:

```text
GaussianNB
MultinomialNB
BernoulliNB
```
```
