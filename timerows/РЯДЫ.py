import sqlite3
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

conn = sqlite3.connect("ietr.db")
cursor = conn.cursor()

def createDB():
    cursor.execute("""CREATE TABLE news
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    link TEXT NOT NULL)
    """)

url = 'https://www.defenseadvancement.com/news/section/technology/'
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")
news = soup.findAll(class_='product-card full-bkg category')

print("----------------------news-------------------------")
name_news = []
link_news = []
date_news = []
text_news = []

for i in range(len(news)):
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
        # print(news_inlink)
        # print('-----------------------------------------------------------')

        name_news.append(new[5])
        date_news.append(new[9])
        link_news.append(link)
        text_news.append('')

# createDB()


# print("----------------------news-------------------------")
for i in range(len(link_news)):
    data = []
    data = [(name_news[i], date_news[i], link_news[i])]
    cursor.executemany("INSERT INTO news (title, date, link) VALUES (?,?,?)", data)
    conn.commit()
    # print('------------------------------------------------------')

db_df = pd.read_sql_query("SELECT * FROM news", conn)
db_df.to_csv('database.csv', index=False)

cursor.execute("SELECT * FROM news")
itog = cursor.fetchall()
itog
print(itog)