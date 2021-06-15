#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the libraries
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from random import randint
from time import sleep


# In[3]:


headers = {"Accept-Language": "en-US,en;q=0.5"}


# In[4]:


#creating empty lists so that the data can be appended 
name = []
year = []
duration = []
movie_type = []
About = []
rating = []
votes = []
gross = []


# In[5]:


pages = np.arange(100,600,100)


# In[6]:


#Iterating over multiple pages
for p in pages:
    p = requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(p)+"&ref_=adv_nxt")
    soup = BeautifulSoup(p.text, 'html.parser')
    movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
    sleep(randint(2,8))
    for movie in movie_data:  #Iterating over each movie_data to fetch the data  
        
        movie_name = movie.h3.a.getText()
        name.append(movie_name)
        
        release = movie.h3.find('span', class_ = "lister-item-year text-muted unbold").getText()
        year.append(release)
        
        time = movie.p.find("span", class_ = 'runtime').getText()
        duration.append(time)
        
        mov_type = movie.p.find("span", class_ = "genre").getText().replace('\n', '')
        movie_type.append(mov_type)
        
        descrip = movie.find_all('p', class_ = 'text-muted')
        tag = descrip[1].text.replace('\n', '') if len(descrip) >1 else 'None'
        About.append(tag)
          
        rate = movie.find('div', class_ = "inline-block ratings-imdb-rating").getText().replace('\n', '')
        rating.append(rate)
      
        alpha = movie.find_all('span', attrs = {'name': "nv"})
        vote = alpha[0].getText()
        votes.append(vote)
        
        earning = alpha[1].getText() if len(alpha)>1 else 'None'
        gross.append(earning)
        


# In[7]:


#Creating a dataframe 
IMDB_list = pd.DataFrame({"Movie Name": name,
                          "Year" : year,
                          "Duration": duration,
                          "Movie Type": movie_type,
                          "About" : About,
                          "Rating": rating,
                          "Votes" : votes,
                          "Gross collections": gross})

IMDB_list.index += 1

#Styling the dataframe
IMDB_list.style.set_properties(**{'background-color': 'LightGrey',
                                  'color': 'black',
                                  'border-color': 'black',
                                  'border-width': '2px',
                                  'border-style': 'solid'})


# In[8]:


#Copying the data to excel file
IMDB_list.to_excel("List of top IMDb movies.xlsx")


# In[ ]:




