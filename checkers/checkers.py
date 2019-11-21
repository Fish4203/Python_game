import pygame
import random
import copy


class game:
    def __init__(self,xmax,ymax):

        self.xmax = xmax
        self.ymax = ymax

        self._runing = True
        self.screen = None
        self.keyinput = None

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


        self.board = [[0 for y in range(self.n)] for x in range(self.n)]
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],[0, 0, -1, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0],[-1, 0, -1, 0, -1, 0, -1, 0],[0, -1, 0, -1, 0, -1, 0, -1],[-1, 0, -1, 0, -1, 0, -1, 0]]

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

        if draw_game == True:
            self.on_init()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self._runing = False

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
        for i in range(len(move)):
            self.movefiltered.append(int(self.move[i]))
        print([y for y in self.movefiltered])

        # test ing if the first peace is a 1
        if self.board[self.movefiltered[0]][self.movefiltered[1]] == 1:
            print('selected a valid peace')

            # checking that the place you want to move to is a 0
            if self.board[self.movefiltered[2]][self.movefiltered[2]] == 0:
                print('target is empty')

                # checks if the move is one or 2 tiles ahed
                if self.movefiltered[2] == (self.movefiltered[0] + self.v1): # one tile ahed
                    if self.movefiltered[1] == (self.movefiltered[3] + 1) or self.movefiltered[1] == (self.movefiltered[3] - 1): # checks if it is one tile across in eithe direction
                        self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                        self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                        self.board = copy.deepcopy(self.board)

                elif self.movefiltered[2] == (self.movefiltered[0] + self.v2): # 2tiles ahed
                    if self.movefiltered[1] == (self.movefiltered[3] + 2) and self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - self.v1] == -1:
                        self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                        self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                        print(self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - self.v1])
                        self.board[self.movefiltered[2] - self.v1][self.movefiltered[3] - self.v1] = 0
                        self.board = copy.deepcopy(self.board)

                    elif self.movefiltered[1] == (self.movefiltered[3] - 2) and self.board[self.movefiltered[2] + self.v1][self.movefiltered[3] + self.v1] == -1:
                        self.board[self.movefiltered[2]][self.movefiltered[3]] = 1 # places the peace in the spot it is ment to go
                        self.board[self.movefiltered[0]][self.movefiltered[1]] = 0 # removes the peace from the starting spot
                        print(self.board[self.movefiltered[2] + self.v1][self.movefiltered[3] + self.v1])
                        self.board[self.movefiltered[2] + self.v1][self.movefiltered[3] + self.v1] = 0
                        print(self.board[self.movefiltered[2] + self.v1][self.movefiltered[3] + self.v1])
                        self.board = copy.deepcopy(self.board)

            print(self.board[3][2])
            # a loop to iterate through all the posable moves
            #for moves in range(int( len(self.movefiltered) / 2 )):
                # this dosent work if the loop is = 0
                #if moves != 0:
                        #if self.movefiltered[(moves*2)] == (self.movefiltered[(moves*2 - 2)] + self.v1) and ( self.movefiltered[(moves*2 + 1)] == (self.movefiltered[(moves*2 - 1)] - 1) or self.movefiltered[(moves*2 + 1)] == (self.movefiltered[(moves*2 - 1)] + 1) ):
                            #self.board[self.movefiltered[-2]][self.movefiltered[-1]] = 1
                            #self.board[self.movefiltered[0]][self.movefiltered[1]] = 0

                        #elif self.movefiltered[(moves*2)] == (self.movefiltered[(moves*2 - 2)] + self.v2) and ( ( self.movefiltered[(moves*2 + 1)] == (self.movefiltered[(moves*2 - 1)] - 2) and self.board[self.movefiltered[(moves*2)] - 1][self.movefiltered[(moves*2 + 1)] - 1] == -1 ) or ( self.movefiltered[(moves*2 + 1)] == (self.movefiltered[(moves*2 - 1)] + 2) and self.board[self.movefiltered[(moves*2)] - 1][self.movefiltered[(moves*2 + 1)] - 1] == -1 ) ):

                            #self.board[self.movefiltered[-2]][self.movefiltered[-1]] = 1
                            #self.board[self.movefiltered[0]][self.movefiltered[1]] = 0

                            #if self.board[self.movefiltered[(moves*2)] - 1][self.movefiltered[(moves*2 + 1)] - 1] == -1:
                                #self.board[self.movefiltered[(moves*2)] - 1][self.movefiltered[(moves*2 + 1)] - 1] = 0
                            #else:
                                #self.board[self.movefiltered[(moves*2)] - 1][self.movefiltered[(moves*2 + 1)] + 1] = 0

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

    def play_game(self,fps):


        while self._runing == True:

            # gets the user input and changes the direction
            self.keyinput = pygame.key.get_pressed()

            # making other cubes move
            self.move = input('make a move')
            self.move = self.move.split(',')

            self.make_move(self.move)

            print('########################')
            for i in range(self.n):
                print([y for y in self.board[i]])

            self.event()
            self.render_game(fps)

        pygame.quit()



if __name__ == "__main__" :
    App = game(800,800)
    App.on_init()
    App.play_game(15)
