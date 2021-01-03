import pygame
import random
from math import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('👾Space Invaders!')
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
baddieImg = pygame.image.load('badguy.png')
baddieImg = pygame.transform.scale(baddieImg, (64, 64))
baddieImages = []
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 490
bulletYC = 10
bulletS = 'ready'
bx = []
by = []
bxc = []
byc = []
num_of_enemies = 6
for i in range(num_of_enemies):
    baddieImages.append(baddieImg)
    byc.append(150)
    bx.append(random.randint(0, 736))
    by.append(random.randint(50, 150))
    bxc.append(1)
px = 370
py = 480
pxc = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_t():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def show_score():
    score_show = font.render(f'Score:{score}', True, (255, 255, 255))
    screen.blit(score_show, (10, 10))
def fire_bullet(x):
    global bulletS
    global bulletY
    bulletS = 'fire'
    screen.blit(bulletImg, (x + 16, bulletY))
def is_collision(ex, ey, bx1, by1):
    distance = sqrt((ex - bx1)**2 + (ey - by1)**2)
    if distance < 32:
        return True
    else:
        return False
def player(x, y):
    screen.blit(playerImg, (x, y))
def baddie(x, y):
    screen.blit(baddieImg, (x, y))
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxc = -5
            elif event.key == pygame.K_RIGHT:
                pxc = 5
            elif event.key == pygame.K_SPACE:
                if bulletS == 'ready':
                    fire_bullet(px)
                    bulletX = px
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pxc = 0
    px += pxc

    for i in range(num_of_enemies):
        if by[i] > 440:
            for j in range(num_of_enemies):
                by[j] = 2000
            game_over_t()
            break
        bx[i] += bxc[i]
        if bx[i] < 0:
            bx[i] = 0
            bxc[i] = 1
            by[i] += byc[i]
        elif bx[i] > 736:
            bx[i] = 736
            bxc[i] = -1
            by[i] += byc[i]
        collision = is_collision(bx[i], by[i], bulletX, bulletY)
        if collision:
            bulletY = 490
            bulletS = 'ready'
            score += 1
            bx[i] = random.randint(0, 736)
            by[i] = random.randint(50, 150)
            bxc[i] = 1
        baddie(bx[i], by[i])
    if bulletS == 'fire':
        fire_bullet(bulletX)
        bulletY -= bulletYC
    if bulletY < 0:
        bulletS = 'ready'
        bulletY = 490
    if px < 0:
        px = 0
    elif px > 736:
        px = 736
    player(px, py)
    show_score()
    pygame.display.update()