import pygame
import pygameproject
from importlib import reload
import json

pygame.init()
height = 600
width = 1100
screenhome = pygame.display.set_mode((width, height))
running = True
sostbut = ("ДА", "НЕТ")
colors = [pygame.Color("red"), pygame.Color(
    "orange"), pygame.Color(
    "yellow"), pygame.Color(
    "green"), pygame.Color(
    "blue"), pygame.Color(
    "pink"), pygame.Color(
    "purple"), pygame.Color(
    "black"), pygame.Color(
    "white"), pygame.Color(
    "grey")]
with open('projectsave.json') as file:
    f = file.read()
    data = json.loads(f)
    buttonsh = data["options"][0]
    screensh = data["options"][1]
    textsh = data["options"][2]
    buttonfill = data["options"][3]
screencolor = colors[screensh]
textcolor = colors[textsh]
buttoncolor = colors[buttonsh]

#функция для сохранения данных в json-файл
def qsave():
    with open('projectsave.json') as file:
        f = file.read()
        data = json.loads(f)
        data["options"][0] = buttonsh
        data["options"][1] = screensh
        data["options"][2] = textsh
        data["options"][3] = buttonfill
        with open('projectsave.json', "w") as file:
            json.dump(data, file, ensure_ascii=False)


# класс для создание и функций стартого экрана
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
            startb = pygame.Rect(text_x - 10, text_y * 4 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, startb, buttonfill)
            startbutton = font.render(
                "Начать игру", True, textcolor)
            screenhome.blit(startbutton, (text_x, text_y * 4))
            tableb = pygame.Rect(text_x - 10, text_y * 5 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, tableb, buttonfill)
            table = font.render(
                "Таблица рекордов", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 5))
            optb = pygame.Rect(text_x - 10, text_y * 6 - 10,
                               text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, optb, buttonfill)
            opt = font.render(
                "Настройки", True, textcolor)
            screenhome.blit(opt, (text_x, text_y * 6))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    qsave()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and startb.collidepoint(event.pos):
                    pygameproject.Game().play()
                    reload(pygameproject)
                    Endgame()
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    RecordTable()
                if event.type == pygame.MOUSEBUTTONDOWN and optb.collidepoint(event.pos):
                    Options()


                    
