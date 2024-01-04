import pandas as pd

# 读取CSV文件
df = pd.read_csv('診所資料.csv')

# 使用str.extract提取地址中的区域数据
df['區域'] = df['地址'].str.extract(r'(\w+)區')

# 计算重复区域的数量
duplicate_count = df['區域'].value_counts()

# 打印重复区域的数量
print(duplicate_count)