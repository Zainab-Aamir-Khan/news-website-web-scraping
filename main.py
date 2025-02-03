from bs4 import BeautifulSoup
import requests


url = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(url, 'lxml')

# print(requests.get("https://news.ycombinator.com/news").status_code)
mainContent = soup.find('body')
print(mainContent)
# print(mainContent)

# for news in mainContent.find_all('td', class_ = 'title'):
    
#     print(news.text)

# for points in mainContent.find_all('span', class_ = 'score'):
#     print(points.text)

#     print(' ')



