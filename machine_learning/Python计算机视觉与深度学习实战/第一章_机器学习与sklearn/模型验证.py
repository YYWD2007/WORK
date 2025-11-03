from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
n_samples = 20
x = np.array([i+2 for i in range(n_samples)]) * 4
y = 3 * np.log(x) + np.random.randint(0,3,n_samples)
plt.scatter(x,y)
plt.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.3) #test_size是验证集占比

def poly_fit(degree):
    poly_reg = PolynomialFeatures(degree=degree)
    #用 PolynomialFeatures 变换后，模型就能学会 x² 的信息，从而学到非线性关系
    x_ploy_train = poly_reg.fit_transform(x_train.reshape(-1,1))
    #形状从 (20,) 变成 (20, 1)，这里的 20 不变，表示样本数量不变
    x_ploy_test = poly_reg.transform(x_test.reshape(-1,1))
    clf = LinearRegression()
    clf.fit(x_ploy_train,y_train.reshape(-1,1))
    plt.subplot(121)
    y_train_pred = clf.predict(x_ploy_train)
    sorted_indices = np.argsort(x_train)
    # 确保 x 的顺序是从小到大
    plt.plot(x_train[sorted_indices], y_train_pred[sorted_indices])
    plt.scatter(x_train, y_train)

    plt.subplot(122)
    y_test_pred = clf.predict(x_ploy_test)
    sorted_indices = np.argsort(x_test)
    plt.plot(x_test[sorted_indices], y_test_pred[sorted_indices])
    
    print("Train R2 score", r2_score(y_train_pred,y_train))
    print("Test R2 score", r2_score(y_test_pred,y_test))


poly_fit(degree=2)
plt.show()
#这个曲线 就是机器“学习”出来的结果，也可以理解为：模型学到的数学规律，用来描述 x 和 y 的关系。
#验证是否有过拟合现象




