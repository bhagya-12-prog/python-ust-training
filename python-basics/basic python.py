#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Set
myset ={'sandeep','umrah','jeffry','anil','ghousiya'}
print(myset)


# In[2]:


# set not allow duplicates
myset ={'sandeep','sandeep','umrah','jeffry','anil','ghousiya'}
print(myset)


# In[5]:


#set can contains diff data types
myset ={'sandeep','sandeep',1,2,3,4}
print(myset)


# In[6]:


myset ={'sandeep','sandeep','umrah','jeffry','anil','ghousiya'}


# In[11]:


# Dictionary
mydict={
    'brand': 'Maruti',
    'model1': 'swift',
     'year':1983
}
print(mydict)


# In[12]:


mydict={
    'brand': 'Maruti',
    'model1': 'swift',
     'year':1983,
    'year':1965
}
print(mydict)


# In[13]:


mydict={
    'brand': 'Maruti',
    'model1': 'swift',
     'year':1983,
    'year':1965
}
print(mydict.keys)


# In[14]:


print(mydict.keys())


# In[16]:


print(mydict.values())


# In[17]:


#changing in dictionary
mydict={
    'brand': 'Maruti',
    'model1': 'swift',
     'year':1983,
    'year':1965
}
mydict["model1"]="celerio"
print(mydict)


# In[19]:


mydict={
    'brand': 'Maruti',
    'model1': 'swift',
     'year':1983,
    'year':1965
}
mydict.(remove("year"))
print(mydict)


# In[20]:


#camel case word = studentId,userName,wordOne,myVariablenameetc.
#camelCase word = employeeId,studentName
#Pascalcase word = EmployeeId,StudentName
#snack_case word = employee_id,student_name


# In[21]:


#Built in Data Types:
 # 1.Text: str
 # 2.Numaric: int,float,complex
 # 3.Sequence: list,tuple,range
 # 4.Mapping: dictionary
 # 5.set: set,frozenset
 # 6.Boolean: bool
 # 7.binary: bytearray,memoryview


# In[22]:


# Multa line code means use 3 double or single line coats

a="""qwertyyufjvns,sldlsksjskks"""
print(a)


# In[23]:


#slice the String
a="hello, world"
print(a[2:5])


# In[24]:


a="hello, world"
print(a[:5])


# In[26]:


a="hello, world"
print(a[5:])


# In[27]:


a="hello, world"
print(a.upper())


# In[28]:


a="hello, world"
print(a.lower())


# In[29]:


a="hello, world"
print(a.replace("h","j"))


# In[30]:


a="hello, world"
print(a.replace('o','j'))


# In[32]:


a = 'hello'
b = 'world'
c = a + b
print(c)


# In[33]:


# Operators
 # 1.Arithmatic : +,-,*,/,%,**,//
 # 2.Assignment : =,+=,-=,*=,/=,%=,//=,**=,&=,|=,>>=,<<=,^=.
 # 3.comparision : ==,!=,>=,<=,>,<.
 # 4.logical : And,OR,NOT.
 # 5.Identity :Is, isnot
 # 6.Membership :In,not in
 # 7.bitwise :&,|,^,~,<<,>>


# In[34]:


i=0
while(i<=5):
    print(i)
    i+=1


# In[36]:


for(i<=3):
    print(i)


# In[39]:


# Converting list to tuple
list = [1,2,3,4,5]
list_to_tuple = tuple(list)
print(list_to_tuple)
print(type(list_to_tuple))


# In[ ]:




