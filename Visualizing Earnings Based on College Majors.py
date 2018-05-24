
# coding: utf-8

# ### Introduction 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
recent_grads = pd.read_csv("./databank/recent-grads.csv")
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
recent_grads.describe()


# ### Getting Familiar and Cleaning the Data Set

# In[2]:


raw_data_count = recent_grads.shape[0]
recent_grads = recent_grads.dropna()
clear_data_count = recent_grads.shape[0]
print(raw_data_count)
print(clear_data_count)


# ### Generating Scatter Plots

# In[3]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter', title='Sample Size vs. Median')


# In[4]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter', title='Sample Size vs. Unemployment Rate')


# In[5]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Full Time vs. Median')


# In[6]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter', title='ShareWomen vs. Unemployment Rate')


# In[7]:


recent_grads.plot(x='Men', y='Median', kind='scatter', title='Men vs. Median')


# In[8]:


recent_grads.plot(x='Women', y='Median', kind='scatter', title='Women vs. Median')


# ### Generating Histograms

# In[9]:


# Generate histogram to explore distributions
recent_grads["Sample_size"].plot(kind='hist', title="Sample Size Distribution")


# In[10]:


recent_grads["Median"].hist()
plt.title("Median Distribution")


# In[11]:


recent_grads["Employed"].hist()
plt.title("Number of Students Employed")


# In[12]:


recent_grads["Full_time"].hist()
plt.title("Full Time Employed Distribution")


# In[13]:


recent_grads["ShareWomen"].hist()
plt.title("Proportion of Women Share")


# In[14]:


recent_grads["Unemployment_rate"].hist()
plt.title("Unemployment Rate Distribution")


# In[15]:


recent_grads["Men"].hist()
plt.title("Male Gender Distribution")


# In[16]:


recent_grads["Women"].hist()
plt.title("Female Gender Distribution")


# #### Prepare Scatter Matrix Plot for Data Statistics & Unemployment Rate

# In[17]:


# Working with Pandas' Scatter Matrix Plot
from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(10,10))


# In[18]:


scatter_matrix(recent_grads[['Sample_size','Median','Unemployment_rate']], figsize=(12,12))


# ### Plot Women Proportions in Different Majors

# In[19]:


# Percent of Women from "ShareWomen" corresponds to top & bottom 10% paying majors
recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
plt.title("Proportion of Women in Top 10% Paying Majors")
plt.show()

recent_grads[163:].plot.bar(x='Major', y='ShareWomen')
plt.title("Proportion of Women in Bottom 10% Paying Majors")
plt.show()


# ### Plot Unemployment Rate in Different Majors

# In[20]:


# Percent of Unemployment Rate corresponds to top & bottom 10% paying majors
recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate')
plt.title("% of Unemployment Rate in Top 10% Paying Majors")
plt.show()

recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate')
plt.title("% of Unemployment Rate in Bottom 10% Paying Majors")
plt.show()


# ## Find Out Gender Participation for Major Categories

# In[21]:


from pandas import *

cols = ["Major_category", "Men", "Women"]
gender_major = recent_grads[cols]
gender_major_cat = gender_major.groupby("Major_category", as_index=True).sum()
print(gender_major_cat)


# ## Plot Number of Men & Women in Each Major Category

# In[22]:


gender_table = pivot_table(gender_major, values=['Men', 'Women'], index='Major_category', aggfunc='sum')
gender_table.plot(kind='bar')
plt.title("Men & Women in Each Major Category")
plt.show()
print()


# ### Plot Showing Distribution of Median Salaries & Unemployment Rate

# In[23]:


# GEt a Box Plot for Median Salaries
fig, ax = plt.subplots()
ax.boxplot(recent_grads['Median'].values)
ax.set_xlabel("Median Salaries")
ax.set_ylabel("Interquartile Range")
ax.set_title("Median Salaries Quartiles")
ax.set_ylim(20000, 65000)
plt.show()
# Get a Box Plot for Unemployment Rate
fig, ax = plt.subplots()
ax.boxplot(recent_grads['Unemployment_rate'].values)
ax.set_xlabel("Unemployment Rate")
ax.set_ylabel("Interquartile Range")
ax.set_title("Unemployment Rate Quartile")
ax.set_ylim(0, 0.14)
plt.show()


# ### Generate Hexagonal Bin Plot to Visualize Data Density

# In[24]:


# Segregating dataframe columns that carry numeric values
numerical_recent_grads = recent_grads.select_dtypes(include=['int64', 'float64'])
print(numerical_recent_grads.dtypes)
print(numerical_recent_grads.columns)


# In[25]:


cols = ['Major_code', 'Men', 'Women', 'ShareWomen', 'Employed', 'Full_time', 'Part_time', 'Unemployed', 
        'Unemployment_rate', 'Median', 'College_jobs', 'Non_college_jobs', 'Low_wage_jobs']

if (len(cols)%3 != 0):
    row_num = len(cols)//3 + 1
else:
    row_num = len(cols)//3
    
fig, ax = plt.subplots(row_num, 3, figsize=(10,16))

j=0
for i in range(1, len(cols)*3, 3):
    sbp = int((i-1)/3)
    ax = fig.add_subplot(row_num, 3, sbp+1)
    X = (numerical_recent_grads[str(cols[j])].values)
    ax.hist(X)
    
    ax.set_title(cols[j])
    for keys, spine in ax.spines.items():
        spine.set_visible(False)
    ax.tick_params(axis='both', left='off', top='off', right='off',                    bottom='off', labelleft='off', labeltop='off',                    labelright='off', labelbottom='off')
    j += 1

plt.title("Hexagonal Bin Plot")
plt.show()

