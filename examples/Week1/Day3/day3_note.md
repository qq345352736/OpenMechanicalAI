好，今天进入 **Week 1 · Day 3。**

如果说 Day 1 是“搭建工具链”，Day 2 是“学会让程序做计算”，那么今天是一个非常关键的转折点：

>Day 3：从 Python 编程进入科学计算。

对于你的机械工程背景来说，NumPy 是整个 AI + 工业软件路线中极其重要的一块基础设施。

以后你接触：

- 车辆动力学
- 有限元
- 多体动力学
- 信号处理
- 机器学习
- 深度学习
- PINN
- 优化
- CFD
- 数据驱动建模

都会反复遇到 NumPy。

# Week 1 · Day 3
今日目标：NumPy 科学计算基础

建议用时：2～3小时

今天完成后，你应该能够理解：
```
Python list
      ↓
NumPy ndarray
      ↓
向量
      ↓
矩阵
      ↓
工程数据
      ↓
科学计算
```
并能够自己完成一个小项目：

>Vehicle Dynamics Data Analyzer v0.1

也就是：

**读取一组车辆动力学数据 → 计算 → 统计 → 绘图。**

## 一、为什么机械工程师必须学 NumPy？

先看一个你非常熟悉的问题。

假设车辆进行了一个仿真，得到：
```
时间       横摆角速度
0.00       0.01
0.01       0.03
0.02       0.06
0.03       0.10
...
```
如果有10000个数据点。

你当然不可能手工处理。

Python的普通列表可以存：
```
time = [0.00, 0.01, 0.02, 0.03]
yaw_rate = [0.01, 0.03, 0.06, 0.10]
```
但是如果需要进行：

- 向量运算
- 矩阵运算
- 统计
- FFT
- 线性代数
- 数值计算

普通 Python list 就不够方便了。

所以出现了：

> NumPy = Numerical Python

## 二、今天第一次安装 NumPy

你之前已经建立：
```
omai-dev
```
所以现在一定先确认：
```
conda activate omai-dev
```
然后：
```
python --version
```
确认你当前使用的是：
```
Python 3.12.x
```
然后安装：
```
pip install numpy
```
**一个非常重要的问题**

你之前问过一个非常好的问题：

> “pip install numpy 难道不是针对当前的 Python 环境吗？”

今天正好把这个问题彻底搞清楚。

如果你现在看到：
```
(omai-dev)
```
再执行：
```
pip install numpy
```
通常意味着：
```
pip
 ↓
omai-dev环境中的Python
 ↓
安装numpy
```
但是为了绝对明确，以后我更推荐你使用：
```
python -m pip install numpy
```
为什么？

因为：
```
python
```
明确告诉系统：

> “使用当前这个 Python。”

然后：
```
-m pip
```
表示：

“使用这个 Python 对应的 pip。”

所以以后推荐：
```
python -m pip install numpy
```
而不是单纯：
```
pip install numpy
```
这是一个非常值得从第一天就养成的习惯。

## 三、确认 NumPy

建立：
```
day3_numpy.py
```
输入：
```
import numpy as np

print(np.__version__)
```
运行。

如果出现：
```
2.x.x
```
说明成功。

## 四、NumPy最核心的概念：ndarray

现在：
```
import numpy as np

speed = np.array([1000, 1500, 2000, 2500, 3000])

print(speed)
```
输出：
```
[1000 1500 2000 2500 3000]
```
这个：
```
np.array(...)
```
生成的对象叫：
```
ndarray
```
即：
```
N-dimensional array
```
也就是：

> N维数组。

## 五、从机械工程角度理解 ndarray

例如：

speed = np.array([1000, 1500, 2000, 2500, 3000])

你可以把它理解成：

n = [1000, 1500, 2000, 2500, 3000]

也就是一个：

一维向量

如果：

A = np.array([
    [1, 2],
    [3, 4]
])

那么：

A =
[1 2
 3 4]

就是一个：

2×2矩阵

这时候你会发现：

NumPy其实和机械工程师非常熟悉的线性代数天然对应。

## 六、今天第一个练习：创建向量

创建：

day3_vector.py

写：

import numpy as np

speed = np.array([1000, 1500, 2000, 2500, 3000])

print(speed)
print(type(speed))
print(speed.shape)

你应该看到类似：

[1000 1500 2000 2500 3000]

<class 'numpy.ndarray'>

(5,)

这里：

(5,)

表示：

这个数组有5个元素。

## 七、NumPy最大的优势：向量化计算

例如：

speed = np.array([1000, 1500, 2000, 2500, 3000])

speed_rad = speed * 2 * np.pi / 60

print(speed_rad)

一次性计算全部数据。

这就是：

Vectorization（向量化）

这和Python list有很大的区别。

普通list：

speed = [1000, 1500, 2000]

不能直接这样进行数学运算：

speed * 2

NumPy则可以：

speed = np.array([1000, 1500, 2000])

print(speed * 2)

得到：

[2000 3000 4000]
## 八、这对你的意义非常大

你以后处理车辆仿真数据时，经常会有：

100000 × 20

