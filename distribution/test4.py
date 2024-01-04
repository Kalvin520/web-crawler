import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 或其他可用的后端，例如 'QtAgg'
import matplotlib
matplotlib.rc('font', family='Apple LiSung')

# 读取CSV文件
df = pd.read_csv('112高雄市圖書館.csv')

# 使用str.extract提取地址中的区域数据
df['區域'] = df['地址'].str.extract(r'(\w+)區')

# 计算每个区域的数量
region_counts = df['區域'].value_counts()

# 创建直方图
plt.figure(figsize=(10, 6))  # 调整图形大小
plt.bar(region_counts.index, region_counts)

# 添加数量标签
for i, count in enumerate(region_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# 添加标题和坐标轴标签
plt.title('圖書館區域分布')
plt.xlabel('區域')
plt.ylabel('區域內圖書館數量')

# 旋转區域标签以避免重叠
plt.xticks(rotation=45)

# 显示图形
plt.show()