import numpy as np
class Network:
    def __init__(self):
        self.params = self.network()

    def network(self):
        network = {}
        network["W1"] = np.array([[0.1,0.3,0.5],[0.2, 0.4, 0.6]])
        network["b1"] = np.array([0.1,0.2,0.3])
        network["W2"] = np.array([[0.1, 0.4],[0.2,0.5],[0.3,0.6]])
        network["b2"] = np.array([0.1,0.2])
        network["W3"] = np.array([[0.1,0.3],[0.2,0.4]])
        network["b3"] = np.array([0.1,0.2])
        return network

    def sigmoid(A):
        return 1 / (1 + np.exp(-A))
    
    def identity_function(x):  #恒等函数(回归问题)
        return x
    
    def forward(self, x):
        W1,W2,W3 = self.params["W1"], self.params["W2"],self.params["W3"]
        b1,b2,b3 = self.params["b1"],self.params["b2"],self.params["b3"]
        A1 = np.dot(x, W1) + b1
        z1 = Network.sigmoid(A1)
        A2 = np.dot(z1, W2) + b2
        z2 = Network.sigmoid(A2)
        A3 = np.dot(z2, W3) + b3
        y = Network.identity_function(A3)
        return y
    
x = np.array([1,0.5])
net = Network()
y = net.forward(x)
print(y)



