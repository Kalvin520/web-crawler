from bs4 import BeautifulSoup
import bs4
import urllib.request as req

base_url = "https://www.nkust.edu.tw/p/403-1000-13-{}.php?Lang=zh-tw"

# 迭代頁數
for page in range(1, 6, 1):  # 假設要爬取1到5頁的資料
    url = base_url.format(page)  # 替換URL中的占位符，生成具體的頁面URL

    # 降低被拒絕訪問顧增加headers設定
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

    # 處理中文字,避免中文出現亂碼
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 使用剖析方法"html.parser"
    root = bs4.BeautifulSoup(data, "html.parser")

    # 搜尋HTML中<div class="mtitle">
    titles = root.find_all("div", class_="mtitle")

    for title in titles:
        # 找尋<div class="mtitle">之內的<a>元素
        if title.a is not None:
            print(title.a.string)

    print("\n-----------\n")