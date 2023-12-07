import requests
from bs4 import BeautifulSoup

#訪問的網址
url = 'https://water.taiwanstat.com/'
#取得URL的全部內容HTML
web = requests.get(url)
#使用剖析方法"html.parser"
soup = BeautifulSoup(web.text, "html.parser")
# 取得所有class為=reservoir的tag
reservoir = soup.select('.reservoir')

for i in reservoir:
  # 取得內容的 class 為 name 的 div 文字
  print(i.find('div', class_='name').get_text(), end=' ')
  # 取得內容 h5 tag 的文字
  print(i.find('h5').get_text(), end=' ')
  print("\n")