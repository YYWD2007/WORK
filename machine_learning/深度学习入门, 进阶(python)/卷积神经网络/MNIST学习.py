import numpy as np
from CNN实现 import SimpleConvNet
from mnist.mnist import load_mnist
import matplotlib.pyplot as plt
from optimizers.optimizers import Adam

def shuffle_dataset(x, t):
    """打乱数据集"""
    permutation = np.random.permutation(x.shape[0])
    return x[permutation], t[permutation]

#抽取十个训练数字
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=False, one_hot_label=True)

"""x_train, t_train = shuffle_dataset(x_train, t_train)

validation_rate = 0.2
validation_num = int(x_train.shape[0] * validation_rate)

x_val = x_train[:validation_num]
t_val = t_train[:validation_num]
#剩下的数据（去掉验证集的部分）作为新的训练集。
x_train = x_train[validation_num:]
t_train = t_train[validation_num:]"""
x_train = x_train[:1000]
t_train = t_train[:1000]
x_test = x_test[:200]
t_test = t_test[:200]

train_size = x_train.shape[0]  #x_train.shape = [60000, 784]
batch_size = 100 #超参数最优化实现，贝叶斯
lr = 0.1
iter_per_epoch = max(train_size / batch_size, 1)

#print(t_batch.shape): (100, 10)
#print(x_batch.shape): (100, 784)

optimizer = Adam()

networks = SimpleConvNet(input_dim=(1,28,28), hidden_size=100, output_size=10)

train_loss_list, test_loss_list = {}, {}
train_acc_list, test_acc_list = {}, {}

train_loss_list = []
test_loss_list = []
train_acc_list = []
test_acc_list = []

for i in range(500):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask] 
    t_batch = t_train[batch_mask]

    grad = networks.gradient(x_batch, t_batch)
    optimizer.update(networks.params, grad)

    if i % iter_per_epoch == 0: #%：取余运算
        train_acc = networks.accuracy(x_train, t_train)
        test_acc = networks.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        loss_2 = networks.loss(x_test, t_test)
        test_loss_list.append(loss_2)
        loss = networks.loss(x_batch, t_batch)
        train_loss_list.append(loss)


# 训练 loss
plt.plot(range(len(train_loss_list)), train_loss_list)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()

# 测试 loss
plt.plot(range(len(test_loss_list)), test_loss_list)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Testing Loss")
plt.show()

# 训练 & 测试准确率
plt.plot(range(len(test_acc_list)), test_acc_list)
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()

