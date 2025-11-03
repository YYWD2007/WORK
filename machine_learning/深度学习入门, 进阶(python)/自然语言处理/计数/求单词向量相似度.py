from 计数 import *

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size)

c0 = C[word_to_id['you']]  #you的单词向量
c1 = C[word_to_id['i']]  #i的单词向量

print(most_similar('you', word_to_id, id_to_word, C, top=5))
print(cos_similarity(c0, c1))



