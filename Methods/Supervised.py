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
        
    comentario1 = ['feliz' , 'alegria' , 'dicha', 'perfecto', 'bueno']
    comentario2 = ['triste', 'rencor', 'odio' , 'coraje']
    comentario3 = ['odio' , 'ira' , 'rencor']
    comentario4 = ['genial', 'feliz' , 'chevere']
    comentario5 = ['bueno' , 'bien' , 'bello' , 'excelente']
    
    data = [comentario1, comentario2, comentario3, comentario4, comentario5]
    labels = ['Feliz' , 'Enojado' , 'Enojado', 'Feliz' , 'Feliz']
    
    nb = NaiveBayes(data,labels)


