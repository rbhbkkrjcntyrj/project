import pygame
import pygameproject
from importlib import reload
import json


pygame.init()
height = 600
width = 1100
screenhome = pygame.display.set_mode((width, height))
screencolor = pygame.Color("black")
textcolor = (100, 255, 100)
running = True


class Startscreen:
    def __init__(self):
        global running
        while running:
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render("Добро пожаловать!", True, textcolor)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screenhome.blit(text, (text_x, text_y))
            startbutton = font.render(
                "Начать игру", True, textcolor)
            startb = pygame.Rect(text_x - 10, text_y * 4 - 10,
                                 text_w + 20, text_h + 20)
            screenhome.blit(startbutton, (text_x, text_y * 4))
            pygame.draw.rect(screenhome, [0, 255, 0], startb, 1)
            table = font.render(
                "Таблица рекордов", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 5))
            tableb = pygame.Rect(text_x - 10, text_y * 5 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, [0, 255, 0], tableb, 1)
            opt = font.render(
                "Настройки", True, textcolor)
            screenhome.blit(opt, (text_x, text_y * 6))
            optb = pygame.Rect(text_x - 10, text_y * 6 - 10,
                               text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, [0, 255, 0], optb, 1)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and startb.collidepoint(event.pos):
                    pygameproject.Game().play()
                    reload(pygameproject)
                    Endgame()
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    RecordTable()
                if event.type == pygame.MOUSEBUTTONDOWN and optb.collidepoint(event.pos):
                    Options()


class Endgame:
    def __init__(self):
        global running
        while running:
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render("Игра окончена!", True, textcolor)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screenhome.blit(text, (text_x, text_y))
            startbutton = font.render(
                "Начать заново?", True, textcolor)
            startb = pygame.Rect(text_x - 10, text_y * 4 - 10,
                                 text_w + 20, text_h + 20)
            screenhome.blit(startbutton, (text_x, text_y * 4))
            with open('projectsave.json') as file:
                    f = file.read()
                    data = json.loads(f)
            shbutton = font.render(
                "Ваш счёт: " + str(data["playerpoint"]), True, textcolor)
            screenhome.blit(shbutton, (text_x, text_y * 2))
            pygame.draw.rect(screenhome, [0, 255, 0], startb, 1)
            table = font.render(
                "К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 5))
            tableb = pygame.Rect(text_x - 10, text_y * 5 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, [0, 255, 0], tableb, 1)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and startb.collidepoint(event.pos):
                    pygameproject.Game().play()
                    reload(pygameproject)
                    Endgame()
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    Startscreen()


class RecordTable:
    def __init__(self):
        global running
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    Startscreen()
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render(
                "Таблица рекордов", True, textcolor)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            with open('projectsave.json') as file:
                    f = file.read()
                    data = json.loads(f)
                    for i in range(1, 9):
                        text = font.render(str(i) + ". " +
                                           str(data["records"][i - 1]), True, textcolor)
                        screenhome.blit(text, (text_x, text_y * i))
            table = font.render("К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 10 - 50))
            tableb = pygame.Rect(text_x - 10, text_y * 10 - 60,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, [0, 255, 0], tableb, 1)
            pygame.display.flip()


class Options:
    def __init__(self):
        global running
        while running:
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render(
                "Таблица рекордов", True, textcolor)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            table = font.render("К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 10 - 50))
            tableb = pygame.Rect(text_x - 10, text_y * 10 - 60,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, [0, 255, 0], tableb, 1)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                        Startscreen()
            pygame.display.flip()


if __name__ == '__main__':
    Startscreen()
