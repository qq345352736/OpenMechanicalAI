# Week 1 · Day 1
建立你的 AI 工业软件开发环境
今天预计用时：2～3小时。
今天结束时，你应该能够：
理解 Python、Git、GitHub、VS Code、Conda 分别是什么
在自己的电脑上安装 Python 开发环境
用 VS Code 写出第一个 Python 程序
创建自己的第一个 GitHub Repository
完成第一次 commit 和 push
理解以后100周学习的基本工作方式
## 一、先建立一个正确的认知
你过去做车辆动力学，很可能是这种工作模式：
建模 → 设置参数 → 仿真 → 看结果 → 优化
以后我们要逐渐变成：
提出工程问题 → 编写程序 → 调用仿真软件 → AI分析 → 自动优化 → 自动生成结果
所以你未来真正需要掌握的是下面这条链：
```
Mechanical Engineering
        ↓
Python
        ↓
Scientific Computing
        ↓
Software Engineering
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
LLM
        ↓
AI Agent
        ↓
Physics + AI
        ↓
Industrial Software
```
今天我们只走第一步：
```
Python + Git + GitHub
```
## 二、今天先不要安装一大堆AI软件
这一点非常重要。
你现在不要安装：
- CUDA
- PyTorch
- TensorFlow
- Ollama
- LangChain
- 各种大模型
- 各种Agent框架
因为现在装这些东西没有意义。
我们先把：
```
Python → Git → GitHub → VS Code
```
这条基础链打通。

## 三、第一项任务：安装 VS Code
官方地址：
Visual Studio Code 官方网站
安装。
安装过程中，如果看到：
```
Add to PATH
```
建议勾选。
如果看到：
```
Add "Open with Code" action
```
也可以勾选。
安装完成以后
打开 VS Code。
你会看到一个类似：
```
Welcome
```
的界面。
暂时不用研究所有按钮。
你只需要认识左边几个：
```
Explorer
Search
Source Control
Run and Debug
Extensions
```
今天重点是：
**Explorer**
和
**Source Control**
以后这两个按钮会非常重要。
## 四、第二项任务：安装 Python
我建议你现在使用：
**Python 3.12**
而不是追求最新版本。
Python官方网站：
Python 官方网站

下载 Python 3.12.x。

安装的时候一定注意：

勾选 Add Python.exe to PATH

然后安装。

## 五、检查 Python 是否安装成功

打开：
```
Windows Terminal
```
或者：

**PowerShell**

输入：
```
python --version
```
如果看到：
```
Python 3.12.x
```
说明成功。

然后输入：
```
pip --version
```
如果出现类似：
```
pip 24.x.x from ...
```
也说明成功。

## 六、第三项任务：认识 Conda

作为普通Python开发者，直接使用Python也可以。

但是你以后会安装：

- PyTorch
- CUDA
- NumPy
- SciPy
- OpenCV
- FEniCS
- 各种AI库

不同项目可能需要不同版本。

所以我们必须从第一天开始养成：
```
每个项目使用独立环境
```
的习惯。

我推荐：

**Miniconda**

而不是完整版Anaconda。

官网：

