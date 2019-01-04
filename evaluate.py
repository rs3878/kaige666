import numpy as np


def get_score(y, predicted):
    N = 5
    W = np.zeros((N,N))
    O = np.zeros((N,N))
    E = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            W[i,j] = (np.square(i-j)) / (np.square(N-1))
    for i in range(len(y)):
        O[y[i],predicted[i]] += 1
        E[y[i],y[i]] +=1
    total = np.sum(E)
    EE = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            EE[i,j] = E[i,i]/total*E[j,j]
    result = 1-np.sum(W*O)/np.sum(W*EE)
    return result
