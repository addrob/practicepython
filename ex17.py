import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
ny_times = requests.get('https://www.nytimes.com/', headers = headers)
soup = BeautifulSoup(ny_times.content, 'html.parser')
headlines = soup.find_all('h3')
title_line = []

for title in headlines:
    if title.has_attr('class') and title.get('class')[0] == 'css-1qoy44n':
        title_line.append(title.string)
print (title_line)

