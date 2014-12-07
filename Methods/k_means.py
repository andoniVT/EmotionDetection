'''
Created on 03/12/2014

@author: Jorge Andoni Valverde Tohalino
@email:  andoni.valverde@ucsp.edu.pe
'''
from random import randint , uniform
from math import pow , sqrt
from scikits.learn.cluster.tests.test_affinity_propagation import n_clusters

def llenar_entrada(size , dimensiones):
    entrada = []
    for i in range(size):
        vector = []
        for j in range(dimensiones):
            #val = randint(1,100)
            val = uniform(0.0 , 1.0)
            vector.append(val)
        entrada.append(vector)
    return entrada

class K_Means(object):
    
    def __init__(self, data , k):
        self.__data = data
        self.__k = k
    
    def distancia(self , vector1 , vector2):
        if len(vector1) == 1: 
            return abs(vector1[0] - vector2[0])
        else:
            sumatoria = 0
            for i in range(len(vector1)):
                sumatoria = sumatoria + pow(vector1[i] - vector2[i] , 2)
            return sqrt(sumatoria)
        
    def distancias_menores(self,matrix):
        size = len(matrix[0])
        k = len(matrix)
        dist_menores = []
        clases = []
        for i in range(size):
            dist_menores.append(1000000)
            clases.append(0)
        for i in range(k):
            for j in range(size):
                if matrix[i][j] < dist_menores[j]:
                    dist_menores[j] = matrix[i][j]
                    clases[j] = i + 1
        return [clases , dist_menores]

    def generar_nuevo_centro(self ,matrix , n_clases , dimensiones):
        clases = []
        sumatorias = []
        tamanios = []
        for i in range(n_clases):
            sumas = []
            for j in range(dimensiones):
                sumas.append(0)
            sumatorias.append(sumas)
            tamanios.append(0)
            clases.append(i+1)
        centros = []    
        for i in range(n_clases):
            for j in range(len(matrix)):
                if matrix[j][1] == clases[i]:
                    tamanios[i]+=1
                    for k in range(dimensiones):
                        sumatorias[i][k] = sumatorias[i][k] + matrix[j][0][k]
            pares = []
            for j in range(len(sumatorias[i])):
                if tamanios[i]!=0:
                    value = sumatorias[i][j] / float(tamanios[i])
                else: 
                    value = 0
                pares.append(value)
            centros.append(pares)
        return centros
    
    def hallar_error(self,centros1 , centros2):
        dist = []
        for i in range(len(centros1)):
            val = self.distancia(centros1[i] , centros2[i])
            dist.append(val)    
        sumatoria = 0
        for i in dist:
            sumatoria = sumatoria + i
        return sumatoria/float(len(dist))
    
    def clusterizar(self):
        size = len(self.__data)
        dimension = len(self.__data[0])
        centros = llenar_entrada(self.__k, dimension)
        distancias = []
        error = 1000000
        agrupados = []
        resultado_final = []
        while error>0.01:
            for j in range(self.__k):
                vec_dis = []
                for l in range(size):
                    dist = self.distancia(centros[j], self.__data[l])
                    vec_dis.append(dist)
                distancias.append(vec_dis)
            clasificando = self.distancias_menores(distancias)
            etiquetas = clasificando[0]
            for j in range(size):
                value = [self.__data[j] , etiquetas[j]]
                agrupados.append(value)
            resultado_final = agrupados
            
            anterior = centros
            centros = self.generar_nuevo_centro(agrupados, self.__k, dimension)
            error = self.hallar_error(anterior, centros)
            agrupados = []
            distancias = []
            print "error: " + str(error)
            print "\n"
        return resultado_final 

    
if __name__ == '__main__':    
    
    entrada = llenar_entrada(20, 6)
    for i in entrada:
        print i 
    print "\n \n"
    
    '''
    kmeans = K_Means(entrada, 4)
    resultado = kmeans.clusterizar()    
    for i in resultado:
        print i
    '''
    
        
