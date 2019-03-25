from message import text
import pygame
from pygame.locals import*

class player():
    lives = 3
    def __init__(self, x, screen, image, lane):
        self.x = x
        self.screen = screen
        self.image = image
        self.lane = lane
        self.jump = False

    def keys(self):
        k = pygame.key.get_pressed() #pressed key variable
        if k[K_LEFT]:
            self.x -= 1
        if k[K_RIGHT]:
            self.x += 2
        if self.lane == 1:
            self.y = 260
        if self.lane == 2:
            self.y = 330
        if self.lane == 3:
            self.y = 400

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def check(self):
        if self.x + self.image.get_width() <= 0 and self.lives - 1 == 0:
            game_over(self.screen)
        if self.x + self.image.get_width() <= 0 and self.lives - 1 > 0:
            conti(self.screen)
            self.x = 100
            self.lives -= 1

    def do(self):
        self.keys()
        self.draw()
        self.x -= 1
        self.check()

text = text()

def game_over(screen):
    w,h = screen.get_width(), screen.get_height()
    not_pressed = True
    text.font1 = pygame.font.Font('fonts/orange.ttf', 40)
    while not_pressed:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                not_pressed = False
        text.write('Game over', text.font1, 70, (255,0,0), (0,0,0), (w,h), screen)
        pygame.display.update()

def conti(screen):
    not_pressed = True

    #while not_pressed:

