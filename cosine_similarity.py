# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:51:05 2021

@author: User
"""

# Compute cosine similarity

def cos_similarity(M):
    
    # M should be an array (n by m matrix)
    
    dotM = np.dot(M, M.T) # covariance matrix
    normM = np.diag(dotM**0.5).reshape(dotM.shape[0],1) # extract variances
    normM = np.dot(normM,normM.T)
    cos_similar = np.multiply(dotM, normM**-1)
    
    return cos_similar
