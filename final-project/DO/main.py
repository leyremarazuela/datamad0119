
# coding: utf-8

# # Final Project : Diagnosing Heart Disease
# 

# In[1]:


from __future__ import print_function
import numpy as np

from hyperopt import Trials, STATUS_OK, tpe
from keras.datasets import mnist
from keras.layers.core import Dense, Dropout, Activation
from keras.models import Sequential
from keras.utils import np_utils

from hyperas import optim
from hyperas.distributions import choice, uniform

# Importing our libraries

# Pandas -> data manipulation
import pandas as pd 
pd.options.mode.chained_assignment = None  #hide any pandas warnings

# Numpy
import numpy as np

# Stats
import scipy.stats as stats

# Matplotlib
import matplotlib
from matplotlib import pyplot
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

# Plotly
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Seaborn
import seaborn as sns

# Wordcloud
from wordcloud import WordCloud 

## Sci-kit learn
# Train & testing
from sklearn.model_selection import train_test_split

# Decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Metrics
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

## Models
# Supervised Learning/Non-deep Algorithms
from sklearn.linear_model import LogisticRegression
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Supervised Learning/Deep Algorithms
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Unsupervised Learning Algorithms
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram

## Extras
# Plotting 3D Models
from mpl_toolkits.mplot3d import Axes3D

# Random
import random

# Asci Letters
from string import ascii_letters


# In[2]:


# Importing our dataset
data = pd.read_csv('./heart.csv')


# ## 1A : Understand Info contained in Data & Examinine Data for Potential Issues

# In[3]:


# display(data.head())


# In[4]:


# data.shape


# In[5]:


# Show how the presence of heart disease varies according to age 

'''
pd.crosstab(data.age,data.target).plot(kind="bar",figsize=(20,6))
plt.title('Heart Disease Distribution by Ages')
plt.xlabel('Age of patients')
plt.ylabel('Presence or Absence of Heart Disease')
plt.show()
'''

# In[6]:


#### Categorise for decades

data.reset_index(drop=True, inplace=True)

data_decade = []

for i in range(len(data)):
    if data.loc[i,"age"] < 40:
        data_decade.append(1)
    elif data.loc[i,"age"] < 50:
        data_decade.append(2)
    elif data.loc[i,"age"] < 60:
        data_decade.append(3)
    elif data.loc[i,"age"] < 70:
        data_decade.append(4)    
    elif data.loc[i,"age"] < 80:
        data_decade.append(5)   
        
data['decade']= data_decade
data.drop(['age'], axis=1)

# data.decade.head()


# # Step 4: Feature selection

# In[7]:


# One hot encode non-numeric columns
a = pd.get_dummies(data['cp'], prefix = "cp", drop_first=True)
b = pd.get_dummies(data['thal'], prefix = "thal", drop_first=True)
c = pd.get_dummies(data['slope'], prefix = "slope", drop_first=True)


# In[8]:


# Concatenate these one-hot-encoded columns with original data
frames = [data, a, b, c]
data = pd.concat(frames, axis = 1)
# data.head()


# In[9]:


# Drop original/not one-hot encoded columns
data = data.drop(columns = ['cp', 'thal', 'slope'])
# data.head()


# # Step 5: Machine learning model training

# In[10]:


# Naming our predictor variables
X = data.drop('target',axis=1)

# Naming our dependent variable
y = data['target']


# In[11]:


# Train the model with the training sample data (80% of original data)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=42)


# In[12]:


# X_train.shape


# In[13]:


# X_test.shape


# In[14]:


# y_train.shape


# # Step 6: Model evaluation 

# In[15]:


from keras.models import Sequential
from keras.layers import Dense, Dropout
model = Sequential()
model.add(Dense(64,activation='relu',input_dim=19))


# In[16]:


model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))


# In[17]:


model.add(Dense(1,activation='sigmoid'))


# In[18]:


model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])


# In[19]:


# To see the same examples more times (since we have very few data points)
model.fit(X_train,y_train,epochs=300)


# In[20]:


score = model.evaluate(X_test, y_test, batch_size=300)
'''
print("\n")
print("\nMulti-Layer Perceptron Loss Value, Accuracy Score:")
score
'''

# ##### Deep learning hyperparameter optimisation

# Talos radically changes the ordinary Keras workflow by fullyautomating hyperparameter tuning and model evaluation. Talos exposes Keras functionality entirely and there is no new syntax or templates to learn.

# In[21]:


# Help


# In[22]:

######### print to file
x = str(score)
with open('scores.txt', 'w') as f: 
    f.write(x) 