import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x = np.array([-1, 1, 2])
y = sigmoid(x)
print(y)

x_2 = np.arange(-5, 5, 0.1)
y = sigmoid(x_2)
plt.plot(x_2, y)
plt.show()
