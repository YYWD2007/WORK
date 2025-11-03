from mnist import load_mnist
from PIL import Image  #Python图像显示
import numpy as np

def img_show(img):
    pil_image = Image.fromarray(np.uint8(img)) 
    #把 NumPy 数组转换成 PIL 图片对象
    pil_image.save("MNIST训练库第一个图片.png")
    pil_image.show()

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28,28)

img_show(img)



    

