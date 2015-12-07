# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:28:49 2015

@author: siriman
"""

import numpy as np
import pandas as pd

def mon_strategie(historique=list):
    rep="oui"
    while rep=="oui":
        n=input('donne la liste des valeurs jouees')
        list.append(n)
        
        l=pd.DataFrame(np.array(list))
        rep=input('voulez vous continuer o/n')
        for i in l.keys():
            d=np.std(l[i])
    return d 
def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(1,100)

