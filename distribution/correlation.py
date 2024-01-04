import matplotlib as matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 或其他可用的后端，例如 'QtAgg'
# 設定中文字型
import matplotlib
matplotlib.rc('font', family='Apple LiSung')

# 讀取資料集
usecol1 = ['件數', '土地筆數', '土地面積', '建物棟數', '建物面積','診所數量', '圖書館數量']

df = pd.read_csv('合併結果.csv',usecols=usecol1)
df = df.dropna()

# 創建DataFrame
df = pd.DataFrame(df)

# 計算特徵之間的皮爾森相關係數
#皮爾森相關係數的值介於-1和1之間，表示兩個變數之間的關聯程度。如果值接近1，則表示兩個變數之間有強正相關；如果值接近-1，則表示兩個變數之間有強負相關；如果值接近0，則表示兩個變數之間幾乎無相關。
correlation_matrix = df.corr()

# 繪製熱力圖
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("相關性矩陣熱力圖")
plt.show()