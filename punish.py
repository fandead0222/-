import pygame as pg
from time import*
pic = "pic.jpg"
cry = "cry.mp3"


def punish():
    # 開工管的懲罰
    for i in range(5):
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        background = pg.image.load(pic).convert()
        s = pg.mixer.Sound(cry)
        s.set_volume(100)
        s.play()
        background = pg.transform.scale(background, (1600, 960))
        screen.blit(background, (0, 0))
        pg.display.update()
        sleep(0.4)
        pg.quit()
