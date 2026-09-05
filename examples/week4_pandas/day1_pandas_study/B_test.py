import pandas as pd

data = {
    "姓名": ["小明", "小红", "小刚", "小李"],
    "语文": [80, 85, 78, 90],
    "数学": [90, 88, 92, 85],
    "英语": [85, 82, 80, 88]
}

df = pd.DataFrame(data)
print(df)
# 计算总分和平均分
df["总分"] = df[["语文", "数学", "英语"]].sum(axis=1)
df["平均分"] = df[["语文", "数学", "英语"]].mean(axis=1)

# 找出平均分最高的学生
top_student = df.loc[df["平均分"].idxmax()]
print(top_student)