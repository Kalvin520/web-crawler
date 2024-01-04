import pandas as pd

# 讀取不動產買賣資料
df_real_estate = pd.read_csv('112-不動產買賣.csv')

# 讀取counts資料
df_counts = pd.read_csv('counts.csv')

# 將不動產買賣資料的區名欄位取前兩個字元
df_real_estate['區名'] = df_real_estate['區名'].str[:2]

# 將counts資料的區名欄位取前兩個字元
df_counts['區名'] = df_counts['區名'].str[:2]

# 將counts資料的診所數量和圖書館數量合併到不動產買賣資料中
df_merged = df_real_estate.merge(df_counts, on='區名', how='left')

# 將合併後的資料儲存到新的CSV檔案
df_merged.to_csv('合併結果.csv', index=False)