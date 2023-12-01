import requests

url='https://tw.news.yahoo.com/'

resp=requests.get(url)
html=resp.text
print(resp.status_code)
q=input("輸入要查詢的字詞:")

while q!="":
    print(html.count(q))
    q=input("輸入要查詢的字詞:")

