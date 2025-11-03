import numpy as np

a = np.array([1010, 1000, 990])
c = np.max(a) #1010
y = np.exp(a-c) / sum(np.exp(a-c))

def softmax(a):
    if a.ndim == 2:
        c = np.max(a, axis=1, keepdims=True)
        exp_a = np.exp(a - c)
        return exp_a / np.sum(exp_a, axis=1, keepdims=True)
    else:
        c = np.max(a)
        exp_a = np.exp(a - c)
        return exp_a / np.sum(exp_a)
