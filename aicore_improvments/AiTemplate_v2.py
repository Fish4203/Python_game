import random
import numpy as np
import pickle
import math

def sigmoid(input_num):
    return 1 / (1 + math.exp(-input_num))

class AI():

    aiwin = 0

    def __init__(self,inputlayers,layers,outputlayers):

        # i define the verables used
        self.outputlayers = outputlayers # the number of outputs
        self.layers = layers # the size of the hiden layers
        self.inputlayers = inputlayers # this is the size of the input

        # result formating
        self.result = np.array([0 for y in range(self.outputlayers)],dtype='float32')
        self.resultfinal = np.array([0 for y in range(self.outputlayers)],dtype='float32')

        # neurons
        self.neuroninput = np.array([0 for y in range(self.inputlayers)],dtype='float32')
        self.neuron2 = np.array([0 for y in range(self.layers)],dtype='float32')
        self.neuron3 = np.array([0 for y in range(self.layers)],dtype='float32')

        # weights
        self.weightinput = np.array([random.uniform(1,-1) for x in range(self.inputlayers*self.layers)],dtype='float32').reshape(self.layers, self.inputlayers)
        self.weight2 = np.array([random.uniform(1,-1) for x in range(self.layers*self.layers)],dtype='float32').reshape(self.layers, self.layers)
        self.weightout = np.array([random.uniform(1,-1) for x in range(self.outputlayers*self.layers)],dtype='float32').reshape(self.outputlayers, self.layers)

        # bias's
        self.biasinput = np.array([random.uniform(5,-5) for y in range(self.layers)],dtype='float32')
        self.bias2 = np.array([random.uniform(5,-5) for y in range(self.layers)],dtype='float32')
        self.biasout = np.array([random.uniform(5,-5) for y in range(self.outputlayers)],dtype='float32')

    def evaluate(self, input1):

        # importing the list from the program
        for i in range(len(input1)):
            self.neuroninput[i] = sigmoid(input1[i])

        # the first dense layer of the neural net
        for i in range(len(self.weightinput)):
            for j in range(len(self.weightinput[i])):
                #print(i,j)
                self.neuron2[i] += self.neuroninput[j] * self.weightinput[i][j]
            self.neuron2[i] += self.biasinput[i]
            self.neuron2[i] = sigmoid(self.neuron2[i])

        # a second dense layer of the neural net this is unused
        for i in range(len(self.weight2)):
            for j in range(len(self.weight2[i])):
                #print(i,j)
                self.neuron3[i] += self.neuron2[j] * self.weight2[i][j]
            self.neuron3[i] += self.bias2[i]
            self.neuron3[i] = sigmoid(self.neuron3[i])

        # a last not dense layer of the neural network
        for i in range(len(self.weightout)):
            for j in range(len(self.weightout[i])):
                #print(i,j,self.weightout[i][j])
                self.result[i] += self.neuron3[j] * self.weightout[i][j]
            self.result[i] += self.biasout[i]
            self.result[i] = sigmoid(self.result[i])

        # this just resets the results verable while still returning a value
        # there is a better way of do ing this
        self.resultfinal = self.result
        self.result = np.array([0 for y in range(self.outputlayers)],dtype='float32')
        self.neuroninput = np.array([0 for y in range(self.inputlayers)],dtype='float32')
        self.neuron2 = np.array([0 for y in range(self.layers)],dtype='float32')
        self.neuron3 = np.array([0 for y in range(self.layers)],dtype='float32')

        return self.resultfinal


    def train(self,distance):
        # all this dose is randomises the weights nothing special
        # the name train is a bit miss leading

        # input random
        for i in range(self.layers):
            self.biasinput[i] += random.uniform(-distance,distance)
            self.bias2[i] += random.uniform(-distance,distance)

            for j in range(self.inputlayers):
                self.weightinput[i][j] += random.uniform(-distance,distance)


        # hiden random
        for i in range(self.layers):
            self.biasinput[i] += random.uniform(-distance,distance)
            self.bias2[i] += random.uniform(-distance,distance)

            for j in range(self.layers):
                self.weight2[i][j] += random.uniform(-distance,distance)

        # output random
        for i in range(self.outputlayers):
            self.biasout[i] += random.uniform(-distance,distance)

            for j in range(self.layers):
                self.weightout[i][j] += random.uniform(-distance,distance)


    def exportAI(self):
        # exports the weights to a txt file
        pickle.dump(self.weightinput, open('weightinput.p', 'wb'))
        pickle.dump(self.weight2, open('weight2.p', 'wb'))
        pickle.dump(self.weightout, open('weightout.p', 'wb'))

        # exports the bias to a txt file
        pickle.dump(self.biasinput, open('biasinput.p', 'wb'))
        pickle.dump(self.bias2, open('bias2.p', 'wb'))
        pickle.dump(self.biasout, open('biasout.p', 'wb'))

    def importAI(self):
        # imports the weights form a txt file
        self.weightinput = pickle.load(open('weightinput.p', 'rb'))
        self.weight2 = pickle.load(open('weight2.p', 'rb'))
        self.weightout = pickle.load(open('weightout.p', 'rb'))

        # imports the bias form a txt file
        self.biasinput = pickle.load(open('biasinput.p', 'rb'))
        self.bias2 = pickle.load(open('bias2.p', 'rb'))
        self.biasout = pickle.load(open('biasout.p', 'rb'))
