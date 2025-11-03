#与门（np）
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
temp = np.sum(w*x) + b
print(temp)
if temp <= 0:
    y = 0
    print(f"y = {y}")
else:
    y = 1
    print(f"y = {y}")



#与门实现(函数+numpy - final version)
def AND(x_1,x_2):
    w = np.array([0.5, 0.5])
    x = np.array([x_1, x_2])
    b = -0.7
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
    y = AND(x_1, x_2)
    print(y)

