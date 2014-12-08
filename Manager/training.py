'''
Created on 07/12/2014

@author: andoni
'''
import glob
from Methods.Supervised import NaiveBayes as NB
from Configuration.settings import trainComments , trainDocuments
from Preprocesser.commentProcess import PreProcessor as PP 

class Manager(object):
    
    def __init__(self, source=""):
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
        id = 0
        for i in self.__data:             
            for j in i:
                data = j.split()
                data = list(set(data))
                self.__all_data.append(data)
                label = "group_" + str(id)
                self.__labels.append(label)
            id+=1
            
    def train_data(self):
        self.loadData()
        self.label_data()        
        nb = NB(self.__all_data, self.__labels)        
        nb.train()
    
    def classify_data(self, querys):                
        procesed_test = []
        for i in querys:
            pre = PP(i)
            i = pre.get_processed_document()
            procesed_test.append(i)
                    
        nb = NB()
        labels = nb.classify(procesed_test)
        print labels
        
if __name__ == '__main__':
    
    #prueba = Manager(trainDocuments)    
    #prueba.train_data()
    
    test_comm = 'diego armando maradona es el mejor futbolista de todos los tiempos'
    test_comm2 = 'el peru es un gran pais'
    test_comm3 = 'musica'
    
    test_data = [test_comm, test_comm2, test_comm3]
    
    
    
    test = Manager()
    test.classify_data(test_data)
    