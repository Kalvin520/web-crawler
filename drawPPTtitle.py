from bs4 import BeautifulSoup
import bs4
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"

# 降低被拒絕訪問顧增加headers設定
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

# 處理中文字,避免中文出現亂碼
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 使用剖析方法"html.parser"
root = bs4.BeautifulSoup(data, "html.parser")

# 搜尋HTML中<div class="title">
titles = root.find_all("div", class_="title")

for title in titles:

    # 找尋<div class="title">之內	<a ...>.....</a>
    if title.a != None:
        print(title.a.string)
