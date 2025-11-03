from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
data = load_iris()
x = data ['data']          #四个长度信息
y = data ['target']        # 0,1,2
pca = PCA(n_components=3)  #3d
x_3d = pca.fit_transform(x)#把四个数据降成三维 比如: 主成分1 = 0.8 * 长度 + 0.6 * 宽度
markers = ["x", "s","^","h","*","<"]   
colors = ["r","g","b","y","o","tomato"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i,item in enumerate(x_3d): #i：当前点的索引（第几个点)item：当前点的数据:x、y、z）
    ax.scatter(item[0], item[1],item[2],color = colors[y[i]],marker = markers[y[i]])
    #color = colors[y[i]]：就是根据这个点的类别，选择对应的颜色。
plt.show()



pca_2d = PCA(n_components=2)
x_2d = pca_2d.fit_transform(x)
plt.figure()
ax = plt.gca()  # gca意思是 Get Current Axes，(获取当前坐标轴)
for i,item in enumerate(x_2d): 
    ax.scatter(item[0], item[1],color = colors[y[i]],marker = markers[y[i]])
plt.show()



pca_1d = PCA(n_components=1)
x_1d = pca_1d.fit_transform(x)
plt.figure()
ax = plt.gca()  
for i,item in enumerate(x_1d):
    ax.scatter(item[0],0,color = colors[y[i]],marker = markers[y[i]])
plt.show()


