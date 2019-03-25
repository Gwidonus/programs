import pygame


class text():
    pygame.font.init()
    def write(self, message, font, size, color1, colo2, place, window):
        self.font1 = pygame.font.Font('fonts/orange.ttf', size)
        text = font.render(message, True, color1, colo2)
        textRect = text.get_rect()
        textRect.center = (place[0]/2, place[1]/2)
        window.blit(text, textRect)

