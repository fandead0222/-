import pygame as pg


def q2():
    pg.quit()
    pg.init()
    screen = pg.display.set_mode((1000, 800), 0, 32)
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.update()
    font = pg.font.Font("fonts/haha.ttc", 24)
    begin = font.render("在座的各位都是電神", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 100))
    pg.display.update()
    begin = font.render("據說「態度」 == 25枚硬幣呢", True, (0, 0, 0), (255, 255, 255))
    screen.blit(begin, (100, 200))
    pg.display.update()
