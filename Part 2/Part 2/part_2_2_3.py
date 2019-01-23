
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
import bokeh.plotting as bkhplt

bkhplt.output_notebook()


# In[2]:


with open('nifty_it_index', 'rb') as f:
    nifty_it_index = pickle.load(f)


# In[3]:


nifty_it_index = nifty_it_index.drop(['week_no', 'week_4'], axis= 1)


# In[4]:


nifty_it_index.info()


# In[5]:


with open('infy_stock', 'rb') as f:
    infy_stock = pickle.load(f)


# In[6]:


infy_stock.info()


# In[7]:


def moving_average(closing_points, size):
    if size <= len(closing_points):
        return pd.Series(np.convolve(closing_points, (np.repeat(1.0, size) / size), 'valid'), 
                         index= nifty_it_index.index[(size - 1):])
    else:
        return sum(closing_points) / len(closing_points)


# In[8]:


def plot_moving_average_index(no_of_days = 3, plot_title = '3/7 week moving average'):
    plot = bkhplt.figure(title = plot_title,  x_axis_type="datetime",
                         x_axis_label='Dates', y_axis_label='Closing Price')
    plot.line(x = nifty_it_index.index, y = nifty_it_index.Close, line_color = 'blue', legend =  'Closing price')
    if no_of_days <= len(nifty_it_index.Close):
        plot.line(x = nifty_it_index.index[no_of_days - 1:], y = moving_average(nifty_it_index.Close, no_of_days),
                  line_color = 'green', legend = 'Moving Average', line_width = 2)
    else:
        plot.scatter(x = nifty_it_index.index[-1], y = moving_average(nifty_it_index.Close, no_of_days),
                  line_color = 'green', legend = 'Moving Average')
    bkhplt.show(plot);


# In[9]:


no_of_weeks = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52]


# In[10]:


for _ in no_of_weeks:
    plot_moving_average_index((_ * 5), "{} week moving average".format(_))


# In[11]:


def moving_average_stock(closing_points, size):
    if size <= len(closing_points):
        return pd.Series(np.convolve(closing_points, (np.repeat(1.0, size) / size), 'valid'), 
                         index= infy_stock.index[(size - 1):])
    else:
        return sum(closing_points) / len(closing_points)


# In[12]:


def plot_moving_average_stock(no_of_days = 3, plot_title = '3/7 week moving average'):
    plot = bkhplt.figure(title = plot_title,  x_axis_type="datetime",
                         x_axis_label='Dates', y_axis_label='Closing Price')
    plot.line(x = infy_stock.index, y = infy_stock.Close, line_color = 'blue', legend =  'Closing price')
    if no_of_days <= len(infy_stock.Close):
        plot.line(x = infy_stock.index[no_of_days - 1:], y = moving_average_stock(infy_stock.Close, no_of_days),
                  line_color = 'green', legend = 'Moving Average', line_width = 2)
    else:
        plot.scatter(x = infy_stock.index[-1], y = moving_average_stock(infy_stock.Close, no_of_days),
                  line_color = 'green', legend = 'Moving Average')
    bkhplt.show(plot);


# In[13]:


for _ in no_of_weeks:
    plot_moving_average_stock((_ * 5), "{} week moving average".format(_))


# In[14]:


plot_moving_average_index(10, '10 day Moving Average')


# In[15]:


plot_moving_average_stock(10, '10 day Moving Average')

