import numpy as np

x = np.array([1.0,2.0,3.0])   #生成数组（array:排列）
print(x)
print(type(x)) #<class 'numpy.ndarray'>



y = np.array([2.0, 4.0, 6.0])   #numpy 运算， 数组运算
print(x + y)
print(x - y)  
print(x * y)
print(x / y)
print(y / 2)



A = np.array([[1 , 2],[3, 4]]) #生成矩阵
print(A)
print(A.shape)   #矩阵形状（2，2）
print(A.dtype)   #矩阵元素的数据类型
B = np.array([[3, 0],[0, 6]])
print(A * B)     #矩阵运算
print(A * 10)
C = np.array([10, 20])
print(C)
print(A * C)  #广播




Z = np.array([[3, 0],[0, 6]])
print(Z[0])  #访问第0行
print(Z[0,1]) #0行第一个元素：0
for row in Z: #访问每一行
    print(row)

Z = Z.flatten()   #把矩阵变成数组（flatten:变平，击倒）
print(Z)
print(Z[0],Z[2])
print(Z[np.array([0,2])]) #访问第一个和第三个元素（数组）
print( Z > 2) #检索比2大的元素(True or False)
print(Z[Z>2]) #检索比2大的元素





import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.plot(x,y_1, label="sin")
plt.plot(x,y_2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()




from matplotlib.image import imread
img = imread('photo.png')
plt.imshow(img)

plt.show()














