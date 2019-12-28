from birb import *
from AiBirb_v2 import *
import random

iterations = int(input())

aisn = 100
running = True
render = False
fps = 10000
ais = [AI(7,2) for i in range(aisn)]

App = game(800,800)
App.on_init()

#for i in App.get_vals():
    #print(i)

while iterations > 0:

    for i in range(aisn):
        while running == True:
            if ais[i].evaluate(App.get_vals())[0] > ais[i].evaluate(App.get_vals())[1]: App.movement(True)
            else: App.movement(False)
            running = App.colisions()
            App.event()
            if render: App.render_game(fps)

        ais[i].aiwin = App.get_points()
        print(ais[i].aiwin)
        running = True
        App.reset(render)

    iterations -= 1
