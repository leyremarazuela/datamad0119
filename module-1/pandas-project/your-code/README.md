# Pandas Project: Demonstration of Data Cleaning and Manipulation with Pandas

## Overview

The goal of this project is to investigate which patients have higher incidence of heart disease. The integer is valued from 0 (no presence) to 4, and corresponds to the "chest pain type" field. For this project, I will use the Dataset of Heart Disease UCI
(https://www.kaggle.com/ronitf/heart-disease-uci/home) from Kaggle.

Our null hypothesis is that age, sex and other attributes are significant determinants in the incidence of chest pain (cp from now on) in patients. The alternative hypothesis, therefore, is that there is generally no greater high correlation between these attributes and the incidence of chest pain.

Overall the project consists of a series of steps as outlined below. In summary, I will import the dataset, use  data wrangling skills to clean it up, prepare it to be analyzed, and then export it as a clean CSV data file.

---

## Intro: Understand info contained in data

This database contains 14 attributes including:

> 1. age 
> 2. sex 
> 3. chest pain type (4 values) 
> 4. resting blood pressure 
> 5. serum cholestoral in mg/dl 
> 6. fasting blood sugar > 120 mg/dl
> 7. resting electrocardiographic results (values 0,1,2)
> 8. maximum heart rate achieved 
> 9. exercise induced angina 
> 10. oldpeak = ST depression induced by exercise relative to rest 
> 11. the slope of the peak exercise ST segment 
> 12. number of major vessels (0-3) colored by flourosopy 
> 13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

This means that each row corresponds to a patient and the columns are equivalent to the attributes.


# Step 0 : Importing libraries and dataset
import pandas as pd 
import numpy as np
data = pd.read_csv('./heart.csv')


# Step 1 : Understand Info contained in Data & Examinine Data for Potential Issues
display(data.head())
data.describe()
data.shape

# Step 2 : Cleaning Data
### Missing Values -> find how prevalent missing values are in our data 
### Incorrect Values 
### Low Variance Columns
### Outliers -> Percentiles
### Extreme Values -> IQR
### Finding and Removing Duplicates

## Step 3: Manipulate and Clean Data.
### Renaming Columns
### Changing Column Order
### Binning Numeric Variables
### Substituting Binned Variables

## Step 4: Export clean CSV version of your data using Pandas.
data.to_csv('./heartClean.csv', index=False)

## Step 5: Interpret results

## Important | Descriptive Attributes
The age is highly indicative of cp, with 50% of the patients suffering cp at the age of 47 - 61. Below 30 and above 75 is extremely rare. 
Meanwhile, sex is an important indicator although not as determining as age. If you are a women you are much more likely to suffer from this disease. Based on a random sample of patients, 68% were women whereas the rest where men.

## Moderately important Attributes| Moderately descriptive Attributes

In this sense, the modal number of major vessels is 0, however there tends to be a large variation with certain patients, which have a much higher std. deviation.
Finally, the ST depression induced by exercise modal's value is also 0 but there is also a high std. deviation (higher than the mean) since there can be large variations among patients. This could be due to few, but very high values distorting the measurement, because other factors affect this variable (such as daily sport practiced).

## Non-important| Non-descriptive Attributes
-> Categorical data 
Furthermore, we can conclude the results of the general symptoms of cp. Indeed, the resting blood pressure tends to average at around 132, with there being very little std. deviation (only 17.5).
Also, cholesterol tends to average at 246 mg/dl with there being 51.7 std. deviation, which is under normal ranges. However, for cholesterol there are certain outliers which could indicate these levels are also related to other factors such as diet.
Additionally, thalac (the maximum heart rate achieved) shows little dispersion in the data since the mean is 150 and the std. deviation is only 22.9.

-> Discrete data (yes or no)
Moreover, most patients tend to not have a fasting blood sugar greater than 120 mg/dl, nor do they usually have exercised induced angina.

---

## References

* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
* [StackOverflow Pandas Questions](https://stackoverflow.com/questions/tagged/pandas)

### Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A cleaned CSV data file** containing the results of my data wrangling work.
* **A Jupyter Notebook (data-wrangling.ipynb)** containing all Python code and commands used in the importing, cleaning, manipulation, and exporting of your data set.
* **A ``README.md`` file** containing a detailed explanation of the process followed in the importing, cleaning, manipulation, and exporting of your data as well as your results, obstacles encountered, and lessons learned.

---
### Outputs (not done)

* A presentation in [slides.com](https://slides.com/)
* A demo deployed on GitHub Pages
* Display an screenshot of your GitHub graphs to show your commit frequency and how much work you did.
