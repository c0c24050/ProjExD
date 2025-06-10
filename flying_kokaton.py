import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習8
    tori_img = pg.image.load("fig/3.png")#練習3
    tori_img = pg.transform.flip(tori_img, True, False)#練習3後半
    tori_rct = tori_img.get_rect()
    tori_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#練習10-->演習1
        dx = -1
        dy = 0

        if key_lst[pg.K_UP]:
            dy = -1
        if key_lst[pg.K_DOWN]:
            dy = 1
        if key_lst[pg.K_RIGHT]:
            dx = 0
        tori_rct.move_ip(dx, dy)#演習2
        screen.blit(bg_img, [-tmr, 0])#練習5
        screen.blit(tori_img, tori_rct)#練習4-->10
        pg.display.update()
        tmr += 1
        clock.tick(200)#練習6
        x = tmr%3200#練習9
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])#練習7-->8
        screen.blit(bg_img, [-x+3200, 0])


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()