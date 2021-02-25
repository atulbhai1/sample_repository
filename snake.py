import pygame, random
from pygame.math import Vector2
score = 0
pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
apple = pygame.image.load('apple.png').convert_alpha()
# noinspection PyAttributeOutsideInit
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10),Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()
        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()
        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
    def draw(self):
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                self.update_head_graphics()
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.update_tail_graphics()
                screen.blit(self.tail, block_rect)
            else:
                prevBlock = self.body[index + 1] - block
                nextBlock = self.body[index - 1] - block
                if prevBlock.x == nextBlock.x:
                    pic = self.body_vertical
                elif prevBlock.y == nextBlock.y:
                    pic = self.body_horizontal
                else:
                    if (prevBlock.x == -1 and nextBlock.y == -1) or (prevBlock.y == -1 and nextBlock.x == -1):
                        pic = self.body_tl
                    elif (prevBlock.x == -1 and nextBlock.y == 1) or (prevBlock.y == 1 and nextBlock.x == -1):
                        pic = self.body_bl
                    elif (prevBlock.x == 1 and nextBlock.y == -1) or (prevBlock.y == -1 and nextBlock.x == 1):
                        pic = self.body_tr
                    elif (prevBlock.x == 1 and nextBlock.y == 1) or (prevBlock.y == 1 and nextBlock.x == 1):
                        pic = self.body_br
                # noinspection PyUnboundLocalVariable
                screen.blit(pic, block_rect)
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):self.head = self.head_left
        elif head_relation == Vector2(-1, 0):self.head = self.head_right
        elif head_relation == Vector2(0, 1):self.head = self.head_up
        elif head_relation == Vector2(0, -1):self.head = self.head_down
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
    def move(self):
        if self.new_block:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
    def add_block(self):
        self.new_block = True
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)
    def draw(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
def draw_score():
    score_text = f'Score : {score}'
    score_surface = font.render(score_text, True, (56, 74, 12))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.move()
        self.check_collision()
        self.checkFail()
    def draw(self):
        self.fruit.draw()
        self.snake.draw()
    def check_collision(self):
        global score
        if self.fruit.pos == self.snake.body[0]:
            score += 1
            self.fruit.pos = Vector2(random.randint(0, cell_num - 1), random.randint(0, cell_num - 1))
            self.fruit.draw()
            self.snake.add_block()
    def checkFail(self):
        if (not 0 <= self.snake.body[0].x < cell_num) or (not 0 <= self.snake.body[0].y < cell_num):
            self.game_over()
        for bl in self.snake.body[1:]:
            if bl == self.snake.body[0]:
                self.game_over()
    # noinspection PyMethodMayBeStatic
    def game_over(self):
        pygame.quit()
        quit()
font = pygame.font.Font('/Users/srinivasansrinivasan/Downloads/PoetsenOne-Regular.ttf', 25)
main = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == SCREEN_UPDATE:
            main.update()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main.snake.direction != Vector2(0, 1):
                main.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and main.snake.direction != Vector2(0, -1):
                main.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and main.snake.direction != Vector2(1, 0):
                main.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and main.snake.direction != Vector2(-1, 0):
                main.snake.direction = Vector2(1, 0)
    screen.fill((175, 215, 70))
    main.draw()
    draw_score()
    pygame.display.update()
    clock.tick(60)