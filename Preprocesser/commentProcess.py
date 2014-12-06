#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 05/12/2014

@author: andoni
'''
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import re
import unicodedata
from unicodedata import normalize
import snowballstemmer
import string
from Configuration.settings import stopword
from Preprocesser.split import separar 
stopWordFile = stopword

class PreProcessor(object):
    
    def __init__(self , comment):
        self.__comment = comment
        self.__new_comment = self.process_comment(self.__comment)        

    def removeNonAscii(self , s): return "".join(i for i in s if ord(i)<128)
    
    def remove_accent(self , word):
        word= word.replace("á", "a")
        word= word.replace("é", "e")
        word= word.replace("í", "i") 
        word= word.replace("ó", "o")
        word= word.replace("ú", "u")
        word= word.replace("ä", "a")
        word= word.replace("ë", "e")
        word= word.replace("ï", "i")
        word= word.replace("ö", "o")
        word= word.replace("ü", "u")
        word= word.replace("Á", "a")
        word= word.replace("É", "e")
        word= word.replace("Í", "i") 
        word= word.replace("Ó", "o")
        word= word.replace("Ú", "u")
        return word 
    
    def find_symbol(self, word):
        alphabet = "abcdefghijklmnñopqrstuvwxyz"
        pos = 0
        flag = 0
        for i in word:
            if alphabet.find(i) != -1:
                pos = pos + 1
            else:
                flag = 1
                break
        return [flag , pos]
    
    def split_symbols(self,lista):
        new = []
        for i in lista:
            val = self.find_symbol(i)
            if val[0] == 0:
                new.append(i)
            else:
                pos = val[1]
                if pos == 0:
                    new.append(i)
                else:
                    param = len(i)-pos
                    uno = i[:pos]
                    dos = i[-param:]
                    new.append(uno)
                    new.append(dos)
        return new
    
    def lemmatizer(self ,word):
        stemmer = snowballstemmer.stemmer('spanish');
        return stemmer.stemWord(word)

    def lemmatized_comment(self , comment):
        lista = comment.split()
        lista = self.split_symbols(lista)
        lematizado = ""
        for i in lista:
            i = self.lemmatizer(i)
            lematizado = lematizado + i + " "
        lematizado = lematizado[:-1]
        return lematizado

    def lemmatized_words(self, comentario):
        lista = comentario.split()
        lematizado = ""
        for i in lista:
            i = self.lemmatizer(i)
            lematizado = lematizado + i + " "
        lematizado = lematizado[:-1]    
        return lematizado
    
    def remove_stop_word(self, comentario):    
        arch = open(stopWordFile , 'r')
        stops = []
        for line in arch:
            word = line.strip()
            stops.append(word)
        text_list = []
        words = re.split("\s+",comentario)        
        for word in words:
            if len(word)>1 and (not word in stops):
                text_list.append(word)
        return " ".join(text_list)
    
    def processHashTag(self ,text):
        words = text.split()
        new = ""
        for i in words:
            if i.find('#') != -1:
                i = re.sub(r'#([^\s]+)', r'\1', i)
                i = separar(i)
                new = new + i + " "
            else:
                new = new + i + " "
        return new 
            
    def process_comment(self , comentario):
        comentario = self.removeNonAscii(comentario)
        comentario = comentario.strip('RT')
        comentario = self.remove_accent(comentario)
        comentario = comentario.lower()
        comentario = self.processHashTag(comentario)
        comentario = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',comentario) 
        comentario = re.sub('@[^\s]+','',comentario) 
        comentario = re.sub('[\s]+', ' ', comentario)
        comentario = comentario.strip('\'"')
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        comentario = pattern.sub(r"\1\1", comentario)
        comentario = self.remove_stop_word(comentario)
        comentario = self.lemmatized_comment(comentario)        
        return comentario 
    
    def get_processed_document(self):
        return self.__new_comment

if __name__ == '__main__':
        
    asking = "@MarianoRajoy:  Las elecciones tienen que ser un grito esperanzado contra la corrupcion http://t.co/RvxFbBfU via @ #elcambioandaluz"    
    procesor = PreProcessor(asking)
    print procesor.get_processed_document()
    