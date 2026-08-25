# 关于函数的使用问题
- 函数的定义和使用方法
- 定义、使用在不同文件夹的情况（例如两个并列的文件夹）

## 函数的定义和使用
### 在同一个.py文件内
```
/ 定义
def add(a,b):
    return a+b

/ 使用
c=add(1,2) / 前面定义，后面直接使用，无需任何添加
```

### 在不同.py文件，但在同一个文件夹
```
/ 定义：./file_a.py
def add(a,b):
    return a+b

/ 使用：./file_b.py
from file_a import add
c=add(1,2)
print(c)
```

### 在不同.py文件，不同文件夹
这种情况下，如果还利用上述第二种方法可能会报错，因为file_a可能在file_b的上一级目录或平行目录下，无法使用.去索引到  
此时，推荐使用包的方法去调用，即将file_a作为一个包安装到当前的python环境，这样就可以直接在file_b中使用 `from 项目名 import add`去引用函数  
**具体操作方法步骤**
1. 更改文件夹结构
   例如函数文件mechanical_calculator.py原本在项目OPENMECHANICALAI的src文件夹下，此时要更改为在`src.openmechanical`目录下，我们把openmechanicalai做成一个包
2. openmechanicalai包的制作
   在openmechanicalai目录下新建__init__.py，内容填写为：
    >from .mechanical_calculator import (calculate_output_speed, calculate_output_torque, calculate_linear_speed,)  
    >\_\_all\_\_ = ["calculate_output_speed","calculate_output_torque","calculate_linear_speed",]

3. 建立pyproject.toml
   在项目OPENMECHANICALAI根目录下新建pyproject.toml，内容填写：

    > [build-system]  
    > requires = ["setuptools>=61"]  
    > build-backend = "setuptools.build_meta"  

    > [project]  
    > name = "openmechanicalai"  
    > version = "0.1.0"  
    > description = "Mechanical engineering calculation tools based on Python"  
    > requires-python = ">=3.10"  

    > [tool.setuptools.packages.find]  
    > where = ["src"]  

4. 在vscode终端中安装包  
   ① 如果项目有自己的conda环境，如omai-dev，先在终端中激活该环境：`conda activate omai-dev`。**因为项目的python环境跟终端的可能不一样**  
   ② 将终端的目录切换到项目根目录，如`cd E:\OpenMechanicalAI`   
   ③ 安装包：`python -m pip install -e .`  
5. 使用函数
   此时，可以直接在任意目录中的py文件内使用`from openmechanicalai import calculate_output_speed`这样的方式调用函数
