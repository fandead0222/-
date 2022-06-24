import pygame as pg
from time import*


def q5():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("槍槍 阿 7ki 7ki 幫幫", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 100))
    pg.display.update()
    begin = font.render("來到孔明病逝的地方就會想起這個旋律呢", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 200))
    pg.display.update()
