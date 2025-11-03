import numpy as np
from 损失函数 import cross_entropy_error
from 函数调用.softmax import softmax
from numerical_gradient.numerical_gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        
        return loss

net = simpleNet()
x = np.array([0.6,0.9])
z = net.predict(x)
t = np.array([0, 0, 1])

def f(loss):
    return net.loss(x, t)

grad = numerical_gradient(f, net.W)
print(grad)




