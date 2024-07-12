#!/usr/bin/env python3
import time
import requests
from bs4 import BeautifulSoup as bs
import webbrowser

def extract_links(html):
    soup = bs(html, 'html.parser')
    body = soup.find(id='mainBody')
    rows = body.find_all('table', {'class', 'table-hover'})[0]\
               .find_all('tbody')[0]\
               .find_all('tr')

    links = [f"{r.find_all('a')[0].get('href')}" for r in rows]

    return links

if __name__ == '__main__':

    seen_tix = set()

    while True:

        page = requests.get('')
        
        links = extract_links(page.content)

        for link in links:
            if link not in seen_tix:
                webbrowser.open(link, new=2)
                s = f'!! NEW:   {link}   !!'
                print('!' * len(s))
                print('!!' + ' ' * (len(s) - 4) + '!!')
                print(s)
                print('!!' + ' ' * (len(s) - 4) + '!!')
                print('!' * len(s))

        seen_tix.update(links)

        time.sleep(1)
