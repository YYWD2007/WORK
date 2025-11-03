import numpy as np
from collections import OrderedDict
from 误差反向传播法.ReLU import Relu
from 误差反向传播法.affine import Affine
from 误差反向传播法.SoftmaxWithLoss import SoftmaxWithLoss
from gradient2 import gradient

class TwoLayerNet:
  
    def __init__(self, input_size, hidden_size, output_size):
        """input_size:输入层的神经元个数(特征数)
        hidden_size:隐藏层的神经元个数
        output_size:输出层的神经元个数(分类任务中就是类别数)
        weight_init_std=0.01:权重初始化的标准差，
        默认为 0.01(意味着随机初始化权重时是一个很小的值，防止初始输出过大)"""
        self.params = {}
        self.params["W1"] = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.params["b2"] = np.zeros(output_size)
        
        """Sigmoid / Tanh → Xavier 初始化   ... * np.sqrt(1.0 / n_in)
           ReLU / LeakyReLU → He 初始化   ... * np.sqrt(2.0 / n_in)"""  

        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x
            
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y,t)
    
    def accuracy(self, x, t):
        y = self.predict(x)

        y = np.argmax(y, axis=1)
        if t.ndim != 1: t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
    
    def grad(self, x, t):
        return gradient(self, x, t)








        


    



        



        