[Miniconda 官方文档](https://docs.anaconda.com/miniconda/?utm_source=chatgpt.com)

安装以后打开：
```
Anaconda Prompt
```
输入：
```
conda --version
```
如果正常输出版本号：
```
conda 25.x.x
```
就可以。

## 七、建立你的第一个Python环境

我们现在创建：
```
omai-dev
```
这个名字很重要。

OMAI就是我们之前规划的：
```
OpenMechanicalAI
```
以后这个环境可以作为你的基础开发环境。

输入：
```
conda create -n omai-dev python=3.12
```
系统询问：
```
Proceed ([y]/n)?
```
输入：
```
y
```
然后激活：
```
conda activate omai-dev
```
如果成功，你的命令行前面会出现：
```
(omai-dev)
```
这意味着：

你现在进入了 OMAI 开发环境。

## 八、第四项任务：让VS Code认识这个环境

打开 VS Code。

安装扩展：
**Python**
搜索：
```
Python
```
发布者：

**Microsoft**

安装。

然后：

`Ctrl + Shift + P`

输入：
```
Python: Select Interpreter
```
选择：
```
omai-dev
```
这样：
```
VS Code
    ↓
Python
    ↓
Conda
    ↓
omai-dev
```
就连起来了。

这一步非常重要。

## 九、今天写第一段代码

现在创建一个文件夹：
```
OpenMechanicalAI
```
建议放在：
```
D:\OpenMechanicalAI
```
或者：
```
C:\Users\你的用户名\Documents\OpenMechanicalAI
```
都可以。

然后用 VS Code 打开这个文件夹。

创建：
```
hello.py
```
输入：
```
print("Hello, OpenMechanicalAI!")
```
运行。

如果终端出现：
```
Hello, OpenMechanicalAI!
```
恭喜。

你的AI工业软件开发之路正式开始。

## 十、但是我们马上把它改成一个“机械工程程序”

因为我不希望你学Python的时候感觉：

“这跟我的机械工程有什么关系？”

所以马上做一个小练习。

创建：
```
shaft_speed.py
```
写：
```
motor_speed = 3000
gear_ratio = 3.0


output_speed = motor_speed / gear_ratio


print("输入转速：", motor_speed, "rpm")
print("传动比：", gear_ratio)
print("输出转速：", output_speed, "rpm")
```
运行。

你应该看到：
```
输入转速： 3000 rpm
传动比： 3.0
输出转速： 1000.0 rpm
```
这就是我们的第一个：

**Mechanical Engineering Python Program**

## 十一、再做一个更有意义的练习

现在修改程序：
```
motor_speed = 3000
gear_ratio = 3.0
efficiency = 0.95


output_speed = motor_speed / gear_ratio


print("输入转速：", motor_speed, "rpm")
print("传动比：", gear_ratio)
print("效率：", efficiency)
print("输出转速：", output_speed, "rpm")
```
然后思考：

如果我们希望用户可以自己输入：
```
输入转速：
传动比：
效率：
```
应该怎么办？

你现在先不要问AI。

自己搜索Python的：
```
input()
```
然后尝试修改。

这是今天第一个重要训练。

## 十二、第五项任务：安装Git

Git官网：

[Git 官方网站](https://git-scm.com/?utm_source=chatgpt.com)

安装。

然后打开Terminal：
```
git --version
```
如果出现：
```
git version 2.x.x
```
就成功。

## 十三、理解Git到底是什么

这一点你一定要理解。

假设你的项目：
```
AI工业软件
```
经过一年开发。

代码变成：
```
10000行
```
某一天：

**你改了500行。**

结果程序崩了。

怎么办？

如果没有Git：

😭

如果有Git：
```
Version 1
    ↓
Version 2
    ↓
Version 3
    ↓
Version 4
```
你可以：

**回到昨天。**

所以Git本质上是：

**代码的版本控制系统。**

## 十四、GitHub又是什么？

这是很多初学者最容易混淆的地方。

简单理解：
```
Git
↓
你电脑上的版本管理工具


GitHub
↓
放在互联网上的代码仓库和协作平台
```
可以类比：
```
Git = 本地实验记录

GitHub = 全球公开实验室
```
以后你的项目：
```
OpenMechanicalAI
```
不仅是你自己的代码。

全世界的人都可以：

- 看
- 下载
- 提Issue
- 提Pull Request
- Fork
- 改代码
- 和你合作

这就是为什么：

**GitHub能力非常重要。**

## 十五、注册GitHub

官网：

[G]itHub 官方网站](https://github.com/?utm_source=chatgpt.com)

注册账号。

用户名尽量专业。

例如：
```
yourname
yourname-ai
yourname-mech
```
以后这个账号就是你的：

**国际技术名片。**

不要随便起一个娱乐化用户名。

## 十六、创建你的第一个Repository

进入GitHub。

点击：

**New repository**

Repository名称：
```
OpenMechanicalAI
```
Description：
```
My journey from mechanical engineering to AI industrial software.
```
选择：
```
Public
```
勾选：
```
Add a README file
（如果本地库里有就不要勾选，以免造成冲突）
```
然后：
```
Create repository
```
## 十七、今天第一次使用Git

进入你的本地：
```
OpenMechanicalAI
```
打开Terminal。

输入：
```
git init
```
然后：
```
git status
```
你会看到Git开始管理这个文件夹。

添加：
```
git add .
```
然后：
```
git commit -m "Initial commit"
```
## 十八、把代码上传GitHub
首先关联本地库与github库：
```
(直接参考新建GitHub库后页面显示的代码)
```
如果你已经把本地仓库与GitHub仓库关联好，可以直接使用：
```
git push
```
如果还没有关联，GitHub会给你对应的Repository地址和命令。

你今天只需要理解这条链：
```
修改代码
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
```
这条命令链，未来三年你会使用成千上万次。

## 十九、今天不要追求“学会”

今天最重要的不是记住命令。

而是形成一个习惯：

所有学习成果都进入GitHub。

以后你的学习路径应该是：
```
学习
 ↓
写代码
 ↓
解决工程问题
 ↓
Git commit
 ↓
GitHub
```
而不是：
```
看视频
 ↓
看视频
 ↓
看视频
 ↓
忘记
```

## 二十、今天的第一个真正小项目

今天最后完成：
```
Mechanical Calculator v0.1
```
创建：
```
mechanical_calculator.py
```
实现至少三个功能：

① 转速计算
```
输入转速
输入传动比
输出转速
```
② 扭矩计算

给定：
```
功率 P
转速 n
```
计算：
```
T = 9550P/n
```
③ 线速度

给定：
```
转速 n
直径 d
```
计算：
```
v = πdn/60
```
这里你已经可以开始体会：

**Python其实就是把你熟悉的机械工程公式变成软件**。

这会成为你以后进入AI工业软件最重要的思维方式。

## 二十一、今天的最终成果

今天结束时，你的电脑应该有：
```
OpenMechanicalAI
│
├── hello.py
│
├── shaft_speed.py
│
└── mechanical_calculator.py
```
GitHub上：
```
python-mechanical-learning
```
并且至少有：
```
Initial commit
```
## 二十二、今天不要学这些

今天明确禁止自己去学：

❌ ChatGPT API

❌ Transformer

❌ CNN

❌ PyTorch

❌ Agent

❌ LangChain

❌ RAG

❌ CUDA

❌ 大模型训练

看到这些内容可以先放到：
```
Later
```
文件夹。

因为：

**你现在缺的不是AI知识，而是软件开发基础。**

## 二十三、第一天的“验收考试”

今天做完以后，不要告诉我：

“我看完了。”

而是告诉我下面这些结果。

**环境**
```
Python：成功/失败
Conda：成功/失败
VS Code：成功/失败
Git：成功/失败
GitHub：成功/失败
```
**程序**
```
hello.py：成功/失败
shaft_speed.py：成功/失败
mechanical_calculator.py：成功/失败
```
**Git**
```
git init：成功/失败
git add：成功/失败
git commit：成功/失败
git push：成功/失败
```

