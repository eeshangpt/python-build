
# coding: utf-8

# In[1]:


import csv
import MySQLdb


# In[2]:


mydb = MySQLdb.connect(host = 'localhost', user = 'root', 
                       passwd = 'yesican', db = 'pythonBuild')

cursor = mydb.cursor()


# In[3]:


with open('../datasets/nifty_it_index.csv') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        if not csv_data.line_num == 1:
            cursor.execute("""INSERT INTO nifty_it_index            (Date, Open, High, Low, Close, Volume, Turnover) values            (%s, %s, %s, %s, %s, %s, %s)""", row)


# In[4]:


with open('../datasets/infy_stock.csv') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        if not csv_data.line_num == 1:
            cursor.execute("""INSERT INTO infy_stock values            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",row)


# In[5]:


mydb.commit()

