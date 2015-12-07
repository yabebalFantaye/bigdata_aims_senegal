import numpy as np
import os
import sys

#This strategy uses the average of the history guesses

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(40, 60)

def myFinal_guess(History=None):
    #guess=[]
    if History!= None:
        sum_guess=np.sum(np.array([History]))
        n=np.shape(np.array([History]))
        tot=len(n)
        my_guess=sum_guess/tot
    else:
        my_guess=my_guess_random()
        
    return "MY GUESS is" , my_guess


