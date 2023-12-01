import requests

#1.指定url
url = 'https://csc.nkust.edu.tw'
#2.發起請求
#get方法會返回一個響應物件
response = requests.get(url=url)
#3.獲取響應資料，.text返回的是字串形式的響應資料
page_text = response.text
print(page_text)
#4.持久化儲存
with open('./csc.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

print('爬取資料結束')

