import pygame
from tower import Tower
from Tile import TileMap
import time

class Game:
    running = False
    towers = pygame.sprite.Group()

    def __init__(self):
        try:
            print("Starting game initialization...")
            self.start()
        except Exception as e:
            print(f"Error during initialization: {e}")

    def place_tower(self, tower: Tower):
        self.towers.add(tower)
    
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1280, 720])
        self.tile_map = TileMap(self.screen)
        self.tile_map.draw_path()
        self.last_update = time.time()

    def place_enemy(self):
        try:
            print("Placing enemy...")
            print(self.tile_map.path_sprites)
            first_path_tile = self.tile_map.path_sprites[0]
            first_path_tile.child = True
            first_path_tile.update()
        except Exception as e:
            print(f"Error placing enemy: {e}")

    def update_enemies(self):
        try:
            current_time = time.time()
            if current_time - self.last_update >= 0.2:
                self.tile_map.move_all_tiles()
                self.last_update = current_time
        except Exception as e:
            print(f"Error updating enemies: {e}")

    def start(self):
        try:
            print("Starting game...")
            self.running = True
            self.init()
            
            print("Entering game loop...")
            while self.running:
                self.screen.fill((255, 255, 255))
                
                self.tile_map.draw_tiles()
                
                for tower in self.towers.sprites():
                    self.screen.blit(tower.surf, tower.positon)
                
                self.update_enemies()
                
                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.place_enemy()
        except Exception as e:
            print(f"Error in game loop: {e}")