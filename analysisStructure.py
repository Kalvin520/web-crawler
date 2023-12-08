import urllib.request as req
import json
import ssl

# 使用SSL module把證書驗證改成不需要驗證
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://spa1.scrape.center/api/movie/?limit=10&offset=10"

# 降低被拒絕訪問顧增加headers設定
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析json資料格式
data = json.loads(data)

posts = data["results"]

for i in range(1, len(posts), 1):
    re = posts[i]["name"]
    print(re)
