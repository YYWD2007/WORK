import numpy as np
from mnist import load_mnist
import pickle


#假设学习已经完成，直接测试

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", "rb") as f: 

        """学习已经完成，权重等数据保存在这里
        rb=read binary,以二进制方式打开文件，适合读取非文本文件，
        比如保存的模型权重、图片、音频等。"""

        network = pickle.load(f)
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def predict(network, x):
    W1,W2,W3 = network["W1"], network["W2"], network["W3"]
    b1,b2,b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
print(len(x))      #10000张手写数字的图片
network = init_network()

accuracy = 0
预测结果 = []
for i in range(len(x)):          #逐一取出测试图像
    y = predict(network, x[i])   #定义函数实参，开始预测
    p = np.argmax(y)             #获得概率最高的元素索引
    预测结果.append(p)
    if p == t[i]:
        accuracy += 1
print(f"某张图片的预测结果: {预测结果[190]}")
print(f"这张的真实标签: {t[190]}")

print("总体准确率:" + str(float(accuracy) / len(x)))


accuracy = 0
批量处理 = 10000
for i in range(0, len(x), 批量处理):   #range[start,end,step] [0,10000]
    x = x[i : i+批量处理]               #取出从i到10000的所有数据
    y = predict(network, x)   
    p = np.argmax(y, axis = 1)   #axis = 1 代表从第一维度开始找(第一行)          
    accuracy += np.sum(p == t[i:i+批量处理])

print("总体准确率:" + str(float(accuracy) / len(x)))
