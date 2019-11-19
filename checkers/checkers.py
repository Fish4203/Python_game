import pygame
import random



class game:
    def __init__(self,xmax,ymax):

        self.xmax = xmax
        self.ymax = ymax

        self._runing = True
        self.screen = None
        self.keyinput = None

        self.n = 8
        self.size = 100
        self.xbackground = []
        self.ybackground = []

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

        if draw_game == True:
            self.on_init()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self._runing = False

    def render_game(self,fps):
        self.screen.fill((0,0,0))

        pygame.draw.rect(self.screen, (0, 25, 120), pygame.Rect(100, 100, 30, 30,))

        for i in range(self.n):
            for j in range(4):
                pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.xbackground[i][j], self.ybackground[i], self.size, self.size))

        self.clock.tick(fps)
        pygame.display.flip()

    def swap_side(self):
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

            self.swap_side()

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
