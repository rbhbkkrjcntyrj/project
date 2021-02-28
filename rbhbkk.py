import pygame
import pygameproject
from importlib import reload

pygame.init()
height = 600
width = 1100
screenhome = pygame.display.set_mode((width, height))
screencolor = pygame.Color("black")
class Startscreen:
    def __init__(self):
        self.running = True
        while self.running:
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render("Добро пожаловать!", True, (100, 255, 100))
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screenhome.blit(text, (text_x, text_y))
            startbutton = font.render(
                "Начать игру", True, (100, 255, 100))
            startb = pygame.Rect(text_x - 10, text_y * 4 - 10,
                                 text_w + 20, text_h + 20)
            screenhome.blit(startbutton, (text_x, text_y * 4))
            pygame.draw.rect(screenhome, [0, 255, 0], startb, 1)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and startb.collidepoint(event.pos):
                    pygameproject.Game().play()
                    reload(pygameproject)

if __name__ == '__main__':
    Startscreen()
