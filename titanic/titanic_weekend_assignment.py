
# coding: utf-8

# In[2]:

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import IPython


# #### First let us define the path to the training and test data sets. Just to be absolutely sure, we will check if the path is correct, that the file exists in the path we provided. This is done using the os.path.exists function.

# In[22]:

training_data_filepath='data/train.csv'
test_data_filepath='data/test.csv'
print 'The path to the training data set is correct: ', os.path.exists(training_data_filepath)
print 'The path to the test data set is correct: ', os.path.exists(training_data_filepath)


# #### Now that we know the files exist, let us first load the training data set to a pandas DataFrame. This DataFrame is just like a table, but with many powerful methods to make analysis on the table very easy. Read more about pandas DataFrame here http://pandas.pydata.org/pandas-docs/stable/dsintro.html

# In[23]:

df_training = pd.read_csv(training_data_filepath)


# In[24]:

df_training.info()


# #### From the above output we see that, the following features have at least one data missing
# * 'Age'
# * 'Cabin'
# * 'Embarked'
# * 'Name'
# * 'Sex'
# * 'Ticket'
# ##### Question: Why?
# 
# #### In principle we should try to fill these missing data through interpolation, mean or any other intelligent method. Bur for this excersise let us drop all  the above features with missing data.
# We use the pandas drop method to drop the columns, hence axis=1, from the training DataFrame. The resulting DataFrame would be a clean training data set.

# In[25]:

df_training_clean = df_training.drop(['Age','Cabin','Embarked','Name','Sex','Ticket','Fare'],axis=1)


# #### Our goal here is to train a machine to learn the relationship between different features about the titanic passangers  and their survival chance. Therefore out target is the column * 'Survived' *. We want to drop this column from our DataFrame assign 
# The pop method drops the Survived column from the data frame and assigns it to a variable target

# In[27]:

target = df_training_clean.pop('Survived') 


# In[28]:

df_training_clean.info()


# In[53]:

get_ipython().magic(u'matplotlib inline')
df_training_clean['Fare'].plot(kind='kde')


# #### Now let us train a decision tree algorithm using the training data and the corresponding target. We will use the scikit-learn (sklearn) python package. Scikit expects a pure numpy array so we should convert our training DataFrame to numpy array as follows.

# In[31]:

array_training_clean=df_training_clean.values
array_target=target.values
#the shape method tells us about the rank of the array
print 'The shape of training array is: ',array_training_clean.shape 
print 'The shape of the target array is: ',array_target.shape 


# #### Now the training part -  it takes only just three lines!!! 

# In[38]:

from sklearn import tree #import tree algorithm from scikit-learn
#Intitialize the DecisionTreeClassifier algorithm with optional parameters 
classifier = tree.DecisionTreeClassifier(min_samples_leaf=5, max_depth=4) 
#use the initialized tree to learn the relationship between 
#known passanger information, features, and know state of survival 
classifier.fit(array_training_clean, array_target)


# #### Let us see what the machine will predict 

# In[42]:

#The variable classifier in the above cell contains a tree which has a 
#knowledge of how passengers features are related to their survival.

#Just to have insight, let's see how our decision tree predicts 
print "First 5 training target"
print array_target[0:5]
print "Prediction on first 5 training Rows"
print classifier.predict(array_training_clean[0:5,:])

# We can see the score, the efficiency of the training as follows
print("Training Score: ", classifier.score(array_training_clean, array_target))
#Since our analysis is simple, we did not attempt to fill the missing data etc.  
#the score score is low, in principle with a proper data cleaning etc. 
# we could get the maximim training score of 1. 


# ## Weekend Assignment
# #### Your task it to do the following - just copy paste the python codes in between the lines and it should work. 
# 
# 1. load the test data into pandas DataFrame 
# 
#         df_test = pd.read_csv(test_data_filepath)
#               
# 2. Check the nature of the test data using the info() method as 
# 
#         df_test.info()    
#      
#      Here you will notice that there is missing data for the Fare column for one passenger. 
#      Since we need the same set of features in the training and test data sets, 
#      **we can NOT drop it**. We need therefore to fill it. i) Compute the mean 
#      Fare for different classes, and put them in a dictionary ii) get the rows whose
#      Fare is missing iii) fill the missing data according to the class the passanger is in 
# 
#         i) mean_fare_by_pclass = df_test[['Pclass','Fare']].groupby(['Pclass']).agg('mean')['Fare']
#     
#         ii) fare_given_pclass=df_test['Pclass'].apply(lambda x: mean_fare_by_pclass[x])
#     
#         iii) df_test['Fare'].fillna(fare_given_pclass,inplace=True)
#     
# 3. Similar to what we did for the training data, drop the columns 
#     ['Age','Cabin','Embarked','Name','Sex','Ticket'] as 
# 
#         df_test_clean = df_test.drop(['Age','Cabin','Embarked','Name','Sex','Ticket'],axis=1)
#                     
# 4. Convert the test DataFrame to numpy array 
# 
#         array_test_clean = df_test_clean.values
#                
# 5. Predict the survival of passengers using the tree we trained as
# 
#         survival_prediction = classifier.predict(array_test_clean)     
#           
# 6. Save the prediction to a file. If you want, you can submit this file in Kaggle page and get your score 
# 
#         with open('prediction.csv', 'w') as csvfile:    
#             for survived in survival_prediction:
#                  csvfile.write("{}\n".format(survived)) 
#     
# 7. **BONUS:** Visualize the result. Be creative :)

# In[ ]:

# df_test = pd.read_csv(test_data_filepath)
# mean_fare_by_pclass = df_test[['Pclass','Fare']].groupby(['Pclass']).agg('mean')['Fare']
# fare_given_pclass=df_test['Pclass'].apply(lambda x: mean_fare_by_pclass[x])
# df_test['Fare'].fillna(fare_given_pclass,inplace=True)
# df_test_clean = df_test.drop(['Age','Cabin','Embarked','Name','Sex','Ticket'],axis=1) 
# array_test_clean = df_test_clean.values
# survival_test = classifier.predict(array_test_clean)
# df_test.info()


# In[ ]:




# In[ ]:




# In[ ]:



