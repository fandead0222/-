from punish import*
from questions import*


def cont():
    # 隨機視窗
    x = rd.randint(1, 10)
    if x == 1:
        q1()
    elif x == 2:
        q2()
    elif x == 3:
        q3()
    elif x == 4:
        q4()
    elif x == 5:
        q5()
    elif x == 6:
        q6()
    elif x == 7:
        q7()
    elif x == 8:
        q8()
    elif x == 9:
        q9()
    elif x == 10:
        q10()

    while True:
        # 偵測操作
        for event in pg.event.get():
            key = pg.key.get_pressed()
            if key[K_RALT] or key[K_LALT] or key[K_LCTRL] or key[K_RCTRL]:
                punish()
                cont()
            if event.type == QUIT:
                # 重開視窗
                pg.quit()
                cont()
