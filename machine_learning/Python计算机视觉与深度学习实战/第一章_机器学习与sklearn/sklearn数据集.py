from sklearn.datasets import load_iris  #数据导入
from sklearn.datasets import load_digits
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

d = load_iris()
print(d.keys())
print(d['feature_names'])    #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

g = load_digits()  #手写数字
plt.imshow(g['data'][0].reshape(8,8), cmap='gray')  #数字0
plt.show()


circle = make_circles()[0]  #此时 circle 是一个形状为 (100, 2) 的 NumPy 数组
plt.scatter(x= circle[:,0],y=circle[:,1]) #取出所有点的 x, y坐标
plt.show()
moons = make_moons()[0]
plt.scatter(x= moons[:,0], y=moons[:,1])
plt.show()



