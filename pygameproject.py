import pygame
import os
from random import randint
import json

pygame.init()
height = 600
width = 1100
screen = pygame.display.set_mode((width, height))
all_sprites = pygame.sprite.Group()
dino_sprite = pygame.sprite.Group()
cloud_sprites = pygame.sprite.Group()
ptero = pygame.sprite.Group()
creator = True
running_pic = [pygame.image.load(os.path.join('Изображения', 'dinosaur_run_one.png')),
               pygame.image.load(os.path.join('Изображения', 'dinosaur_run_two.png'))]
jumping_pic = pygame.image.load(
    os.path.join('Изображения', 'dinosaur_jump.png'))
ducking_pic = [pygame.image.load(os.path.join('Изображения', 'dinosaur_duck_one.png')),
               pygame.image.load(os.path.join('Изображения', 'dinosaur_duck_two.png'))]
small_cactus_pic = [pygame.image.load(os.path.join('Изображения', 'small_cactus_one.png')),
                    pygame.image.load(os.path.join(
                        'Изображения', 'small_cactus_two.png')),
                    pygame.image.load(os.path.join('Изображения', 'small_cactus_three.png'))]
big_cactus_pic = [pygame.image.load(os.path.join('Изображения', 'big_cactus_one.png')),
                  pygame.image.load(os.path.join(
                      'Изображения', 'big_cactus_two.png')),
                  pygame.image.load(os.path.join('Изображения', 'big_cactus_three.png'))]
pterodactyl = [pygame.image.load(os.path.join('Изображения', 'pterodactyl_one.png')),
               pygame.image.load(os.path.join('Изображения', 'pterodactyl_two.png'))]
cloud = pygame.image.load(os.path.join(
    'Изображения', 'cloud.png'))
ground = pygame.image.load(os.path.join(
    'Изображения', 'ground.png'))
speed_of_game = 14


class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.position_x_two = 0
        self.position_y_two = 380
        self.points_of_player = 0
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def score(self):
        global speed_of_game
        self.points_of_player += 1
        if not self.points_of_player % 250:
            speed_of_game += 1
        text = self.font.render(
            'Счёт: ' + str(self.points_of_player), True, (0, 0, 0))
        rectangle_of_text = text.get_rect()
        rectangle_of_text.center = (1000, 40)
        screen.blit(text, rectangle_of_text)

    def background(self):
        global speed_of_game
        image_width = ground.get_width()
        screen.blit(ground, (self.position_x_two, self.position_y_two))
        screen.blit(ground, (self.position_x_two +
                             image_width, self.position_y_two))
        if self.position_x_two <= -image_width:
            screen.blit(ground, (self.position_x_two +
                                 image_width, self.position_y_two))
            self.position_x_two = 0
        self.position_x_two -= speed_of_game

    def play(self):
        global speed_of_game
        fps = 30
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            screen.fill((255, 255, 255))
            input_of_user = pygame.key.get_pressed()
            if len(cloud_sprites.sprites()) == 0:
                for _ in range(randint(1, 4)):
                    Cloud(cloud_sprites)
            if len(all_sprites.sprites()) == 0:
                for _ in range(randint(1, 3)):
                    Cactus(all_sprites)
            if self.points_of_player % 250 == 0 and self.points_of_player > 500:
                Pterodactyl()
            self.player.draw(screen)
            self.player.update(input_of_user)
            ptero.draw(screen)
            ptero.update()
            all_sprites.draw(screen)
            all_sprites.update()
            cloud_sprites.draw(screen)
            cloud_sprites.update()
            #условие на проверку столкновения
            if pygame.sprite.spritecollideany(self.player, all_sprites) or pygame.sprite.spritecollideany(self.player, ptero):
                speed_of_game = 0
                with open('projectsave.json') as file:
                    f = file.read()
                    data = json.loads(f)
                    for i in range(len(data["records"])):
                        if self.points_of_player > max(data["records"]):
                            data["records"] = [self.points_of_player] + \
                                data["records"][:-1]
                            break
                        if self.points_of_player > data["records"][i]:
                            data["records"] = data["records"][0:i] + \
                                [self.points_of_player] + \
                                data["records"][i:-1]
                            break
                    data["playerpoint"] = self.points_of_player
                    with open('projectsave.json', "w") as file:
                        json.dump(data, file, ensure_ascii=False)
                self.running = False
            self.background()
            self.score()
            self.clock.tick(fps)
            pygame.display.update()


class Dinosaur(pygame.sprite.Sprite):
    position_x = 80
    position_y = 310
    position_y_of_duck = 340
    jump_val_first = 8.5

    def __init__(self):
        super().__init__(dino_sprite)
        self.duck_img = ducking_pic
        self.run_img = running_pic
        self.jump_img = jumping_pic
        self.dinosaur_duck = False
        self.dinosaur_run = True
        self.dinosaur_jump = False
        self.step_index = 0
        self.jump_val = self.jump_val_first
        self.image = self.run_img[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def update(self, event):
        if self.dinosaur_duck:
            self.duck()
        if self.dinosaur_run:
            self.run()
        if self.dinosaur_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        if event[pygame.K_UP] and not self.dinosaur_jump and self.rect.y == 310:
            self.dinosaur_duck = False
            self.dinosaur_run = False
            self.dinosaur_jump = True
        elif event[pygame.K_DOWN] and not self.dinosaur_jump:
            self.dinosaur_duck = True
            self.dinosaur_run = False
            self.dinosaur_jump = False
        elif not (self.dinosaur_jump or event[pygame.K_DOWN]):
            self.dinosaur_duck = False
            self.dinosaur_run = True
            self.dinosaur_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y_of_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = self.position_y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        self.mask = pygame.mask.from_surface(self.image)
        if self.dinosaur_jump:
            self.rect.y -= self.jump_val * 4
            self.jump_val -= 0.8
        if self.jump_val < - self.jump_val_first:
            self.dinosaur_jump = False
            self.jump_val = self.jump_val_first

    def draw(self, screen):
        dino_sprite.add(self)
        dino_sprite.draw(screen)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = cloud
        self.rect = self.image.get_rect()
        self.rect.x = width + randint(20, 180)
        self.rect.y = randint(30, 100)
        self.width = self.image.get_width()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global speed_of_game
        self.rect.x -= speed_of_game
        if self.rect.x <= -self.width:
            self.kill()


class Cactus(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = [small_cactus_pic[randint(
            0, 1)], big_cactus_pic[randint(0, 2)]][randint(0, 1)]
        self.rect = self.image.get_rect()
        self.rect.x = width + randint(480, 1080) + \
            360 * len(all_sprites.sprites())
        if self.image in small_cactus_pic:
            self.rect.y = 340
        else:
            self.rect.y = 310
        self.width = self.image.get_width()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global speed_of_game
        self.rect.x -= speed_of_game
        if self.rect.x <= -self.width:
            self.kill()


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ptero)
        self.step_index = 0
        self.image = pterodactyl[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.rect.x = width + randint(20, 180)
        self.rect.y = 100

    def update(self):
        global speed_of_game
        self.image = pterodactyl[self.step_index // 5]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x -= speed_of_game
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        if self.rect.x <= -self.width:
            self.kill()


if __name__ == '__main__':
    Game().play()