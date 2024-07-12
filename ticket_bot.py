#!/usr/bin/env python3
import time
import requests
from bs4 import BeautifulSoup as bs
import webbrowser

LINK = 'https://secure.onreg.com/onreg2/bibexchange/?eventid=6277'

def extract_links(html):
    soup = bs(html, 'html.parser')

    tbody = soup.find_all('tbody')
    links = []
    if len(tbody) > 0:
        buttons = tbody[0].find_all('a', {'class': 'button_cphhalf'})
        for button in buttons:
            if 'disabled' not in button['class']:
                print('Found non-disabled button!')
                webbrowser.open(f'{LINK}/{button.get("href")}', new=2)
                webbrowser.open(LINK, new=2)
                links.append(button.get('href'))

    return links

if __name__ == '__main__':

    seen_tix = set()

    while True:

        page = requests.get(LINK)
        
        links = extract_links(page.content)

        for link in links:
            if link not in seen_tix:
                webbrowser.open(f'https://secure.onreg.com/onreg2/bibexchange/{link}', new=2)
                webbrowser.open(link, new=2)
                seen_tix.add(link)
                s = f'!! NEW:   {link}   !!'
                print('!' * len(s))
                print('!!' + ' ' * (len(s) - 4) + '!!')
                print(s)
                print('!!' + ' ' * (len(s) - 4) + '!!')
                print('!' * len(s))

        seen_tix.update(links)

        time.sleep(1)
