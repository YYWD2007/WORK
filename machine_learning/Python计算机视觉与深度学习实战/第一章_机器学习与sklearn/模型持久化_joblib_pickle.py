import joblib
from sklearn.linear_model import LinearRegression
import numpy as np
x =[[0,0],[1,1]]
y = [0,1]
clf = LinearRegression()
clf.fit(x,y)
joblib.dump(clf, "lr.m")                #将模型保存为文件 "lr.m"

clf = joblib.load("lr.m")               #从文件中加载模型
print(np.round(clf.predict(x), 10))     #使用加载后的模型进行预测



import pickle
z =[[0,0],[1,1]]
y = [0,1]
clf = LinearRegression()
clf.fit(x,y)
s = pickle.dumps(clf)               
f = open("lr.pkl","wb")
f.write(s)
f.close()
g = open("lr.pkl","rb")
s = g.read()
clf = pickle.loads(s)
print(np.round(clf.predict(z), 10)) 


