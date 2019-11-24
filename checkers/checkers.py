import pygame
import random
import copy
import time


class game:

    def __init__(self,xmax,ymax):

        self.xmax = xmax
        self.ymax = ymax

        self._runing = True
        self.screen = None
        self.keyinput = None


        #verables that dont need to be reset
        self.flat_board = []

        #verables that need to be reset probs
        self.n = 8
        self.size = 100
        self.v1 = 1
        self.v2 = 2
        self.xbackground = []
        self.ybackground = []
        self.bluex = []
        self.bluey = []
        self.redx = []
        self.redy = []
        self.input_status = False
        self.move = []
        self.fitness = [0, 0]


        self.board = [[0 for y in range(self.n)] for x in range(self.n)]
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[-1, 0, -1, 0, -1, 0, -1, 0],[0, -1, 0, -1, 0, -1, 0, -1],[-1, 0, -1, 0, -1, 0, -1, 0]]

        for i in range(self.n):
            if (i % 2) == 0:
                self.xbackground.append([0,200,400,600])
                self.ybackground.append(i*100)
            else:
                self.xbackground.append([100,300,500,700])
                self.ybackground.append(i*100)

    def on_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.xmax, self.ymax))
        self._runing = True
        self.clock = pygame.time.Clock()

    def reset(self, draw_game):
        self._runing = True
        self.screen = None
        self.keyinput = None

        # verables that probebly need to be reset
        self.n = 8
        self.size = 100
        self.v1 = 1
        self.v2 = 2
        self.xbackground = []
        self.ybackground = []
        self.bluex = []
        self.bluey = []
        self.redx = []
        self.redy = []
        self.input_status = False
        self.move = []
        self.fitness = [0, 0]

        self.board = [[0 for y in range(self.n)] for x in range(self.n)]
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[-1, 0, -1, 0, -1, 0, -1, 0],[0, -1, 0, -1, 0, -1, 0, -1],[-1, 0, -1, 0, -1, 0, -1, 0]]

        for i in range(self.n):
            if (i % 2) == 0:
                self.xbackground.append([0,200,400,600])
                self.ybackground.append(i*100)
            else:
                self.xbackground.append([100,300,500,700])
                self.ybackground.append(i*100)

        if draw_game == True:
            self.on_init()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self._runing = False

    def return_board(self, generate):
        if generate == True:
            for i in range(self.n):
                for j in range(self.n):
                    if (i % 2) == 0 and (j % 2) == 1:
                        self.board[i][j] = random.randint(-1,1)
                    elif (i % 2) == 1 and (j % 2) == 0:
                        self.board[i][j] = random.randint(-1,1)
                        
        for i in self.board:
            for j in i:
                self.flat_board.append(j)

        self.flat_board_out = copy.copy(self.flat_board)
        self.flat_board = []
        return self.flat_board_out

    def return_fitness(self):
        return self.fitness

    def render_game(self,fps):

        # reset the display verables
        self.bluex = []
        self.bluey = []
        self.redx = []
        self.redy = []

        #fill the scren with the board empty
        self.screen.fill((0,0,0))
        for i in range(self.n):
            for j in range(4):
                pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.xbackground[i][j], self.ybackground[i], self.size, self.size))

        # asigns the display verables baised on the board state
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.redx.append(100 * j + 25)
                    self.redy.append(100 * i + 25)
                elif self.board[i][j] == -1:
                    self.bluex.append(100 * j + 25)
                    self.bluey.append(100 * i + 25)

        # draws the red peaces
        for i in range(len(self.redx)):
            pygame.draw.rect(self.screen, (255, 10, 10), pygame.Rect(self.redx[i], self.redy[i], 50, 50,))
        # draws the blue peaces
        for i in range(len(self.bluex)):
            pygame.draw.rect(self.screen, (10, 10, 255), pygame.Rect(self.bluex[i], self.bluey[i], 50, 50,))

        # displays the graphics and sets the framerate
        self.clock.tick(fps)
        pygame.display.flip()

    def make_move(self, move):

        self.movefiltered = []

        if len(move) == 4:
            for i in range(len(move)):
                self.movefiltered.append(int(move[i]))
            #print([y for y in self.movefiltered])

            ########## mAKING MOVE ########
            # test ing if the first peace is a 1
            if self.board[self.movefiltered[0]][self.movefiltered[1]] == 1:
                #print('selected a valid peace')

                # checking that the place you want to move to is a 0
                if self.board[self.movefiltered[2]][self.movefiltered[3]] == 0:
                    #print('target is empty')

                    # checks if the move is one or 2 tiles ahed
                    if self.movefiltered[2] == (self.movefiltered[0] + self.v1): # one tile ahed
                        #print('one ahed')
                        if self.movefiltered[1] == (self.movefiltered[3] + 1) or self.movefiltered[1] == (self.movefiltered[3] - 1): # checks if it is one tile across in eithe direction
                            self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                            self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot

                            # adding self.fitness
                            if self.v1 == 1:
                                self.fitness[0] += 1
                            else:
                                self.fitness[1] += 1

                    elif self.movefiltered[2] == (self.movefiltered[0] + self.v2): # 2tiles ahed
                        #print('2 ahed')
                        if self.movefiltered[1] == (self.movefiltered[3] + 2):
                            #print('-2 x')
                            #print(self.movefiltered[2] - self.v1, self.movefiltered[3] + 1)
                            if self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] + 1] == -1:
                                #print('making move')

                                self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                                self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                                self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] + 1] = 0

                                # adding self.fitness
                                if self.v1 == 1:
                                    self.fitness[0] += 10
                                    self.fitness[1] -= 5
                                else:
                                    self.fitness[1] += 10
                                    self.fitness[0] -= 5


                        elif self.movefiltered[1] == (self.movefiltered[3] - 2):
                            #print('+2 x')
                            #print(self.movefiltered[2] - self.v1, self.movefiltered[3] - 1)
                            if self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - 1] == -1:
                                #print('making move')

                                self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                                self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                                self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - 1] = 0

                                # adding self.fitness
                                if self.v1 == 1:
                                    self.fitness[0] += 10
                                    self.fitness[1] -= 5
                                else:
                                    self.fitness[1] += 10
                                    self.fitness[0] -= 5
            #######DONE MOVE######

        else:
            for i in range(2):
                self.movefiltered.append(int(move[i]))

            if move[2] == 0:
                self.movefiltered.append(move[0] + self.v1)
                self.movefiltered.append(move[1] + 1)
            elif move[2] == 1:
                self.movefiltered.append(move[0] + self.v1)
                self.movefiltered.append(move[1] - 1)
            elif move[2] == 2:
                self.movefiltered.append(move[0] + self.v2)
                self.movefiltered.append(move[1] + 2)
            elif move[2] == 3:
                self.movefiltered.append(move[0] + self.v2)
                self.movefiltered.append(move[1] - 2)
            else:
                self.movefiltered.append(0)
                self.movefiltered.append(0)

            if self.movefiltered[2] > 7 or self.movefiltered[2] < 0 or self.movefiltered[3] > 7 or self.movefiltered[3] < 0:
                self.movefiltered[2] = 0
                self.movefiltered[3] = 0
            #print(self.movefiltered[0], self.movefiltered[1],self.movefiltered[2],self.movefiltered[3])

            ########## mAKING MOVE ########
            # test ing if the first peace is a 1
            if self.board[self.movefiltered[0]][self.movefiltered[1]] == 1:
                #print('selected a valid peace')

                # checking that the place you want to move to is a 0
                if self.board[self.movefiltered[2]][self.movefiltered[3]] == 0:
                    #print('target is empty')

                    # checks if the move is one or 2 tiles ahed
                    if move[2] == 0 or move[2] == 1: # one tile ahed
                        #print('one ahed')

                        self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                        self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot

                        # adding self.fitness
                        if self.v1 == 1:
                            self.fitness[0] += 1
                        else:
                            self.fitness[1] += 1

                    elif move[2] == 3: # 2tiles ahed
                        #print('-2 x')
                        #print(self.movefiltered[2] - self.v1, self.movefiltered[3] + 1)
                        if self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] + 1] == -1:
                            #print('making move')

                            self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                            self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                            self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] + 1] = 0

                            # adding self.fitness
                            if self.v1 == 1:
                                self.fitness[0] += 10
                                self.fitness[1] -= 5
                            else:
                                self.fitness[1] += 10
                                self.fitness[0] -= 5

                    elif move[2] == 2: # 2tiles ahed
                        #print('+2 x')
                        #print(self.movefiltered[2] - self.v1, self.movefiltered[3] - 1)
                        if self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - 1] == -1:
                            #print('making move')

                            self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                            self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                            self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - 1] = 0

                            # adding self.fitness
                            if self.v1 == 1:
                                self.fitness[0] += 10
                                self.fitness[1] -= 5
                            else:
                                self.fitness[1] += 10
                                self.fitness[0] -= 5
            #######DONE MOVE######



        # swaping v1
        if self.v1 == -1:
            self.v1 = 1
        else:
            self.v1 = -1

        # swaping v2
        if self.v2 == -2:
            self.v2 = 2
        else:
            self.v2 = -2

        # swaping the board
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.board[i][j] = -1
                elif self.board[i][j] == -1:
                    self.board[i][j] = 1

        self.move = []

    def play_game(self,fps):


        while self._runing == True:

            # player input
            if pygame.mouse.get_pressed()[0] == 1:
                #print(int(pygame.mouse.get_pos()[1] / 100),int(pygame.mouse.get_pos()[0] / 100))
                self.move.append(int(pygame.mouse.get_pos()[1] / 100))
                self.move.append(int(pygame.mouse.get_pos()[0] / 100))
                time.sleep(0.5)


            if len(self.move) == 4:
                self.make_move(self.move)

            #print('########################')
            #for i in range(self.n):
                #print([y for y in self.board[i]])

            self.event()
            self.render_game(fps)

        pygame.quit()


if __name__ == "__main__" :
    App = game(800,800)
    App.on_init()
    App.play_game(15)
