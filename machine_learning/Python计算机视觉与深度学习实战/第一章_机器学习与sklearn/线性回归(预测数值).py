from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from 随机房屋信息_California import data # type: ignore
D = fetch_california_housing()
print(D.keys())
#dict_keys(['data', 'target', 'frame', 'target_names', 'feature_names', 'DESCR'])
print(D["feature_names"])
#['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
print(D["target_names"])
#['MedHouseVal'] 房子价值（美元）， target是房价
clf = LinearRegression()
x = D['data'] 
y = D['target']
print(D["data"][:20]) #房子的数据
clf.fit(x,y)
data_2 = np.array(data)
y_pred =clf.predict(data_2)   #训练模型之后，预测一些随机数据
plt.figure(figsize=(10,5))
plt.plot(y_pred, color = 'g')
plt.show()

y_pred =clf.predict(x[:20])  
plt.figure(figsize=(10,5))
plt.plot(y_pred, linestyle = '--', color = 'g')  #根据每个房子数据预测的价格
plt.plot(y[:20], color = 'r')                    #数据库里的真实价格
plt.show()

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
y_pred = clf.predict(x)
print("MSE", mean_squared_error(y_pred,y))
print("MAE", mean_absolute_error(y_pred,y))
print("r2_score", r2_score(y_pred,y))



