import pygame as pg
pic = "time.png"

def q9():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    background = pg.image.load(pic).convert()
    screen.blit(background, (400, 300))
    pg.display.update()

