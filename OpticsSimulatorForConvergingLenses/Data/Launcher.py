#Importing extensions.
import sys
import pygame
import math
import webbrowser
import time
#Importing important elements.
from pygame import *
pygame.init()
#Images.
Logo=pygame.image.load("Optique logo.png")
French_Flag=pygame.image.load("French flag.png")
UK_flag=pygame.image.load("UK flag.png")
pygame.display.set_icon(Logo)
pygame.display.set_caption('Optics Simulator.')

#Font and text.
font = pygame.font.Font('3666-font.otf', 32)
text = font.render('Langue/Language :', True, (255, 255, 255), 1)
choix_1 = font.render('Français.', True, (255, 255, 255), 1)
choix_2 = font.render('English.', True, (255, 255, 255), 1)
bouton_gauche=0

#Main loop.
screen = pygame.display.set_mode([700, 600])


running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if (pygame.key.get_pressed()[pygame.K_RIGHT]==True) :
        bouton_gauche=1
    if (pygame.key.get_pressed()[pygame.K_LEFT]==True) :
        bouton_gauche=0
    
    screen.fill((0, 0, 0))
    screen.blit(French_Flag, (30, 230))
    screen.blit(UK_flag, (350, 250))
    screen.blit(text, (225, 115))
    screen.blit(choix_1, (115, 445))
    screen.blit(choix_2, (455, 445))
    pygame.draw.rect(screen, (10, 10, 10), (10, 20, 680, 560), 15)
    pygame.draw.rect(screen, (20, 20, 20), (15, 25, 670, 555), 5)
    if bouton_gauche==1 :
        pygame.draw.rect(screen, (255, 0, 0), (445, 435, 150, 55), 5)
        pygame.draw.rect(screen, (225, 0, 0), (445, 435, 150, 55), 4)
        pygame.draw.rect(screen, (185, 0, 0), (445, 435, 150, 55), 3)
        pygame.draw.rect(screen, (155, 0, 0), (445, 435, 150, 55), 2)
        pygame.draw.rect(screen, (125, 0, 0), (445, 435, 150, 55), 1)
    else :
        
        pygame.draw.rect(screen, (255, 0, 0), (105, 435, 150, 55), 5)
        pygame.draw.rect(screen, (225, 0, 0), (105, 435, 150, 55), 4)
        pygame.draw.rect(screen, (185, 0, 0), (105, 435, 150, 55), 3)
        pygame.draw.rect(screen, (155, 0, 0), (105, 435, 150, 55), 2)
        pygame.draw.rect(screen, (125, 0, 0), (105, 435, 150, 55), 1)
    
    if (pygame.key.get_pressed()[pygame.K_RETURN]==True and bouton_gauche==1) :
        webbrowser.open_new_tab("English version of the simulator.html")
        pygame.time.delay(1500)
        sys.exit()
    if (pygame.key.get_pressed()[pygame.K_RETURN]==True and bouton_gauche==0) :
        webbrowser.open_new_tab("simulateur lentilles convergentes physique.html")
        pygame.time.delay(1500)
        sys.exit()
    pygame.display.flip()


pygame.quit()