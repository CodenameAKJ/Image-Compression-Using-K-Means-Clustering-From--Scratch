#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.cluster import KMeans


# In[ ]:


def kmeans(X,K,max_iters):
    model = KMeans(n_clusters = K, max_iter = max_iters,n_init = 'auto',verbose = 0)
    model.fit(X)
    return model.cluster_centers_,model.predict(X)


# In[23]:


#This is a fn that iteratively run above two functions

def run_kMeans(X,K = 16,max_iters=10):
    
    m, n, c = X.shape
    og_image_n = X/255
    red_img = np.reshape(og_image_n,(m*n,c))   

    centroids,idx = kmeans(red_img,K,max_iters)
    
    idx = idx.astype(int)
    rec_img = centroids[idx, : ]
    rec_img = np.reshape(rec_img,X.shape)

    return rec_img

