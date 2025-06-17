# Critical Statistical Knowledge Summary

## Introduction to Statistics
Statistics is the science of collecting, analyzing, interpreting, and presenting data. It’s divided into:
- **Descriptive Statistics**: Summarizes data (e.g., mean, variance).
- **Inferential Statistics**: Makes conclusions about populations from samples (e.g., hypothesis testing).

Statistics is vital for data-driven decisions in fields like business, science, and technology (e.g., AB testing at Netflix).

## Descriptive Statistics
Tools to summarize data:
- **Central Tendency**:
  - Mean: $\mu = \frac{\sum x_i}{n}$ (average).
  - Median: Middle value.
  - Mode: Most frequent value.
- **Variability**:
  - Range: Max - Min.
  - Variance: $\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}$.
  - Standard Deviation: $\sigma = \sqrt{\sigma^2}$.
- **Distributions**: Normal (bell curve), binomial, Poisson.

These help describe data patterns, like user engagement metrics.

## Probability
The foundation of statistical inference:
- **Rules**:
  - Addition: $P(A \cup B) = P(A) + P(B)$ (mutually exclusive).
  - Multiplication: $P(A \cap B) = P(A) \times P(B)$ (independent).
  - Conditional: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
- **Distributions**:
  - Discrete: Binomial, Poisson.
  - Continuous: Normal, Exponential.
- **Expected Value**: $E(X) = \sum {x_i P(x_i)}$ (discrete).

Probability models uncertainty, crucial for predicting outcomes.

## Inferential Statistics
Draws conclusions from samples:
- **Sampling**: Random, stratified (ensures representativeness).
- **Central Limit Theorem**: Sample means approximate a normal distribution as sample size grows.
- **Hypothesis Testing**:
  - Null (\(H_0\)): No effect.
  - Alternative (\(H_a\)): Effect exists.
  - P-Value: Probability of data under \(H_0\).
  - Significance (\(\alpha\)): Risk of false positive (Type I error).
- **Confidence Intervals**: Range for population parameter (e.g., 95%).

Used in AB testing to assess if changes are significant.

## Hypothesis Testing in AB Testing
- **T-Test** (means):
  \[
  t = \frac{\bar{Y}_t - \bar{Y}_c}{\sqrt{\frac{s_t^2}{n_t} + \frac{s_c^2}{n_c}}}
  \]
- **Z-Test** (proportions):
  \[
  z = \frac{\hat{p}_t - \hat{p}_c}{\sqrt{\hat{p}(1 - \hat{p}) \left( \frac{1}{n_t} + \frac{1}{n_c} \right)}}
  \]

Tests determine if differences between control and test groups are real.

## Minimum Detectable Effect (MDE)
Smallest effect an experiment can detect:
- For means: \(\delta = \sqrt{\frac{2(\sigma_t^2 + \sigma_c^2)}{n}} \times (Z_{1 - \alpha/2} + Z_{1 - \beta})\).

Guides sample size planning.

## Variance Reduction
Increases test sensitivity:
- **Stratified Sampling**: Reduces variance by grouping (e.g., by user type).
- **CUPED**: Adjusts metrics with pre-experiment data: \(Y_{CUPED} = Y - \theta (X - \bar{X})\).

Key for detecting small changes, like at Netflix.

## Additional Concepts
- **Type I Error**: False positive.
- **Type II Error**: False negative.
- **Correlation vs. Causation**: AB tests help establish causality.

## Applications
- **Business**: Forecasting, quality control.
- **Science**: Experimental analysis.
- **Tech**: AB testing, machine learning.

Statistics powers decisions by quantifying uncertainty and significance.