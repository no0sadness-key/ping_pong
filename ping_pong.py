from pygame import *
font.init()

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('поле.webp'), (700, 500))
game = True
finish = False
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, imageo, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(imageo), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 320:
            self.rect.y += 10
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_l] and self.rect.y < 320:
            self.rect.y += 10
            
left = Player('платформа1.png', 2, 10, 200, 20, 180)
right = Player('платформа2.png', 2, 670, 200, 20, 180)


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    window.blit(background,(0,0))
    left.reset()
    left.update_left()
    right.reset()
    right.update_right()
    display.update()
    clock.tick(60)