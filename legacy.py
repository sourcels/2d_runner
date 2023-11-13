from pygame import *
from random import randint

window = display.set_mode((800, 600))
display.set_caption('2D Runner')
display.set_icon(image.load("icon.bmp"))
background = transform.scale(image.load("background.png"), (800, 600))
game = True
lose = False
with open('best_score.txt', 'r') as file:
    best_score = file.read()
lives = 3
absortion_time = 0
with open('money.txt', 'r') as file:
    money_count = file.read()
score = 0
s_speed = 3.5
ad_timer = 0
temp_rand = randint(1, 12)
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()
font.init()
lose_txt = font.SysFont('Arial', 80).render('You lose!!', True, (0, 255, 0))
score_txt = font.SysFont('Arial', 40).render('Score:' + str(score), True, (255, 0, 255))
lives_txt = font.SysFont('Arial', 90).render('x' + str(lives), True, (255, 0, 0))
money_txt = font.SysFont('Arial', 40).render(money_count, True, (25, 150, 25))

class gamespr(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(gamespr):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 349:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= 623:
            self.rect.x += self.speed


class abuser(gamespr):
    def update(self):
        self.rect.y += self.speed


wall1 = gamespr('vertical_wall.png', 725, 0, 75, 820, 0)
wall2 = gamespr('vertical_wall.png', 275, 0, 75, 820, 0)
avatar = gamespr('avatar.png', 0, 150, 125, 125, 0)
s_speed = 3
money = gamespr('money.png', 0, 45, 75, 75, s_speed)
player1000_7 = Player('KANEKI.png', 500, 425, 100, 100, s_speed)
dmg1 = sprite.Group()
addvertise = gamespr('ad' + str(temp_rand) + '.png', 0, 400, 275, 200, 0)
for i in range(2):
    if (randint(1, 2) == 1):
        zxc1 = abuser('rule.png', 349, 0, 90, 75, s_speed)
    elif (randint(1, 2) == 2):
        zxc1 = abuser('rule.png', 486, 0, 90, 75, s_speed)
    else:
        zxc1 = abuser('rule.png', 623, 0, 90, 75, s_speed)
    dmg1.add(zxc1)
dmg2 = sprite.Group()
for i in range(2):
    if (randint(1, 2) == 1):
        zxc2 = abuser('rule.png', 349, -100, 90, 75, s_speed)
    elif (randint(1, 2) == 2):
        zxc2 = abuser('rule.png', 486, -100, 90, 75, s_speed)
    else:
        zxc2 = abuser('rule.png', 623, -100, 90, 75, s_speed)
    dmg2.add(zxc2)
brawl_stars = sprite.Group()
for i in range(2):
    if (randint(1, 3) == 2):
        if (randint(1, 2) == 1):
            monk = abuser('money.png', 349, -200, 90, 75, s_speed)
        elif (randint(1, 2) == 2):
            monk = abuser('money.png', 486, -200, 90, 75, s_speed)
        else:
            monk = abuser('money.png', 623, -200, 90, 75, s_speed)
        brawl_stars.add(monk)
    else:
        monk = abuser('money.png', 1000, -200, 90, 75, s_speed)
        brawl_stars.add(monk)
while game:
    window.blit(background, (0, 0))
    window.blit(score_txt, (0, 0))
    window.blit(lives_txt, (160, 170))

    addvertise.reset()
    wall1.reset()
    wall2.reset()
    avatar.reset()
    money.reset()
    ad_timer += 1
    window.blit(money_txt, (90, 60))
    if (ad_timer >= 500):
        temp_rand = randint(1, 12)
        addvertise = gamespr('ad' + str(temp_rand) + '.png', 0, 400, 275, 200, 0)
        score += 25
        score_txt = font.SysFont('Arial', 40).render('Score:' + str(score), True, (255, 0, 0))
        ad_timer = 0
    if lives <= 0:
        window.blit(lose_txt, (400, 300))
        best_score = score
        score = 0
    else:
        player1000_7.reset()
        player1000_7.update()
        if (zxc1.rect.y >= 600):
            for i in range(2):
                if (randint(1, 3) == 1):
                    zxc1 = abuser('rule.png', 349, 0, 90, 75, s_speed)
                elif (randint(1, 3) == 2):
                    zxc1 = abuser('rule.png', 486, 0, 90, 75, s_speed)
                else:
                    zxc1 = abuser('rule.png', 623, 0, 90, 75, s_speed)
            dmg1.add(zxc1)
        if (zxc2.rect.y >= 600):
            for i in range(2):
                if (randint(1, 2) == 1):
                    zxc2 = abuser('rule.png', 349, -100, 90, 75, s_speed)
                elif (randint(1, 2) == 2):
                    zxc2 = abuser('rule.png', 486, -100, 90, 75, s_speed)
                else:
                    zxc2 = abuser('rule.png', 623, -100, 90, 75, s_speed)
            dmg2.add(zxc2)
        if (monk.rect.y >= 600):
            for i in range(2):
                if (randint(1, 3) == 2):
                    if (randint(1, 2) == 1):
                        monk = abuser('money.png', 349, -200, 90, 75, s_speed)
                    elif (randint(1, 2) == 2):
                        monk = abuser('money.png', 486, -200, 90, 75, s_speed)
                    else:
                        monk = abuser('money.png', 623, -200, 90, 75, s_speed)
            brawl_stars.add(monk)
        if absortion_time >= 0:
            absortion_time -= 1
        if sprite.spritecollide(player1000_7, dmg1, False) and absortion_time <= 0 or sprite.spritecollide(player1000_7,
                                                                                                           dmg2,
                                                                                                           False) and absortion_time <= 0:
            lives -= 1
            lives_txt = font.SysFont('Arial', 90).render('x' + str(lives), True, (255, 0, 0))
            absortion_time = 125
        if sprite.spritecollide(player1000_7, brawl_stars, False):
            money_count += 1
            money_txt = font.SysFont('Arial', 40).render(money_count, True, (25, 150, 25))
        dmg1.update()
        dmg1.draw(window)
        dmg2.update()
        dmg2.draw(window)
        brawl_stars.update()
        brawl_stars.draw(window)
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                lives = 3
    display.update()
    clock.tick(FPS)