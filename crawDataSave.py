import requests
from bs4 import BeautifulSoup

#訪問的網址
url = 'https://water.taiwanstat.com/'
#取得URL的全部內容HTML
web = requests.get(url)
#使用剖析方法"html.parser"
soup = BeautifulSoup(web.text, "html.parser")
#取得所有class為=reservoir的tag
reservoir = soup.select('.reservoir')
#宣告headlines為一個(陣列)容器
headlines = list()

for i in reservoir:
    # 取得內容的 class 為 name 的 div 文字
    title = i.find('div', class_='name').get_text()
    # 把title塞進容器
    headlines.append(title)
    print(i.find('div', class_='name').get_text(), end=' ')
    # 取得內容 h5 tag 的文字
    text = i.find('h5').get_text()
    # 把title塞進容器
    headlines.append(text)
    print(i.find('h5').get_text(), end=' ')

# 把容器的內容丟進info
info = "\n".join(headlines)
# 開啟一個text檔命名為waterinfo把info存進去
with open("waterinfo.txt", "wt", encoding="utf=8") as fp:
    fp.write(info)

print("Done!")
