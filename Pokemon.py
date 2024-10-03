#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
pok=pd.read_txt('pokemon_data.txt',delimiter='\t')
print(poke.head())


# In[4]:


poke=pd.read_csv('pokemon_data.csv')
poke.head()


# In[9]:


print(poke.columns)


# In[11]:


print(poke['Name'][0:5])


# In[13]:


poke.iloc[1:4]


# In[14]:


poke.loc[poke['Type 1']=='Water']


# In[15]:


poke.describe()


# In[16]:


poke.sort_values('Name')


# In[20]:


poke.sort_values(['Type 1','HP'], ascending=[0,0])


# In[27]:


x=poke.sort_values(['Attack','Defense','Speed','HP'],ascending=False)
print(x.head(10))


# In[29]:


poke.loc[poke['Name']=='Arceus']


# In[33]:


poke['Total'] = poke['HP']+ poke['Attack']+ poke['Defense']+ poke['Sp. Atk']+ poke['Sp. Def']+ poke['Speed']+poke['Generation']


# In[34]:


poke.head()


# In[37]:


poke=poke.drop(columns=['Total'])
poke.head()


# In[55]:


# poke.to_csv('Modified.csv',index=False)


# In[48]:


# Filtering data


# In[ ]:




