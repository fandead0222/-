from continu import*

pg.init()
# 開頭
screen = pg.display.set_mode((1000, 800), 0, 32)
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))
screen.blit(bg, (0, 0))
pg.display.update()
font = pg.font.Font("fonts/haha.ttc", 50)
begin = font.render("歡迎來到無盡煉獄", True, (0, 0, 0), (255, 255, 255))
screen.blit(begin, (100, 100))
pg.display.update()
sleep(1)
begin = font.render("在解完謎之前", True, (0, 0, 0), (255, 255, 255))
screen.blit(begin, (100, 200))
pg.display.update()
sleep(1)
begin = font.render("你都出不去呦~~", True, (0, 0, 0), (255, 255, 255))
screen.blit(begin, (100, 300))
pg.display.update()
sleep(1)
begin = font.render("多久能離開就看你運氣嘍", True, (0, 0, 0), (255, 255, 255))
screen.blit(begin, (100, 400))
pg.display.update()
sleep(1)
font = pg.font.Font("fonts/haha.ttc", 20)
begin = font.render("別想開工管，你會受到懲罰", True, (255, 0, 0), (255, 255, 255))
screen.blit(begin, (200, 500))
pg.display.update()
sleep(0.5)
cont()
