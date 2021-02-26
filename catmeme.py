import pygame, random
class ParticleStar:
    def __init__(self):
        self.particles = []
        self.surface = star
        self.width = self.surface.get_rect().width
        self.height = self.surface.get_rect().height
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x += particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.2
                screen.blit(self.surface, particle[0])
    def add_particles(self):
        pos = list(pygame.mouse.get_pos())
        pos[0] -= self.width/2
        pos[1] -= self.width/2
        lifetime = random.randint(4, 10)
        particle_rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
        self.particles.append([particle_rect, random.randint(-3, 3), random.randint(-3, 3), lifetime])
    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[3] > 0]
class ParticleNyan:
    def __init__(self):
        self.particles = []
        self.size = 12
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pygame.draw.rect(screen, particle[1], particle[0])
        self.draw_cat()
    def add_particles(self, offset, color):
        pos = list(pygame.mouse.get_pos())
        pos[1] += offset
        particle_rect = pygame.Rect(pos[0] - self.size/2, pos[1] - self.size/2, self.size, self.size)
        self.particles.append((particle_rect, color))
    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[0].x > 0]
    # noinspection PyMethodMayBeStatic
    def draw_cat(self):
        cat_rect = cat.get_rect(center=pygame.mouse.get_pos())
        screen.blit(cat, cat_rect)
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
cat = pygame.image.load('nyan_cat.png').convert_alpha()
star = pygame.image.load('star.png').convert_alpha()
clock = pygame.time.Clock()
PARTICLEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLEEVENT, 40)
particles2 = ParticleNyan()
particles3 = ParticleStar()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == PARTICLEEVENT:
            particles2.add_particles(-30, pygame.Color('Red'))
            particles2.add_particles(-18, pygame.Color('Orange'))
            particles2.add_particles(-6, pygame.Color('Yellow'))
            particles2.add_particles(6, pygame.Color('Green'))
            particles2.add_particles(18, pygame.Color('Blue'))
            particles2.add_particles(30, pygame.Color('Red'))
            particles3.add_particles()
    screen.fill((30, 30, 30))
    particles2.emit()
    particles3.emit()
    pygame.display.update()
    clock.tick(60)