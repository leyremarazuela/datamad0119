## Pipelines Project 

# # Step 0 : Importing libraries and dataset
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # Step 1 : Data Acquisition

def data_acquisition(filename):
    
    data = pd.read_csv(filename)

    print("Data Types :")
    print(data.dtypes)
    print("Check all data types of old and new variables are correct")    
    print("============== ")
        
    print("Data Shape :")
    print(data.shape)
    print("============== ")

    print("Data Head :")
    print(data.head())
    print("============== ")
    return data

# # Step 2 : Data Wrangling

def data_wrangling_null(data):
    # Find how prevalent missing values are in our data 
    null_cols = data.isnull().sum()
    if null_cols.any() > 0:
        # eliminarmos filas con nulos
        data.dropna(axis='index')
        
        # eliminarmos columnas con nulos
        data.dropna(axis='columns')

    return data

def data_wrangling_outliers(data):
    stats = data.describe().transpose()
    stats['IQR'] = stats['75%'] - stats['25%']
    outliers = pd.DataFrame(columns=data.columns)
    
    for col in stats.index:
        iqr = stats.at[col,'IQR']
        cutoff = iqr * 3
        lower = stats.at[col,'25%'] - cutoff
        upper = stats.at[col,'75%'] + cutoff
        results = data[(data[col] < lower) | 
                       (data[col] > upper)].copy()
        results['Outlier'] = col
        outliers = outliers.append(results)
    data.drop(index = list(outliers.index), inplace=True)
    return data

def data_wrangling_duplicates(data):
    before = len(data)
    data = data.drop_duplicates()
    after = len(data)
    print('Number of duplicate records dropped: ', str(before - after))
    return data

# # Step 3 : Data Wrangling

def data_analysis_reporting(data):
    print("Analysing this below, you can find mean, max, min, std and more measures of dispersion and central tendency:")
    print(data.describe())
    print("============== ")
    
    ls = []
    ls.append(data['Happiness Score'].corr(data['Economy (GDP per Capita)']))
    ls.append(data['Happiness Score'].corr(data['Family']))
    ls.append(data['Happiness Score'].corr(data['Health (Life Expectancy)']))
    ls.append(data['Happiness Score'].corr(data['Freedom']))
    ls.append(data['Happiness Score'].corr(data['Trust (Government Corruption)']))
    ls.append(data['Happiness Score'].corr(data['Generosity']))

# # Step 4 : Data Reporting
    ls2 = ['Economy (GDP per Capita)', 
           'Family', 'Health (Life Expectancy)', 
           'Freedom', 'Trust (Government Corruption)',
           'Generosity']
    counter = 0
    for i in ls:
        if i > 0.75:    
            print(ls2[counter] + " = very relevant")
        elif i > 0.70:
            print(ls2[counter] + " = moderately relevant")
        else:
            print(ls2[counter] + " = not relevant")
        counter +=1
        
    return data

# # Step 5 : Save clean CSV 

def clean_csv(data):
    data = data.to_csv('./{}_happinness.csv'.format(year), index=False)
    return data 

# # Step 6 : Execute pipeline

if __name__ == "__main__":
    
    year = input('Year: ')
    filename = './{}.csv'.format(year)
    
    data = data_acquisition(filename)
    data = data_wrangling_null(data)
    data = data_wrangling_outliers(data)
    data = data_wrangling_duplicates(data)
    data = data_analysis_reporting(data)
    data = data_analysis_reporting(data)
    data = clean_csv(data)


