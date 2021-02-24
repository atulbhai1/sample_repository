import pygame, random
def draw_floor():
    screen.blit(floor_surface, (floorX, 700))
    screen.blit(floor_surface, (floorX + 576, 700))
pygame.init()
screen = pygame.display.set_mode((576, 800))
clock = pygame.time.Clock()
if random.randint(0, 1) == 1:
    bg_surface = pygame.image.load('background-day.png').convert()
else:
    bg_surface = pygame.image.load('background-night.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.transform.scale2x(pygame.image.load('base.png').convert())
floorX = 0
gravity = 0.25
bird_movement = 0
bird = random.randint(0, 2)
if bird == 0:
     bird_downflap = pygame.image.load('yellowbird-downflap.png').convert_alpha()
     bird_midflap = pygame.image.load('yellowbird-midflap.png').convert_alpha()
     bird_upflap = pygame.image.load('yellowbird-upflap.png')
elif bird == 1:
    bird_downflap = pygame.image.load('redbird-midflap.png').convert_alpha()
    bird_midflap = pygame.image.load('redbird-midflap.png').convert_alpha()
    bird_upflap = pygame.image.load('redbird-upflap.png')
else:
    bird_downflap = pygame.image.load('bluebird-midflap.png').convert_alpha()
    bird_midflap = pygame.image.load('bluebird-midflap.png').convert_alpha()
    bird_upflap = pygame.image.load('bluebird-upflap.png')
bird_downflap = pygame.transform.scale2x(bird_downflap)
bird_upflap = pygame.transform.scale2x(bird_upflap)
bird_midflap = pygame.transform.scale2x(bird_midflap)
bird_frames = [bird_downflap, bird_midflap, bird_midflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 400))
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
def rotate_bird(birdSurf):
    new_bird = pygame.transform.rotozoom(birdSurf, -bird_movement * 3, 1)
    return new_bird
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect
if random.randint(0, 1) == 0:
    pipe_surface = pygame.image.load('pipe-green.png').convert()
else:
    pipe_surface = pygame.image.load('pipe-red.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_height = [600, 500, 400]
game_active = True
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 700:
            return False
    return True
end_message = ''
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
score = 0
high_score = 0
font = pygame.font.Font('/Users/srinivasansrinivasan/Downloads/04B_19.TTF', 40)
def score_display(game_state):
    score_surface = font.render(f'Score : {int(score)}', True, (0, 0, 0))
    score_rect = score_surface.get_rect(center=(288, 50))
    screen.blit(score_surface, score_rect)
    if not game_state:
        high_score_surface = font.render(f'High Score : {high_score}', True, (0, 0, 0))
        high_score_rect = high_score_surface.get_rect(center=(288, 650))
        screen.blit(high_score_surface, high_score_rect)
game_over_surface = pygame.transform.scale2x(pygame.image.load('message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288, 350))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
                if not game_active:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100, 400)
                    bird_movement = 0
                    score = 0
        elif event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        elif event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()
    screen.blit(bg_surface, (0, 0))
    floorX -= 1
    draw_floor()
    if floorX <= -576:
        floorX = 0
    if game_active:
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collision(pipe_list)
        score += 0.01
        if int(score) > high_score:
            high_score = int(score)
        score_display(game_active)
    else:
        score_display(game_active)
        screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    clock.tick(60)