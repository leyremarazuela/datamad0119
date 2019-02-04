
# coding: utf-8

# ## Pipelines Project 

# # Step 0 : Importing libraries and dataset
# 

# In[24]:


# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


# Import our dataset
data = pd.read_csv('./2015.csv')


# # Step 1 : Data Acquisition

# In[26]:


data.head()


# In[27]:


data.shape


# In[28]:


data.dtypes


# ## STEP 2: Data Wrangling 
# 

# In[29]:


# Find how prevalent missing values are in our data 
null_cols = data.isnull().sum()
null_cols


# In[30]:


stats = data.describe().transpose()
stats['IQR'] = stats['75%'] - stats['25%']
stats


# In[31]:


outliers = pd.DataFrame(columns=data.columns)
outliers


# In[32]:


for col in stats.index:
    iqr = stats.at[col,'IQR']
    cutoff = iqr * 3
    lower = stats.at[col,'25%'] - cutoff
    upper = stats.at[col,'75%'] + cutoff
    results = data[(data[col] < lower) | 
                   (data[col] > upper)].copy()
    results['Outlier'] = col
    outliers = outliers.append(results)
    
outliers


# In[33]:


data.drop(index = list(outliers.index), inplace=True)


# In[42]:


outliers.index


# In[17]:


data.head(68)


# In[34]:


before = len(data)
data = data.drop_duplicates()
after = len(data)
print('Number of duplicate records dropped: ', str(before - after))


# ## STEP 3: Data Analysis
# 

# In[35]:


data.describe()


# In[36]:


# Most important determinants happinness

print(data['Happiness Score'].corr(data['Economy (GDP per Capita)']))
print("---")

print(data['Happiness Score'].corr(data['Family']))
print(data['Happiness Score'].corr(data['Health (Life Expectancy)']))

print("---")
print(data['Happiness Score'].corr(data['Freedom']))
print(data['Happiness Score'].corr(data['Trust (Government Corruption)']))
print(data['Happiness Score'].corr(data['Generosity']))


# In[37]:


data.corr


# ##  STEP 4: Reporting and Distribution  
# 

# In[39]:


"""
#### Important determinant happinness
Economy (GDP per Capita)

#### Moderately important determinant happinness
Family
Health (Life Expectancy)

#### Not very important determinant happinness
Freedom
Trust (Government Corruption)
Generosity
"""


# ## STEP 5: Get yearly report as csv
# 

# In[40]:


data.to_csv('./2015_happinness.csv', index=False)

