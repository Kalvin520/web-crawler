import requests
from bs4 import BeautifulSoup

url = "https://water.taiwanstat.com/"
web = requests.get(url) #取得網站內容
soup = BeautifulSoup(web.text,"html.parser") #轉換成標籤樹
title = soup.title # 取得 title
print(soup)
print(title) # 印出 title ( 台灣水庫即時水情 )
# with open('./taiwaiWater.html','w',encoding='utf-8') as tw:
#     tw.write(web.text)
