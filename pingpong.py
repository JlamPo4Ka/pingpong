from pygame import *
#окно и фпс
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#фон
background = transform.scale(image.load("FON.png"), (700, 500))
#классы
class objekt(sprite.Sprite): #основной класс
    def __init__(self, pic, px, py):    
        super().__init__()
        self.image = transform.scale(image.load(pic), (75, 65))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class playir(objekt): #игрок
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_w] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
gg = playir("sprite2.png", 25, 100)
class playir2(objekt): #игрок2
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_UP] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
g2g = playir2("sprite1.png", 625, 100)
class ball(objekt): #мяч
    def update(self):
        if self.rect.x < 0:
            self.rect.x += 3
myach = ball("images.jpg", 320, 200)
#игровой цикл

gm = True
while gm:
    okno.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            gm = False
#апдейты и ресеты
    myach.update()
    myach.reset()
    gg.update()
    gg.reset()
    g2g.update()
    g2g.reset()
    display.update()
    fpsiki.tick(FPS) 
