import pygame
from tkinter.filedialog import askopenfilename
pygame.init()
display = pygame.display.set_mode((800, 600))
file = input('Enter file location')
image = pygame.image.load(file)
while True:
    display.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

