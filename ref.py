import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((397, 562))


N = 1
i = 1
z = 1
#___________________________________________________________________________________________________
#фон
rect(screen, (175, 221, 233), (0, 0, 397, 562))  # ãîëóáîé ôîí

# горы
polygon(screen, (179, 179, 179), [(0, 173), (47, 56),
                                  (83, 136), (136, 74),
                                  (237, 224), (309, 69),
                                  (333, 86), (397, 19),
                                  (397, 332), (222, 332),
                                  (222, 282), (0, 296)])
polygon(screen, (0, 0, 0), [(0, 173), (47, 56),
                            (83, 136), (136, 74),
                            (237, 224), (309, 69),
                            (333, 86), (397, 19),
                            (397, 332), (222, 332),
                            (222, 282), (0, 296)], 2)

# поле
polygon(screen, (170, 222, 135), [(0, 296), (222, 282),
                                  (222, 332), (397, 332),
                                  (397, 562), (0, 562)])
polygon(screen, (0, 0, 0), [(0, 296), (222, 282),
                            (222, 332), (397, 332),
                            (397, 562), (0, 562)], 1)
##___________________________________________________________________________________________________
# куст
cc = [
    [350, 370]#правый
    ,
      [100, 320]#левый
    ,
      [300, 500]#нижний
]
for coord in cc:
    circle(screen, (113, 200, 55), (coord[0], coord[1]), coord[1] // 10)#куст_зел

    # romashki
    ellipse(screen, (255, 255, 255), (coord[0] + 10, coord[1] - 30, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] + 10, coord[1] - 30, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] - 0, coord[1] - 33, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] - 0, coord[1] - 33, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] - 5, coord[1] - 30, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] - 5, coord[1] - 30, 20, 10), 1)

    ellipse(screen, (255, 255, 0), (coord[0] - 0, coord[1] - 25, 20, 10))

    ellipse(screen, (255, 255, 255), (coord[0] + 10, coord[1] - 20, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] + 10, coord[1] - 20, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] + 15, coord[1] - 25, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] + 15, coord[1] - 25, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] - 15, coord[1] - 25, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] - 15, coord[1] - 25, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] - 10, coord[1] - 20, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] - 10, coord[1] - 20, 20, 10), 1)

    ellipse(screen, (255, 255, 255), (coord[0] - 0, coord[1] - 17, 20, 10))
    ellipse(screen, (190, 191, 188), (coord[0] - 0, coord[1] - 17, 20, 10), 1)
#___________________________________________________________________________________________________

for i in range (N):
    def draw_lama(x, y, k):

        # telo
        ellipse(screen, (255, 255, 255), (x+70//k, y+345//k, 91//k, 38//k))
        ellipse(screen, (255, 255, 255), (x+140//k, y+298//k, 25//k, 64//k))
        ellipse(screen, (255, 255, 255), (x+140//k, y+285//k, 38//k, 19//k))

        # uhi
        polygon(screen, (255, 255, 255), [(x+143//k, y+294//k), (x+135//k, y+273//k), (x+152//k, y+293//k)])
        polygon(screen, (255, 255, 255), [(x+153//k, y+294//k), (x+145//k, y+273//k), (x+162//k, y+293//k)])

        # telo
        ellipse(screen, (255, 255, 255), (x+70//k, y+345//k, 91//k, 38//k))
        ellipse(screen, (255, 255, 255), (x+140//k, y+298//k, 25//k, 64//k))
        ellipse(screen, (255, 255, 255), (x+140//k, y+285//k, 38//k, 19//k))

        # nogi pered blij
        ellipse(screen, (255, 255, 255), (x+140//k, y+370//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+140//k, y+395//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+143//k, y+423//k, 14//k, 10//k))

        # nogi pered dal
        ellipse(screen, (255, 255, 255), (x+125//k, y+360//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+125//k, y+385//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+128//k, y+413//k, 14//k, 10//k))

        # nogi zad blij
        ellipse(screen, (255, 255, 255), (x+95//k, y+370//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+95//k, y+395//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+98//k, y+423//k, 14//k, 10//k))

        # nogi pered dal
        ellipse(screen, (255, 255, 255), (x+75//k, y+360//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+75//k, y+385//k, 14//k, 31//k))
        ellipse(screen, (255, 255, 255), (x+78//k, y+413//k, 14//k, 10//k))

        # glaz
        circle(screen, (229, 128, 255), (x+157//k, y+293//k), 7//k)
        circle(screen, (0, 0, 0), (x+160//k, y+293//k), 3//k)

    mas_lama = [
        [210, -50, -50]
        ,
        [0, 0, 0]
        ,
        [65, 5, 55]
        ,
        [5, 55, 65]
        ]

    for coord in mas_lama:
        print(coord[0], coord[1], coord[2])
        x = coord[0]
        y = coord[1]
        k = coord[2]
        z = z + 0.1
        draw_lama(x, y + (k * i), z)
        i += 1

#___________________________________________________________________________________________________
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()