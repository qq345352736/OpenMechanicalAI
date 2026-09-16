import matplotlib.pyplot as plt
import numpy as np

# 1. 设置全局字体和大小（科研论文常用 Times New Roman 或 Arial）
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# 2. 创建画布和坐标系（figsize 控制图片尺寸，单位是英寸）
fig, ax = plt.subplots(figsize=(6, 4))  # 6x4 英寸，适合单栏插图

# 3. 生成数据（这里用正弦函数举例）
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 4. 绘图
ax.plot(x, y1, label='sin(x)', color='#1f77b4', linewidth=1.5, linestyle='-')
ax.plot(x, y2, label='cos(x)', color='#d62728', linewidth=1.5, linestyle='--')

# 5. 添加标签和标题（科研论文中标题通常放在图注里，图内可不加标题）
ax.set_xlabel('x (rad)', fontsize=12)
ax.set_ylabel('y', fontsize=12)

# 6. 添加图例（frameon=False 去掉图例边框，更简洁）
ax.legend(frameon=False, loc='best')

# 7. 设置刻度朝内（科研论文常见风格）
ax.tick_params(direction='in', top=True, right=True)

# 8. 保存图片（dpi=300 是期刊最低要求，bbox_inches='tight' 避免内容被裁剪）
plt.tight_layout()
plt.savefig('figure1.svg', dpi=300, bbox_inches='tight')
plt.show()