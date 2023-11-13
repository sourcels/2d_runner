from pygame import *
from random import randint
from cryptography.fernet import Fernet
import pickle, os

SAVE_KEY = b'MhomXZKEikLv5k-iYX5MpE7d56TTOVpsZe8eqkgPz3I='

window = display.set_mode((800, 600))
display.set_caption('2D Runner')
display.set_icon(image.load("assets/icon.bmp"))
background = transform.scale(image.load("assets/background.png"), (800, 600))

def load(key: bytes | str) -> dict:
    cipher_suite = Fernet(key)
    api_folder_path = os.path.join(os.path.expanduser('~'), ".2d_runner")
    save_file_path = os.path.join(api_folder_path, "data.bin")
    try:
        with open(file=save_file_path, mode='r') as file:
            cipher_text = file.read()
        data = eval(cipher_suite.decrypt(cipher_text).decode(encoding="utf-8"))
    except FileNotFoundError:
        os.mkdir(api_folder_path) if not os.path.exists(api_folder_path) else ...
        data = {}
    return data

def save(key: bytes | str, data: dict) -> None:
    cipher_suite = Fernet(key)
    data_str = str(data)
    cipher_text = cipher_suite.encrypt(data_str.encode(encoding="utf-8"))
    api_folder_path = os.path.join(os.path.expanduser('~'), ".2d_runner")
    save_file_path = os.path.join(api_folder_path, "data.bin")
    with open(file=save_file_path, mode='wb') as file:
        file.write(cipher_text)

data = load(SAVE_KEY)
score = 0
s_speed = 3.5
timer = 0
game = True
lose = False
clock = time.Clock()
FPS = 75
mixer.init()
mixer.music.load('assets/music.ogg')
mixer.music.play()
font.init()
lose_txt = font.SysFont('Arial', 80).render('You lose!!', True, (0, 255, 0))

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
    def __init__(self, sprite_image, x, y, size_x, size_y, speed):
        super().__init__(sprite_image, x, y, size_x, size_y, speed)
        self.lives = 3
        self.absortion_time = 0
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x >= 349:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <= 623:
            self.rect.x += self.speed

class Obstacle(gamespr):
    def __init__(self):
        x, y = self.revoke()
        super().__init__("assets/rule.png", x, y, 90, 75, 3)

    def revoke(self) -> (int, int):
        for i in range(2):
            rand = randint(0, 2)
            if (rand == 0):
                x = 349
            elif (rand == 1):
                x = 486
            else:
                x = 623
            rand = randint(0, 1)
            if (rand == 0):
                y = 0
            else:
                y = -110
        return x, y

    def update(self, player: Player):
        if sprite.spritecollide(player, dmg, False) and player.absortion_time <= 0:
            player.lives -= 1
            global lives_txt
            lives_txt = font.SysFont('Arial', 90).render('x' + str(player.lives), True, (255, 0, 0))
            player.absortion_time = FPS * 2
        self.rect.y += self.speed

class Treasure(gamespr):
    def __init__(self):
        x, y = self.revoke()
        super().__init__("assets/money.png", x, y, 90, 75, 3)

    def revoke(self) -> (int, int):
        rand = randint(0, 1)
        x = 349
        if (rand == 0):
            x = 486
        elif (rand == 1):
            x = 623
        y = -200
        return x, y

    def update(self, player: Player):
        if sprite.spritecollide(player, brawl_stars, True):
            data["money"] += 1
            global money_txt
            money_txt = font.SysFont('Arial', 40).render(str(data["money"]), True, (25, 150, 25))
        self.rect.y += self.speed

player = Player('assets/KANEKI.png', 500, 425, 100, 100, s_speed)
wall1 = gamespr('assets/vertical_wall.png', 725, 0, 75, 820, 0)
wall2 = gamespr('assets/vertical_wall.png', 275, 0, 75, 820, 0)
avatar = gamespr('assets/avatar.png', 0, 150, 125, 125, 0)
lives_txt = font.SysFont('Arial', 90).render('x' + str(player.lives), True, (255, 0, 0))
score_txt = font.SysFont('Arial', 40).render('Score:' + str(score), True, (255, 0, 255))
money_txt = font.SysFont('Arial', 40).render(str(data["money"]), True, (25, 150, 25))
best_score_txt = font.SysFont('Arial', 40).render("Best score: " + str(data["best"]), True, (100, 150, 25))
advertise_banner = gamespr('assets/ad' + str(randint(1, 12)) + '.png', 0, 400, 275, 200, 0)
money = gamespr('assets/money.png', 0, 45, 75, 75, s_speed)
brawl_stars = sprite.Group()
dmg = sprite.Group()
while game:
    window.blit(background, (0, 0))
    window.blit(score_txt, (0, 0))
    window.blit(best_score_txt, (0, 300))
    window.blit(lives_txt, (160, 170))

    advertise_banner.reset()
    wall1.reset()
    wall2.reset()
    avatar.reset()
    money.reset()
    timer += 1
    window.blit(money_txt, (90, 60))
    if player.absortion_time > 0:
        player.absortion_time -= 1
    if timer >= FPS * 10:
        advertise_banner = gamespr('assets/ad' + str(randint(1, 12)) + '.png', 0, 400, 275, 200, 0)
        timer = 0
    if player.lives > 0:
        if timer % FPS == 0:
            score += 1
            score_txt = font.SysFont('Arial', 40).render('Score:' + str(score), True, (255, 0, 255))
            if randint(0, 1) == 1:
                brawl_stars.add(Treasure())
        if timer % FPS * 1.5 == 0:
            dmg.add(Obstacle())
        player.reset()
        player.update()
        for obstacle in dmg:
            if obstacle.rect.y >= 600 or not obstacle.alive():
                obstacle.kill()
        for treasure in brawl_stars:
            if treasure.rect.y >= 600 or not treasure.alive():
                treasure.kill()
        dmg.update(player)
        dmg.draw(window)
        brawl_stars.update(player)
        brawl_stars.draw(window)
    else:
        window.blit(lose_txt, (400, 300))
        if data["best"] < score:
            data["best"] = score
            best_score_txt = font.SysFont('Arial', 40).render("Best score: " + str(data["best"]), True, (100, 150, 25))
        score = 0
        save(key=SAVE_KEY, data=data)
    for i in event.get():
        if i.type == QUIT:
            if data["best"] < score:
                data["best"] = score
                best_score_txt = font.SysFont('Arial', 40).render("Best score: " + str(data["best"]), True, (100, 150, 25))
            save(key=SAVE_KEY, data=data)
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.lives = 3
    display.update()
    clock.tick(FPS)