import numpy as np
import matplotlib.pyplot as plt
import pickle
from PIL import Image

from CNN实现 import SimpleConvNet
from mnist.mnist import load_mnist
from optimizers.optimizers import Adam


# ========== 数据准备 ==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=False, one_hot_label=True)


# 为了加快训练，用子集
x_train, t_train = x_train[:60000], t_train[:60000]
x_test, t_test = x_test[:10000], t_test[:10000]



train_size = x_train.shape[0]
batch_size = 100
iter_per_epoch = max(train_size // batch_size, 1)

# ========== 初始化网络 ==========
networks = SimpleConvNet(input_dim=(1, 28, 28), hidden_size=100, output_size=10)
optimizer = Adam()

train_loss_list, test_loss_list = [], []
train_acc_list, test_acc_list = [], []


# ========== 训练或加载 ==========
try:
    # 尝试加载保存的模型参数
    with open("/home/yywd/work/machine_learning/深度学习入门(1,2), 进阶(基于python)/卷积神经网络/cnn_params.pkl", "rb") as f:
        networks.params = pickle.load(f)

    # 重新绑定各层权重
    networks.layers['Conv1'].W = networks.params['W1']
    networks.layers['Conv1'].b = networks.params['b1']
    networks.layers['Affine1'].W = networks.params['W2']
    networks.layers['Affine1'].b = networks.params['b2']
    networks.layers['Affine2'].W = networks.params['W3']
    networks.layers['Affine2'].b = networks.params['b3']

    print("已加载保存好的模型参数。")

except FileNotFoundError:
    # 如果没有保存的模型，就训练新的
    print("未找到保存的模型参数，开始训练...")
    for i in range(5000):  # 训练  次迭代
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        grad = networks.gradient(x_batch, t_batch)
        optimizer.update(networks.params, grad)

        if i % iter_per_epoch == 0:
            # 精度（随机抽样 100 张）
            idx = np.random.choice(train_size, 100, replace=False)
            train_acc = networks.accuracy(x_train[idx], t_train[idx])
            idx_test = np.random.choice(len(x_test), 100, replace=False)
            test_acc = networks.accuracy(x_test[idx_test], t_test[idx_test])

            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)

            train_loss_list.append(networks.loss(x_batch, t_batch))
            test_loss_list.append(networks.loss(x_test[idx_test], t_test[idx_test]))

            print(f"iter {i}: train_acc={train_acc:.3f}, test_acc={test_acc:.3f}")

    # 训练完成后保存参数
    with open("/home/yywd/work/machine_learning/深度学习入门(1,2), 进阶(基于python)/卷积神经网络/cnn_params.pkl", "wb") as f:
        pickle.dump(networks.params, f)
    print("训练完成，模型参数已保存到 cnn_params.pkl")


# ========== 绘制训练曲线 ==========
if len(train_loss_list) > 0:
    plt.plot(train_loss_list, label="train loss")
    plt.plot(test_loss_list, label="test loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig("loss_curve.png")
    plt.close()

    plt.plot(train_acc_list, label="train acc")
    plt.plot(test_acc_list, label="test acc")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig("acc_curve.png")
    plt.close()
    print("训练曲线已保存为 loss_curve.png 和 acc_curve.png")


# ========== 用外部图片预测 ==========
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# ================== 处理图片 ==================
import cv2
import numpy as np
from PIL import Image

def preprocess_image_rpg_style(img_path, flatten=False, normalize=True):
    """用 GrabCut 原理去背景，得到 MNIST 风格图片"""
    # 1️⃣ 读图
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2️⃣ 初始 mask
    mask = np.zeros(img.shape[:2], np.uint8)

    # 3️⃣ 定义背景/前景模型
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)

    # 4️⃣ 用整张图做 ROI，grabCut 自动分割
    rect = (1,1,img.shape[1]-2,img.shape[0]-2)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # 5️⃣ 前景 = 1 或 3，背景 = 0 或 2
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img_fg = gray * mask2  # 只保留前景

    # 6️⃣ 裁剪非零区域
    coords = cv2.findNonZero(img_fg)
    x,y,w,h = cv2.boundingRect(coords)
    img_fg = img_fg[y:y+h, x:x+w]

    # 7️⃣ 缩放 & 居中到 28x28
    img_pil = Image.fromarray(img_fg)
    img_pil.thumbnail((20,20), Image.Resampling.LANCZOS)
    canvas = Image.new('L', (28,28), 0)
    x_offset = (28 - img_pil.width) // 2
    y_offset = (28 - img_pil.height) // 2
    canvas.paste(img_pil, (x_offset, y_offset))

    img_arr = np.array(canvas, dtype=np.float32)

    # 8️⃣ 归一化
    if normalize:
        img_arr /= 255.0

    if flatten:
        return img_arr.reshape(1,784)
    else:
        return img_arr.reshape(1,1,28,28)


# ================== 预测函数 ==================
def predict_image(networks, img_path, flatten=False, normalize=True):
    """用训练好的网络预测外部图片"""
    x_input = preprocess_image_rpg_style(img_path, flatten, normalize)
    y = networks.predict(x_input)
    pred_label = np.argmax(y)

    # 显示处理后的图片
    plt.imshow(x_input[0,0] if not flatten else x_input[0].reshape(28,28), cmap='gray')
    plt.title(f"Predicted: {pred_label}")
    plt.axis('off')
    plt.show()

    return pred_label

# ================== 示例 ==================
result = predict_image(networks, "/home/yywd/work/machine_learning/深度学习入门(1,2), 进阶(基于python)/卷积神经网络/my_digit.png", flatten=False)
print("外部图片预测结果:", result)


