import matplotlib.pyplot as plt
from sklearn.datasets import make_moons,make_blobs
from sklearn.cluster import KMeans,DBSCAN
data = make_blobs(centers = 2)
data_2 = make_moons()
x = data[0]   #制作图形-所有点的位置（numpy矩阵）(150,2)
x_2 = data_2[0]
model_km = KMeans(n_clusters=2)
model_db = DBSCAN(eps=0.3) 
y_pred_km = model_km.fit_predict(x)
y_pred_db = model_db.fit_predict(x_2)
markers = ["x", "s","^","h","*","<"]
colors = ["r","g","b","y","o","tomato"]
#plt.subplot(121) - 同一个窗口中画多个图的函数， 121代表1行2列的第1个图
plt.title('KMeans')
for i,y in enumerate(y_pred_km): #i代表是第几个点，y代表是哪个类别（kMeans）
    plt.scatter(x[i,0], x[i,1],marker=markers[y], color = colors[y])  
    #marker=markers[y]：根据 y（聚类的类别标签），选择不同的点的形状
    #x[i,0], x[i,1]代表第i个点的x轴和y轴
plt.show()


plt.title("DBSCAN")
for i,y in enumerate(y_pred_db):
    plt.scatter(x_2[i,0],x_2[i,1],marker=markers[y],color=colors[y])
plt.show()




