from pygame import*
#Недочёт- платформу переделалить
width, height = 600,400
bg_color = (156, 176, 104)
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(_image, x,y, width, height )
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y = - self.speed
        if keys[self.key_down]:
            self.rect.x = + self.speed

mw = display.set_mode((width, height))
mw.fill(bg_color)
display.set_caption('Пин-подг')
clock = time.Clock()

player_1 = GameSprite('pixil-frame-0 (3).png', 10, 200, 30, 90)

run = True
while run:
    player_1.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)