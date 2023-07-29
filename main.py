from gameboard import GameBoard
import pygame



if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard()
    bg = board.createBoard()
    king = board.setupBoard()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(bg, bg.get_rect())
        
        screen.blit(king, (80*5,80))

        pygame.display.flip()    
        
        clock.tick(60)

    pygame.quit()
