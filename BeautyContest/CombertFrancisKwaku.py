import numpy as np
import os
import sys



#functions=['my_guess_constant','my_guess_random','myFinal_guess']

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(45,55)

#My Guessing function= myFinal_guess 
def myFinal_guess(History=None):
    
    if History:
        sum_guess=np.sum(np.array([History]))
        n=np.shape(np.array([History]))
        tot=n[0]*n[1]
        my_guess=(sum_guess/tot)
    else:
        my_guess=my_guess_random()
        




    return "My guess number = "+str( my_guess)
             
        
