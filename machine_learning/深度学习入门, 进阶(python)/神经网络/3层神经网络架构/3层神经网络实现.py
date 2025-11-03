import numpy as np

x = np.array([1,0.5])
w1 = np.array([[0.1,0.3,0.5],[0.2, 0.4, 0.6]])
b1 = np.array([0.1,0.2,0.3])

A1 = np.dot(x, w1) + b1
print(A1)

def sigmoid(A):
    return 1 / (1 + np.exp(-A))
z1 = sigmoid(A1)
print(z1)


w2 = np.array([[0.1, 0.4],[0.2,0.5],[0.3,0.6]])
b2 = np.array([0.1,0.2])
A2 = np.dot(z1, w2) + b2
print(A2)
z2 = sigmoid(A2)
print(z2)

def identity_function(x):
    return x
w3 = np.array([[0.1,0.3],[0.2,0.4]])
b3 = np.array([0.1,0.2])
A3 = np.dot(z2, w3) + b3
y = identity_function(A3)
print(y)


