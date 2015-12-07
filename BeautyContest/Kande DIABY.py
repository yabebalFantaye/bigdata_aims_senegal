import numpy as np
import os
import sys
def my_guess_constant(History=None):
    return 50
def my_guess_random(History=None):
    return np.random.randint(1,100)
# i define a empty list 
a=[]
# i define the game function whith my strategi is to pick the last mean
def number_of_players(n):
    a.append(my_guess_constant(History=None))
    for j in range(n-2):
        a.append(my_guess_random(History=None))
    my_first_choice=100
    a.append(my_first_choice)
    y=0
    for j in a:
        y=y+j*j
    t=np.mean(a)
    b=[]
    b.append(my_guess_constant(History=None))
    for j in range(n-2):
        b.append(my_guess_random(History=None))
    my_choice=t
    b.append(my_choice)
    print b,np.mean(b)
