from bs4 import BeautifulSoup
import requests
import bs4
import urllib.request as req

url = "https://spa1.scrape.center/"

# 降低被拒絕訪問顧增加headers設定
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

# 處理中文字,避免中文出現亂碼
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")


# 使用剖析方法"html.parser"
root = BeautifulSoup(data, "html.parser")
# 搜尋HTML中<div class="title">
print(root)
