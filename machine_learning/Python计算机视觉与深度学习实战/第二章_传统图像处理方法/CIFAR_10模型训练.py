from skimage.feature import hog
from CIFAR_10数据加载 import Cifar
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from tqdm import tqdm
from sklearn.model_selection import GridSearchCV

class RFClassifier:
    def __init__(self):
        self.data = Cifar()
        self.train_x, self.train_y,self.test_x,self.test_y = (
            self.data.load_cifar10()
        )
        #建立模型
        self.clf = RandomForestClassifier(
            n_estimators=800, min_samples_leaf=5, verbose=True, n_jobs=-1
        ) #森林里树的数量...
        print("loading train data")
        self.train_hog = []
        for img in tqdm(self.train_x):
            self.train_hog.append(self.extract_feature(img))
        print("loading test data")
        self.test_hog = []
        for img in tqdm(self.test_x):
            self.test_hog.append(self.extract_feature(img))
    
    #提取hog特征
    def extract_feature(self, img):
        hog_feat = hog(
            img,
            orientations=9,
            pixels_per_cell=[3,3],
            cells_per_block=[2,3],
            feature_vector=True,
        )
        return hog_feat
    
    #训练模型
    def fit(self):
        self.clf.fit(self.train_hog, self.train_y)
    
    #验证模型
    def evaluate(self):
        train_pred = self.clf.predict(self.test_hog)
        
    



