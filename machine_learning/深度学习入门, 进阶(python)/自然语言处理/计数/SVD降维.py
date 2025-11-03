import numpy as numpy
import matplotlib.pyplot as plt
from 计数 import *

text = "You say goodbye and I say hello."
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size)
W = ppmi(C)

# SVD
U, S, V = np.linalg.svd(W)

print(C[0])
print(W[0])
print(U[0])      # 密集向量
print(U[0, :2])  # 对这个密集向量降维，比如降到二维，取出前两个元素即可

#用二维向量表示各个单词，画图
for word, word_id in word_to_id.items():
    plt.annotate(word, (U[word_id, 0], U[word_id, 1]))

plt.scatter(U[:,0], U[:,1], alpha=0.5)
plt.show()




