import pygame
import random as rd
from questions import*
from pygame.locals import*
import continu


def q10():
    width = 1000
    height = 800
    color_background = (0, 0, 0)
    color_inactive = (100, 100, 200)
    color_active = (200, 200, 255)
    color = color_inactive
    text = ""
    active = False
    running = True

    pygame.quit()
    pygame.init()
    screen = pygame.display.set_mode((width, height), 0, 32)

    font = pygame.font.Font("fonts/haha.ttc", 23)

    input_box = pygame.Rect(100, 100, 140, 32)
    while running:
        for event in pygame.event.get():
            # 懲罰
            key = pygame.key.get_pressed()
            if key[K_RALT] or key[K_LALT] or key[K_LCTRL] or key[K_RCTRL]:
                continu.cont()
            # 跳出輸入密碼
            if event.type == pygame.QUIT:
                running = False
            # 偵測是否要輸入密碼
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = True if input_box.collidepoint(event.pos) else False
                # 點集框框時變色
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        k = text
                        if k == "3754":
                            exit()
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        text_surface = font.render(text, True, color)
        input_box.center = (width/2, height/2)

        # 更新
        screen.fill(color_background)
        screen.blit(text_surface, (input_box.x+5, input_box.y))
        pygame.draw.rect(screen, color, input_box, 3)
        pygame.display.flip()
        tex = font.render("要重新找答案請按右上角三次", True, (255, 255, 255))
        screen.blit(tex, (500, 100))
        pygame.display.update()



