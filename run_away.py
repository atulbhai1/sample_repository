import pygame
import random
import math
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Run!')
player = pygame.image.load('player1.png')
player = pygame.transform.scale(player, (64, 64))
lost = False
already_lost = False
px = 370
py = 480
pxc = 0
pyc = 0
font = pygame.font.Font('freesansbold.ttf', 64)
def you_lost():
    over_text = font.render('GAME OVER', True, (255, 255, 255))
    gameDisplay.blit(over_text, (200, 250))

def make_player(x, y):
    gameDisplay.blit(player, (x, y))
enemy = pygame.image.load('badguy.png')
enemy = pygame.transform.scale(enemy, (64, 64))
ex = random.randint(50, 150)
ey = random.randint(50, 150)
exc = random.randint(-5, 5)
eyc = random.randint(-5, 5)
if exc == 0 or eyc == 0:
    exc = random.randint(-10, 10)
    eyc = random.randint(-10, 10)
def make_enemy(x, y):
    gameDisplay.blit(enemy, (x, y))
def collision(ob1x, ob1y, ob2x, ob2y):
    distance = math.sqrt((ob1x - ob2x) ** 2 + (ob1y - ob2y) ** 2)
    if distance < 32:
        return True
    else:
        return False
while True:
    gameDisplay.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxc = -5
            elif event.key == pygame.K_RIGHT:
                pxc = 5
            elif event.key == pygame.K_UP:
                pyc = -5
            elif event.key == pygame.K_DOWN:
                pyc = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pyc = 0
                pxc = 0
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
    px += pxc
    py += pyc
    if px < 0:
        px = 0
    elif px > 736:
        px = 736
    if py < 0:
        py = 0
    elif py > 536:
        py = 536
    if not already_lost:
        lost = collision(ex, ey, px, py)
        if lost:
            already_lost = True
    if exc == 0 or eyc == 0:
        exc = random.randint(-10, 10)
        eyc = random.randint(-10, 10)
    ex += exc
    ey += eyc
    if ex < 0:
        ex = 0
        exc = random.randint(-10, 10)
        eyc = random.randint(-10, 10)
    elif ex > 736:
        ex = 736
        exc = random.randint(-10, 10)
        eyc = random.randint(-10, 10)
    if ey < 0:
        ey = 0
        exc = random.randint(-10, 10)
        eyc = random.randint(-10, 10)
    elif ey > 536:
        ey = 536
        exc = random.randint(-10, 10)
        eyc = random.randint(-10, 10)
    make_enemy(ex, ey)
    if not lost:
        make_player(px, py)
    else:
        you_lost()
    pygame.display.update()