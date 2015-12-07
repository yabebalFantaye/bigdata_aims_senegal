
# coding: utf-8

# In[105]:


import numpy as np
def ouse1_gusess(History=None):
    return 50
def ouse2_gusess(History=None):
    return np.random.randint(1,100)

for i in range (100):
    c1 = ouse1_gusess()  
    c2 = ouse2_gusess() 
    c3= ouse2_gusess()
    c4 =ouse2_gusess()
ca = [c1,c2,c3,c4]
print c1,c2,c3,c4,np.mean(ca)
ca.append(np.mean(ca))
val_max=ca
for i in range(4):
        if(ca[i]<ca[i+1]):
            val_max=ca[i+1]
        else:
            val_max=ca[i]
    
print 'le gagnant est:',ca[i-1]
ca=sorted(ca) 

print ca


# In[104]:




# In[100]:




# In[ ]:



