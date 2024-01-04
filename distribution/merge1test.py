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




import pandas as pd

# 讀取診所資料的CSV檔案
df_clinic = pd.read_csv('診所資料.csv')
df_clinic['區域'] = df_clinic['行政區'].str.extract(r'(\w+)區')
clinic_counts = df_clinic['區域'].value_counts().to_dict()

# 讀取圖書館資料的CSV檔案
df_library = pd.read_csv('112高雄市圖書館.csv')
df_library['區域'] = df_library['地址'].str.extract(r'(\w+)區')
library_counts = df_library['區域'].value_counts().to_dict()

# 輸出診所的區域與數量
print("診所區域與數量:")
for area, count in clinic_counts.items():
    print(f"{area}: {count}")

# 輸出診所的區域與數量
print("圖書館區域與數量:")
for area, count in library_counts.items():
    print(f"{area}: {count}")

########################


import pandas as pd

# 建立包含區域、診所數量和圖書館數量的 DataFrame
df_counts = pd.DataFrame(columns=['區名', '診所數量', '圖書館數量'])

# 迭代每個區域，將數量加入 DataFrame
for area in set(clinic_counts.keys()).union(set(library_counts.keys())):
    clinic_count = clinic_counts.get(area, 0)
    library_count = library_counts.get(area, 0)
    df_counts = pd.concat([df_counts, pd.DataFrame({'區名': [area], '診所數量': [clinic_count], '圖書館數量': [library_count]})], ignore_index=True)

# 將 DataFrame 存成 CSV 檔案
df_counts.to_csv('counts.csv', index=False)

print("區域、診所數量和圖書館數量已保存至 counts.csv！")