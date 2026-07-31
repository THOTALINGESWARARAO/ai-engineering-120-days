# Day 7 – Probability & Statistics Foundations

# Chapter 1: Why AI Engineers Need Probability and Statistics

## Need

Traditional programs work with certainty, but AI systems work with uncertainty. Probability helps AI make decisions under uncertainty, while statistics helps AI understand data before learning from it.

## Key Ideas

* Traditional programming is deterministic.
* AI makes probabilistic predictions.
* Statistics analyzes data.
* Probability predicts uncertain outcomes.

## Official Definitions

### Probability

Probability is the branch of mathematics that measures the likelihood of an event occurring.

### Statistics

Statistics is the branch of mathematics concerned with collecting, organizing, analyzing, interpreting, and presenting data.

## AI Examples

* Spam Detection
* Face Recognition
* Weather Prediction
* Recommendation Systems
* Large Language Models

## Difference

| Statistics       | Probability             |
| ---------------- | ----------------------- |
| Starts with data | Starts with uncertainty |
| Understands data | Predicts outcomes       |
| Data → Knowledge | Knowledge → Prediction  |

## Revision

* Statistics helps understand data.
* Probability helps make predictions.
* Machine Learning uses both.

---

# Chapter 2: Deterministic vs Probabilistic Systems

## Deterministic System

### Definition

A system in which the same input always produces the same output.

### Examples

* Calculator
* Sorting Algorithm
* Arithmetic Operations

### Characteristics

* Exact rules
* No uncertainty
* Predictable output

---

## Probabilistic System

### Definition

A system that assigns probabilities to possible outcomes instead of guaranteeing one exact answer.

### Examples

* ChatGPT
* Spam Detection
* Image Classification
* Speech Recognition

### Characteristics

* Handles uncertainty
* Learns patterns
* Produces confidence scores

---

## Comparison

| Deterministic | Probabilistic            |
| ------------- | ------------------------ |
| Rule Based    | Data Driven              |
| Certain       | Uncertain                |
| Fixed Output  | Probability Distribution |

## Revision

* Traditional software is deterministic.
* AI models are probabilistic.

---

# Chapter 3: What is Uncertainty?

## Definition

Uncertainty is the condition in which the exact outcome of an event cannot be known beforehand.

## Why Does Uncertainty Exist?

* Future events
* Incomplete information
* Randomness
* Measurement noise

## Types of Uncertainty

### Aleatoric Uncertainty

Randomness inherent in nature.

Examples

* Coin toss
* Dice roll
* Sensor noise

### Epistemic Uncertainty

Lack of knowledge.

Examples

* Missing data
* Limited training data
* Incomplete medical tests

## Important Points

* Probability measures uncertainty.
* Probability does not eliminate uncertainty.

## AI Examples

* Image Classification
* Weather Forecasting
* Self-driving Cars
* ChatGPT

## Revision

* No uncertainty → No need for probability.
* More uncertainty → Greater importance of probability.

---

# Chapter 4: Random Experiment

## Definition

A random experiment is a process that:

1. Can be repeated.
2. Has known possible outcomes.
3. Has an unknown exact outcome before it is performed.

## Examples

* Coin Toss
* Dice Roll
* Drawing a Card
* Measuring Today's Temperature

## Not Random Experiments

* 2 + 2
* Sorting an Array
* Multiplication Table

## Flow

Random Experiment
↓
Possible Outcomes
↓
One Outcome Occurs

## AI Connection

Input Image
↓
AI Model
↓
Predicted Class

The prediction is uncertain before inference.

## Revision

A random experiment:

* Is repeatable.
* Has known possible outcomes.
* Produces one unknown outcome.

---

# Chapter 5: Outcome

## Definition

An outcome is a single possible result of a random experiment.

## Examples

### Coin Toss

Experiment:
Flip a Coin

Possible Outcomes:

* Heads
* Tails

Actual Outcome:

* Heads

---

### Dice Roll

Experiment:
Roll a Die

Possible Outcomes:
1, 2, 3, 4, 5, 6

Actual Outcome:
4

---

## Important Concepts

Possible Outcomes
All results that may occur.

Actual Outcome
The single result that actually occurs.

## Outcome vs Experiment

Experiment:
Roll a Die

Outcome:
5

Experiment is the action.

Outcome is the result.

## AI Example

Image Classification

Possible Outcomes:

* Cat
* Dog
* Horse
* Rabbit

Predicted Outcome:
Dog

## Revision

* An outcome is always one result.
* One experiment can have many possible outcomes.
* One execution produces exactly one actual outcome.

---

# Overall Mental Map

```
Why AI Needs Probability & Statistics
                │
                ▼
Deterministic vs Probabilistic Systems
                │
                ▼
          Uncertainty
                │
                ▼
      Random Experiment
                │
                ▼
            Outcome
                │
                ▼
         Sample Space (Next)
```

---

# Key Takeaways

* Statistics helps us understand data.
* Probability helps us make decisions under uncertainty.
* AI systems are probabilistic, not deterministic.
* Uncertainty is the reason probability exists.
* A random experiment is repeatable and has an unknown outcome.
* An outcome is the single result produced by a random experiment.
