'''
Created on 07/12/2014

@author: andoni
'''
from sklearn.cluster import KMeans

class K_Means(object):
    
    def __init__(self, data, k):
        self.__data = data 
        self.__k = k
    
    def clusterizar(self):
        k_means = KMeans(n_clusters=self.__k)
        k_means.fit(self.__data)
        y_pred = k_means.predict(self.__data)
        return y_pred 
