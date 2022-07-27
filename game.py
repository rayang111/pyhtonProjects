from pygame import *
from pygame.locals import *
import pygame
import random
import time as tt
from time import *

pygame.init()

gamewindow = pygame.display.set_mode((610, 168))

software_is_on = 1

x2 = 610
y2 = 70
x3 = 610
y3 = 80
timess = tt.localtime()[5]

def theBads_1():
    global score



    
x = 20    
y = 70
ymove = 0
done = 0
score = 0
while software_is_on:
    score += 0.035
    scoreus = int(score)
    jtime = 0
    timing = int(pygame.time.get_ticks()/1000)
    
    
    if done == 0:
        x2 -= 0.05
    if done == 1:
        x3 -= 0.05    
    gamewindow.fill((220,220,220))
    pygame.draw.line(gamewindow,(0,0,0),(0,100),(610,100),2)
    

    for event in pygame.event.get():
        if event.type == QUIT:
            software_is_on = 0
            pygame.quit()
            print(score)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                ymove = 1
    if ymove == 1:
        times = tt.localtime()[5]
        jtime = times - timess
        y -= 5
        if jtime > 0.25:
            y = 70
            ymove = 0

                
        
    if x2 < -35:
        if done == 0:
            done = 1
        x2 = 610
    if x3 < -50:
        x3 = 610
        done = 2
        
    
    mainchac = pygame.Rect(x,y,35,45)
    theBads_1 = pygame.Rect(x2,y2,35,45)
    theBads_2 = pygame.Rect(x3,y3,50,35)
    pygame.draw.rect(gamewindow,(0,0,0),mainchac)
    pygame.draw.rect(gamewindow,(0,0,0),theBads_1)
    pygame.draw.rect(gamewindow,(0,0,0),theBads_2)
    pygame.display.flip()
