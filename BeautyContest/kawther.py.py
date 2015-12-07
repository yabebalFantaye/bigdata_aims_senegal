
# coding: utf-8

# In[18]:

import numpy as np

def kawther_guess(History=None):
    return 90
def tayseer_guess(History=None):
    return np.random.randint(1,100)


# In[6]:




# In[19]:

for i in range(100):
    c1 = kawther_guess()
    c2 = tayseer_guess()
    ca = [c1,c2]
    print c1, c2, np.mean(ca)


# In[4]:




# In[ ]:



