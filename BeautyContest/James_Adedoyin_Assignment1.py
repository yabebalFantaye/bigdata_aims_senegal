#Adedoyin James
#AIMS-Senegal
#Introduction to Big-Data Assignment 1
#6/12/2015

#.................................................................................

'''Program to guess a number between 0 and 100 such that the number you 
guessed is close to the mean of the guesses from everyone else'''


import numpy as np
import os
import sys

functions=['my_guess_constant','my_guess_random']

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(1,100)

for i in range (100):
    a = my_guess_constant()
    b = my_guess_random()
    a = (2 * a)/3    #2/3rd of the first guess
    b = (2 * b)/3    #2/3rd of the second guess
    c = [a, b]
    d = (2 * 100)/3  #the guess should be less than d
    print 'The guess must be less than', d

    #Calculating the mean of the guesses
    e = np.mean(c)
    print c, 'The mean of the guesses is:', e
    print "first guess: %s and the 2/3rds of the mean is: %s" % (a, 2 * a/3)
    print "second guess: %s and the 2/3rds of the mean is: %s" % (b, 2 * b/3)
    
    x = min(c, key=lambda x:abs(x-d))    #to check for the guess that is closest to d 
     
    print 'winner is:', x
