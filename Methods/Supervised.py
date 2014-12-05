'''
Created on 03/12/2014

@author: andoni
'''

class NaiveBayes(object):
    
    def __init__(self, data, labels):
        self.__data = data 
        self.__labels = labels
        self.__number_of_elements = 0
        self.__number_of_classes = 0
        self.__clases = []
        self.__dictionary = []
        self.__features = []
        self.__features_and_values = []
        self.__frequency_table = []
        self.__probability_table = []

    def number_of_elements_per_class(self):
        counts = []
        for i in range(len(self.__clases)): counts.append(0)        
        for i in range(len(self.__clases)):
            for j in self.__labels:
                if self.__clases[i] == j: counts[i]+=1
        dictionary = []
        for i in range(len(counts)):
            value = (self.__clases[i] , counts[i])
            dictionary.append(value)
        return dictionary

    def get_features(self):
        elements = []
        for i in self.__data:
            elements = elements + i 
        return list(set(elements))

    def find_position(self, dictionary, word):
        for i in range(len(dictionary)):
            if dictionary[i][0] == word:
                return i 
        return -1

    def get_frequency_table(self):
        features_values = []
        for i in range(len(self.__features)):
            vec = []
            for j in range(self.__number_of_classes+1): vec.append(0)
            value = (self.__features[i] , vec)
            features_values.append(value)

        for i in range(len(self.__data)):
            label_position = self.find_position(self.__dictionary, self.__labels[i])
            for j in range(len(self.__data[i])):
                position = self.find_position(features_values, self.__data[i][j])
                features_values[position][1][label_position]+=1

        for i in features_values:
            the_sum = sum(i[1])
            i[1][len(i[1])-1] = the_sum

        return features_values

    def get_probability_table(self):
        features_values = []
        for i in range(len(self.__features)):
            vec = []
            for j in range(self.__number_of_classes): vec.append(0.01)
            value = (self.__features[i] , vec)
            features_values.append(value)

        for i in range(len(features_values)):
            for j in range(len(features_values[i][1])):
                if self.__frequency_table[i][1][j]!=0:
                    prob = self.__frequency_table[i][1][j]/float(self.__dictionary[j][1])
                    features_values[i][1][j] = round(prob,4)

        return features_values

    def train(self):
        self.__number_of_elements = len(self.__data)
        self.__number_of_classes = len(set(self.__labels))
        for i in set(self.__labels):
            self.__clases.append(i)
        self.__dictionary = self.number_of_elements_per_class()
        self.__features = self.get_features()
        
        self.__frequency_table = self.get_frequency_table()
        self.__probability_table = self.get_probability_table()
        
    def multiply(self, vector):
        prod = 1.0
        for i in vector: prod *=i
        return prod

    def greater(self, vector):
        value = 0
        best = 0.0
        for i in vector:
            if best < i[1]:
                best = i[1]
                value = i
        return value 

    def classify_comment(self , test):
        vec_indexes = []
        for i in test:
            index = self.find_position(self.__frequency_table, i)
            vec_indexes.append(index)

        prob_values = []

        for i in range(len(self.__dictionary)):
            #print "prob(" +  self.__dictionary[i][0] + "): "
            prob_class = self.__dictionary[i][1]/float(len(self.__data))           
            #print "prob class: " + str(prob_class)            
            num_values = []
            den_values = []
            for j in vec_indexes:
                if j!=-1:
                    value = self.__probability_table[j][1][i]
                    num_values.append(value) 
                    index = len(self.__frequency_table[j][1])-1
                    value2 = self.__frequency_table[j][1][index]
                    value2 = value2/float(len(self.__data)) 
                    den_values.append(value2)            

            num_value = self.multiply(num_values)
            den_value = self.multiply(den_values)
            prob = (prob_class*num_value)/den_value

            prob_value = (self.__dictionary[i][0] , prob)
            prob_values.append(prob_value)
            '''
            print "num: " + str(num_value)
            print "den: " + str(den_value)
            print "FINAL: " + str(prob) 
            '''
            #print " "

        print prob_values

        #print ""

        label = self.greater(prob_values)
        #print label
        return label[0]

    def classify(self, test_data):
        labels  = []
        for i in test_data:
            lista = i.split()
            label = self.classify_comment(lista)
            labels.append(label)
        return labels



if __name__ == '__main__':
        
    comentario1 = ['feliz'  , 'alegria' , 'dicha', 'perfecto', 'bueno']
    comentario2 = ['triste', 'rencor', 'odio' , 'coraje']
    comentario3 = ['odio' , 'ira' , 'rencor']
    comentario4 = ['genial', 'feliz' , 'chevere']
    comentario5 = ['bueno' , 'bien' , 'bello' , 'excelente']
    comentario6 = ['triste' , 'lagrimas' , '=(']
    
    data = [comentario1, comentario2, comentario3, comentario4, comentario5 , comentario6]
    labels = ['Feliz' , 'Enojado' , 'Enojado', 'Feliz' , 'Feliz' , 'Triste']
    
    nb = NaiveBayes(data,labels) 
    
    nb.train()

    test_comment = 'feliz bello bueno lala'
    test_comment2 = 'lagrimas odio =( rencor'

    test_data = [test_comment , test_comment2]
    #nb.classify(test_data)
    #nb.classify_comment(test_comment2.split())


    labels = nb.classify(test_data)
    print labels
