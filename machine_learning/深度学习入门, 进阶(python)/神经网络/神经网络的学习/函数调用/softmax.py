import numpy as np

def softmax(a):
    c = np.max(a, axis=-1, keepdims=True)  # 批量安全
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a, axis=-1, keepdims=True)
    y = exp_a / sum_exp_a
    return y
