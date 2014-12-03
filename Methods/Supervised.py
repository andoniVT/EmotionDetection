'''
Created on 03/12/2014

@author: andoni
'''

class NaiveBayes(object):
    
    def __init__(self, data, labels):
        self.__data = data 
        self.__labels = labels
        self.__number_of_classes = len(set(self.__labels))
        print self.__number_of_classes

if __name__ == '__main__':
    
    data = [[1,2,3] , [4,5,6], [7,8,9], [9,8,7] , [5,3,1]]
    labels = [1, 3 , 0 ,1 ,2]
    
    nb = NaiveBayes(data,labels)


