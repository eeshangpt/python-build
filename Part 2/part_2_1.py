
# coding: utf-8

# In[1]:


import pandas as pd
import MySQLdb
import pickle


# In[2]:


my_db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'yesican', db = 'pythonBuild')
cursor = my_db.cursor()


# In[3]:


read_query = 'SELECT * FROM nifty_it_index;'


# In[4]:


nifty_it_index = pd.read_sql(read_query, my_db, index_col=['Date'], parse_dates=True)


# In[5]:


nifty_it_index.info()


# In[6]:


nifty_it_index.head()


# In[7]:


read_query = 'SELECT * FROM infy_stock;'


# In[8]:


infy_stock = pd.read_sql(read_query, my_db, index_col=['Date'], parse_dates=True)


# In[9]:


infy_stock.info()


# In[10]:


infy_stock.head()


# In[11]:


with open('nifty_it_index', 'wb') as f:
    pickle.dump(nifty_it_index, f)


# In[12]:


with open('infy_stock', 'wb') as f:
    pickle.dump(infy_stock, f)

