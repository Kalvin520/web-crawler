import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib
matplotlib.rc('font', family='Apple LiSung')

# 读取第一个CSV文件并创建第一个直方图
df1 = pd.read_csv('診所資料.csv')
df1['區域'] = df1['行政區'].str.extract(r'(\w+)區')
region_counts1 = df1['區域'].value_counts()

# 创建第一个子图
fig, ax = plt.subplots(2, 1, figsize=(10, 12))

# 绘制第一个直方图
ax[0].bar(region_counts1.index, region_counts1)
for i, count in enumerate(region_counts1):
    ax[0].text(i, count, str(count), ha='center', va='bottom')
ax[0].set_title('診所區域分布')
# ax[0].set_xlabel('區域')
ax[0].set_ylabel('區域內診所數量')
ax[0].set_xticks(region_counts1.index)
ax[0].tick_params(axis='x', rotation=45)

# 读取第二个CSV文件并创建第二个直方图
df2 = pd.read_csv('112高雄市圖書館.csv')
df2['區域'] = df2['地址'].str.extract(r'(\w+)區')
region_counts2 = df2['區域'].value_counts()
print(df2)
# 绘制第二个直方图
ax[1].bar(region_counts2.index, region_counts2)
for i, count in enumerate(region_counts2):
    ax[1].text(i, count, str(count), ha='center', va='bottom')
ax[1].set_title('圖書館區域分布')
ax[1].set_xlabel('區域')
ax[1].set_ylabel('區域內圖書館數量')
ax[1].set_xticks(region_counts2.index)
ax[1].tick_params(axis='x', rotation=45)

# 调整子图间距
plt.tight_layout()

# 显示图形
plt.show()




