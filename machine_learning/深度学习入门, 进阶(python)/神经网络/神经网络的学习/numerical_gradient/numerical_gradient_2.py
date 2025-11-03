#求损失函数的最小值
import numpy as np
import matplotlib.pyplot as plt

#导数公式
def numerical_diff(f,x):
    h = np.float32(10e-5)
    return (f(x + h) - f(x)) / h 

#函数f_1(x)
def function_1(x):
    return 0.01*x**2 + 0.1*x
 
#f_1(x)图像
x = np.arange(0,20,0.1)
y = function_1(x)
plt.plot(x,y)
plt.show()

#打印在x=5和x=10函数f_1的导数
print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

#函数f_2(x,z),这两个未知数可代表权重和偏置
def function_2(x,z):
    return x**2 + z**2  
x = np.arange(0,10,0.1)
z = np.arange(0,10,0.1)
X, Z = np.meshgrid(x, z)  #让坐标对应
y = function_2(X,Z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Z, y, cmap='viridis')
plt.show()

#算f_2的导数（梯度）
def numerical_gradient(f, x, z):
    h = 1e-4
    grad_x = 0
    grad_z = 0
    
    # x的梯度
    fxh1 = f(x + h, z)
    fxh2 = f(x - h, z)
    grad_x = (fxh1 - fxh2) / (2*h)
    
    # z的梯度
    fxh1 = f(x, z + h)
    fxh2 = f(x, z - h)
    grad_z = (fxh1 - fxh2) / (2*h)
    
    return grad_x, grad_z

print(numerical_gradient(function_2, 3, 4))

#梯度下降    
def gradient_descent(f, init_x, init_z, lr=0.1, step_num=100):
    x = init_x
    z = init_z
    for i in range(step_num):
        grad_x, grad_z= numerical_gradient(f,x,z)
        x -= lr * grad_x
        z -= lr * grad_z

    return x,z
    
init_x = -3
init_z = 4
print(gradient_descent(function_2, init_x, init_z) )








