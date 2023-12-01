# 用{}作為標記,我們需要置換的值

# url = "https://www.kkday.com/zh-tw/city/kaohsiung/attractions-and-tickets?cat=TAG_2_1&sort=prec&page={}"

# url = "https://technews.tw/page/{}/"]

url = "https://www.nkust.edu.tw/p/422-1000-1001-{}.php?Lang=zh-tw"

for i in range(1, 6, 1):
    print(url.format(i))

