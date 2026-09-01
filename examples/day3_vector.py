import numpy as np

speed=np.array([1000,1500,2000,2500,3000])
# speed=[1000,1500,2000,2500,3000]

print(speed)
print(type(speed))
print(speed.shape)

speed_rad=speed*np.pi/180
print(speed_rad)

# 数组的索引
print(speed[0])


# 切片
print(speed[1:4])

# 矩阵
A=np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)

# 矩阵运算
B=np.transpose(np.array([[7,8,9],[10,11,12]]))
C=A@B
print(C)

# 机械工程例子
K=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.array([1,2,3])
F=K@x
print('F=',F)

# numpy 的统计功能
print('mean:', np.mean(speed))
print('std:', np.std(speed))
print('min:', np.min(speed))
print('max:', np.max(speed))
print('sum:', np.sum(speed))
print('median:', np.median(speed))
