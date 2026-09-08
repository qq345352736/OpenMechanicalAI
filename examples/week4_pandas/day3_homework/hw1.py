import pandas as pd

data = {
    "订单号": ["A001", "A002", "a003", "A004", "A002", "A005", None],
    "客户名": [" 张三 ", "李四", "王五", "赵六", "李四", "钱七", "孙八"],
    "金额": [100, -50, 300, 999999, 100, None, 200],
    "下单日期": ["2024-01-01", "2024/01/02", "24-Jan-03", "2024-01-04", "2024/01/02", None, "invalid"],
    "产品": ["手机", "电脑", "手机", "平板", "电脑", "耳机", "手机"]
}

df = pd.DataFrame(data)
# 你的任务：
# 1. 处理缺失值
# 2. 金额异常值（合理范围 0~50000）
# 3. 订单号统一大写
# 4. 客户名去空格
# 5. 日期统一格式
# 6. 按订单号去重
# 7. 保存清洗后的结果

# Step 0: 先看看数据的整体情况
print("整体信息:\n", df.info())
print("缺失值情况:\n", df.isnull().sum())
print("异常值情况:\n", df.describe())


# Step 1: 处理缺失值
# 处理订单号
df=df.dropna(subset="订单号") # 删除没有订单号的行,因为没有订单号就没有意义
# 处理日期
df["下单日期"]=df["下单日期"].replace({"2024/01/02": "2024-01-02","24-Jan-03": "2024-01-03"}) # 统一日期格式
df["下单日期"]=pd.to_datetime(df["下单日期"], errors="coerce") # 将无法解析的日期变成 NaT
df["下单日期"]=df["下单日期"].fillna(pd.Timestamp.today().normalize()) # 用今天的日期填充缺失值
print("处理缺失值后的数据:\n", df)

# Step 2: 处理金额异常值
# 处理金额
df.loc[(df["金额"] < 0), "金额"] = 0
df.loc[(df["金额"] > 50000), "金额"] = 50000
df["金额"]=df["金额"].fillna(df["金额"].median()) # 用中位数填充缺失值
print("处理金额异常值后的数据:\n", df)

# Step 3: 处理订单号格式
df["订单号"]=df["订单号"].str.upper() # 统一大写
print("处理订单号格式后的数据:\n", df)

# Step 4: 处理客户名格式
df["客户名"]=df["客户名"].str.strip() # 去空格
print("处理客户名格式后的数据:\n", df)

# Step 5: 订单号去重
df=df.drop_duplicates(subset="订单号", keep="first") # 按订单号去重，保留第1条
print("处理重复值后的数据:\n", df)

# Step 6: 查看处理后的数据
print("处理后的数据:\n", df)
print("处理后的数据形状:\n", df.shape)
print("处理后的数据缺失值情况:\n", df.isnull().sum())
print("处理后的数据异常值情况:\n", df.describe())
print("处理后的数据信息:\n", df.info())

# 保存清洗后的结果
df.to_csv("cleaned_data.csv", index=False)