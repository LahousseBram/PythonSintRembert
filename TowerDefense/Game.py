import pygame
from tower import Tower

class Game:
    running = False
    towers = pygame.sprite.Group()

    def __init__(self):
        self.start()

    def place_tower(self, tower: Tower):
        self.towers.add(tower)
    
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1280, 720])

    def start(self):
        self.running = True
        self.init()
        while self.running:
            print(len(self.towers.sprites()))
            self.screen.fill((255, 255, 255))
            for tower in self.towers.sprites():
                self.screen.blit(tower.surf, tower.positon)
            
            pygame.display.flip()
            
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.place_tower(tower=Tower(pos[0], pos[1]))

                    
