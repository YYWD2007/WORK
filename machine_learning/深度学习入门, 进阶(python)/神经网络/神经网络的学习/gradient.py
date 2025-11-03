import numpy as np
from 函数调用.sigmoid import sigmoid
from 函数调用.softmax import softmax
from sigmoid_grad import sigmoid_grad

def s_g(x):
    return sigmoid_grad(x)

def gradient(self, x, t):
    # 前向传播
    W1, W2 = self.params['W1'], self.params['W2']
    b1, b2 = self.params['b1'], self.params['b2']
    
    # ----- forward -----
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)                      # 隐藏层激活
    a2 = np.dot(z1, W2) + b2
    y = softmax(a2)                       # 输出层

    # ----- backward -----
    grads = {}
    
    # 输出层误差
    batch_size = x.shape[0]
    dy = (y - t) / batch_size

    # W2, b2 梯度
    grads['W2'] = np.dot(z1.T, dy)
    grads['b2'] = np.sum(dy, axis=0)

    # 反传到隐藏层
    dz1 = np.dot(dy, W2.T)
    da1 = s_g(a1) * dz1

    # W1, b1 梯度
    grads['W1'] = np.dot(x.T, da1)
    grads['b1'] = np.sum(da1, axis=0)

    return grads