#!/usr/bin/env python
# coding: utf-8

# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[7]:


get_ipython().system('pip install pandas')
import pandas as pd


# In[15]:


list = [4,8,15,16,23,42]


# In[16]:


df = pd.Series(list)


# In[17]:


print(df)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[18]:


list = [4,8,15,16,23,42,48,96,128,132]


# In[19]:


df1 = pd.Series(list)


# In[20]:


print(df1)

Q3. Create a Pandas DataFrame that contains the following data:
Name        Age        Gender
Alice           25            Female
Bob             30            Male
Claire          27            Female

Then, print the DataFrame.
# In[25]:


data = {'Name' : ['Alice', 'Bob', 'Claire'],
        'Age' : ['25','30','27'],
        'Gender' : ['Female', 'Male', 'Female']}


# In[26]:


df = pd.DataFrame(data)


# In[27]:


print(df)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In Pandas, a DataFrame is a two-dimensional, labeled data structure that is widely used for handling and manipulating data. It is similar to a spreadsheet or SQL table, where data is organized in rows and columns. Each column in a DataFrame can be of a different data type (e.g., integers, floats, strings), and it is possible to perform various operations like filtering, grouping, and aggregation on the data.
# 
# On the other hand, a Series is a one-dimensional labeled array in Pandas. It can be thought of as a single column of a DataFrame. A DataFrame is essentially a collection of Series, where each column of the DataFrame is a Series.

# In[28]:


# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Claire'],
        'Age': [25, 30, 27],
        'Gender': ['Female', 'Male', 'Female']}

df = pd.DataFrame(data)

# Printing the DataFrame
print("DataFrame:")
print(df)
print()

# Extracting a Series from the DataFrame
name_series = df['Name']

# Printing the Series
print("Series:")
print(name_series)


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# In[29]:


data = {'Name' : ['Alice', 'Bob', 'Claire','Jash','Sanket'],
        'Age' : ['25','30','27','24','23'],
        'Gender' : ['Female', 'Male', 'Female','Male','Male']}


# In[30]:


df = pd.DataFrame(data)


# In[32]:


df.head(3)


# In[33]:


df.tail(3)


# In[34]:


df.columns


# You will use the above df.columns function to list down the name of columns 

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# All of them are mutable

# Q7. Create a DataFrame using multiple Series. Explain with an example.

# In[37]:


name_series = pd.Series(['Alice', 'Bob', 'Claire'], name='Name')
age_series = pd.Series([25, 30, 27], name='Age')
gender_series = pd.Series(['Female', 'Male', 'Female'], name='Gender')

data = {'Name': name_series, 'Age': age_series, 'Gender': gender_series}
df = pd.DataFrame(data)
print(df)


# In[ ]:




