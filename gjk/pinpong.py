from pygame import*
window = display.set_mode((700,500))
display.set_caption('Пинпонг')
background = transform.scale(image.load('a.jpg'),(700,500))

clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, Image, xx,yy, x, y, speed):
        super().__init__()

        self.image = transform.scale(
           image.load(Image),
            (xx,yy)
        )
        self.rect = self.image.get_rect()
        self.Speed = speed

        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y
   

    def show(self, Window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def Control(self, keys):
        if keys[pygame.K_a] and self.y >5:
            self.y -= self.speed
        if keys[pygame.K_d] and self.y < 555:
            self.y += self.speed
    
    def Control2(self, keys):
        if keys[pygame.K_UP] and self.y >5:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < 555:
            self.y += self.speed
p1 = Player('a1.png', 20, 100, 20, 150, 5)
p2 = Player('a1.png', 20, 100, 660, 150, 5)
m0 = GameSprite('b1', 20, 20, 0, 0, 15)
game = True
while game:
    window.blit(background,(0,0))
    p1.show(window)
    p2.show(window)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
