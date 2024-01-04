import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 或其他可用的後端，例如 'QtAgg'
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
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%')

# 添加标题
plt.title('區域分布')

# 显示图形
plt.show()