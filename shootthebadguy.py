#!/usr/bin/env python3
import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Shoot The Bad Guy')
enemy = pygame.image.load('badguy.png')
pygame.display.set_icon(enemy)
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
PlayerX = 370
PlayerXC = 0
PlayerY = 400
PlayerYC = 0
player_direction = 'forwards'
def player():
    screen.blit(playerImg, (PlayerX, PlayerY))
def change_player_movement_angle(angle=0, pxc=0, pyc=0, pd='forwards'):
    global playerImg, PlayerXC, PlayerYC, player_direction
    playerImg = pygame.image.load('player.png')
    playerImg = pygame.transform.scale(playerImg, (64, 64))
    playerImg = pygame.transform.rotate(playerImg, angle)
    PlayerYC = pyc
    PlayerXC = pxc
    player_direction = pd
enemy = pygame.transform.scale(enemy, (64, 64))
ex = random.randint(50, 150)
ey = random.randint(50, 150)
exc = random.randint(-10, 10)
eyc = random.randint(-10, -10)
def change_enemy_movement():
    global exc
    global eyc
    exc = random.randint(-10, 10)
    eyc = random.randint(-10, 10)
if exc == 0 or eyc == 0:
    change_enemy_movement()
def make_enemy():
    screen.blit(enemy, (ex, ey))
bx = 0
by = 0
bs = 'ready'
bullet_direction = player_direction
def bullet():
    global bs
    screen.blit(bulletImg, (bx, by))
    bs = 'fired'
def change_bullet(byc, bxc, rotate_needed, angle):
    global by, bx, bulletImg
    by = PlayerY - byc
    bx = PlayerX + bxc
    bulletImg = pygame.image.load('bullet.png')
    bulletImg = pygame.transform.scale(bulletImg, (64, 64))
    if rotate_needed:
        bulletImg = pygame.transform.rotate(bulletImg, angle)
def collision():
    distance = math.sqrt((PlayerX - ex) ** 2 + (PlayerY - ey) ** 2)
    if distance < 32:
        return True
    else:
        return False
already_lost = False
lost = False
def collision2():
    distance = math.sqrt((bx - ex) ** 2 + (by - ey) ** 2)
    if distance < 32:
        return True
    else:
        return False
score = 0
font = pygame.font.Font('freesansbold.ttf', 40)
over_font = pygame.font.Font('freesansbold.ttf', 40)
def show_score():
    score_show = font.render(f'Score:{score}', True, (255, 255, 255))
    screen.blit(score_show, (10, 10))
def game_over():
    game_over_show = over_font.render(f'YOU LOST! YOUR FINAL SCORE WAS {score}', True, (255, 255, 255))
    screen.blit(game_over_show, (10, 250))
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_player_movement_angle(90, -5, pd='left')
            elif event.key == pygame.K_UP:
                change_player_movement_angle(pyc=-5)
            elif event.key == pygame.K_DOWN:
                change_player_movement_angle(180, pyc=5, pd='backwards')
            elif event.key == pygame.K_RIGHT:
                change_player_movement_angle(270, 5, pd='right')
            elif event.key == pygame.K_SPACE:
                if bs == 'ready':
                    bullet_direction = player_direction
                    if bullet_direction == 'left':
                        change_bullet(16, 0, True, 90)
                    elif bullet_direction == 'right':
                        change_bullet(16, 32, True, 270)
                    elif bullet_direction == 'forwards':
                        change_bullet(0, 16, False, 0)
                    else:
                        change_bullet(32, 16, True, 180)
                    bullet()
        elif event.type == pygame.KEYUP:
            PlayerXC = 0
            PlayerYC = 0
    if exc == 0 or eyc == 0:
        change_enemy_movement()
    ex += exc
    ey += eyc
    if ex < 0:
        ex = 0
        change_enemy_movement()
    elif ex > 736:
        ex = 736
        change_enemy_movement()
    if ey < 0:
        ey = 0
        change_enemy_movement()
    elif ey > 536:
        ey = 536
        change_enemy_movement()
    make_enemy()
    if not already_lost:
        lost = collision()
        if lost:
            already_lost = True
    if not already_lost:
        PlayerX += PlayerXC
        PlayerY += PlayerYC
        if PlayerX < 0:
            PlayerX = 0
        elif PlayerX > 736:
            PlayerX = 736
        if PlayerY < 0:
            PlayerY = 0
        elif PlayerY > 536:
            PlayerY = 536
        player()
        if bs == 'fired':
            if bullet_direction == 'left':
                bx -= 10
            elif bullet_direction == 'right':
                bx += 10
            elif bullet_direction == 'forwards':
                by -= 10
            else:
                by += 10
            bullet()
        if by < 0 or by > 536 or bx > 736 or bx < 0:
            bs = 'ready'
        if collision2():
            bs = 'ready'
            score += 1
            ex = random.randint(50, 150)
            ey = random.randint(50, 150)
            change_enemy_movement()
            if exc == 0 or eyc == 0:
                change_enemy_movement()
        show_score()
    else:
        game_over()
    pygame.display.update()