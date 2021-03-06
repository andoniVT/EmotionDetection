'''
Created on 05/12/2014

@author: Jorge Andoni Valverde Tohalino
@email:  andoni.valverde@ucsp.edu.pe
'''

path = "/home/andoni/Escritorio/PythonProjets/EmotionDetection"


stopword = path + '/Resource/stopwords_spanish.txt'
big_text = path + '/Resource/big2.txt'


unlabeledData = path + '/Data/train/unlabeledComments.txt'
unlabeledDocuments = path + '/Data/train/documents/*.txt'

labeledData = path + '/Data/train/labeled/'


labeledDataDocuments = path + '/Data/train/documentLabeled/documents/'
labeledDataTitles = path + '/Data/train/documentLabeled/titles/'


trainComments = path + '/Data/train/labeled/*.txt'
trainDocuments = path + '/Data/train/documentLabeled/documents/*.txt'


dataDocumentTrained = path + '/DataTrained'
sizeDataDT = dataDocumentTrained + '/size.pk1'
frequencyTableDT = dataDocumentTrained + '/frequencyTable.pk1'
probabilityTableDT = dataDocumentTrained + '/probabilityTable.pk1'
dictionaryDT = dataDocumentTrained + '/dictionary.pk1'
