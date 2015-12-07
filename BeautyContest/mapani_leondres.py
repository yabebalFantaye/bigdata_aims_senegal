import numpy as np
import os
import sys
def mapani(History=None):
    return(50)
def leondres(History=None):
    return np.random.randint(1,100)
for i in range(100):
    x1=mapani()
    x2=leondres()
    x=[x1,x2]
    print x1, x2, np.mean(x)
Y=np.min(np.abs(x-np.mean(x)))
print 'winner =', Y
