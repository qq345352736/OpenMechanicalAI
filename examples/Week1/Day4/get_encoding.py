import pandas as pd
import chardet #

# 检测文件编码
with open('sales.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"检测到编码：{encoding}")

# 用检测到的编码读取
df = pd.read_csv('sales.csv', encoding=encoding)
print(df)