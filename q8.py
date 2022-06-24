import pygame as pg
pic = "d.png"


def q8():
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    background = pg.image.load(pic).convert()
    screen.blit(background, (450, 350))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("大老二老大 茅野愛衣 梅花三弄 正方角數 ", True, (255, 255, 255), (0, 0, 0))
    screen.blit(begin, (100, 100))
    pg.display.update()