这样的数据。

例如：

时间
车速
横摆角速度
侧向加速度
纵向加速度
侧偏角
方向盘转角
轮胎力
...

如果使用NumPy：

data * scale

可能一行代码就能完成大量计算。

这就是：

科学计算程序的基础。

## 九、今天学习数组的索引

例如：

speed = np.array([1000, 1500, 2000, 2500, 3000])

取第一个：

print(speed[0])

得到：

1000

注意：

Python从 0 开始计数。

所以：

speed[0] → 1000
speed[1] → 1500
speed[2] → 2000
## 十、切片

例如：
```
print(speed[1:4])
```
结果：
```
[1500 2000 2500]
```
这叫：
```
slicing
```
以后处理仿真时间窗口的时候非常重要。

例如：
```
time_window = time[1000:5000]
```
表示取第1000～4999个数据点。

## 十一、二维数组

现在创建一个矩阵：
```
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A)
print(A.shape)
```
输出：
```
[[1 2 3]
 [4 5 6]]

(2, 3)
```
意思：

> 2行3列。

## 十二、这就是你熟悉的矩阵

例如：

$$ M= \begin{bmatrix} m_{11}&m_{12}\\ m_{21}&m_{22} \end{bmatrix} $$

在Python里：
```
M = np.array([
    [m11, m12],
    [m21, m22]
])
```
这就是：

机械数学模型 → Python数据结构

这是你以后开发工业软件非常重要的一步。

## 十三、矩阵运算

例如：
```
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(A + B)
```
得到：
```
[[ 6  8]
 [10 12]]
```
矩阵乘法：
```
C = A @ B

print(C)
```
这里：
```
@
```
非常重要。

它表示：

矩阵乘法

## 十四、一个机械工程例子

假设：

$$ F=Kx $$

其中：
```
K = 刚度矩阵
x = 位移向量
F = 力向量
```
Python：
```
import numpy as np

K = np.array([
    [1000, -500],
    [-500, 1000]
])

x = np.array([
    0.01,
    0.02
])

F = K @ x

print(F)
```
这已经开始接近：

**有限元程序的底层思想。**

虽然真正的有限元远比这个复杂，但本质上离不开：
```
矩阵
+
向量
+
线性代数
```

## 十五、NumPy统计功能

假设：
```
yaw_rate = np.array([
    0.1,
    0.2,
    0.3,
    0.2,
    0.15
])
```
最大值：
```
np.max(yaw_rate)
```
最小值：
```
np.min(yaw_rate)
```
平均值：
```
np.mean(yaw_rate)
```
标准差：
```
np.std(yaw_rate)
```
这意味着以后你可以自动分析：

车辆仿真结果最大横摆角速度是多少？

直接：
```
max_yaw_rate = np.max(yaw_rate)
```

## 十六、今天第一次接触“工程数据处理”

现在做一个真正的小程序。

建立：
```
vehicle_data.py
```
写：
```
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
```
运行。

## 十七、现在增加一个“工程判断”

加入：
```
max_yaw_rate = np.max(yaw_rate)

if max_yaw_rate > 0.18:
    print("警告：横摆角速度峰值较高")
else:
    print("横摆角速度处于正常范围")
```
现在你的程序已经具备：
```
数据
 ↓
计算
 ↓
统计
 ↓
判断
 ↓
工程结论
```
**这已经开始接近真正的工程分析软件。**

## 十八、今天最重要的练习：速度数据

现在给你一个任务。

假设车辆速度为：
```
speed_kmh = np.array([
    60,
    65,
    70,
    75,
    80
])
```
你需要完成：

① 转换成 m/s

公式：

$$ v_{m/s}=\frac{v_{km/h}}{3.6} $$

② 计算平均速度

使用：
```
np.mean()
```
③ 找最大速度

使用：
```
np.max()
```
④ 找最小速度

使用：
```
np.min()
```
⑤ 判断

如果最大速度超过：
```
75 km/h
```
输出：
```
高速工况
```
否则：
```
一般工况
```

## 十九、进一步挑战：计算车辆动能

这是把 Day 2 和 Day 3 联系起来。

假设：
```
mass = 1500
```
以及：
```
speed_kmh = np.array([
    60,
    65,
    70,
    75,
    80
])
```
先：
```
speed_mps = speed_kmh / 3.6
```
然后：

$$ E=\frac12mv^2 $$

代码：
```
energy = 0.5 * mass * speed_mps ** 2
```
注意：
```
**
```
表示幂。

所以：
```
speed_mps ** 2
```
就是：

$$ v^2 $$

然后：
```
print(energy)
```
你会得到一个数组。

这就是：

**一次性计算整个车辆速度工况的动能**。

## 二十、今天开始接触工程绘图

安装：
```
python -m pip install matplotlib
```
然后创建：
```
plot_vehicle_data.py
```
写：
```
import numpy as np
import matplotlib.pyplot as plt

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

plt.plot(time, yaw_rate)

plt.xlabel("Time (s)")
plt.ylabel("Yaw Rate (rad/s)")
plt.title("Vehicle Yaw Rate")

plt.show()
```

