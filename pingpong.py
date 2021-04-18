from pygame import *
#?окно и фпс
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#?фон
background = transform.scale(image.load("FON.png"), (700, 500))
#?классы
class objekt(sprite.Sprite): #*основной класс
    def __init__(self, pic, px, py, ph, pw):    
        super().__init__()
        self.image = transform.scale(image.load(pic), (pw, ph))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class playir(objekt): #*игрок
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_w] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
gg = playir("sprite2.png", 25, 100, 65, 65)
class playir2(objekt): #*игрок2
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_UP] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
g2g = playir2("sprite1.png", 625, 100, 65 ,65)
class ball(objekt): #*мяч
    def update(self):
        if self.rect.x < 0:
            self.rect.x += 4
myach = ball("Ball.png", 320, 200, 110, 65)
#?игровой цикл
gm = True
while gm:
    okno.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            gm = False

#!поведение мяча
#!bsy = 5
#!bsx = -5
#!после while
#!мяч.rect.x += bsx
#!мяч.rect.y += bsy
#!столкновение
#!bsx *= -1
#!bsy *= -1

#?функции
    myach.update()
    myach.reset()
    gg.update()
    gg.reset()
    g2g.update()
    g2g.reset()
    display.update()
    fpsiki.tick(FPS) 
