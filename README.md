# Data-Visualization-Labs
# Lab 1: Exploring the IRIS Dataset  

## **Objective**
The objective of this lab is to explore the IRIS dataset through data manipulation and summary statistics. The following tasks were performed:  
- Data loading and inspection  
- Summary statistics computation  
- Data filtering and visualization  

---

## **Table of Contents**
1. [Introduction](#introduction)  
2. [Dataset Overview](#dataset-overview)  
3. [Tasks Performed](#tasks-performed)  
4. [Results and Insights](#results-and-insights)  
5. [Dependencies](#dependencies)  

---

## **Introduction**
The IRIS dataset is a classic dataset in machine learning and data visualization. It contains 150 samples of iris flowers from three species—*Iris setosa*, *Iris versicolor*, and *Iris virginica*. Each sample includes four features:  
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

This lab demonstrates basic data handling, summary statistics, and filtering techniques.  

---

## **Dataset Overview**
- **File Format:** CSV  
- **Features:**  
  - SepalLengthCm  
  - SepalWidthCm  
  - PetalLengthCm  
  - PetalWidthCm  
  - Species  
- **Rows and Columns:** 150 rows, 5 columns  

---

## **Tasks Performed**

### **1. Data Loading and Inspection**
- Imported necessary libraries such as `pandas` and `numpy`.  
- Loaded the IRIS dataset from a CSV file.  
- Displayed the first and last `n` rows for a quick overview.  
- Checked the dataset's shape and printed column names.  
- Accessed individual elements for better understanding of the data.  
- Retrieved data type information for each column.  

### **2. Data Manipulation**
- Added and removed specific rows/columns.  
- Filtered the dataset to include only rows where the `Species` is "setosa".  

### **3. Data Summary**
Calculated the following summary statistics for numerical columns:  
- **Measures of Central Tendency:** Mean, Median  
- **Measures of Dispersion:** Standard Deviation, Variance  
- **Extreme Values:** Minimum, Maximum, Quartiles, Range  

### **4. Visualization**
- Counted the number of instances for each species.  
- Plotted a basic bar plot to visualize species counts.  

---

## **Results and Insights**
- The filtered dataset for *Iris setosa* contains 50 rows.  
- The mean and median values for each feature were close, indicating a relatively symmetric distribution.  
- The standard deviation and variance provided insights into the variability of the data.  
- A bar plot revealed that the dataset is balanced, with equal instances for each species (*setosa*, *versicolor*, and *virginica*).  

---

## **Dependencies**
This lab was implemented using the following libraries:  
- **Python Version:** 3.x  
- **Required Libraries:**  
  - `pandas`  
  - `numpy`  
  - `matplotlib`  

---

## **Usage Instructions**
1. Clone the repository:
   ```bash
   git clone <https://github.com/Vansh-1007/Data-Visualization-Labs>
   cd Data-Visualization-Labs
2.pip install -r requirements.txt
3.python analysis.py

