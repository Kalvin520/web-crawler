import requests
from bs4 import BeautifulSoup

url="https://www.edu.tw/News.aspx?n=4F8ED5441E33EA7B&sms=B69F3267D6C0F22D"
html=requests.get(url).text

soup=BeautifulSoup(html,"html.parser")
table=soup.find("table")
headlines=list()

for row in soup.find_all("tr"):
    cells=row.find_all("td")
    for cell in cells:
        a=cell.find("a")
        if a is not None and a.text != "下一頁":
            headlines.append(a.text)

news="\n".join(headlines)

with open("eduheadline.text","wt",encoding="utf=8") as fp:
    fp.write(news)

print("Done!")