#!/usr/bin/env python
# coding: utf-8

# In[2]:


#csv file handling
import csv


# Reading File

# In[7]:


with open('a.csv')as x:
    f_read = x.read()
    print(f_read)


# In[11]:


w = open('a.csv')
read = csv.reader(w)
for i in read:
    print(i)


# In[12]:


# slicing
w = open('a.csv')
read = csv.reader(w)
slic = list(read)
print(slic)


# In[13]:


w = open('a.csv')
read = csv.reader(w)
slic = list(read)
print(slic[1:4])


# In[14]:


w = open('a.csv')
read = csv.reader(w)
slice = list(read)
for i in slice[:4]:
    print(i)
    


# In[15]:


#length
w = open('a.csv')
read = csv.reader(w)
slice = list(read)
print(len(slice))


# In[25]:


#append
w = open('a.csv')
read = csv.reader(w)
slice = list(read)
emp_list = ['bhagya','Netra']
for i in slice[1:]:
    emp_list.append(i[3])
print(emp_list)


# In[27]:


#full name with append
w = open('a.csv')
read = csv.reader(w)
slicing = list(read)
full_name = []
for i in slicing[1:6]:
    full_name.append(i[0]+' '+i[1])
print(full_name)


# Writing File
# 

# In[36]:


with open('b_w.csv','w')as r:
    x=csv.writer(r)
    x.writerow(['python','java','m','csv'])
    x.writerows([['python','java','m','csv'],['bhagya','Netra','ganga'],['biriyani','banana','orange']])
    x.writerow(['pot','god','bad'])


# In[5]:


import PyPDF2
#from pyPDF2 import PdfFileReader
with open('WBP.pdf','rb')as pdf_handle:
    pdf_read = PyPDF2.PdfFileReader(pdf_handle)


# In[10]:


with open('WBP.pdf','rb')as pdf_handle:
    pdf_read = PyPDF2.PdfFileReader(pdf_handle)
    page = pdf_read.numPages
    print(page)


# In[17]:


import PyPDF2
#from PyPDF2 import PdfFileReader
with open('WBp.pdf','rb')as pdf_handle:
    pdf_read = PyPDF2.PdfFileReader(pdf_handle)
    page_one = pdf_read.getPage(2)
    page_text = page_one.extractText()
    print(page_text)


# In[3]:


#     copy pages and append pages to new pdf
with open('WBP.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    page_one=pdf_reader.getPage(0)
    pdf_writer=PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output= open('new.pdf','wb')
    pdf_writer.write(pdf_output)
    pdf_output.close


# In[2]:


# read all the text from pdf file
import PyPDF2
with open('WBP.pdf','rb')as pdf_handle:
    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)
    f = open('WBP.pdf','rb')
    text = []
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)    
        text.append(page.extractText())
    # print(text)#prin all text
    print(text[2])#perticular page


# In[ ]:




