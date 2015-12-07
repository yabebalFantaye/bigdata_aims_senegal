
import os
import sys
import numpy as np
from scipy import *
#import pandas as pd

def generanint(n,k): # This function randomly generates a history of 'n' tricks with 'k' participants
	N = 100
	history1 = {} # definition of History empty
	for i in range(n):
		history1 [i] = list(np.random.randint(N+1, size = k)) # random generation history
	return history1


def fwin(H, r): # This function calculates the average of the general historical and considers this value as my choice
    M = H.values() # Historical values
    N = 100
    n = np.mean(np.mean(M,axis=1)) # General of the historical average
    k = len(M[0])
    P = []
    P = np.random.randint(N+1, size = k) # random selection of values ​​for the other players
    P[r] = n  		#Here, I make my choice which is the mean of the historical mean 
    H[len(M)+1] = P
    m = np.mean(P) # mean of Draw
    Q = []
    for i in range(len(P)):
        Q.append(np.abs(P[i] - m)) # Q contains the deviations between the selection of players and the average 'm'
    return H, 'The mean is', m, 'and the winner is the player number', Q.index(np.min(Q)),'with selected number as', P[Q.index(np.min(Q))], 'and', P[r], 'is your number choice'


if __name__ == '__main__':
    n = input('Enter the number of tours already cheeks : n = ')
    p = input('Enter the number of participants: p =')
    Hist = generanint(n,p)
    k = input('Enter your number or rank among participants : k =')
    if k > p :
        print ' Please enter a rank < ', p
    
    M = fwin(Hist, k)
    Hist = M[0]
    print M[1:11]
    
    print 'Do you still want to play ?'
    Res = input('O for Yes, Answer = ')
    
    while Res == 'O' :
        M = fwin(Hist, k)   
        Hist = M[0]
        print M[1:11] 
        print 'Do you still want to play?'
        print Hist 
        Res = input('O for Yes, Answer = ')
        
# For this exercise, I have another idea , which is that of finding a correlation between 
#the choice of the players and the stage of the game
#I intend to program this week. I would like you to help me implement that
