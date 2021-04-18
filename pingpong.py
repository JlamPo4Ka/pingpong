from pygame import *
#
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#
background = transform.scale(image.load("fonchik.jpg"), (1280, 700))
gg = transform.scale(image.load("sprite2.png"), (70, 70))
g2g = transform.scale(image.load("sprite1.png"), (70, 70))
#
y1 = 100
x1 = 25
y2 = 100
x2 = 600
gm = True
while gm:
    #okno.fill((46, 139, 87))
    okno.blit(background, (0, 0))
    okno.blit(gg, (x1, y1))
    okno.blit(g2g, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            gm = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_DOWN]:
        y1 += 5
    if keys_pressed[K_UP]:
        y1 -= 5
#2 игрок

    if keys_pressed[K_s]:
        y2 += 5
    if keys_pressed[K_w]:
        y2 -= 5
#
    display.update()
    fpsiki.tick(FPS) 