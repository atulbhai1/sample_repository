import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Race Car!!!')
car = pygame.image.load('Audi.png')
pygame.display.set_icon(car)
background = pygame.image.load('Track.png').convert_alpha()
playerImg = pygame.image.load('Audi.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (64, 64))
PlayerX = 370
PlayerXC = 0
PlayerY = 400
PlayerYC = 0
speed = 3
player_direction = 'forwards'
def player():
    screen.blit(playerImg, (PlayerX, PlayerY))
def change_player_movement_angle(angle=0, pxc=0, pyc=0, pd='forwards'):
    global playerImg, PlayerXC, PlayerYC, player_direction
    playerImg = pygame.image.load('Audi.png').convert_alpha()
    playerImg = pygame.transform.scale(playerImg, (64, 64))
    playerImg = pygame.transform.rotate(playerImg, angle)
    PlayerYC = pyc
    PlayerXC = pxc
    player_direction = pd
def draw_background():
    screen.blit(background, (0, 0))
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_player_movement_angle(90, -speed, pd='left')
            elif event.key == pygame.K_UP:
                change_player_movement_angle(pyc=-speed)
            elif event.key == pygame.K_DOWN:
                change_player_movement_angle(180, pyc=speed, pd='backwards')
            elif event.key == pygame.K_RIGHT:
                change_player_movement_angle(270, speed, pd='right')
        elif event.type == pygame.KEYUP:
            PlayerXC = 0
            PlayerYC = 0
    draw_background()
    PlayerX += PlayerXC
    PlayerY += PlayerYC
    if PlayerX < 0:
            PlayerX = 0
    elif PlayerX > screen.get_size()[0] - 64:
            PlayerX = screen.get_size()[0] - 64
    if PlayerY < 0:
            PlayerY = 0
    elif PlayerY > screen.get_size()[1] - 64:
            PlayerY = screen.get_size()[1] - 64
    player()
    pygame.display.update()