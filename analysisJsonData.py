import urllib.request as req

url = "https://medium.com/_/api/home-feed"

# 降低被拒絕訪問顧增加headers設定
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析json資料格式
import json

data = data.replace("])}while(1);</x>", "")
data = json.loads(data)
# print(data)

posts = data["payload"]["references"]["Post"]
for key in posts:
    P = posts[key]
    print(P["title"])
