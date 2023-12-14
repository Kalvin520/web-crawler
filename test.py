from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

web = requests.get('https://www.nkust.edu.tw/p/412-1000-2797.php', cookies={'over18': '1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')

name = 0
base_url = 'https://www.nkust.edu.tw'  # 網站的基本網址

for i in imgs:
    img = urljoin(base_url, i['src'])  # 轉換相對網址為絕對網址
    print(img)
    img_data = requests.get(img).content # 下載圖片的內容

    with open(f'img/test_{name}.jpg', 'wb') as f:
        f.write(img_data)  # 寫入圖片的內容
    name += 1
