import numpy as np

class Affine:
    def __init__ (self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out
    
    def backward(self, dout):
        dx = np.dot(dout, self.W.T) 
        #计算损失对输入x的梯度，传给前一层
        self.dW = np.dot(self.x.T, dout)
        #计算损失对权重 W 的梯度。
        self.db = np.sum(dout, axis=0)

        return dx
    
    


