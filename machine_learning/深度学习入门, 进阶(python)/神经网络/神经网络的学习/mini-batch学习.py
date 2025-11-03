import numpy as np
from TwoLayerNet import TwoLayerNet
from mnist.mnist import load_mnist
import matplotlib.pyplot as plt
from optimizers.optimizers import SGD, Adam, Momentum, AdaGrad

def shuffle_dataset(x, t):
    """打乱数据集"""
    permutation = np.random.permutation(x.shape[0])
    return x[permutation], t[permutation]

#抽取十个训练数字
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=True)

"""x_train, t_train = shuffle_dataset(x_train, t_train)

validation_rate = 0.2
validation_num = int(x_train.shape[0] * validation_rate)

x_val = x_train[:validation_num]
t_val = t_train[:validation_num]
#剩下的数据（去掉验证集的部分）作为新的训练集。
x_train = x_train[validation_num:]
t_train = t_train[validation_num:]"""

train_size = x_train.shape[0]  #x_train.shape = [60000, 784]
batch_size = 100 #超参数最优化实现，贝叶斯
lr = 0.1
networks = {}
iter_per_epoch = max(train_size / batch_size, 1)

#print(t_batch.shape): (100, 10)
#print(x_batch.shape): (100, 784)

optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()

for key in optimizers:
    networks[key] = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

train_loss_list, test_loss_list = {}, {}
train_acc_list, test_acc_list = {}, {}

for key in optimizers.keys():
    train_loss_list[key] = []
    test_loss_list[key] = []
    train_acc_list[key] = []
    test_acc_list[key] = []

for i in range(8000):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask] 
    t_batch = t_train[batch_mask]

    for key in optimizers.keys():
        grad = networks[key].grad(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grad)

    if i % iter_per_epoch == 0: #%：取余运算
        for key in optimizers.keys():
            train_acc = networks[key].accuracy(x_train, t_train)
            test_acc = networks[key].accuracy(x_test, t_test)
            train_acc_list[key].append(train_acc)
            test_acc_list[key].append(test_acc)
            loss_2 = networks[key].loss(x_test, t_test)
            test_loss_list[key].append(loss_2)
            loss = networks[key].loss(x_batch, t_batch)
            train_loss_list[key].append(loss)



markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D"}

# 训练 loss
for key in optimizers.keys():
    plt.plot(range(len(train_loss_list[key])), train_loss_list[key], 
             marker=markers[key], markevery=5, label=key)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.legend()
plt.show()

# 测试 loss
for key in optimizers.keys():
    plt.plot(range(len(test_loss_list[key])), test_loss_list[key], 
             marker=markers[key], markevery=5, label=key)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Testing Loss")
plt.legend()
plt.show()

# 训练 & 测试准确率
for key in optimizers.keys():
    plt.plot(range(len(test_acc_list[key])), test_acc_list[key], label=f"{key} Test Acc")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()


