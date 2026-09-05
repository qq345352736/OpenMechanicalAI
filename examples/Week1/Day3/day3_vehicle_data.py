import numpy as np

time = np.array([
    0.0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5
])

yaw_rate = np.array([
    0.05,
    0.08,
    0.12,
    0.20,
    0.15,
    0.10
])

print("最大横摆角速度：", np.max(yaw_rate))
print("最小横摆角速度：", np.min(yaw_rate))
print("平均横摆角速度：", np.mean(yaw_rate))
print("横摆角速度标准差：", np.std(yaw_rate))

# 增加工程判断
max_yaw_rate=np.max(yaw_rate)
if max_yaw_rate > 0.15:
    print("警告：横摆角速度超过安全阈值！")
else:
    print("横摆角速度在安全范围内。")