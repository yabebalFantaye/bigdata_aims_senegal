
#
#-------------------------------------------
import numpy as np
import os
import sys


functions=['my_guess_constant','my_guess_random']

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(1,100)

#------ code ends here -----