运行。

你应该看到一张：

横摆角速度—时间曲线。

## 二十一、你会发现一件非常有意思的事情

昨天：
```
Python
=
计算器
```
今天：
```
Python + NumPy
=
科学计算工具
```
再加上：
```
Matplotlib
```
就变成：
```
数据
 ↓
计算
 ↓
可视化
```
再往后：
```
Pandas
 ↓
机器学习
 ↓
PyTorch
 ↓
AI
```
所以整个路线其实是一层一层搭起来的。

## 二十二、今天的Mini Project

今天不要做太多零碎练习。

完成一个：
```
Vehicle Dynamics Data Analyzer v0.1
```
目录：
```
OpenMechanicalAI
│
├── examples
│   └── vehicle_data_analyzer.py
│
└── README.md
```
程序至少实现：

- 输入
- 车辆质量
- 时间序列
- 车辆速度
- 横摆角速度
- 自动计算
- 最大速度
- 平均速度
- 最小速度
- 最大横摆角速度
- 平均横摆角速度
- 车辆动能
- 自动判断
- 是否属于高速工况
- 横摆角速度峰值是否较高
- 自动绘图

至少两张：

- 速度-时间
- 横摆角速度-时间
  
## 二十三、一个重要要求：不要复制我的代码

今天这个项目，我建议你：

先自己写。

遇到不会的地方，再查：

- Python官方文档
- NumPy官方文档
- Matplotlib官方文档
- 搜索引擎
- ChatGPT

但是不要直接把我的代码整段复制进去。

因为我们的目标不是：

“把代码跑起来。”

而是：

培养你自己构建工业软件的能力。

## 二十四、今天需要掌握的NumPy命令

今天不用背100个。

只掌握这些：
```
np.array()

np.zeros()

np.ones()

np.arange()

np.linspace()

np.max()

np.min()

np.mean()

np.std()

np.sum()

np.sqrt()

array.shape

array[0]

array[1:4]

A @ B
```
尤其是：
```
np.array()
np.mean()
np.max()
np.min()
array.shape
```

## 二十五、今天的Git任务

项目完成以后：
```
git status
```
确认文件。

然后：
```
git add .
```
提交：
```
git commit -m "Add NumPy vehicle dynamics data analysis"
```
然后：
```
git push
```
> 打开GitHub确认。

## 二十六、今天还有一个非常重要的“环境实验”

因为你之前已经遇到过：

VS Code解释器和终端Python环境不一致。

今天我们主动验证一次。

在 VS Code 里面运行：
```
import sys
import numpy as np

print("Python:", sys.executable)
print("NumPy:", np.__version__)
```
你应该看到类似：
```
Python: D:\...\miniconda3\envs\omai-dev\python.exe
NumPy: 2.x.x
```
这一行非常重要：
```
sys.executable
```
它告诉你：

当前这个Python程序究竟由哪个Python解释器执行。

以后你碰到：
```
ModuleNotFoundError
```
第一件事就应该检查：
```
import sys
print(sys.executable)
```
这会帮你解决大量环境问题。

## 二十七、今天的验收标准

今天完成以下内容就算通过：

**环境**
 - omai**-dev 环境正常
 - NumPy安装成功
-  Matplotlib安装成功
 - VS Code使用 omai-dev
**NumPy**
 - 理解 ndarray
 - 会创建一维数组
 - 会创建二维数组
 - 会使用索引
 - 会切片
 - 会进行向量运算
 - 理解 shape
 - 理解 @
**数据分析**
 - np.max()
 - np.min()
 - np.mean()
 - np.std()
**工程项目**
 - Vehicle Dynamics Data Analyzer v0.1
 - 速度数据分析
 - 横摆角速度分析
 - 动能计算
 - 两张工程图
**GitHub**
 - commit
 - push
最后给你一个今天的思考题

不要急着回答。

想一想：
```
如果现在给你一个Adams仿真导出的CSV文件，里面有10万个时间点、20个车辆动力学变量，你能不能让Python自动读取它，然后自动识别“速度、横摆角速度、侧向加速度”等变量，并自动生成一份工程分析报告？
```
答案现在是：
```
不能。
```
但我们已经开始一步一步构建这个能力。

接下来：
```
Day 1
Python环境
 ↓
Day 2
Python编程
 ↓
Day 3
NumPy
 ↓
Day 4
Matplotlib + 数据可视化
 ↓
Day 5
Pandas + CSV/Excel
 ↓
Day 6
函数与模块化
 ↓
Day 7
Week 1项目整合
```
而到第一阶段结束，我们会逐渐做到：
```
Adams
 ↓
CSV
 ↓
Python
 ↓
自动读取
 ↓
自动分析
 ↓
自动绘图
 ↓
自动生成报告
```
这就是我们最终构建 OpenMechanicalAI 的第一块砖。

今天先把 Vehicle Dynamics Data Analyzer v0.1 做出来。完成后把你的代码贴给我，我会继续按照真实工业软件项目的 Code Review 标准帮你修改，然后我们进入 Day 4。