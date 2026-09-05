# 初步学习pandas
# pandas 让你像操作 Excel 表格一样，用代码高效地读、写、清洗、分析数据。

import pandas as pd
# 读取csv文件
data1=pd.read_csv("./data.csv", encoding="gbk")
print(data1)
# 直接声明pandas数据
data={"姓名":["张三","李四","王五"],
      "年龄":[25, 30, 35],
      "城市":["北京","上海","广州"],
      "籍贯":["山东","江苏","广东"]}

data2=pd.DataFrame(data)
print(data2)

# 1. 常规命令
print("前5行数据：",data1.head()) # 默认5行
print("后2行数据：",data1.tail(2))
print("数据形状：",data1.shape)
print("列名：",data1.columns)
print("数据信息：",data1.info())
print("数值列的统计信息：",data1.describe())

# 2. 数据选取
print("选取特定列：",data1["时间(s)"]) # 单列
print("选取特定列：",data1[["时间(s)","加速度(m/s2)"]]) # 多列
print("选取特定行：",data1.iloc[0]) # 第一行
print("选取特定行：",data1.iloc[0:2]) # 第一行和第二行

# 3. 筛选(超常用!)
print("筛选数据：",data1[data1["时间(s)"] > 0.005])
print("范围筛选：",data1[(data1["时间(s)"] >= 0.005) & (data1["时间(s)"] < 0.007)])

# 4. 新增 / 修改列
data1["速度(m/s)"] = data1["加速度(m/s2)"] * data1["时间(s)"]  # 仅演示
print("新增列后：",data1)

# 5. 排序
print("按时间排序：",data1.sort_values("时间(s)", ascending=False))

# 6. 缺失值处理
score=pd.read_csv("./score.csv", encoding="gbk")
print(score)
print("哪些是缺失的：", score.isnull().sum())
# score.dropna(inplace=True)  # 删掉有缺失值的行.inplace=True的含义是改原来的变量
score=score.dropna() # 把改后的变量赋值给原变量
print("删掉缺失值后：\n", score)
# score.fillna(0, inplace=True)  # 用0填充缺失值
# print("填充缺失值后：\n", score)

# 7. 读写文件
score2=pd.read_csv("./score.csv", encoding="gbk")
print("原始表格\n:", score2)
score2=score2.fillna(score2["英语成绩"].mean()) # 用平均值填充缺失值
print("填充缺失值后：\n", score2)
# 保存
score2.to_csv("./score_filled.csv", index=False, encoding="gbk")