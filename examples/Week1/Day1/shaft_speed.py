# motor_speed = 3000
motor_speed = float(input("请输入电机转速（rpm）："))
# gear_ratio = 3.0
gear_ratio = float(input("请输入电机传动比："))
# efficiency = 0.95
efficiency = float(input("请输入传动效率（0-1）："))

output_speed = motor_speed / gear_ratio

print("输入转速：", motor_speed, "rpm")
print("传动比：", gear_ratio)
print("效率：", efficiency)
print("输出转速：", output_speed, "rpm")