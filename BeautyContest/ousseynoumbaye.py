# -*- coding: utf-8 -*-
#Assignment n°1 Big data
# Auteur: Oussenou mbaye

import numpy as np
def joueur1(History=None):
    return 50
def joueur2(History=None):
    return np.random.randint(1,100)

for i in range (100):
    c1 = joueur1()  
    c2 = joueur2() 
    c3 = joueur2()
    c4 = joueur2()
liste = [c1,c2,c3,c4]
m=np.mean(liste)
liste.append(m)
#print liste
liste.sort()
print liste
for i in range(1,4):
    if liste[i]==m:
        p=m-liste[i-1]
        q=liste[i+1]-m
        print  p,q
if p>q:
    print format(liste[i+1])
    print "est le numero gagnant"

elif p==q:
    print format(liste[i-1] , liste[i+1])
    print "sont les numeros gagnants"
else:
    print format(liste[i-1] )
    print"est le numero gagnant"

    
    
            
    
