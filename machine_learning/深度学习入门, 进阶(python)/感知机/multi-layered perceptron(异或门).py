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
        
def OR(x_1, x_2):   
    x = np.array([x_1, x_2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1
    
def AND(s_1,s_2):
    w = np.array([0.5, 0.5])
    x = np.array([s_1, s_2])
    b = -0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1
    
def XOR(x_1, x_2):
    s_1 = NAND(x_1, x_2)
    s_2 = OR(x_1, x_2) 
    y = AND(s_1, s_2) 
    return y 

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
    F = XOR(x_1, x_2)
    print(F)




