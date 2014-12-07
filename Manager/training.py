'''
Created on 07/12/2014

@author: andoni
'''
import glob
from Methods.Supervised import NaiveBayes as NB
from Configuration.settings import trainComments , trainDocuments
 

class Training(object):
    
    def __init__(self, source):
        self.__source = source
        self.__data = []
        self.__all_data = []
        self.__labels = []
    
    def loadData(self):
        files = glob.glob(self.__source)
        for name in files:
            f = open(name, 'r')
            vector = []
            for line in f.readlines():
                line = line.rstrip('\n')
                vector.append(line)
            self.__data.append(vector)
            f.close()
    
    def label_data(self):
        id = 1
        for i in self.__data:             
            for j in i:
                data = j.split()
                data = list(set(data))
                self.__all_data.append(data)
                label = "group_" + str(id)
                self.__labels.append(label)
            id+=1
            
    def train_data(self):        
        nb = NB(self.__all_data, self.__labels)        
        nb.train()
        
        test_comm = 'ciencia de la computacion esta relacionada con algoritmos arboles binarios base de datos y estructuras de datos'
        test_data = [test_comm]
        
        labels = nb.classify(test_data)
        print labels
        
                        

if __name__ == '__main__':
    
    prueba = Training(trainDocuments)
    prueba.loadData()
    prueba.label_data()
    prueba.train_data()