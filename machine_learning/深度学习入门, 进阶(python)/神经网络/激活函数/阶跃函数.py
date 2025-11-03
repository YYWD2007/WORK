import numpy as np
x = np.array([-1, 1, 2]) #x为公式结果
y = x > 0
print(y)
y = np.array(x>0, dtype=int) #astype - 生成一个新数组
print(y)



import matplotlib.pyplot as plt
def step_function(x):
    return np.array(x>0, dtype=int)
x = np.arange(-5, 5, 0.1) #-5到5，以0.1为单位生成np数组
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #指定y轴范围
plt.show()






