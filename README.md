# Data Visualization Labs

This repository contains seven data visualization labs that explore various data visualization techniques, including basic plots, advanced visualizations, and smoothing methods using stock price data.

## Table of Contents
1. [Lab 1: Exploring the IRIS Dataset](Lab1/README.md)
2. [Lab 2: Exploring Univariate Data Visualization](Lab2/README.md)
3. [Lab 3: Exploring Bivariate Data Visualization](Lab3/README.md)
4. [Lab 4: Visualizing NIRF Rankings](Lab4/README.md)
5. [Lab 5: Exploring Data Science Trends](Lab5/README.md)
6. [Lab 6: Time Series Visualization](Lab6/README.md)
7. [Lab 7: LOESS Smoothing](Lab7/README.md)

## Lab Summaries

### Lab 1: Exploring the IRIS Dataset
- **Objective:** Understand the IRIS dataset and visualize different features.
- **Key Tasks:** 
  - Load the IRIS dataset.
  - Create visualizations to show relationships between different features (e.g., scatter plots, box plots).

### Lab 2: Exploring Univariate Data Visualization
- **Objective:** Explore univariate visualizations for a single dataset.
- **Key Tasks:**
  - Create histograms, box plots, and density plots for understanding distributions.

### Lab 3: Exploring Bivariate Data Visualization
- **Objective:** Explore bivariate relationships in a dataset.
- **Key Tasks:**
  - Create scatter plots, heat maps, and correlation matrices to visualize relationships between pairs of variables.

### Lab 4: Visualizing NIRF Rankings
- **Objective:** Visualize data from the National Institutional Ranking Framework (NIRF) of India.
- **Key Tasks:**
  - Visualize rankings for various institutions using bar plots and pie charts.
  - Compare performance across years and institutions.

### Lab 5: Exploring Data Science Trends
- **Objective:** Visualize and analyze trends in the data science field.
- **Key Tasks:**
  - Create visualizations of data science job market trends, education, and salary data.
  - Use line charts and bar plots to explore long-term trends.

### Lab 6: Time Series Visualization
- **Objective:** Explore and visualize stock price data over time using different smoothing techniques.
- **Key Tasks:**
  - **Data Collection:** Download daily closing prices of Reliance India stock from 16th October 2023 to 16th October 2024.
  - **Plot Raw Data:** Visualize the raw stock price data.
  - **Apply Smoothing Techniques:**
    - Simple Moving Average (SMA) for window sizes of 7, 15, and 30 days.
    - Centered Moving Average (CMA) for window sizes of 5, 10, and 15 days.
    - Weighted Moving Average (WMA) with a 5-day window, using higher weights for recent days.

### Lab 7: LOESS Smoothing
- **Objective:** Apply LOESS smoothing to stock price data and analyze its effects.
- **Key Tasks:**
  - **Dataset:** Reliance Stock Price Data for the last 60 days.
  - **Plot Stock Prices:** Visualize the raw stock prices as a scatter plot.
  - **Apply LOESS Smoothing:** Use 6 different span values (0.15, 0.30, 0.45, 0.60, 0.75, 0.90).
  - **Compare Polynomial Fits:** For the optimal span, compare linear (degree 1) vs quadratic (degree 2) polynomial smoothing and discuss which fits the data better.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Vansh-1007/Data-Visualization-Labs.git
