from AiTemplate_v2 import AI
import random
import numpy as np
import time

n = 100
outputlayers = 50
ai = AI(100,100,50)

#ai.importAI()
#input = np.array([1 for y in range(n)])

#input = np.array([random.uniform(-1,1) for y in range(n)],dtype='float32')
ai.train(1)

#print(input.dtype)
#for i in range(10):
    #print(ai.evaluate(input))
    #ai.exportAI()


#bench mark
print(time.time())
while True:
    inttime = time.time()
    input = np.array([random.uniform(-1,1) for y in range(n)],dtype='float32')
    for i in range(100):
         ai.evaluate(input)
    ai.train(1)
    print(100/(time.time()-inttime))




# stuff to rember

#t = np.array([random.uniform(1,-1) for x in range(n*n)]).reshape(n, n)
#print(t[1])