# класс для создание и функций конечного экрана
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
            startb = pygame.Rect(text_x - 10, text_y * 4 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, startb, buttonfill)
            startbutton = font.render(
                "Начать заново?", True, textcolor)
            screenhome.blit(startbutton, (text_x, text_y * 4))
            with open('projectsave.json') as file:
                f = file.read()
                data = json.loads(f)
            shbutton = font.render(
                "Ваш счёт: " + str(data["playerpoint"]), True, textcolor)
            screenhome.blit(shbutton, (text_x, text_y * 2))
            tableb = pygame.Rect(text_x - 10, text_y * 5 - 10,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, tableb, buttonfill)
            table = font.render(
                "К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 5))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    qsave()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and startb.collidepoint(event.pos):
                    pygameproject.Game().play()
                    reload(pygameproject)
                    Endgame()
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    Startscreen()


                    
# класс для вывода таблицы рекордов из сохранённых
class RecordTable:
    def __init__(self):
        global running
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    qsave()
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
            tableb = pygame.Rect(text_x - 10, text_y * 10 - 60,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, tableb, buttonfill)
            table = font.render("К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 10 - 50))
            pygame.display.flip()


            
# класс для изменения заливки, цвета кнопки, цвета экрана, проверки нажатия кнопок обозначающих эти ф-ии
class Options:
    def __init__(self):
        global running, buttonfill, textsh, screensh, buttonsh, textcolor, buttoncolor, screencolor
        while running:
            screenhome.fill(screencolor)
            font = pygame.font.Font(None, 50)
            text = font.render(
                "Таблица рекордов", True, textcolor)
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            tableb = pygame.Rect(text_x - 10, text_y * 10 - 60,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, tableb, buttonfill)
            table = font.render("К началу", True, textcolor)
            screenhome.blit(table, (text_x, text_y * 10 - 50))
            colb = pygame.Rect(text_x - 10, text_y * 2 - 60,
                               text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, colb, buttonfill)
            col = font.render("Цвет экрана", True, textcolor)
            screenhome.blit(col, (text_x, text_y * 2 - 50))
            col1b = pygame.Rect(text_x - 10, text_y * 3 - 60,
                                text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, col1b, buttonfill)
            col1 = font.render("Цвет букв", True, textcolor)
            screenhome.blit(col1, (text_x, text_y * 3 - 50))
            col2b = pygame.Rect(text_x - 10, text_y * 4 - 60,
                                text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, col2b, buttonfill)
            col2 = font.render("Цвет кнопки", True, textcolor)
            screenhome.blit(col2, (text_x, text_y * 4 - 50))
            col3b = pygame.Rect(text_x - 10, text_y * 5 - 60,
                                text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, col3b, buttonfill)
            col3 = font.render(
                "Заливка: " + sostbut[buttonfill], True, textcolor)
            screenhome.blit(col3, (text_x, text_y * 5 - 50))
            baseb = pygame.Rect(text_x - 10, text_y * 9 - 60,
                                text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, baseb, buttonfill)
            base = font.render("Стартовые", True, textcolor)
            screenhome.blit(base, (text_x, text_y * 9 - 50))
            nulb = pygame.Rect(text_x - 10, text_y * 8 - 60,
                               text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, buttoncolor, nulb, buttonfill)
            nul = font.render("Обнулить рекорды", True, textcolor)
            screenhome.blit(nul, (text_x, text_y * 8 - 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    qsave()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    Startscreen()
                if event.type == pygame.MOUSEBUTTONDOWN and col3b.collidepoint(event.pos):
                    if buttoncolor != textcolor:
                        buttonfill = (buttonfill + 1) % 2
                if event.type == pygame.MOUSEBUTTONDOWN and nulb.collidepoint(event.pos):
                    with open('projectsave.json') as file:
                        f = file.read()
                        data = json.loads(f)
                        data["records"] = [0, 0, 0, 0, 0, 0, 0, 0]
                        with open('projectsave.json', "w") as file:
                            json.dump(data, file, ensure_ascii=False)
                if event.type == pygame.MOUSEBUTTONDOWN and col1b.collidepoint(event.pos):
                    textsh = (textsh + 1) % 10
                    if screensh != textsh != buttonsh:
                        textcolor = colors[textsh]
                if event.type == pygame.MOUSEBUTTONDOWN and colb.collidepoint(event.pos):
                    screensh = (screensh + 1) % 10
                    if buttonsh != screensh != textsh:
                        screencolor = colors[screensh]
                if event.type == pygame.MOUSEBUTTONDOWN and col2b.collidepoint(event.pos):
                    buttonsh = (buttonsh + 1) % 10
                    if screensh != buttonsh != textsh:
                        buttoncolor = colors[buttonsh]
                if event.type == pygame.MOUSEBUTTONDOWN and baseb.collidepoint(event.pos):
                    qsave()
                    buttonsh = 3
                    screensh = 7
                    textsh = 3
                    buttonfill = 1
                    buttoncolor = colors[buttonsh]
                    screencolor = colors[screensh]
                    textcolor = colors[textsh]
            pygame.display.flip()


            
# класс вывода сообщения об ощибке в случае проблемы 
class Fault:
    def __init__(self):
        global running
        while running:
            screenhome.fill(colors[2])
            font = pygame.font.Font(None, 50)
            text = font.render("Что-то пошло не так!", True, colors[4])
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screenhome.blit(text, (text_x, text_y))
            text1 = font.render("Просим вас начать заново.", True, colors[4])
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 8 - text.get_height() // 2
            screenhome.blit(text1, (text_x, text_y * 2))
            tableb = pygame.Rect(text_x - 10, text_y * 6 - 60,
                                 text_w + 20, text_h + 20)
            pygame.draw.rect(screenhome, colors[7], tableb, 1)
            table = font.render("К началу", True, colors[4])
            screenhome.blit(table, (text_x, text_y * 6 - 50))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and tableb.collidepoint(event.pos):
                    Startscreen()


if __name__ == '__main__':
    try:
        Startscreen()
    except:
        Fault()
