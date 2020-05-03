#!/usr/bin/env python
# coding: utf-8

# # Working with Text Files

# * working with F-strings for formatted print
# * working with csv & tsv files for read and write
# * working with %%writefile to create simple .txt files **[Works in jupiter note books only]**
# * working with python inbuilt file for read and write`

# ## String Format

# In[1]:


name = 'KGP Talkie'


# In[3]:


print('The youtube channel is  {}'.format(name))


# In[4]:


print(f'The Youtube channel is {name}')


# In[7]:


#minimun width, alighment between columns
#day value
#1 10
#10 1


# In[8]:


data_science_tuts = [('Pyhton for Beginners',19), 
                    ('feature selections', 11),
                    ('Machine learning tutorials', 11),
                    ('Deep learning', 19)]


# In[9]:


data_science_tuts


# In[10]:


for info in data_science_tuts:
    print(info)


# In[18]:


for info in data_science_tuts:
    print(f'{info[0]:{50}} {info[1]:{10}}')


# In[23]:


#>, <, ^ for alighment

for info in data_science_tuts:
    print(f'{info[0]:<{50}} {info[1]:.>{10}}')


# ### Working with CSV & TSV file

# In[25]:


import pandas as pd


# In[26]:


data = pd.read_csv('moviereviews.tsv.txt', sep ='\t')


# In[27]:


data.head()


# In[28]:


data.shape


# In[30]:


data['label'].value_counts()


# In[34]:


pos = data[data['label'] =='pos']


# In[35]:


pos.head()


# In[40]:


pos.to_csv('pos.tsv', sep ='\t', index = False)


# In[41]:


pos.head()


# In[42]:


pd.read_csv('pos.tsv', sep = '\t')


# ### built in Magic command with %%write file in jupiter

# In[43]:


get_ipython().run_cell_magic('writefile', 'text1.txt', "hi this is Ramanjaneyulu\ni'm learning NLP")


# In[45]:


get_ipython().run_cell_magic('writefile', '-a text1.txt', 'so i need spend more time in this chapater')


# ### Using Python's in built command to read and write text file

# In[46]:


file = open('text1.txt', 'r')


# In[48]:


file.read()


# In[49]:


file.read()


# In[50]:


file.seek(0)


# In[51]:


file.read()


# In[57]:


file.seek(0)


# In[58]:


file.readline()


# In[59]:


file.readlines()


# In[60]:


file.close()


# In[61]:


file.read()


# In[69]:


with open('text1.txt') as file:
    text_data= file.read()
    print(text)


# In[72]:


for temp in text_data:
    print(temp.strip())


# In[74]:


for i, temp in enumerate(text_data):
    print(str(i)+'......>'+ temp)


# ### File writing

# In[78]:


file = open('tet2.txt', 'w')


# In[79]:


file


# In[80]:


file.write("this is another lesson")


# In[81]:


file.close()


# In[87]:


with open('text3.txt', 'w') as file:
    file.write("This is third file \n")


# In[88]:


text_data


# In[89]:


with open('text3.txt', 'a') as file:
    for temp in text_data:
        file.write(temp)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




