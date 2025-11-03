import numpy as np
class Dropout:
    def __init__(self, dropout_ratio=0.5):
        self.dropout_ratio = dropout_ratio
        self.mask = None
        """dropout_ratio：随机“丢弃”的神经元比例，默认是 0.5，也就是一半神经元会被屏蔽。
        mask：保存当前 batch 的“屏蔽矩阵”，用来记录哪些神经元被丢弃。"""

    def forward(self, x, train_flg=True):
        if train_flg:
            self.mask = np.random.rand(*x.shape) > self.dropout_ratio
            return x * self.mask
        else:
            return x * (1 - self.dropout_ratio)
    """训练模式 (train_flg=True)

    np.random.rand(*x.shape) 会生成一个与 x 形状相同、元素在 [0,1) 之间的随机矩阵。
    self.dropout_ratio：把大于 dropout_ratio 的位置标记为 True（保留神经元），小于等于的为 False（丢弃神经元）。
    比如 dropout_ratio=0.5，那么大约一半的神经元会被置为 0。
    x * self.mask：丢弃神经元（对应 mask=False → 0），保留下来的神经元原样输出。

    推理模式 (train_flg=False)

    不再随机丢弃，而是对所有神经元按比例缩放：x * (1 - dropout_ratio)。"""
        
    def backward(self, dout):
        return dout * self.mask
    #只有保留下来的神经元才会更新参数。