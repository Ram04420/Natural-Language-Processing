#!/usr/bin/env python
# coding: utf-8

# ## Extract Text from Pdf's files in Python for NLP

# In[2]:


#!pip install PyPDF2


# In[3]:


import PyPDF2 as pdf


# In[4]:


file = open('statistics.pdf', 'rb')


# In[5]:


file


# In[6]:


pdf_reader = pdf.PdfFileReader(file)


# In[7]:


pdf_reader


# In[9]:


help(pdf_reader)


# In[10]:


pdf_reader.getIsEncrypted()


# In[11]:


pdf_reader.getNumPages()


# In[12]:


page1 = pdf_reader.getPage(0)


# In[14]:


page1.extractText()


# In[15]:


page2 = pdf_reader.getPage(1)


# In[16]:


page2.extractText()


# ## Append Write and Merge PDF's

# In[17]:


pdf_writer = pdf.PdfFileWriter()


# In[22]:


pdf_writer.addPage(page2)
pdf_writer.addPage(page1)


# In[24]:


output = open('pages.pdf', 'wb')
pdf_writer.write(output)
output.close()


# In[ ]:




