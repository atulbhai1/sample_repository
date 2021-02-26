import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('Audi.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(640, 360))
        self.angle = 0
        self.rotation_speed = 1.8
        self.direction = 0
        self.forward = pygame.math.Vector2(0, -1)
        self.active = False
    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        elif self.direction == -1:
            self.angle += self.rotation_speed
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.25)
        self.rect = self.image.get_rect(center=self.rect.center)
    def update(self):
        self.set_rotation()
        self.get_rotation()
        self.accelerate()
    def get_rotation(self):
        if self.direction == 1:
            self.forward.rotate_ip(self.rotation_speed)
        elif self.direction == -1:
            self.forward.rotate_ip(-self.rotation_speed)
    def accelerate(self):
        if self.active:
            self.rect.center += self.forward * 5
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg = pygame.image.load('Track.png').convert_alpha()
car = pygame.sprite.GroupSingle(Car())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # noinspection PyUnresolvedReferences
                car.sprite.direction += 1
            elif event.key == pygame.K_LEFT:
                # noinspection PyUnresolvedReferences
                car.sprite.direction -= 1
            elif event.key == pygame.K_SPACE:car.sprite.active = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # noinspection PyUnresolvedReferences
                car.sprite.direction -= 1
            elif event.key == pygame.K_LEFT:
                # noinspection PyUnresolvedReferences
                car.sprite.direction += 1
            elif event.key == pygame.K_SPACE:car.sprite.active = False
    screen.blit(bg, (0, 0))
    car.draw(screen)
    car.update()
    pygame.display.update()
    clock.tick(60)