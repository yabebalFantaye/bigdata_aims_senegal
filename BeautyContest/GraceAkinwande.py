import numpy as np
import os
import sys


#functions=['my_guess_constant','my_guess_random']

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(1,100)

for i in range(1,101):
    c1=my_guess_constant()
    c2=my_guess_random()
    
    cm=np.array([c1,c2])
    cm_diff=abs(cm-cm.mean())
    
    iwinner = cm_diff.argmin()+1
    
    if (cm_diff - cm_diff.mean()).any():
        print 'The winner is c'+str(iwinner)+'!'
        print 'c array',cm,'mean=',cm.mean()
    else:
        print 'A tie! guess array=',cm
        print 'mean=',cm.mean()
        
