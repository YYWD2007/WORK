import sys
sys.path.append("/home/yywd/work/machine_learning/深度学习入门(1,2), 进阶(基于python)/自然语言处理/dataset/")
sys.path.append("/home/yywd/work/machine_learning/深度学习入门(1,2), 进阶(基于python)/自然语言处理/计数/")
from 计数 import *
import ptb 
import numpy as np

window_size = 2
wordvec_size = 100

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
print('counting co-occurrence ...')
C = create_co_matrix(corpus, vocab_size, window_size)
print('calculating PPMI ...')
W = ppmi(C, verbose=True)

print('calculating SVD ...')
try:
    from sklearn.utils.extmath import randomized_svd
    U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5,
                             random_state=None)
except ImportError:
    U, S, V = np.linalg.svd(W)

word_vecs = U[:, :wordvec_size]

querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)
