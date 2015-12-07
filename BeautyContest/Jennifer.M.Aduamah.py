import numpy as np
import os
import sys



functions=['Jennifer_guess','Player1_guess']

def Jennifer_guess(History=None):
    return np.random.randint(1,100)

def Player1_guess(History=None):
    return np.random.randint(1,100)
    
for i in range(100):
	A1 = Jennifer_guess()
	A2 = Player1_guess()
	A12 = [A1, A2]
	A3 = np.mean(A12)
	print A1, "and",  A2, "the mean is", A3
	B = min(A12, key=lambda x:abs(x-A3))
	print "So", B, "is the winner!"
    
    
