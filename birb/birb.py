import pygame
import random



class game:

    def __init__(self,xmax,ymax):

        self.xmax = xmax
        self.ymax = ymax

        self._runing = True
        self.screen = None
        self.keyinput = None

        self.xb = [int(self.xmax /2), self.xmax]
        self.ybt = [random.randint(20, int (self.xmax + (self.xmax/-6 - 10))) for x in range(2)]
        #self.ybt = [350, 350]
        self.ybb = [self.ybt[0] + (self.xmax/6), self.ybt[1] + (self.xmax/6)]

        self.y = 100
        self.x = int(self.xmax / 10)
        self.aceleration = 0
        self.size = int(self.xmax / 20)
        self.sizeb = int(self.xmax / 10)
        self.speed = int(self.xmax / 160)
        self.points = 0


    def on_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.xmax, self.ymax))
        self._runing = True
        self.clock = pygame.time.Clock()

    def reset(self, draw_game):

        self._runing = True
        self.screen = None
        self.keyinput = None

        self.xb = [int(self.xmax /2), self.xmax]
        self.ybt = [random.randint(20, int (self.xmax + (self.xmax/-6 - 10))) for x in range(2)]
        #self.ybt = [350, 350]
        self.ybb = [self.ybt[0] + (self.xmax/6), self.ybt[1] + (self.xmax/6)]

        self.y = 100
        self.x = int(self.xmax / 10)
        self.aceleration = 0
        self.size = int(self.xmax / 20)
        self.sizeb = int(self.xmax / 10)
        self.speed = int(self.xmax / 160)
        self.points = 0

        if draw_game == True:
            self.on_init()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self._runing = False

    def get_vals(self):
        vals = [int(self.x), int(self.xb[0]), int(self.ybt[0]), int(self.ybb[0]), int(self.xb[1]), int(self.ybt[1]), int(self.ybb[1])]
        return vals

    def get_points(self):
        return self.points

    def colisions(self):
        # death
        if self.y > self.ymax or self.y < 0:
            self._runing = False
            self.points -= 1
            #print('out',self.points)

        # player with barrer
        for i in range(2):
            if self.xb[i] < self.x + self.size and self.xb[i] > self.x - self.sizeb:
                if self.y < self.ybt[i]:
                    self._runing = False
                    #print('hit')
                elif self.y + self.size > self.ybb[i]:
                    self._runing = False
                    #print('hit')
            if self.xb[i] == self.x:
                self.points += 1
                #print(self.points)

        # moving barer
        for i in range(2):
            if self.xb[i] + self.sizeb == 0:
                self.xb[i] = self.xmax
                self.ybt[i] = random.randint(20, int (self.xmax + (self.xmax/-6 - 10)))
                self.ybb[i] = self.ybt[i] + (self.xmax/6)

        return self._runing

    def movement(self, press):

        # gets the user input and sets the player aceleration
        if press:
            self.aceleration = -10

            if self.xb[0] > self.xb[1]:
                if self.ybt[1] > self.y:
                    self.points -= 0.5
            else:
                if self.ybt[0] > self.y:
                    self.points -= 0.5
        else:
            self.aceleration += 1

            if self.xb[0] > self.xb[1]:
                if self.ybb[1] > self.y:
                    self.points -= 0.5
            else:
                if self.ybb[0] > self.y:
                    self.points -= 0.5


        # movement
        self.y += self.aceleration
        #print(self.aceleration, self.y)
        self.xb[0] -= self.speed
        self.xb[1] -= self.speed


    def render_game(self,fps):
        self.screen.fill((0,0,0))

        pygame.draw.rect(self.screen, (0, 25, 120), pygame.Rect(self.x, self.y, self.size, self.size))

        for i in range(2):
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.xb[i], self.ybb[i], self.sizeb, self.xmax))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.xb[i], 0, self.sizeb, self.ybt[i]))

        self.clock.tick(fps)
        pygame.display.flip()

    def play_game(self,fps):


        while self._runing == True:

            self.movement(pygame.key.get_pressed()[pygame.K_SPACE])
            self.colisions()
            self.event()
            self.render_game(fps)

        pygame.quit()

if __name__ == "__main__" :
    App = game(800,800)
    App.on_init()
    print(App.play_game(30))
