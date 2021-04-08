import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from csv import writer
import urllib
import urllib.request
import html.parser
import requests
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar



'''def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        write_obj.close()'''
url = 'https://doaj.org/search?ref=homepage-box&source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22data%20mining%22%2C%22default_operator%22%3A%22AND%22%7D%7D%7D'

try:
    req=Request(url, None, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; G518Rco3Yp0uLV40Lcc9hAzC1BOROTJADjicLjOmlr4=) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'gzip, deflate, sdch','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
    response = urlopen(req)
    raw_response = response.read().decode('utf8', errors='ignore')
    soup = BeautifulSoup(raw_response,'html.parser')
    result = soup.find('ol',{'id':'results'})
    print(result)
except urllib.request.HTTPError as inst:
    pass

'''
req = Request('https://doaj.org/search?ref=homepage-box&source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22data%20mining%22%2C%22default_operator%22%3A%22AND%22%7D%7D%7D', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')

title=[] #List to store title of the article
author_complete=[] #List to store all the author names
year=[] #List to store published year
link = [] # List to store link of the title

result = soup.find('ol',{'id' : 'results'})
if result is not None:
    jobs = result.find_all('li',class_='search-results__record')
    for job in jobs:
        t = job.find('h3',class_='search-results__heading')
        li = job.find('a')
        if None in (t,link):
            continue
        title.append(t.text.strip())
        link.append(li.get('href'))
        writter = job.find('em')
        author_complete.append(writter.text.strip())
        date = job.find('side',class_='col-sm-4 search-results__aside')
        year.append(date[0])
print(title[:2])'''