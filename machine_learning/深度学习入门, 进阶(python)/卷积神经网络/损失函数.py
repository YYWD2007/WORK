import numpy as np 
import matplotlib.pyplot as plt

def mean_squared_error(y, t):
    z = 0.5 * np.sum((y-t)**2)
    return z

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size) 
        #如果 y.shape = (10,) → y.shape[0] = 10（它会错误地当成 batch_size=10）
        y = y.reshape(1, y.size)
    
    #当多个数据时
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

