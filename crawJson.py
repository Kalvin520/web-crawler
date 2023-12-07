import urllib.request as req
import json

# 爬取網址
url = "https://spa1.scrape.center/api/movie/?limit=10&offset=0"

# 仿製瀏覽器資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

# 針對中文字解碼(採用UTF-8)
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# json資料載入
print(data)

data = data.replace("])}while(1);</x>","")
data = json.loads(data)
print(data)

