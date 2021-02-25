import pygame, pymunk
def create_apple(sp, pos=(400, 0)):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 80)
    sp.add(body, shape)
    return shape
def draw_apples(ap):
    for apl in ap:
        pygame.draw.circle(screen, pygame.color.Color('green'), (apl.body.position.x, apl.body.position.y), 80)
def static_ball(sp, pos=(500, 500)):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    sp.add(body, shape)
    return shape
def draw_static_balls(st):
    for ball in st:
        pygame.draw.circle(screen, pygame.color.Color('orange'), ball.body.position, 50)
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 100)
apples = [create_apple(space)]
static = [static_ball(space), static_ball(space, (300, 650))]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
    screen.fill((217, 217, 217))
    space.step(1/50)
    draw_apples(apples)
    draw_static_balls(static)
    pygame.display.update()
    clock.tick(60)