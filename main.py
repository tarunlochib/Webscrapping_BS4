#If you want to Scrape a website:
# 1. Use The API
# 2. HTML Scrapping using some tool like Beautiful soup


#step0

#Install all the Requirements 
#pip install bs4    
#pip install html5lib
#pip install requests 

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#step1: Get the HTMl

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step2: parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#step3: HTML Tree traversal
#
#commonly used types of objects :
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment 

#Get the title of the Html Page
title = soup.title 


#Get all the Paragraphs from the page 
paras = soup.findAll('p')
#print(paras)

#Get first element in the HTML page 
#print(soup.find('p'))

#Get class of any element in the HTML page 
#print(soup.find('p')['class'])

#Find all the elements with class lead 
#print(soup.find_all("p", class_="mt-2"))

#Get the text from the tags/soup
#print(soup.find('p').get_text())

#Get all the links on the page:
#anchors =soup.find_all('a') 
#all_links = set()
#for link in anchors:
#    if(link.get('href') != '#'):
#        linkText = "https://codewithharry.com" +link.get('href')
#        all_links.add(link)
#        print(linkText)


#navbarSupportedContent  =   soup.find(id='navbarSupportedContent')
#for elem in navbarSupportedContent.children:
#    print(elem)

# .contents - A tag's children are available as a list
# .children - A tag's children are avaiable as a generator

#print(navbarSupportedContent.parent)
#for item in navbarSupportedContent.parents:
#    print(item)


Span = soup.find(id='span')
print(Span)    