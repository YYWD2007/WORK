import matplotlib.pyplot as plt
import numpy as np

def relu(x):
    return np.maximum(0, x) #数组 x 中的每个元素，和 0 比较，取较大值。
x = np.arange(-5,5,0.1)
y = relu(x)
plt.plot(x,y)
plt.show()