import numpy as np
import matplotlib.pyplot as plt

# 函数 f(x) ：x 为 1x2 的向量，x[0]=原来的x，x[1]=原来的z
def function_2(x):
    return x[0]**2 + x[1]**2

# 数值梯度
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    # 使用多维迭代器
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        
        # f(x+h)
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        # f(x-h)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        
        # 恢复原值
        x[idx] = tmp_val
        it.iternext()
    
    return grad

# 梯度下降
def gradient_descent(f, init_x, lr=0.1, step_num=100):
    x = init_x.copy()  # 避免修改原数组
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

# 初始化 x = [x, z]
""" init_x = np.array([-3.0, 4.0])
x_min = gradient_descent(function_2, init_x)
print(x_min) """
