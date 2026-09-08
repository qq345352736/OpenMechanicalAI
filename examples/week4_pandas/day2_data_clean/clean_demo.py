import pandas as pd

# 先创建一个有缺失且有异常值的数据框
data = {
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", None,"张三"],
    "年龄": [25, -5, 200, 30, None, 28, 35, 40, 25],
    "城市": ["北京", " 上海 ", "广州", "beijing", None, "深圳", "杭州", "北京","北京"],
    "工资": [10000, 15000, 8000, -500, 20000, None, 12000, 999999,10000],
    "入职日期": ["2023-01-15", "2021/03/20", "2023-05-01", "invalid", "2020-11-10", "2022.08.15", None, "2023-01-01","2022-01-15"]
} 

df = pd.DataFrame(data)
print(f"原始属于:\n",df)
print(f"\n形状: ",df.shape)
# df.to_csv("original_data.csv", index=False)


'''
这份数据里几乎涵盖了所有常见问题：
问题                       出现在哪
空值                       姓名、年龄、城市、工资、入职日期
异常值（负数、离谱数字）     年龄-5、年龄200、工资-500、工资999999
格式不统一                  城市有空格、大小写混用
日期格式混乱                四种不同格式 + 一个 invalid
重复值                     后面会看到
'''

# Step 1: 先看看"脏"在哪里
print("整体信息:\n", df.info())
print("缺失值情况:\n", df.isnull().sum())
print("异常值情况:\n", df.describe())

# Step 2：处理缺失值
df=df.dropna(subset=["姓名"]) # 删除没有姓名的行,因为没有姓名就没有意义
print("处理姓名缺失值后的数据:\n", df)

# Step 3: 处理异常值
# 年龄：合理范围是18~65，超出异常值的用中位数填充
df.loc[(df["年龄"] < 18) | (df["年龄"] > 65), "年龄"] = df["年龄"].median()
df["年龄"]=df["年龄"].fillna(df["年龄"].median()) # 用中位数填充缺失值
print("处理年龄异常值后的数据:\n", df)

# 工资：合理范围是3000~20000，超出异常值的用中位数填充
df.loc[(df["工资"] < 3000) | (df["工资"] > 20000), "工资"] = df["工资"].median()
df["工资"] = df["工资"].fillna(df["工资"].median()) # 用中位数填充缺失值
print("处理工资异常值后的数据:\n", df)

# Step 4: 处理格式不统一
# 城市：去空格，统一小写
df["城市"] = df["城市"].str.strip().str.lower().str.replace("beijing", "北京")
df["城市"] = df["城市"].fillna("未知") # 用"未知"填充缺失值
print("处理城市格式后的数据:\n", df)

# 日期：统一格式为YYYY-MM-DD，无法解析的日期用缺失值填充
df["入职日期"] = df["入职日期"].str.replace("invalid", "2026-09-08") # 将invalid替换为缺失值

# 日期：统一转成 datetime，转不了的变成 NaT

df["入职日期"] = pd.to_datetime(df["入职日期"], errors="coerce")
df["入职日期"] = df["入职日期"].fillna(pd.Timestamp.today().normalize()) # 用"2026-09-08"填充缺失值
print("处理入职日期格式后的数据:\n", df)

# Step 5: 处理重复值
print(f"重复行数：", df.duplicated().sum()) # 注意：这里查找的是完全重复的行
# 按姓名去重，保留第1条 （仅找姓名相同的行）
df = df.drop_duplicates(subset=["姓名"], keep="first")
print("处理重复值后的数据:\n", df)

# Step 6: 最终检查
print("最终数据:\n", df)
print("最终数据形状: ", df.shape)
print("最终数据缺失值情况:\n", df.isnull().sum())
print("最终数据异常值情况:\n", df.describe())
print("最终数据整体信息:\n", df.info())