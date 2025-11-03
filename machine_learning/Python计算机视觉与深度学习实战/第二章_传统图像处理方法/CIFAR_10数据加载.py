#从本地硬盘上已下载并解压的 CIFAR-10 原始数据集（pickle 格式）里
#加载训练集和测试集图像数据与标签，然后把它们转换成方便后续处理的 NumPy 数组格式

import pickle
import os.path as osp
import numpy as np

cifar_folder = "C:\\Users\\YYWD2\\Desktop\\python_work\\Python计算机视觉与深度学习实战\\第二章_传统图像处理方法\\cifar-10-batches-py"

class Cifar:
    def __init__(self, folder=cifar_folder):
        self.folder = folder
        # 构建训练集数据文件路径，共 5 个训练批次文件
        self.files = [osp.join(self.folder, "data_batch_%d" % n) for n in range(1, 6)]

    # 读取单个 pickle 格式文件，解析出数据和标签
    def load_pickle(self, path):
        f = open(path, "rb")
        data_dict = pickle.load(f, encoding="bytes")
        X = data_dict[b"data"]
        Y = data_dict[b"labels"]
        # 将数据reshape并转换维度顺序，适配图像数据格式（通道在后）
        X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1)  
        Y = np.array(Y)
        return X, Y

    # 加载 CIFAR-10 数据集，包括训练集和测试集
    def load_cifar10(self):
        xs = []
        ys = []
        # 遍历训练集文件，读取数据并拼接
        for file in self.files:
            X, Y = self.load_pickle(file)
            xs.append(X)
            ys.append(Y)
        train_x = np.concatenate(xs)
        train_y = np.concatenate(ys)
        # 读取测试集文件
        test_x, test_y = self.load_pickle(osp.join(self.folder, "test_batch"))
        return train_x, train_y, test_x, test_y

if __name__ == "__main__":
    data = Cifar()
    train_x, train_y, test_x, test_y = data.load_cifar10()
    # 打印数据集各部分的形状，查看数据维度信息
    print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)





