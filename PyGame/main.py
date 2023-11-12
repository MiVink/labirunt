
from pygame import *

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption("Dying Light")

background = transform.scale(image.load("dl_city.jpg"), (w, h))

class GameSprite(sprite.Sprite):
    def __init__(self, pImage, pX, pY, pSpeed):
        super().__init__()
        self.image = transform.scale(image.load(pImage), (70, 70))
        self.speed = pSpeed
        self.rect = self.image.get_rect()
        self.rect.x = pX
        self.rect.y = pY
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < w-70:
            self.rect.x += self.speed
        
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < h-70:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'

    def updateX(self, left_side, right_side):
        if self.rect.x <= left_side:
            self.direction = "right"
        if self.rect.x >= right_side:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
    direction2 = 'up'
    def updateY(self, up_side, down_side):
        if self.rect.y <= up_side:
            self.direction2 = "down"
        if self.rect.y >= down_side:
            self.direction2 = "up"

        if self.direction2 == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, width, height):
        super().__init__()
        self.c1 = c1
        self.c2 = c2    
        self.c3 = c3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player("dl_cranee2.png", 5, 5, 4)
enemy = Enemy("dl_zombie.png", w-70, 300, 3)
enemy2 = Enemy("dl_zombie.png", 120, 325, 2.3)
enemy3 = Enemy("dl_zombie.png", 220, 160, 2.5)
treasure = GameSprite("dl_save.png", 550, 400, 0)



game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("dl_sound.mp3")
mixer.music.play()
#55, 186, 99
w1 = Wall(24, 29, 27, 100, 100, 10, 200)
w2 = Wall(24, 29, 27, 0, 300, 110, 10)
w3 = Wall(24, 29, 27, 200, 100, 300, 10)
w4 = Wall(24, 29, 27, 200, 200, 10, 200)
w5 = Wall(24, 29, 27, 200, 300, 250, 10)
w6 = Wall(24, 29, 27, 300, 300, 10, 300)
w7 = Wall(24, 29, 27, 450, 10, 10, 200)
w8 = Wall(24, 29, 27, 450, 200, 250, 10)
w9 = Wall(24, 29, 27, 450, 300, 10, 250)

font.init()
font = font.Font(None, 40)
lose = font.render("YOU LOSE", True, (255, 0, 0))
win = font.render("YOU WIN", True, (255, 0, 0))
def collidePW(wall, player):
    global lose
    global finish
    if sprite.collide_rect(wall, player):
        finish = True
        window.blit(lose, (300, 200))
        #kick.play()

def collideG(treasure, player):
    global lose
    global finish
    if sprite.collide_rect(treasure, player):
        finish = True
        window.blit(win, (300, 200))
        money.play()

def collideE(enemy, player):
    global lose
    global finish
    if sprite.collide_rect(enemy, player):
        finish = True
        window.blit(lose, (300, 200))
        #kick.play()

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0,0))
        collidePW(w1, player)
        collidePW(w2, player)
        collidePW(w3, player)
        collidePW(w4, player)
        collidePW(w5, player)
        collidePW(w6, player)
        collidePW(w7, player)
        collidePW(w8, player)
        collidePW(w9, player)
        collideE(enemy, player)
        collideE(enemy2, player)
        collideE(enemy3, player)
        collideG(treasure, player)

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        player.draw()
        enemy.draw()
        enemy2.draw()
        enemy3.draw()
        treasure.draw()

        player.update()
        treasure.update()
        enemy.updateX(450, 650)
        enemy2.updateY(0, 440)
        enemy3.updateY(100, 250)

    display.update()
    clock.tick(FPS)


