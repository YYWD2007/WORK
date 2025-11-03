from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
data = load_iris()
x = data["data"]
y = data["target"]
lda = LDA(n_components=2)
x_2d = lda.fit_transform(x,y)
markers = ["x", "s","^","h","*","<"]   
colors = ["r","g","b","y","o","tomato"]
plt.figure()
ax = plt.gca()
for i,item in enumerate(x_2d):
    ax.scatter(item[0],item[1],marker=markers[y[i]],color=colors[y[i]])
plt.show()

lda = LDA(n_components=1)
x_1d = lda.fit_transform(x,y)
markers = ["x", "s","^","h","*","<"]   
colors = ["r","g","b","y","o","tomato"]
plt.figure()
ax = plt.gca()
for i,item in enumerate(x_1d):
    ax.scatter(item[0],0,marker=markers[y[i]],color=colors[y[i]])
plt.show()
