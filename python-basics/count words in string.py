#!/usr/bin/env python
# coding: utf-8

# In[9]:


my_string = input('Enter the string : ')
word_list = my_string. split() 
number_of_words = len(word_list)
print('\nThe number of words in given string is :',number_of_words)


# In[2]:


with open('word.txt','r') as f:
    lines = f.read()
    word_list = lines.split()
    num_of_words = len(word_list)
    print('\nThe number of words in a file is: ',num_of_words)
f.close()


# In[ ]:




