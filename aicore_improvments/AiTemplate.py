import random


class AI():

    aiwin = 0

    def __init__(self):

        # i define the verables used
        self.outputlayers = 4 # the number of outputs
        self.n = 64 # this is the size of the grid
        self.result = [0 for y in range(self.outputlayers)]
        self.resultfinal = [0 for y in range(self.outputlayers)]
        # theses are the neurons and weights
        self.neuron1 = []
        #self.neuron1 = [0 for x in range(self.n)]
        self.neuron2 = [0 for y in range(self.n)]
        self.neuron3 = [0 for y in range(self.n)]
        self.weight1 = [[random.uniform(1,-1) for x in range(self.n)] for y in range(self.n)]
        self.weight2 = [[random.uniform(1,-1) for x in range(self.n)] for y in range(self.n)]
        self.weight3 = [[random.uniform(1,-1) for x in range(self.n)] for y in range(self.outputlayers)]



    def evaluate(self, input1):

        # importing the list from the program
        self.neuron1 = input1

        # the first dense layer of the neural net
        for i in range(self.n):
            for j in range(self.n):
                #print(i,j)
                self.neuron2[i] += self.neuron1[j] * self.weight1[i][j]

        # a second dense layer of the neural net this is unused
        #for i in range(self.n):
            #for j in range(self.n):
                #print(i,j)
                #self.neuron3[i] += self.neuron2[j] * self.weight2[i][j]
        self.neuron3 = self.neuron2

        # a last not dense layer of the neural network
        for i in range(self.outputlayers):
            for j in range(self.n):
                #print(i,j)
                self.result[i] += self.neuron3[j] * self.weight3[i][j]

        # this just resets the results verable while still returning a value
        # there is a better way of do ing this
        self.resultfinal = self.result
        self.result = [0, 0]
        self.neuron1 = []
        self.neuron2 = [0 for y in range(self.n)]
        self.neuron3 = [0 for y in range(self.n)]

        return self.resultfinal


    def train(self):
        # all this dose is randomises the weights nothing special
        # the name train is a bit miss leading
        for i in range(len(self.weight1)):

            for j in range(len(self.weight1[i])):
                self.weight1[i][j] += random.uniform(-1,1)

        for i in range(len(self.weight2)):

            for j in range(len(self.weight2[i])):
                self.weight2[i][j] += random.uniform(-1,1)

        for i in range(len(self.weight3)):
            for j in range(len(self.weight3[i])):
                self.weight3[i][j] += random.uniform(-1,1)


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
