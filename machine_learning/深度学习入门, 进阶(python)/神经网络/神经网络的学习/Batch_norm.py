import numpy as np

class BatchNormalization:
    """
    http://arxiv.org/abs/1502.03167
    """
    def __init__(self, gamma, beta, momentum=0.9, running_mean=None, running_var=None):
        self.gamma = gamma
        self.beta = beta
        self.momentum = momentum
        self.input_shape = None  # Conv层为4维，全连接为2维  

        # 测试时使用的平均值和方差
        self.running_mean = running_mean
        self.running_var = running_var  

        # backward时使用的中间数据
        self.batch_size = None
        self.xc = None
        self.xn = None
        self.std = None
        self.dgamma = None
        self.dbeta = None

    def forward(self, x, train_flg=True):
        self.input_shape = x.shape
        if x.ndim != 2:
            N, C, H, W = x.shape
            x = x.reshape(N, -1)

        out = self.__forward(x, train_flg)
        return out.reshape(*self.input_shape)

    def __forward(self, x, train_flg):
        if self.running_mean is None:
            N, D = x.shape
            self.running_mean = np.zeros(D)
            self.running_var = np.zeros(D)

        if train_flg:
            mu = x.mean(axis=0)
            xc = x - mu
            var = np.mean(xc**2, axis=0)
            std = np.sqrt(var + 1e-7)
            xn = xc / std

            self.batch_size = x.shape[0]
            self.xc = xc
            self.xn = xn
            self.std = std
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mu
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var
        else:
            # 测试阶段也保存变量，保证 backward 不报错（用于调试）
            xc = x - self.running_mean
            std = np.sqrt(self.running_var + 1e-7)
            xn = xc / std

            self.batch_size = x.shape[0]
            self.xc = xc
            self.xn = xn
            self.std = std

        # 在 forward 里
        xn_safe = np.clip(self.xn, -1e2, 1e2)  # 限制 xn 范围 [-100, 100]
        out = self.gamma * xn_safe + self.beta

        return out


    def backward(self, dout):
        if dout.ndim != 2:
            N, C, H, W = dout.shape
            dout = dout.reshape(N, -1)

        dx = self.__backward(dout)

        dx = dx.reshape(*self.input_shape)
        return dx

    def __backward(self, dout):
        dbeta = dout.sum(axis=0)
        dgamma = np.sum(self.xn * dout, axis=0)

        dxn = self.gamma * dout
        dxc = dxn / (self.std + 1e-7)  # 防止除零

        dstd = -np.sum((dxn * self.xc) / (self.std**2 + 1e-7), axis=0)
        dvar = 0.5 * dstd / (self.std + 1e-7)

        # 防止 dxc += (2/N) * xc * dvar 溢出
        delta = (2.0 / self.batch_size) * self.xc * dvar
        delta = np.clip(delta, -1e5, 1e5)  # 限制增量
        dxc += delta

        dmu = np.sum(dxc, axis=0)
        dx = dxc - dmu / self.batch_size

        self.dgamma = dgamma
        self.dbeta = dbeta

        # 最终梯度裁剪，防止反向传播梯度爆炸
        dx = np.clip(dx, -1e5, 1e5)
        return dx
