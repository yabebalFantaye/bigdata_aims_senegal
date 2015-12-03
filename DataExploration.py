
# coding: utf-8

# K-Means Clustering - Data Exploration
# ==========================================
# ***
# 
# ###UN Data on Countries of the World
# 
# We are going to explore or dataset which we get in a csv format but
# may have missing values.  We need to be able to drill down on useful
# dimensions to explore after cleaning up the data.  Since we only
# have one observation per country, we may not have the option to use
# columns where there are many missing values as we are effectively
# going to drop many countries when we drop rows with missing values.
# But then how did we drop such rows before? Because in those cases
# there were many observations per individual entity and dropping some
# did not eliminate an entity altogether.
# 
# So first we import the data and explore the columns and types - this
# time rather than doing it manually we are going to use the
# facilities in our software to do that.
# 

# In[5]:


import pandas as pd
df = pd.read_csv('UN.csv')
print('----')
# print the raw column information plus summary header
print(df)
print('----')
# look at the types of each column explicitly
print('Individual columns - Python data types')
[(x, type(df[x][0])) for x in df.columns] 


# Here we see that we have 14 columns with country and region being
# string types and the rest being floats.  We also see that the
# country column has 207 values, ie this is data on 207 countries.
# The region columns also has 207 entries, but the rest of the columns
# have many missing entries, indicated by number of non-null values
# less than 207.
# 
# We see that tfr, lifeMale, lifeFemale and GDP, and infantMortality
# are the columns closest to 207.  That is, if we use these columns we
# will only drop a few countries and not whole clusters as we might if
# we used educationMale and educationFemale.  On the other hand were
# we to use educationMale and educatonFemale we would have to drop
# almost 2/3 of the data. So we focus on the columns with non-null
# values close to 207.
# 
# So our short list is now, country, region, tfr, lifeMale, lifeFemale
# and GDP, and infantMortality.
# 
# We suspect that there is clustering of lifeMale, lifeFemale and
# infantMortality according to GDP and we are going to pull out the
# heavy machinery of K-Means sofwtare to analyse this in detail and
# look at the clusters.
# 
# We don't know in advance how many clusters there will be which is
# different from the iris example where we had a 'species' label and
# there were three unique species.
# 
# So while using our KMeans software we will also look at some
# analytical measures to decide what the right number of clusters
# might be after looking at multiple such possibilities from 1 through
# 10 candidate clusters.
# 
# Finally, to be able to apply the KMeans modeling software we convert
# each field in our file to a scientific float format that the
# numerical algorithms expect.
# 
# Onward!




