from checkers import game
from AiCheckers import AI
import pickle
import operator
import copy
import random

iterations = int(input('iterations'))
n = 50
aitop = [AI() for y in range(n)]
aibottom = [AI() for y in range(n)]
render = False
fps = 10

App = game(800,800)
#App.on_init()
App.reset(render)

#print(App.return_board(), App.fitness[0], App.fitness[1])

while iterations > 0:

    aitop[0].importAI('top')
    aibottom[0].importAI('bottom')

    for aj in range(n):
        for ai in range(n):
            for turn in range(100):
                App.make_move([y for y in aitop[ai].evaluate(App.return_board(False))])
                #print([y for y in aitop[ai].evaluate(App.return_board())])
                App.make_move([y for y in aibottom[aj].evaluate(App.return_board(False))])
                #print([y for y in aibottom[aj].evaluate(App.return_board())])
                if render == True:
                    App.event()
                    App.render_game(fps)
                    print(turn)
            aitop[ai].aiwin += App.return_fitness()[0]
            aibottom[aj].aiwin += App.return_fitness()[1]
            print(aitop[ai].aiwin, aibottom[aj].aiwin)
            App.reset(render)
            #print(ai.aiwin)

    aitop.sort(key=operator.attrgetter('aiwin'))
    aibottom.sort(key=operator.attrgetter('aiwin'))
    aitop[-1].exportAI('top')
    aibottom[-1].exportAI('bottom')

    print(aitop[-1].aiwin, aibottom[-1].aiwin)
    print(iterations)

    for i in range(n):
        aitop[i].importAI('top')
        aibottom[i].importAI('bottom')
        aitop[i].train()
        aibottom[i].train()
        aitop[i].aiwin = 0
        aibottom[i].aiwin = 0

    iterations -= 1

while iterations < 0:

    aitop[0].importAI('top')
    aibottom[0].importAI('bottom')

    for aj in range(n):
        for ai in range(n):
            App.return_board(True)

            for turn in range(10):
                App.make_move([y for y in aitop[ai].evaluate(App.return_board(False))])
                #print([y for y in aitop[ai].evaluate(App.return_board())])
                App.make_move([y for y in aibottom[aj].evaluate(App.return_board(False))])
                #print([y for y in aibottom[aj].evaluate(App.return_board())])
                if render == True:
                    App.event()
                    App.render_game(fps)
                    print(turn)

            aitop[ai].aiwin += App.return_fitness()[0]
            aibottom[aj].aiwin += App.return_fitness()[1]
            print(aitop[ai].aiwin, aibottom[aj].aiwin)
            App.reset(render)
            #print(ai.aiwin)

    aitop.sort(key=operator.attrgetter('aiwin'))
    aibottom.sort(key=operator.attrgetter('aiwin'))
    aitop[-1].exportAI('top1')
    aibottom[-1].exportAI('bottom1')

    print(aitop[-1].aiwin, aibottom[-1].aiwin)
    print(iterations)

    for i in range(n):
        aitop[i].importAI('top')
        aibottom[i].importAI('bottom')
        aitop[i].train()
        aibottom[i].train()
        aitop[i].aiwin = 0
        aibottom[i].aiwin = 0

    iterations += 1

if iterations == 0:
    App.reset(True)

    top = AI()
    bottom = AI()
    top.importAI('top')
    bottom.importAI('bottom')

    App.return_board(True)

    for turn in range(200):
        #print([y for y in top.evaluate(App.return_board(False))])
        App.make_move([y for y in top.evaluate(App.return_board(False))])

        #print([y for y in bottom.evaluate(App.return_board(False))])
        App.make_move([y for y in bottom.evaluate(App.return_board(False))])


        App.event()
        App.render_game(fps)
        print(turn, [x for x in App.return_fitness()])

    #for z in range(len(ais)):
        #ais[z].aiwin = 0






#print(App.return_board(), App.fitness[0], App.fitness[1])


'''
    def ai_game(self, fps, draw_game, move):


        while self._runing == True:

            self.move = move

            if len(self.move) == 4:
                self.make_move(self.move)
            else:
                print('invalid input')

            #print('########################')
            #for i in range(self.n):
                #print([y for y in self.board[i]])

            if draw_game == True:
                self.event()
                self.render_game(fps)

        pygame.quit()
        return self.fitness

'''
