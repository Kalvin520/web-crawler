import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

web = requests.get('https://www.nkust.edu.tw/p/412-1000-2797.php', cookies={'over18': '1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')

target_name = "高科大散步地圖"  # 設定目標圖片的名稱

name = 0
base_url = 'https://www.nkust.edu.tw'  # 網站的基本網址

for i in imgs:
    if i.get('alt') == target_name:  # 使用條件判斷來選擇符合名稱的圖片
        img_url = urljoin(base_url, i['src'])  # 轉換相對網址為絕對網址
        img_data = requests.get(img_url).content  # 下載圖片的內容
        os.makedirs('img2', exist_ok=True)  # 自動建立 img 資料夾
        with open(f'img2/test_{name}.jpg', 'wb') as f:
            f.write(img_data)  # 寫入圖片的內容
        name += 1