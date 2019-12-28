import random
import numpy as np
import pickle
import math

def sigmoid(input_num):
    return 1 / (1 + math.exp(-input_num))

class AI():

    aiwin = 0

    def __init__(self,n,outputlayers):

        # i define the verables used
        self.outputlayers = outputlayers # the number of outputs
        self.n = n # this is the size of the grid
        self.result = np.array([0 for y in range(self.outputlayers)],dtype='float32')
        self.resultfinal = np.array([0 for y in range(self.outputlayers)],dtype='float32')
        # theses are the neurons and weights
        self.neuron1 = np.array([0 for y in range(self.n)],dtype='float32')
        #self.neuron1 = [0 for x in range(self.n)]
        self.neuron2 = np.array([0 for y in range(self.n)],dtype='float32')
        self.neuron3 = np.array([0 for y in range(self.n)],dtype='float32')
        self.weight1 = np.array([random.uniform(1,-1) for x in range(self.n*self.n)],dtype='float32').reshape(self.n, self.n)
        self.weight2 = np.array([random.uniform(1,-1) for x in range(self.n*self.n)],dtype='float32').reshape(self.n, self.n)
        self.weight3 = np.array([random.uniform(1,-1) for x in range(self.outputlayers*self.n)],dtype='float32').reshape(self.outputlayers, self.n)


    def evaluate(self, input1):

        # importing the list from the program
        for i in range(len(input1)):
            self.neuron1[i] = sigmoid(input1[i])

        # the first dense layer of the neural net
        for i in range(self.n):
            for j in range(self.n):
                #print(i,j)
                self.neuron2[i] += self.neuron1[j] * self.weight1[i][j]
            self.neuron2[i] = sigmoid(self.neuron2[i])

        # a second dense layer of the neural net this is unused
        for i in range(self.n):
            for j in range(self.n):
                #print(i,j)
                self.neuron3[i] += self.neuron2[j] * self.weight2[i][j]
            self.neuron3[i] = sigmoid(self.neuron3[i])

        # a last not dense layer of the neural network
        for i in range(self.outputlayers):
            for j in range(self.n):
                #print(i,j,self.weight3[i][j])
                self.result[i] += self.neuron3[j] * self.weight3[i][j]
            self.result[i] = sigmoid(self.result[i])

        # this just resets the results verable while still returning a value
        # there is a better way of do ing this
        self.resultfinal = self.result
        self.result = np.array([0 for y in range(self.outputlayers)],dtype='float32')
        self.neuron1 = np.array([0 for y in range(self.n)],dtype='float32')
        self.neuron2 = np.array([0 for y in range(self.n)],dtype='float32')
        self.neuron3 = np.array([0 for y in range(self.n)],dtype='float32')

        return self.resultfinal


    def train(self,distance):
        # all this dose is randomises the weights nothing special
        # the name train is a bit miss leading

        for i in range(len(self.weight1)):

            for j in range(len(self.weight1[i])):
                self.weight1[i][j] += random.uniform(-distance,distance)

        for i in range(len(self.weight2)):

            for j in range(len(self.weight2[i])):
                self.weight2[i][j] += random.uniform(-distance,distance)

        for i in range(len(self.weight3)):
            for j in range(len(self.weight3[i])):
                self.weight3[i][j] += random.uniform(-distance,distance)


    def exportAI(self):
        # exports the weights to a txt file
        pickle.dump(self.weight1, open('weight1.p', 'wb'))
        pickle.dump(self.weight2, open('weight2.p', 'wb'))
        pickle.dump(self.weight3, open('weight3.p', 'wb'))

    def importAI(self):
        # imports the weights form a txt file
        self.weight1 = pickle.load(open('weight1.p', 'rb'))
        self.weight2 = pickle.load(open('weight2.p', 'rb'))
        self.weight3 = pickle.load(open('weight3.p', 'rb'))
