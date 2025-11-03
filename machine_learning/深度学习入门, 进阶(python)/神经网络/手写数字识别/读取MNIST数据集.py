from mnist import load_mnist
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)

"""x_train：训练集的输入数据（图片），通常是多张图片的集合。
t_train：训练集对应的标签（数字类别）。
x_test：测试集的输入数据（图片）。
t_test：测试集对应的标签。

normalize=False
表示不对图像像素值做归一化。
MNIST 图片的像素是 0255 的整数，normalize=True 会把它们缩放到 01 之间，False 就保留原始数值。

flatten=True
表示把二维的图片（28x28）展开成一维向量（长度 784）。
方便送入全连接神经网络的输入层。
如果是 flatten=False，则保留图片的二维形状（28,28），一般用于卷积神经网络。"""




