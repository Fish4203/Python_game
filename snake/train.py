from snake import game
from AiSnake import AI
import pickle
import operator
import copy

iterations = 1
number_ais = 50
ais = [AI() for y in range(number_ais)]
App = game(700,700)
App.on_init()
ais[0].importAI()
aiwinout = []

for i in range(number_ais):
    ais[i].train()

while iterations > 0:
    for ai in ais:
        ai.aiwin = App.ai_game(ai,False)
        App.reset(False)
        #print(ai.aiwin)

    ais.sort(key=operator.attrgetter('aiwin'))
    print(ais[-1].aiwin)
    ais[-1].exportAI()

    for i in range(number_ais):
        ais[i].importAI()
        ais[i].train()

    ais[0].importAI()

    iterations -= 1

    for z in range(len(ais)):
        ais[z].aiwin = 0
