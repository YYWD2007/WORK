#创建两个矩阵：target:目标词的id，context:目标词左右的单词id
import numpy as np

def create_contexts_target(corpus, window_size=1):
    target = corpus[window_size:-window_size]
    contexts = []

    for idx in range(window_size, len(corpus)-window_size):
        cs = []
        for t in range(-window_size, window_size + 1):
            if t == 0:
                cs.append(corpus[idx + t])
            contexts.append(cs)

    return np.array(contexts), np.array(target)

