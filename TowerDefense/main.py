from Game import Game
import pygame

from Tile import TileMap

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    
    tile_map = TileMap(screen)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        tile_map.draw_tiles()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
