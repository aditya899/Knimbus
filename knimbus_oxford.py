import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from csv import writer



def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        write_obj.close()

req = Request('https://academic.oup.com/journals/search-results?page=1&q=data+mining&SearchSourceType=1&allJournals=1', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
 
#print(page.status_code)
title=[] #List to store title of the article
author_complete=[] #List to store all the author names
year=[] #List to store published year
link = [] # List to store link of the title
result = soup.find('div',{'id' : 'main'})
if result is not None:
    jobs = result.find_all('div',class_='sr-list al-article-box al-normal clearfix')
    for job in jobs:
        t = job.find('h4',class_='sri-title customLink al-title')
        li = job.find('a',{'class':'article-link'})
        if None in (t,link):
            continue
        title.append(t.text.strip())
        link.append(li.get('href'))
        writter = job.find('div',class_='sri-authors al-authors-list')
        author_complete.append(writter.text.strip())
        date = job.find('div',class_='sri-date al-pub-date')
        year.append(date.text.strip())

for i in range(len(title)):
    yr = year[i].split(':')
    lst = [title[i],link[i],yr[1],author_complete[i]]
    append_list_as_row('knimbus_oxford.csv',lst)
