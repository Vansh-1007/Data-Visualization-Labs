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

# Lab 2: Exploring Univariate Data Visualization  

## **Objective**
The objective of this lab is to understand and visualize univariate data using different types of plots and to explore the importance of visualization over summary statistics using the **Datasaurus dozen** dataset.

---

## **Table of Contents**
1. [Introduction](#introduction)  
2. [Dataset Descriptions](#dataset-descriptions)  
   - [MTCars Dataset](#mtcars-dataset)  
   - [Datasaurus Dozen Dataset](#datasaurus-dozen-dataset)  
3. [Tasks Performed](#tasks-performed)  
   - [Exploring MTCars Dataset](#2a-exploring-mtcars-dataset)  
   - [Visualizing Datasaurus Dozen](#2b-visualizing-datasaurus-dozen)  
4. [Results and Insights](#results-and-insights)  
5. [Dependencies](#dependencies)  

---

## **Introduction**
Data visualization is a fundamental part of data analysis, allowing us to uncover patterns and anomalies that may be missed by summary statistics alone.  
This lab is divided into two parts:  
1. **MTCars Dataset:** Visualizing univariate data using various plot types.  
2. **Datasaurus Dozen:** Demonstrating how similar summary statistics can represent vastly different data distributions.  

---

## **Dataset Descriptions**

### **MTCars Dataset**
The **MTCars** dataset contains 32 observations of cars with the following 11 numeric variables:  
| **Column Name** | **Description** |
|------------------|------------------|
| `mpg`            | Miles per gallon |
| `cyl`            | Number of cylinders |
| `disp`           | Displacement (cu.in.) |
| `hp`             | Gross horsepower |
| `drat`           | Rear axle ratio |
| `wt`             | Weight (1000 lbs) |
| `qsec`           | 1/4 mile time |
| `vs`             | Engine type (0 = V-shaped, 1 = straight) |
| `am`             | Transmission (0 = automatic, 1 = manual) |
| `gear`           | Number of forward gears |
| `carb`           | Number of carburetors |

### **Datasaurus Dozen Dataset**
The **Datasaurus dozen** dataset consists of several data subsets with nearly identical summary statistics (mean, variance, correlation) but vastly different visual distributions.  
- **Link to dataset:** [Download Here](https://drive.google.com/file/d/1Cr9Z9l17Npm19c2Nq34lhb15sQpodxPB/view?usp=sharing)

---

## **Tasks Performed**

### **2.a. Exploring MTCars Dataset**
The following questions were explored using visualizations:  
1. **What is the distribution of the `mpg` variable?**  
   - Used a histogram and density plot.  
2. **What are the counts of cars for each cylinder type (`cyl`)?**  
   - Created a bar plot.  
3. **What is the proportion of cars with automatic (`am = 0`) versus manual (`am = 1`) transmission?**  
   - Used a pie chart and bar plot.  
4. **How does the distribution of horsepower (`hp`) look?**  
   - Created a boxplot and identified outliers.  
5. **What is the frequency distribution of cars with different numbers of gears (`gear`)?**  
   - Visualized using a bar plot.  

**Bonus Questions:**  
- Visualized the relationship between `wt` (weight) and `mpg` using a scatter plot.  
- Analyzed the distribution of `qsec` (1/4 mile time) using a violin plot.  

---

### **2.b. Visualizing Datasaurus Dozen**
- Visualized all subsets of the **Datasaurus dozen** dataset.  
- Compared the summary statistics of each subset (mean, variance, correlation).  
- Highlighted the differences in data distributions through scatter plots.  

---

## **Results and Insights**

### **MTCars Dataset**
- The `mpg` variable has a slightly right-skewed distribution.  
- Cars with 4 cylinders are more common than those with 6 or 8 cylinders.  
- There is a near-equal proportion of cars with automatic and manual transmissions.  
- Horsepower (`hp`) data has a few outliers, as revealed by the boxplot.  
- Most cars have either 3 or 4 forward gears, with very few having 5.  

### **Datasaurus Dozen**
- Despite identical summary statistics, each subset of the Datasaurus dozen dataset displayed unique patterns when visualized.  
- The visualizations emphasized the importance of always plotting data rather than relying solely on statistics.  

---

## **Dependencies**
This lab was implemented using the following libraries:  
- **Python Version:** 3.x  
- **Required Libraries:**  
  - `pandas`  
  - `matplotlib`  
  - `seaborn`  

---

## **Usage Instructions**
1. Clone the repository:
   ```bash
   git clone <https://github.com/Vansh-1007/Data-Visualization-Labs>
   cd Data-Visualization-Labs

2.pip install -r requirements.txt
3.python mtcars_analysis.py
4.python datasaurus_visualization.py

