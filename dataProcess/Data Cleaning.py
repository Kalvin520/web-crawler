import pandas as pd
import numpy as np

data = {
'degree': ['asdf-1231','asdf-1231', 'wert-4567', 'dfgh-1562', 'jhgf-5555', 'iyuy-9999', 'mkij-5842'],
'location': ['A', 'A','A', '', 'C', 'A', np.nan],
}

df = pd.DataFrame(data)
df = df.replace('',np.nan)# 將空字串''中的東西轉換為DataFrame中的NaN
print(df)

df = df.dropna()#刪除空值NaN
print(df)

df = df.drop_duplicates()#刪除重複資料
print(df)