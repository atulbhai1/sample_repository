import pygame
print()
print('Prepare to have the image ready in Pycharm.')
print()
pygame.init()
display = pygame.display.set_mode((800, 600))
image = pygame.image.load(input('What image are you trying to see?'))
while True:
    display.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

