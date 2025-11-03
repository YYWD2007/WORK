#与门实现
def AND(x_1,x_2):
    w_1, w_2, theta = 0.5, 0.5, 0.7
    temp = x_1*w_1 + x_2*w_2
    if temp <= theta:
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



