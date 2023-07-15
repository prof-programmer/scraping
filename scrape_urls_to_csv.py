# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:11:03 2019

@author: mrauhut
"""
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

#Create csv
outfile = open("scrape.csv","w",newline='')
writer = csv.writer(outfile)

#define URLs
urls = ['example.com', 
        'example.com/blog']

#define dataframe
df = pd.DataFrame(columns=['pagename','alt'])

#Loop URLs and retrieve HTML data
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #print titles and store variable
    h1 = soup.find('h1')
    print(h1.get_text())
    page_title = h1.get_text()
    
    #print alt tags and append data to dataframe
    images = soup.find_all(class_ = 'content-header')
    for image in images:
        print(image['alt'])
        alt_attr = image['alt']
        df2 = pd.DataFrame([[page_title,alt_attr]],columns=['pagename','alt'])
        df = df.append(df2,ignore_index=True)
        
#save to CSV
df.to_csv('scrape.csv')
outfile.close()