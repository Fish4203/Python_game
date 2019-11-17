from snake import game
from AiSnake import AI
import pickle
import operator
import copy
import random

iterations = int(input('iterations'))
number_ais = 50
ais = [AI() for y in range(number_ais)]
App = game(700,700)
App.on_init()
ais[0].importAI()
aiwinout = []

for i in range(number_ais):
    ais[i].train()

while iterations > 0:
    ais[0].importAI()

    for i in range(number_ais):
        for ai in ais:
            ai.aiwin += App.ai_game(ai,False,10000,random.random())
            App.reset(False)
            #print(ai.aiwin)

        ais.sort(key=operator.attrgetter('aiwin'))
        print(ais[-1].aiwin)
        ais[-1].exportAI()

    for i in range(number_ais):
        ais[i].importAI()
        ais[i].train()

    iterations -= 1

    for z in range(len(ais)):
        ais[z].aiwin = 0

ais[0].importAI()
if iterations == 0:
    App.reset(True)
    print(App.ai_game(ais[0],True,1,random.random()))
