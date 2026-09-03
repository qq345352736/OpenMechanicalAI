import os
import pandas as pd

# 查看当前工作目录
print("当前目录：", os.getcwd())

# 查看当前目录下所有文件
print("文件列表：", os.listdir())

import pandas as pd
df = pd.read_csv('sales_utf8.csv')  # 使用 UTF-8 编码读取 CSV 文件
print(df)
print(df.info())
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df.head(3))
print(df.tail(2))

# 数据筛选与切片

print("选择单列（返回 Series）")
print(df['地区'])

# 2. 选择多列（返回 DataFrame）
print(df[['地区', '销售额']])

# 3. 按行筛选（条件过滤）
# 找出销售额大于 1500 的记录
print(df[df['销售额'] > 1500])

# 4. 多条件筛选（用 & 表示且，| 表示或）
# 找出重庆且销售额大于 1000 的记录
print(df[(df['地区'] == '重庆') & (df['销售额'] > 1000)])

# 5. 按位置取数据（iloc：第 2 行到第 3 行，第 0 列到第 2 列）
print(df.iloc[1:3, 0:2])

# 6. 按标签取数据（loc：取“地区”列所有行）
print(df.loc[:, '地区'])