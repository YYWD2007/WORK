from sklearn.datasets import load_iris
D = load_iris()
print(D.keys()) 
#dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
x = D['data']
y = D['target']
print(D["target_names"])
#['setosa' 'versicolor' 'virginica']
print(D["feature_names"])
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

from sklearn.linear_model import LogisticRegression
import numpy as np
clf = LogisticRegression()
clf.fit(x,y)     #用x 和 y 训练模型
sepal_length_cm = float(input("sepal length (cm): "))
sepal_width_cm = float(input('sepal width (cm): '))
petal_length_cm = float(input('petal length (cm): '))
petal_width_cm = float(input('petal width (cm): '))
data = np.array([sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm])
y_pred = clf.predict([data])       #根据输入的特征数据 x，让模型预测属于哪个类别(target)
target_name = D.target_names[y_pred[0]]
print("预测这个鸢尾花的种类为：", target_name)
#列子：
#Setosa：[5.1, 3.5, 1.4, 0.2]
#Versicolor：[6.0, 2.2, 4.0, 1.0]
#Virginica：[6.5, 3.0, 5.2, 2.0]

y_pred = clf.predict(x)  #分类所有的data
accuracy = sum(y_pred == y) / len(y)  #正确的样本数量/ ...
print(accuracy)

from sklearn.metrics import classification_report
report = classification_report(y, y_pred, target_names=["setosa", "versicolor", "virginica"] )
print(report)





from sklearn.metrics import confusion_matrix  #混淆矩阵（测量精准度）
import matplotlib.pyplot as plt
c = confusion_matrix(y_pred, y)               #设定x, y 轴
xlocations = [0,1,2]
ylocations = xlocations
labels = D['target_names']
plt.xticks(xlocations, labels)
plt.yticks(ylocations, labels)
plt.ylabel("True label")
plt.xlabel("Predict label")
plt.imshow(c)
plt.show()





