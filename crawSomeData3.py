from bs4 import BeautifulSoup
import requests

url = "https://spa1.scrape.center/"

# 發送請求並獲取網頁內容
response = requests.get(url)
data = response.text

# 使用剖析方法"html.parser"來解析HTML內容
soup = BeautifulSoup(data, "html.parser")

# 提取所需資料
movie_data = []  # 用於存儲提取的電影資料的列表
movies = soup.find_all("div", class_="el-card__body")  # 找到所有具有class為"el-card__body"的div元素

for movie in movies:
    # 從每個div元素中提取電影的名稱、上映日期和評分
    name = movie.find_all("h2", class_="m-b-sm").text  # 提取電影名稱
    published_at = movie.find_all("span", class_="m-v-sm").text  # 提取上映日期
    score = movie.find("p", class_="score").text  # 提取評分

    # 將提取的資料組成字典並添加到電影資料列表中
    movie_data.append({
        "name": name,
        "published_at": published_at,
        "score": score
    })

# 打印提取的資料
for movie in movie_data:
    print("片名:", movie["name"])
    print("上映日期:", movie["published_at"])
    print("評分:", movie["score"])