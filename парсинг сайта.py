import sqlite3
from bs4 import BeautifulSoup
import requests

url = 'https://www.defenseadvancement.com/news/section/technology/'
page = requests.get(url)
# если сайт на русском:
# page.encoding = 'utf8'
print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")
news = soup.findAll(class_='product-card full-bkg category')
# text_link = soup.findAll('div', class_='product-body')
# print(text_link)

# news-card-content
# news-card-date
print("----------------------news-------------------------")

name_news = []
link_news = []
date_news = []
text_news = []
for i in range(len(news)):
    # print('Новость: ')
    # print(news[i])
    # print('')
    if news[i].find(class_='news-card-heading') is not None:
        new = news[i].text.split('\n')
        if i == 0:
            new.pop(0)
            new.pop(7)

        link = news[i].find('a').get('href')
        newurl = link
        newpage = requests.get(newurl)
        newpage.encoding = 'utf8'
        news_inlink = soup.findAll('div', class_='container')
        print(news_inlink)
        print('-----------------------------------------------------------')

        # name = new[5]
        # with open(name, 'w') as file: # можно указать и папку 'html/microwavejournal_news_index.html'
        #     file.write(scr)

        name_news.append(new[5])
        date_news.append(new[9])
        link_news.append(link)
        text_news.append('')


    # if news[i].find('div', class_='product-body') is not None:
    #     link_news.append(news[i].text)

print("----------------------news-------------------------")
for i in range(len(link_news)):
    print("Новость ", i, ': ')
    print('Название: ', name_news[i])
    print('Дата: ', date_news[i])
    print('Ссылка: ', link_news[i])
    print('------------------------------------------------------')
# print(0)
# print(new_news[0])
# print(0)
