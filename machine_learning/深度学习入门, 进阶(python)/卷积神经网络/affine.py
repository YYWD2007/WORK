import numpy as np

class Affine:
    def __init__ (self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.original_x_shape = x.shape  # 记录原始形状
        N = x.shape[0]
        x = x.reshape(N, -1)             # 展平成 (N, D)

        self.x = x
        out = np.dot(self.x, self.W) + self.b
        return out

    
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        dx = dx.reshape(*self.original_x_shape)  # 还原成 (N, C, H, W)

        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx



