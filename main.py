from bs4 import BeautifulSoup
import requests


url = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(url, 'lxml')

# print(requests.get("https://news.ycombinator.com/news").status_code)
mainContent = soup.find('body')
content = mainContent.find('td', class_ = 'subtext')
# print(mainContent.prettify())
heading = mainContent.find('b', class_ = 'hnname')
print(heading.text)




for news in mainContent.find_all('tr', class_ = 'athing submission'):

    myNews = news.find('span', class_ = 'titleline').text
    print(myNews)

    points = news.find('span', class_ = 'score')
    print(points)

for time in content.find_all('span', class_ = 'age'):
    
    times 


    






# print(mainContent)

# for news in mainContent.find_all('td', class_ = 'title'):
    
#     print(news.text)

# for points in mainContent.find_all('span', class_ = 'score'):
#     print(points.text)

#     print(' ')



