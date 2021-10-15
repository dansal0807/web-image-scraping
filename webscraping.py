
import requests 
from bs4 import BeautifulSoup 

class WebScraping(): 
    def soup(html):
        imgs_links = []
        r = requests.get(html) 
        htmldata = r.text
        soup = BeautifulSoup(htmldata, 'html.parser')
        for item in soup.find_all('img'):
            imgs_links.append(item['src'])
        return imgs_links


    