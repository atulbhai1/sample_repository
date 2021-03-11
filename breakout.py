import pygame, math
pygame.init()
pygame.display.set_caption('Breakout!!!')
clock = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
window = pygame.display.set_mode((WIDTH, HEIGHT))
class Paddle:
    def __init__(self):
        self.x = WIDTH/2
        self.y = 700
        self.dx = 0
        self.width = 200
        self.height = 25
    def render(self):
        pygame.draw.rect(window, WHITE, pygame.Rect(int(self.x - self.width/2), int(self.y - self.height/2), self.width, self.height))
    def left(self):
        self.dx = -12
    def right(self):
        self.dx = 12
    def move(self):
        self.x += self.dx
        if self.x > 1200 - self.width/2:
            self.x = 1100
            self.dx = 0
        elif self.x < 0 + self.width/2:
            self.x = 100
            self.dx = 0
        self.render()
    def collisionDetection(self, other):
        xCollision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        yCollision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return xCollision and yCollision
paddle = Paddle()
class Ball:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.dx = 6
        self.dy = -6
        self.width = 20
        self.height = 20
    def render(self):
        pygame.draw.rect(window, WHITE, pygame.Rect(int(self.x - self.width/2), int(self.y - self.height/2), self.width, self.height))
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 1200 - self.width/2:
            self.x = 1100
            self.dx *= -1
        elif self.x < 0 + self.width/2:
            self.x = 100
            self.dx *= -1
        if self.y > 1200 - self.height/2:
            self.x = WIDTH / 2
            self.y = HEIGHT / 2
        elif self.y < 0 + self.height/2:
            self.y = 0 + self.height/2
            self.dy *= -1
        self.render()
    def collisionDetection(self, other):
        xCollision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        yCollision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return xCollision and yCollision
ball = Ball()
class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.color = GREEN
    def render(self):
        pygame.draw.rect(window, GREEN, pygame.Rect(int(self.x - self.width/2), int(self.y - self.height/2), self.width, self.height))
bricks = []
for y in range(25, 200, 25):
    for x in range(25, 1200, 50):
        bricks.append(Brick(x, y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left()
            elif event.key == pygame.K_RIGHT:
                paddle.right()
    window.fill(BLACK)
    paddle.move()
    ball.move()
    paddle.render()
    for brick in bricks:
        brick.render()
        if ball.collisionDetection(brick):
            ball.dy *= -1
            bricks.remove(brick)
    if ball.collisionDetection(paddle): ball.dy *= -1
    ball.render()
    clock.tick(60)
    if len(bricks) == 0:
        pygame.quit()
        quit()
    pygame.display.flip()