import pygame as pg
from time import*


def q4():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    pg.display.set_caption("好像有誰講過態度的和是多少來著")
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("有時候要跳脫一下框架", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (600, 600))
    pg.display.update()
