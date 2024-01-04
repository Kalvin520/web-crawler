import csv
import matplotlib
matplotlib.use('TkAgg')  # 或其他可用的後端，例如 'QtAgg'
import matplotlib.pyplot as plt

# 開啟 CSV 檔案
with open('診所資料.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 統計列數
    row_count = sum(1 for row in reader)

# 繪製長條圖
plt.bar(['CSV file'], [row_count], color='blue')
plt.xlabel('file')
plt.ylabel('Total count')
plt.title('')
plt.show()