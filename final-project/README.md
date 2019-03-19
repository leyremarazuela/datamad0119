# Final Project: Finding presence of heart disease

**Leyre Marazuela**

**Data Analysis Bootcamp January 2019**

## Overview

The goal of this project is to investigate if patients have heart disease or not based on other values. The integer is accounted for in the column "target" valued 0 (no presence) or 1 (indicating presence of heart disease). For this project, I will use the Dataset of Heart Disease UCI (https://archive.ics.uci.edu/ml/datasets/heart+Disease) which is public and is available to download in Kaggle:
https://www.kaggle.com/ronitf/heart-disease-uci/home.

Therefore, the research question I would like to answer is whether the presence of heart disease can be predicted based on several independent variables. We will test this question using a variety of supervised machine learning models.

Our null hypothesis is that age, sex and other attributes do not allow us to predict if patients have heart disease or not at a 0.20 significance level. The alternative hypothesis, therefore, is that these attributes do allow us to predict if patients have heart disease at a 0.20 significance level.

Overall the project consists of a series of steps as outlined below. In summary, I will import the dataset, use data wrangling skills to clean it up, prepare it to be analyzed, export it as a clean CSV data file, analyse it to find meaningful insights and use a machine learning algorithm to predict if the patient has heart disease or not. 

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

--------------------------------------

# Step 0 : Data acquisition
# Step 1 : Data wrangling
    ## 1A : Understand Info contained in Data & Examinine Data for Potential Issues
    ## 1B: Cleaning Data
    ## 1C : Manipulating Data
# Step 2: Data storage
# Step 3: Data exploration and analysis
# Step 4: Feature selection
# Step 5: Machine learning model training
# Step 6: Model evaluation (Supervised Learning Algorithms)
    ## 1 : Logistic Regression
    ## 2: K-Nearest Neighbour (KNN) Classification
    ## 3 : Support Vector Machine (SVM) Algorithm
    ## 4 : Naive Bayes Algorithm
    ## 5: Decision Tree Algorithm
    ## 6 : Random Forest Classification
    ## 7 : Neural Network

# Step 7: Reporting and presentation of insights


--------------------------------------

## Conclusion

At the 0.2 significance level there is sufficient evidence to reject the null hypothesis and accept the alternative hypothesis, which means we are able to predict whether patients have heart disease based on a set of predictor variables.

However, it must be said that this dataset is old and small and we must not rely solely on it to make pre-emptive diagnoses of patients. We must make sure that the precision and recall of the machine learning models is improved to ensure patients get a correct diagnosis.

--------------------------------------

### Deliverables

* **A cleaned CSV data file** containing the results of my data wrangling work.
* **A Jupyter Notebook (data-wrangling.ipynb)** containing all Python code and commands used in the importing, cleaning, manipulation, and exporting of your data set.
* **A ``README.md`` file** containing a detailed explanation of the process followed in the importing, cleaning, manipulation, and exporting of your data as well as your results, obstacles encountered, and lessons learned.