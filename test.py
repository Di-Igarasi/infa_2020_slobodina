import pygame

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

rect(screen, (135, 206, 250), (0, 0, 800, 300)) #небо
rect(screen, (34, 139, 34 ), (0,300, 800,500))  #земля

rect(screen, (0, 0, 0), (600, 270, 25, 130))    #ствол дерева
ellipse(screen, (0, 100, 0), (610, 240, 70, 70)) #круг1
ellipse(screen, (0, 0, 0), (610, 240, 70, 70), 1)
ellipse(screen, (0, 100, 0), (540, 235, 70, 70)) #круг2
ellipse(screen, (0, 0, 0), (540, 235, 70, 70), 1)
ellipse(screen, (0, 100, 0), (575, 205, 70, 70)) #круг3
ellipse(screen, (0, 0, 0), (575, 205, 70, 70), 1)
ellipse(screen, (0, 100, 0), (615, 190, 70, 70)) #круг4
ellipse(screen, (0, 0, 0), (615, 190, 70, 70), 1)
ellipse(screen, (0, 100, 0), (535, 185, 70, 70)) #круг5
ellipse(screen, (0, 0, 0), (535, 185, 70, 70), 1)
ellipse(screen, (0, 100, 0), (575, 150, 70, 70)) #круг6
ellipse(screen, (0, 0, 0), (575, 150, 70, 70), 1)

ellipse(screen, (255, 250, 250), (300, 100, 70, 70)) #облако1
ellipse(screen, (0, 0, 0), (300, 100, 70, 70), 1)
ellipse(screen, (255, 250, 250), (340, 100, 70, 70)) #облако2
ellipse(screen, (0, 0, 0), (340, 100, 70, 70), 1)
ellipse(screen, (255, 250, 250), (380, 100, 70, 70))#облако3
ellipse(screen, (0, 0, 0), (380, 100, 70, 70), 1)
ellipse(screen, (255, 250, 250), (420, 100, 70, 70))#облако4
ellipse(screen, (0, 0, 0), (420, 100, 70, 70), 1)
ellipse(screen, (255, 250, 250), (345, 65, 70, 70))#облако5
ellipse(screen, (0, 0, 0), (345, 65, 70, 70), 1)
ellipse(screen, (255, 250, 250), (380, 65, 70, 70))#облако6
ellipse(screen, (0, 0, 0), (380, 65, 70, 70), 1)
ellipse(screen,  (255, 218, 185), (680, 65, 70, 70))  #солнце
ellipse(screen,  (255, 99, 71), (680, 65, 70, 70), 2)

rect(screen, (160, 82, 45 ), (100,270,220 ,150)) #дом
rect(screen, (0, 0, 0 ), (100,270,220 ,150), 1)
rect(screen, (95, 158, 160 ), (179,320,65 ,45)) #окно
rect(screen, (255, 165, 0 ), (179,320,65 ,45), 2)
polygon(screen, (139, 0, 0), [(319,270), (210, 183), (102,270)])#крыша
polygon(screen, (0, 0, 0), [(319,270), (210, 183), (102,270)], 1)













pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()