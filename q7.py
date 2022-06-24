import pygame as pg
from time import*


def q7():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("哪種劍看不到？", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 100))
    pg.display.update()
    sleep(2)
    begin = font.render("看不見!!", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 200))
    pg.display.update()
    sleep(1)
    begin = font.render("那哪種劍拔不出來呢", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 400))
    pg.display.update()
