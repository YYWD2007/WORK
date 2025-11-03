#非门
import numpy as np

def NAND(x_1, x_2):
    x = np.array([x_1, x_2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

#接收x_1 和 x_2 数值
print("输入'q'结束运行")
while True:
    x_1 = input("x_1: ")
    if x_1 == "q":
        break
    x_1 = int(x_1)
    x_2 = input("x_2: ")
    if x_2 == "q":
        break
    x_2 = int(x_2)
    y = NAND(x_1, x_2)
    print(y)


#或门
import numpy as np

def OR(x_1, x_2):
    x = np.array([x_1, x_2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

#接收x_1 和 x_2 数值
print("输入'q'结束运行")
while True:
    x_1 = input("x_1: ")
    if x_1 == "q":
        break
    x_1 = int(x_1)
    x_2 = input("x_2: ")
    if x_2 == "q":
        break
    x_2 = int(x_2)
    z = OR(x_1, x_2)
    print(z)

