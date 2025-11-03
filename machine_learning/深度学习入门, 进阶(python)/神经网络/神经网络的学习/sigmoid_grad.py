import numpy as np

def sigmoid_grad(x):
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)