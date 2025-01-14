import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Tower, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.positon = pygame.math.Vector2(x, y)

    def update(self):
        pass