#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES
(MOVIE_ID INT PRIMARY KEY NOT NULL,
MOVIE_NAME TEXT NOT NULL,
ACTOR_NAME TEXT NOT NULL,
ACTRESS_NAME TEXT NOT NULL,
DIRECTOR_NAME TEXT NOT NULL,
YEAR INT NOT NULL);''')
print ("Table created successfully")


# In[3]:


conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("INSERT INTO MOVIES (MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR) VALUES (1, 'Inception', 'Leonardo Dicaprio', 'Marion cotillard', 'Christopher Nolan', 2010 )");

conn.execute("INSERT INTO  MOVIES (MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR) VALUES (2, 'Pulp fiction', 'Samuel L Jackson', 'Uma Thurman','Quentin Tarantino', 1994 )");

conn.execute("INSERT INTO  MOVIES (MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR) VALUES (3, 'The Godfather', 'Al pacino', 'Diane Keaton','Francis Ford Coppola', 1972 )");

conn.execute("INSERT INTO  MOVIES (MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR) VALUES (4, 'La La land', 'Ryan gosling', 'Emma Stone ','Damien Chazelle', 2016 )");

conn.execute("INSERT INTO  MOVIES (MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR) VALUES (5, 'Midnight in paris', 'Owen Wilson', 'Rachel McAdams','Woody Allen', 2011 )");

print ("Records created successfully")


# In[4]:


print ("Opened database successfully")
cursor = conn.execute("SELECT MOVIE_ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,DIRECTOR_NAME,YEAR from MOVIES")
for row in cursor:
    print("MOVIE_ID = ", row[0])
    print("MOVIE_NAME= ", row[1])
    print("ACTOR_NAME = ", row[2])
    print("ACTRESS_NAME = ", row[3])
    print("DIRECTOR_NAME = ", row[4]) 
    print("YEAR = ", row[5], "\n")
print("operation done successfully")


# In[5]:


print ("Opened database successfully")
cursor = conn.execute("SELECT ACTOR_NAME,MOVIE_NAME from MOVIES")
for row in cursor:
    print("Mr.",row[0], "is the lead actor in the movie" ,row[1])
    print("         ")
print("operation completed")


# In[ ]:




