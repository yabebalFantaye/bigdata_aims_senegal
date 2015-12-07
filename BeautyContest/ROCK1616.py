import os
import sys
import numpy as np
from scipy import *
import pandas as pd

def jeu(n,k):
	C = 100
	history1 = {}
	for i in range(n):
		history1 [i] = list(np.random.randint(C+1, size = k))
	return history1


def funct(H, r):
    A = H.values()
    C = 100
    n = np.mean(np.mean(M,axis=1))
    k = len(M[0])
    P = []
    P = np.random.randint(C+1, size = k)
    P[r] = n
    m = np.mean(P)
    Q = []
    for i in range(len(P)):
        Q.append(np.abs(P[i] - m))
    H[len(A)+1] = list(P)
    return '#-------#', 'The average', m,' his number', P[Q.index(np.min(Q))] , 'the winner is', Q.index(np.min(Q))

