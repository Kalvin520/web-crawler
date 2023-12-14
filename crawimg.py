from bs4 import BeautifulSoup
import requests

web = requests.get('https://www.nkust.edu.tw/p/412-1000-2797.php', cookies={'over18':'1'})
# 傳送 Cookies 資訊後，抓取頁面內容

soup = BeautifulSoup(web.text, "html.parser")
# 使用 BeautifulSoup 取得網頁結構

imgs = soup.find_all('img')
 # 取得所有 img tag 的內容
base_url = 'https://www.nkust.edu.tw'
name = 0 #圖片編號
for i in imgs:
    print(i['src'])
# 取得所有 img 內src 的內容
    jpg = requests.get(i["src"])   # 使用 requests 讀取圖片網址，取得圖片編碼
    f = open(f'PIC/test_{name}.jpg', 'wb')
    f.write(jpg.content)  # 寫入圖片的 content
    f.close()  # 寫入完成後關閉圖片檔案
    name = name + 1


