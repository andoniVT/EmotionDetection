'''
Created on 07/12/2014

@author: andoni
'''
import glob
from Configuration.settings import unlabeledData , labeledData , unlabeledDocuments , labeledDataDocuments , labeledDataTitles
from Preprocesser.commentProcess import PreProcessor as PP
from Methods.vectorModel import VectorModel as VM
from some_test import K_Means as KM

def create_file(id,  fpath , comentario):
    source = fpath + "labeled_"+ str(id) + ".txt"
    file = open(source, 'a')
    file.write(comentario)
    file.write('\n')

class ClusterData(object):
    
    def __init__(self, dataSource , type_data, groups):
        self.__data = []
        self.__dataSource = dataSource
        self.__groups = groups
        self.__vectorized_data = []
        self.__type = type_data
        self.__titles = []
    
    def readData(self):
        file = open(self.__dataSource, 'r')
        for i in file:
            i = i.rstrip('\n')
            pre = PP(i)
            self.__data.append(pre.get_processed_document())
    
    def removeNonAscii(self , s): return "".join(i for i in s if ord(i)<128)
    
    def get_title_name(self , file):
        i = len(file)-1
        fin = i 
        while file[i] != '/':
            i-=1        
        ini = i+1
        fin-=3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        word = ''
        for k in range(ini , fin):
            word = word + file[k]
        word = word.replace('_', ' ')
        return word  
    
    def readMultipleData(self):        
        files = glob.glob(self.__dataSource)        
        for name in files:
            value = (name, self.get_title_name(name))
            self.__titles.append(value)
            f = open(name, 'r')
            words = ""
            for line in f.readlines():
                line = line.rstrip('\n')       
                words = words + line + " "
            pre = PP(words)
            words = pre.get_processed_document() 
            self.__data.append(words)
            f.close()        
    
    def vectorizeData(self):
        model = VM(self.__data)
        matrix = model.prepare_models()
        self.__vectorized_data = matrix[3]
    
    def manage(self):
        if self.__type:
            self.readData()
        else:
            self.readMultipleData()
        
        self.vectorizeData()
        
        groups = KM(self.__vectorized_data, self.__groups)
        predicted = groups.clusterizar()         
        if self.__type:            
            for i in range(len(predicted)):
                print self.__data[i]
                print predicted[i]
                create_file(predicted[i], labeledData ,self.__data[i])
            
        else:
            for i in range(len(predicted)):
                print self.__data[i]
                print predicted[i]
                create_file(predicted[i], labeledDataDocuments, self.__data[i])
                create_file(predicted[i], labeledDataTitles, self.__titles[i][1])
        
        

if __name__ == '__main__':
    
    #clus = ClusterData(unlabeledDocuments,False,4)
    clus = ClusterData(unlabeledData,True,4)
    clus.manage()