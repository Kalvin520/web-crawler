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

# 创建饼图
plt.figure(figsize=(10, 10))  # 调整图形大小
wedges, _ = plt.pie(region_counts, startangle=90)

# 添加区域的颜色和数量标签
color_palette = plt.cm.Set3(range(len(region_counts)))
for i, wedge in enumerate(wedges):
    wedge.set_edgecolor('white')

    # 添加区域的数量和名称标签
    x, y = wedge.center
    angle = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
    radius = wedge.r
    x += radius * 0.85 * np.cos(np.deg2rad(angle))
    y += radius * 0.85 * np.sin(np.deg2rad(angle))
    plt.text(x, y, f"{region_counts.index[i]}\n{region_counts[i]}", fontsize=12, weight='bold', ha='center', va='center')

# 添加标题
plt.title('區域分布')

# 显示图形
plt.show()