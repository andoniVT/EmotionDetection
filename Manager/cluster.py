'''
Created on 06/12/2014

@author: Jorge Andoni Valverde Tohalino
@email:  andoni.valverde@ucsp.edu.pe
'''

from Configuration.settings import unlabeledData , labeledData
from Preprocesser.commentProcess import PreProcessor as PP
from Methods.vectorModel import VectorModel as VM
from Methods.k_means import K_Means as KM

def create_file(id, comentario):
    source = labeledData + "labeled_"+ str(id) + ".txt"
    file = open(source, 'a')
    file.write(comentario + '\n')

class ClusterData(object):
    
    def __init__(self, dataSource , groups):
        self.__dataSource = dataSource
        self.__data = []
        self.__groups = groups
        self.__vectorized_data = []
    
    def readData(self):
        file = open(self.__dataSource, 'r')
        for i in file:
            i = i.rstrip('\n')
            pre = PP(i)
            self.__data.append(pre.get_processed_document())
    
    def vectorizeData(self):
        model = VM(self.__data)
        matrix = model.prepare_models()
        self.__vectorized_data = matrix[3]
        
    def manage(self):
        self.readData()
        self.vectorizeData()
        groups = KM(self.__vectorized_data, self.__groups)
        grupos = groups.clusterizar()
        print "data sin clusterizar"
        for i in self.__vectorized_data:
            print i 
        print "data clusterizada"
        for i in range(len(grupos)):
            #print grupos[i][1]
            print grupos[i]
            print self.__data[i]
            create_file(grupos[i][1], self.__data[i])
                                            

if __name__ == '__main__':
    
    file = "prueba.txt"
    
    clus = ClusterData(unlabeledData,4)
    clus.manage()
    
     