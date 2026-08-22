# 机械计算器

# 转速计算
print("机械计算器 - 转速计算")
input_rpm = float(input("请输入转速（rpm）："))
ratio = float(input("请输入传动比："))
output_rpm = input_rpm / ratio
print("输出转速：", output_rpm, "rpm")

# 扭矩计算
print("机械计算器 - 扭矩计算")
input_power = float(input("请输入输入功率（W）："))
input_speed = float(input("请输入输入转速（rpm）："))
output_torque = 9550*input_power/input_speed
print("输出扭矩：", output_torque, "N·m")

# 计算线速度
print("机械计算器 - 线速度计算")
input_rotation_speed = float(input("请输入输入转速（rpm）："))
input_diameter = float(input("请输入输入直径（mm）："))
output_linear_speed = (input_rotation_speed * input_diameter * 3.14159) / 60
print("输出线速度：", output_linear_speed, "m/s")






