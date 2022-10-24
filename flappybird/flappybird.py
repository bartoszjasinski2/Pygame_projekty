
from random import randint
from tkinter import font
from tkinter.ttk import tclobjs_to_py
from typing import Counter
import pygame 



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_1 = pygame.image.load('C:/Projekty/Pygame/floppy_bird/grapihcs/bird0.png').convert_alpha()
        self.bird_2 = pygame.image.load('C:/Projekty/Pygame/floppy_bird/grapihcs/bird0.png').convert_alpha()
        self.bird_3 = pygame.image.load('C:/Projekty/Pygame/floppy_bird/grapihcs/bird0.png').convert_alpha()
        self.image = self.bird_1
        
        self.rect = self.image.get_rect(midbottom =(100,300))
        self.gravity = 0 
        self.player = self.rect

    def gravity_apllay(self):
        self.gravity += 0.5
        self.rect.y += self.gravity

    def player_position(self):
        if self.rect.y >= 700:
            self.rect.y = randint(300,400)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gravity = -10

#    def player_animation(self):
#        if self.rect.y > 

    def update(self):
        self.player_input()
        self.gravity_apllay()
        self.player_position()

class Top_obstaclle(Player):
    def __init__(self):
        super().__init__()
        self.distance_between_obstacle = 140 
        self.odstep_rur_y = randint(200,500)
        self.top_obst = pygame.image.load ('C:/Projekty/Pygame/floppy_bird/grapihcs/top.png').convert_alpha()
        self.top_obst_rect = self.top_obst.get_rect( topleft = (400,-250))
        self.image = self.top_obst
        self.rect = self.top_obst_rect

 
    def score_dispaly(self):
        screen.blit = (self.score_surface,(self.score_rect))
        pygame.display.flip()
        
    def top_obstacle_movment(self):
        self.rect.x -= 5
        if self.rect.x < -100:
            self.rect.x = 400
            self.top_obstacle_distance()

    def top_obstacle_distance(self):
        self.rect.y = odstep_rur_y - (self.distance_between_obstacle//2 + 500)
        

    def update(self):
        self.top_obstacle_movment()

class Bottom_obstaclle(Top_obstaclle):
    def __init__(self):
        super().__init__()
        self.distance_between_obstacle = 200
        self.bottom_obst = pygame.image.load ('C:/Projekty/Pygame/floppy_bird/grapihcs/bottom.png').convert_alpha()
        self.bottom_obst_rect = self.bottom_obst.get_rect(bottomleft =(400,950))
        self.image = self.bottom_obst
        self.rect = self.bottom_obst_rect

    
    def bottom_obstacle_movment(self):
        self.rect.x -= 5
        if self.rect.x < -100:
            self.rect.x = 400
            self.bottom_obstacle_distance()

    def bottom_obstacle_distance(self): 
        self.rect.y = odstep_rur_y + self.distance_between_obstacle//2

    def update(self):
      self.bottom_obstacle_movment()
        
def counter_show():
    score_surface = score_font.render(f'Score: {str(score)}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (200,150))
    screen.blit(score_surface,score_rect)
    if player.rect.x == t_obstacle.rect.x:
        score += 1


def counter_show_v2():
    global score
    score_surface = score_font.render(f'Score: {str(score)}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (200,150))
    screen.blit(score_surface,score_rect)
    if player.rect.x == t_obstacle.rect.x:
        score += 1
    return score

def collision():
    if pygame.sprite.spritecollide(player,all_sprite,False):
        all_sprite.empty()
        return True
    else: return False

#Obrazy i protokąty 

pygame.init()
#parametry i zmienne 
screen = pygame.display.set_mode((400,700))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()
game_status = False
score = 0
score_font = pygame.font.Font('C:/Projekty/Pygame/floppy_bird/grapihcs/Pixeltype.ttf',50)
flappy_font = pygame.font.Font('C:/Projekty/Pygame/floppy_bird/grapihcs/FlappyBirdy.ttf',50)
#Ekran startowy 
flappy_stant = pygame.image.load('C:/Projekty/Pygame/floppy_bird/grapihcs/bird0.png')
flappy_stant = pygame.transform.rotozoom(flappy_stant,0,2).convert_alpha()
flappy_stant_rect = flappy_stant.get_rect(center = (200,350))
#Tytuł i instrukcje 
title = flappy_font.render('Flappy Bird',False,(146, 12, 204))
title = pygame.transform.rotozoom(title,0,2).convert_alpha()
instruction = score_font.render('Press space', False, (146,12,204))
instruction_v2 = score_font.render('to start the game', False,(146,12,204))

title_rect = title.get_rect(center = (200,200))
instruction_rect = instruction.get_rect(center = (200,550))
instruction_v2_rect = instruction_v2.get_rect(center = (200,580))

#Obiekty i grupy 
player = Player()
t_obstacle = Top_obstaclle()
b_obstacle = Bottom_obstaclle()
#score = Score(player)
all_sprite = pygame.sprite.Group()
score_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group() 
all_sprite.add(t_obstacle)
all_sprite.add(b_obstacle)
#score_sprite.add(score)
player_sprite.add(player)


obstacle_event = pygame.USEREVENT + 1

#Tło 
background = pygame.image.load("C:/Projekty/Pygame/floppy_bird/grapihcs/background.png")


while True:
    odstep_rur_y = randint(200,500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           # all_sprite.empty()
            game_status = False

    if game_status == False:
        screen.blit(background,(0,0))
        all_sprite.draw(screen)
        all_sprite.update()
        player_sprite.draw(screen)
        player_sprite.update()
        score = counter_show_v2()
        game_status = collision()

    elif game_status == True :
        screen.blit(background,(0,0))
        screen.blit(flappy_stant,(flappy_stant_rect))
        screen.blit(title,title_rect)

        if score == 0:
            screen.blit(instruction,instruction_rect)
            screen.blit(instruction_v2,instruction_v2_rect)
            
        else:
            print(score)
            score_message = score_font.render('Your score is: ' + f'{str(score)}',False,(146,12,204))
            score_message_rect = score_message.get_rect(center = (200,400))
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)

    

