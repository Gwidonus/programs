from player import player
from enemies import Enemies
import pygame, sys
from pygame.locals import*


WWIDTH , WHEIGHT = (700, 500)
FPS = 120

def main():
    global window, bg_img

    pygame.init()
    window = pygame.display.set_mode((WWIDTH,WHEIGHT))
    pygame.display.set_caption("game")

    city = pygame.image.load("images/city.png").convert()
    farm = pygame.image.load("images/farm.png").convert()
    man = pygame.image.load("images/man1.png")#.convert()


    bg_img = city
    CLOCK = pygame.time.Clock()

    x = 0 # the x coordinate of bliting city

    mx = 100
    lane = 2
    Player = player(mx,window, man,lane)
    enemies = Enemies()

    while True:
        x = bg_image(x)
        Player.do()
        enemies.do(window)

        if Player.lives == 2:
            bg_img = farm
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_DOWN and Player.lane + 1 <= 3:
                Player.lane += 1
            if event.type == KEYDOWN and event.key == K_UP and Player.lane - 1 >= 0:
                Player.lane -= 1
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                exit()
        pygame.display.update()
        CLOCK.tick(FPS)

def exit():
    pygame.quit()
    sys.exit()

def bg_image(x):
    x2 = x % WWIDTH
    window.blit(bg_img, (x2 - bg_img.get_width(),0))
    window.blit(bg_img, (x2,0))
    x -= 1
    return x

if __name__ == '__main__':
    main()
