#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[2]:


import mysql.connector


# In[24]:


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test"
)
print(mydb)


# In[5]:


mycursor = mydb.cursor()
mycursor.execute("create database ustpythontarining")


# In[6]:


db = mycursor.execute("show databases")
for x in mycursor:
    print(x)


# In[7]:


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("create database stude")
db = mycursor.execute("show databases")
for x in mycursor:
    print(x)


# In[10]:


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test",
    database = "mysql"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("create database w")
mycursor.execute("create table tutorial_in(tutorial_id INT NOT NULL AUTO_INCREMENT, tutorial_title VARCHAR(100) NOT NULL, tutorial_author VARCHAR(40) NOT NULL, submission_date DATE, PRIMARY KEY ( tutorial_id ));")
mycursor.execute("show databases")
for x in mycursor:
    print(x)


# In[27]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="w"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer_in(name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")


for x in mycursor:
    print(x)


# In[28]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="w"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer_in(name, address) VALUES (%s, %s)"
val =("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[29]:


mycursor.execute("select * from customer_in")


# In[30]:


result = mycursor.fetchall()
for x in result:
    print(x)


# In[32]:



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="w"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer_in(name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# In[19]:


mycursor.execute("select * from customers")
result = mycursor.fetchall()
for x in result:
    print(x)


# In[26]:


#mycursor = mydb.cursor()
#mycursor.execute("create database name")

db = mycursor.execute("show databases")
for x in mycursor:
    print(x)


# In[ ]:




