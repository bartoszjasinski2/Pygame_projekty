import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Player/jump.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('C:/Projekty/Pygame/Runner/audio/jump.mp3')
        self.jump_sound.set_volume(0.2)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    def applay_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    def update(self):
        self.player_input()
        self.applay_gravity()
        self.player_animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'fly':
            fly_frame1 = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Fly/Fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Fly/Fly2.png').convert_alpha()
            self.frames= [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            snail_frame1 =pygame.image.load('C:/Projekty/Pygame/Runner/graphics/snail/snail1.png').convert_alpha()
            snail_frame2 =pygame.image.load('C:/Projekty/Pygame/Runner/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300
        self. animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom =(randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

def display_score():
    current_time = round((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect ( center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time


def collision_spirte():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else: return True

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:/Projekty/Pygame/Runner/font/Pixeltype.ttf',50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('C:/Projekty/Pygame/Runner/audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.05)

#Grupy
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()
#Tło
sky_surface = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/ground.png').convert()

#Ekran startowy
player_scale = pygame.image.load('C:/Projekty/Pygame/Runner/graphics/Player/player_stand.png').convert_alpha()
player_scale = pygame.transform.rotozoom(player_scale,0,2).convert_alpha()
player_scale_rect = player_scale.get_rect(midbottom =(400,250))

#Tytuł, instrukcja
title= test_font.render('Pixel'+' Runner', False, (111,196,169))
title_rect = title.get_rect(center = (400,50))

instruction = test_font.render('Press ' 'space ' 'to ' 'play ' 'Runner', False, (111,196,169))
instruction_rect =instruction.get_rect(center =(400,300))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score()
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        #Collision
        game_active = collision_spirte()
    else:
        screen.fill((94,129,162))
        screen.blit(player_scale,player_scale_rect)
        screen.blit(title,title_rect)
        score_message = test_font.render(f'Your Score:{score}',False,(11,196,169))
        score_message_rect = score_message.get_rect(center = (400,300))
        if score == 0:
            screen.blit(instruction,instruction_rect)
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update()
    clock.tick(60)
