import numpy as np

vehicle_velocity=np.array([10, 20, 30, 40, 50, 90])
print("最大车速：", np.max(vehicle_velocity))
print("最小车速：", np.min(vehicle_velocity))
print("平均车速：", np.mean(vehicle_velocity))
print("车速标准差：", np.std(vehicle_velocity))
print("车速中位数：", np.median(vehicle_velocity))
print("车速总和：", np.sum(vehicle_velocity))

# 增加工程判断
limit_velocity=100
max_vehicle_velocity=np.max(vehicle_velocity)
if max_vehicle_velocity > limit_velocity:
    print("警告：车速超过安全阈值！")
else:
    print("车速在安全范围内。")
