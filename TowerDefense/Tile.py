import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, is_path, x, y, child=None):
        super().__init__()
        self.width = 40
        self.height = 40
        self.is_path = is_path
        self.child = child
        self.image = pygame.Surface((self.width, self.height))
        self.color = (200, 200, 200) if not is_path else (100, 100, 100)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

class TileMap:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = pygame.sprite.Group()
        self.tile_size = 40
        self.grid_width = screen.get_width() // self.tile_size
        self.grid_height = screen.get_height() // self.tile_size
        self.path = [
            (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9),(8, 8), (8, 7), 
            (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (12, 7), (12, 8), (12, 9), (13, 9), 
            (14, 9), (15, 9), (16, 9), (17, 9), (17, 8), (17, 7), (17, 6), (18, 6), (19, 6), 
            (20, 6), (21, 6), (22, 6), (23, 6), (23, 7), (23, 8), (23, 9), (24, 9), (25, 9), (26, 9), 
            (27, 9), (28, 9), (29, 9), (30, 9), (31, 9)
        ]
        self.create_tiles()

    def create_tiles(self):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                tile = Tile((x,y) in self.path, x * self.tile_size, y * self.tile_size)
                self.tiles.add(tile)

    def draw_path(self):
        path_indexes = [0,1,2,3]
        for index in path_indexes:
            self.tiles.sprites()[index].is_path = True

    def draw_tiles(self):
        self.tiles.draw(self.screen)
