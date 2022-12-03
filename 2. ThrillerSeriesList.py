from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pandas as pd
import numpy as np


def name(x):
    i = x.find('.')
    j = x.find('(')
    
    nam = x[i+2:j-1]
    year = x[j+1:-1]
    
    return nam, year
    
    
def certificate_genre(x):
    i = x.split('|')
    # print(i)
    if len(i) != 3:
        return i[0], '.', i[1]
    else:
        return i[0],i[1],i[2]
    

def rating(x):
    i = x.split()
    return i[0]

def actor(x):
    i = x.split(':')
    
    return i[-1]

def votes(x):
    i = x.split(':')
    
    return i[-1]
  
  
namee =[]
year =[]
certificate =[]
duration = []
genre = []
rate = []
performer =[]
vote =[]




path = r"C:\Users\User\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver  = webdriver.Chrome(path)

driver.get('https://www.imdb.com/search/title/?title_type=tv_series&genres=thriller')

classes = driver.find_elements(By.CLASS_NAME,'lister-item')
print(len(classes))
for i in classes:
    content = i.find_element(By.CLASS_NAME, 'lister-item-content')
    # print(f"len  {len(content.text.split('\n'))}")
    namee.append(name(content.text.split('\n')[0])[0])
    year.append(name(content.text.split('\n')[0])[1])
    
    certificate.append(certificate_genre(content.text.split('\n')[1])[0])
    duration.append(certificate_genre(content.text.split('\n')[1])[1])
    genre.append(certificate_genre(content.text.split('\n')[1])[2])
    
    rate.append(rating(content.text.split('\n')[2]))
    
    performer.append(actor(content.text.split('\n')[4]))
    
    vote.append(votes(content.text.split('\n')[5]))
    
    
    # print(content.text.split('\n')[2])
    

datas = []

for i in range(len(namee)):
    datas.append([namee[i],year[i],certificate[i],duration[i],genre[i],rate[i],performer[i],vote[i]])

cols = ['Name','Year','Tv Certificate','Duration per episode','Genre','Ratings','Actor/Actress','Votes']



data = pd.DataFrame(data=datas, columns=cols)

# print(data.head(2))
print(data.head(2))

# print(x for x in datas)

data.to_csv('thrillerMovie.csv')
time.sleep(25)
driver.quit() 