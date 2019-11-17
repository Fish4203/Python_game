import pygame
import random



class game:
    def __init__(self,xmax,ymax):

        self.xmax = xmax
        self.ymax = ymax

        self._runing = True
        self.screen = None
        self.keyinput = None

        self.xobj = random.randint(0,self.xmax - 10)
        self.yobj = random.randint(0,self.ymax - 10)
        self.y = [100]
        self.x = [100]
        self.direction = 0
        self.fitness = 0
        self.speed = 30
        self.size = 30
        self.aiin = []
        self.aiout = []
        self.movesremaining = 10000
        self.tempdirection1 = None
        self.tempdirection2 = None
        self.paused = False

    def on_init(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.xmax, self.ymax))
        self._runing = True
        self.clock = pygame.time.Clock()

    def reset(self, draw_game):
        self._runing = True
        self.screen = None
        self.keyinput = None

        self.xobj = random.randint(0,self.xmax - 10)
        self.yobj = random.randint(0,self.ymax - 10)
        self.y = [100]
        self.x = [100]
        self.direction = 0
        self.fitness = 0
        self.speed = 30
        self.size = 30
        self.aiin = []
        self.aiout = []
        self.movesremaining = 10000
        self.tempdirection1 = None
        self.tempdirection2 = None

        if draw_game == True:
            self.on_init()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self._runing = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.paused == False:
                self.paused = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.paused == True:
                self.paused = False

    def get_point(self):
        self.fitness += 20000
        self.xobj = random.randint(0,self.xmax - 10)
        self.yobj = random.randint(0,self.ymax - 10)
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def render_game(self,fps):
        self.screen.fill((0,0,0))

        pygame.draw.rect(self.screen, (0, 25, 120), pygame.Rect(self.xobj, self.yobj, self.size, self.size))

        for i in range(len(self.x)):
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x[i], self.y[i], self.size, self.size))

        self.clock.tick(fps)
        pygame.display.flip()

    def play_game(self,fps):


        while self._runing == True:

            # gets the user input and changes the direction
            self.keyinput = pygame.key.get_pressed()
            if self.keyinput[pygame.K_w]: self.direction = 1
            elif self.keyinput[pygame.K_s]: self.direction = 0
            elif self.keyinput[pygame.K_d]: self.direction = 2
            elif self.keyinput[pygame.K_a]: self.direction =3

            # making other cubes move
            for i in reversed(range(len(self.x))):
                if i != 0:
                    self.x[i] = self.x[int(i-1)]
                    self.y[i] = self.y[int(i-1)]

            # moving the first cube
            if self.direction == 0: self.y[0] += self.speed
            elif self.direction == 1: self.y[0] -= self.speed
            elif self.direction == 2: self.x[0] += self.speed
            elif self.direction == 3: self.x[0] -= self.speed

            # pasing to the other side x
            if self.x[0] > self.xmax: self.x[0] = 1
            elif self.x[0] < 0: self.x[0] = self.xmax - 1

            # pasing to the other side y
            if self.y[0] > self.ymax: self.y[0] = 1
            elif self.y[0] < 0: self.y[0] = self.ymax -1

            if self.x[0] > self.xobj - self.size and self.x[0] < self.xobj + self.size and self.y[0] > self.yobj - self.size and self.y[0] < self.yobj + self.size:
                self.get_point()
            else:
                for i in reversed(range(len(self.x))):
                    if i != 0:
                        if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                            print('die')
                            self._runing = False

            self.event()
            self.render_game(fps)

        pygame.quit()

    def ai_game(self, ai, draw_game, fps, seeds):

                if seeds != None:
                    random.seed(seeds)
                    self.xobj = random.randint(0,self.xmax - 10)
                    self.yobj = random.randint(0,self.ymax - 10)

                while self._runing == True:

                    while self.paused == True:
                        self.render_game(fps)
                        self.event()

                    self.aiin.append(self.xobj)
                    self.aiin.append(self.yobj)

                    for i in range(len(self.x)):
                        self.aiin.append(self.x[i])
                        self.aiin.append(self.y[i])

                    self.aiout = ai.evaluate(self.aiin)
                    self.aiin = []

                    self.tempdirection2 = self.tempdirection1
                    self.tempdirection1 = self.direction
                    if self.aiout[0] == max(self.aiout): self.direction = 0 #s
                    elif self.aiout[1] == max(self.aiout): self.direction = 1 #w
                    elif self.aiout[2] == max(self.aiout): self.direction = 2 #d
                    elif self.aiout[3] == max(self.aiout): self.direction =3 #a

                    if self.tempdirection1 == self.direction:
                        self.movesremaining -= 200
                    elif self.tempdirection2 == self.direction:
                        self.movesremaining -= 200

                    # making other cubes move
                    for i in reversed(range(len(self.x))):
                        if i != 0:
                            self.x[i] = self.x[int(i-1)]
                            self.y[i] = self.y[int(i-1)]

                    # moving the first cube
                    if self.direction == 0: self.y[0] += self.speed
                    elif self.direction == 1: self.y[0] -= self.speed
                    elif self.direction == 2: self.x[0] += self.speed
                    elif self.direction == 3: self.x[0] -= self.speed

                    # pasing to the other side x
                    if self.x[0] > self.xmax: self.x[0] = 1
                    elif self.x[0] < 0: self.x[0] = self.xmax - 1

                    # pasing to the other side y
                    if self.y[0] > self.ymax: self.y[0] = 1
                    elif self.y[0] < 0: self.y[0] = self.ymax -1

                    #not dieing
                    if self.x[0] > self.xobj - self.size and self.x[0] < self.xobj + self.size and self.y[0] > self.yobj - self.size and self.y[0] < self.yobj + self.size:
                        self.get_point()
                    else:
                        for i in reversed(range(len(self.x))):
                            if i != 0:
                                if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                                    print('die')
                                    self._runing = False
                    if self.movesremaining < 0:
                        self._runing = False

                    self.movesremaining -= 1
                    #print(self.movesremaining)

                    # fitness
                    if self.x[0] > self.xobj:
                        if self.y[0] > self.yobj:
                            self.fitness -= (self.x[0] - self.xobj) + (self.y[0] - self.yobj)
                        elif self.y[0] < self.yobj:
                            self.fitness -= (self.x[0] - self.xobj) + (self.yobj - self.y[0])
                    elif self.x[0] < self.xobj:
                            if self.y[0] > self.yobj:
                                self.fitness -= (self.xobj - self.x[0]) + (self.y[0] - self.yobj)
                            elif self.y[0] < self.yobj:
                                self.fitness -= (self.xobj - self.x[0]) + (self.yobj - self.y[0])

                    #if ( self.x[0] - self.xobj < 100 or self.x[0] - self.xobj < -100 ) and ( self.y[0] - self.yobj < 100 or self.y[0] - self.yobj < -100 ):
                        #self.fitness += 1

                    # options to draw the game
                    if draw_game == True:
                        self.render_game(fps)
                        self.event()

                pygame.quit()
                return self.fitness



if __name__ == "__main__" :
    App = game(700,700)
    App.on_init()
    App.play_game(15)


'''


while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    # gets the user input and changes the direction
    keyinput = pygame.key.get_pressed()
    if keyinput[pygame.K_w]: direction = 1
    elif keyinput[pygame.K_s]: direction = 0
    elif keyinput[pygame.K_d]: direction = 2
    elif keyinput[pygame.K_a]: direction =3

    # changes the direction of the verlocety
    if direction == 0: y += 5
    elif direction == 1: y -= 5
    elif direction == 2: x += 5
    elif direction == 3: x -= 5

    # pasing to the other side x
    if x > xmax: x = 1
    elif x < 0: x = xmax - 1

    # pasing to the other side y
    if y > ymax: y = 1
    elif y < 0: y = ymax -1

    pygame.draw.rect(screen, (0, 25, 120), pygame.Rect(xobj, yobj, 30, 30))
    pygame.draw.rect(screen, colour, pygame.Rect(x, y, 30, 30))

    clock.tick(60)
    pygame.display.flip()


snake

'''
