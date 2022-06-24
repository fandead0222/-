import pygame as pg
from time import*


def q3():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("等待是一種美德", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 100))
    pg.display.update()
    sleep(2.5)
    begin = font.render("你還真得等了喔，不嫌無聊嗎哈哈", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 200))
    pg.display.update()
    sleep(2)
    begin = font.render("酒杯的形狀真像x^2-6x+9呢，甚麼時候會見底呢?", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 300))
    pg.display.update()
