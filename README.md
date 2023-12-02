# web-crawler
練習利用爬蟲取得網頁資料 tag結構,XML....

- crawl page 抓取的是一整張頁面資料


- wordCount 使用Regular Expression剖析網頁
正則表達式（Regular Expression 、regex、regexp or Re）透過我們自行定義的字符串規則，幫助我們從文本中找尋對應規則的字符串
過濾出我們所需的資料後，幫助我們將這些資料組成串列，方便我們對文本進行下一步的分析
舉個例子：我們要在文章中的眾多文字資料中，找尋文章提到的人物的身份證資料，我們就會去定義一個規則，第一個字符要是大寫的英文，後面要接續著九個數字，接著它就會根據這個規則找尋匹配的字符串，收集好後，回傳給我們
其他用法:https://ithelp.ithome.com.tw/articles/10197315


- crawMantUrl 適用於以分頁結構製成的網頁
觀察網頁的網址結構，因應需要抓多頁的應用 利用{}+ for loop來使用format函數更新

- 抓取< title>的內容 利用內建html.parser BeautifulSoup()

- 抓取標題< h1>< h2>...搜尋

- < img>搜尋
- < tag>搜尋

- #抓取PTT標題

