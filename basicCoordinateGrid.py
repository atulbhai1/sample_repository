import pygame
size = 20
num = 40
pygame.init()
def draw(point_list):
    for point in point_list:
        pygame.draw.circle(screen, pygame.Color('White'), (point.x, point.y), 5)
screen = pygame.display.set_mode((size*num, size*num))
points = []
for i in range(num):
    pygame.draw.line(screen, (255, 255, 255), (i * size, 0),
                     (i * size, size * num), 1)
for i in range(num):
    pygame.draw.line(screen, (255, 255, 255), (0, i * size),
                     (size * num, i * size))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.Vector2(event.pos))
    draw(points)
    pygame.display.update()