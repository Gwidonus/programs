import pygame, random

class Enemies():
    enemies = [
        pygame.image.load('images/laska.png'),
        pygame.image.load('images/autko.png'),
        pygame.image.load('images/pies.png'),
        pygame.image.load('images/wozek.png')
    ]
    queue = []
    x, y = [], []
    def add(self, screen):
        self.w = screen.get_width()
        self.x.append(self.w + 100)
        c = 1
        r = 1
        while len(self.queue) != 10:
            self.queue.append(random.randint(0, 3))
            self.x.append(self.x[len(self.x)-1] + self.enemies[self.queue[len(self.queue)-1]].get_width() + 100)
            if r == 1 and c == -1:
                self.y.append(260)
                c *= -1
            elif r == 1 :
                self.y.append(260)
            if r == 2:
                self.y.append(330)
            if r == 3 and c == 1:
                self.y.append(400)
                c *= -1
            r += c

    def draw(self, screen):
        for i in range(len(self.queue)):
            screen.blit(self.enemies[self.queue[i]], (self.x[i], self.y[i]))
            self.x[i] -= 1
            
    def check(self):
            if self.x[0] < 0:
                del self.x[0]
            
    def do(self, screen):
        self.add(screen)
        self.draw(screen)
        self.check()
