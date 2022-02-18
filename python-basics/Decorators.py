#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Functions

def func():
    return 1


# In[5]:


func()


# In[6]:


#Scope of the function

s='Global variable'

def check_for_locals():
    print(locals())


# In[7]:


print(globals())


# In[8]:


print(globals().keys())


# In[9]:


globals()['s']


# In[10]:



def hello(name='Jose'):
    return 'Hello '+name


# In[11]:


hello()


# In[12]:


#Assigning a new label to hello() function

greet = hello


# In[13]:


greet


# In[14]:


greet()


# In[15]:


del hello


# In[16]:


hello()


# In[18]:


greet()


# In[22]:


#Functions within a Function

def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
   # def welcome():
    #    return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")
 
def welcome():
     return "\t This is inside the welcome() function"


# In[23]:


def welcome():
     return "\t This is inside the welcome() function"


# In[24]:


welcome()


# In[20]:


hello()


# In[ ]:





# In[21]:


welcome()


# In[25]:


#Returning Function

def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome


# In[26]:


x = hello()


# In[27]:


x


# In[28]:


print(x())  #x() is pointing to the greet function inside of the hello() function


# In[31]:


x = hello(name='sam')
x


# In[32]:


print(x())


# In[34]:


# now let us see how we can pass Function as argument to other function

def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())


# In[35]:


other(hello)


# In[36]:


#Creating a Decorator

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


# In[37]:


func_needs_decorator()


# In[39]:


# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)


# In[40]:


func_needs_decorator()  #A decorator simply wrapped the function and modified its behavior.


# In[41]:


#Rewritting the function using @symbol, which is what python uses for decorator
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


# In[42]:


func_needs_decorator()


# In[ ]:




