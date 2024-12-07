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

# Lab 3: Exploring Univariate and Bivariate Data Visualization  

## **Objective**  
The objective of this lab is to explore and visualize univariate and bivariate relationships in the **Movielens 100k dataset**, focusing on movie ratings, user demographics, and genre popularity.  

---

## **Dataset Description**  
The **Movielens 100k dataset** is a benchmark dataset widely used in recommender systems research. It contains:  
- **Ratings:** 100,000 ratings (1-5) provided by 943 users for 1,682 movies.  
- **Users:** Each user has rated at least 20 movies and has demographic attributes such as age, gender, occupation, and ZIP code.  
- **Movies:** Each movie is associated with one or more genres.  

---

## **Key Features**
| **Attribute**  | **Description** |
|-----------------|-----------------|
| `user_id`       | Unique identifier for each user. |
| `movie_id`      | Unique identifier for each movie. |
| `rating`        | Movie rating (integer between 1 and 5). |
| `timestamp`     | When the rating was provided. |
| `age`           | User's age group. |
| `gender`        | User's gender (M/F). |
| `occupation`    | User's occupation. |
| `zip_code`      | User's ZIP code. |
| `genres`        | Genres associated with each movie. |

---

## **Visualization Questions**  
### **Univariate Analysis**  
1. What is the average rating for each movie genre?  
2. Which genres are the most popular based on the number of ratings received?  

### **Bivariate Analysis**  
3. Which movies (Top-10) have received the highest number of ratings?  
4. Are there significant differences in preferences for different movie genres between male and female users?  
5. Do male or female users rate more movies on average?  
6. Which movies have the highest average ratings within each genre?  
7. How do ratings vary across different user age groups?  
8. How do ratings vary across different user occupations?  
9. Which genres are preferred by different age groups?  
10. How do user preferences evolve over time? Can we observe any shifts in genre popularity?  

---

## **Analysis Overview**  

### **Univariate Analysis**  
- **Average Rating for Each Genre:**  
  - Bar plots were used to display the average ratings for genres.  

- **Popularity of Genres (Number of Ratings):**  
  - A horizontal bar plot visualized the number of ratings for each genre.  

### **Bivariate Analysis**  
- **Top-10 Movies with the Most Ratings:**  
  - A sorted bar plot identified the most rated movies.  

- **Gender Preferences for Genres:**  
  - Grouped bar plots compared male and female preferences for various genres.  

- **Average Ratings by Gender:**  
  - Calculated the average number of movies rated by male and female users.  

- **Highest-Rated Movies by Genre:**  
  - Filtered and plotted the top-rated movies for each genre.  

- **Ratings by Age Groups:**  
  - Boxplots showed the distribution of ratings across different age groups.  

- **Ratings by Occupation:**  
  - Grouped bar plots visualized how ratings varied across occupations.  

- **Age-Group Preferences for Genres:**  
  - Heatmaps displayed genre preferences by age groups.  

- **Genre Popularity Over Time:**  
  - Line charts tracked the number of ratings per genre across time.  

---

## **Results and Insights**  
1. **Most Popular Genres:**  
   - Action, Drama, and Comedy were the most rated genres.  
2. **Gender-Based Preferences:**  
   - Male users rated Action and Sci-Fi movies more, while female users preferred Drama and Romance.  
3. **Age-Based Patterns:**  
   - Older age groups rated Drama and Western genres more, while younger users rated Action and Sci-Fi more.  
4. **Top-Rated Movies:**  
   - Some lesser-known movies within niche genres had the highest average ratings.  
5. **Time Trends:**  
   - Over time, Comedy and Romance ratings showed a steady increase in popularity.  

---

## **Dependencies**
This analysis requires the following Python libraries:  
- `pandas`  
- `numpy`  
- `matplotlib`  
- `seaborn`  

Install the required dependencies using the command:  
```bash
pip install -r requirements.txt
git clone https://github.com/Vansh-1007/Data-Visualization-Labs
cd Data-Visualization-Labs/Lab3
pip install -r requirements.txt
python movielens_analysis.py


