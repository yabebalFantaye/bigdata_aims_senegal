import random  
import numpy as np
def hubert_gusess(History=None):
    return np.random.randint(45,55)
my_randoms=[]
m = n = 0
for i in range (100):    
    my_randoms.append(random.randrange(1,100))   
    c1 = hubert_gusess()
for i in range (100):
    m = m + random.randrange(1,100)
n = m/100
print 'my guess is ', c1, my_randoms,'the mean is',n
