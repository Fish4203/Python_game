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

App = game(800,800)
#App.on_init()
App.reset(False)

#print(App.return_board(), App.fitness[0], App.fitness[1])

while iterations > 0:

    aitop[0].importAI('top')
    aibottom[0].importAI('bottom')

    for aj in range(n):
        for ai in range(n):
            for turn in range(200):
                App.make_move([y for y in aitop[ai].evaluate(App.return_board())])
                #print([y for y in aitop[ai].evaluate(App.return_board())])
                App.make_move([y for y in aibottom[aj].evaluate(App.return_board())])
                #print([y for y in aibottom[aj].evaluate(App.return_board())])
            aitop[ai].aiwin += App.return_fitness()[0]
            aibottom[aj].aiwin += App.return_fitness()[1]
            print(aitop[ai].aiwin, aibottom[aj].aiwin)
            App.reset(False)
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
