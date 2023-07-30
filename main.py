from gameboard import GameBoard
import pygame



if __name__ == "__main__":
    
    pygame.init()    
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard()
    print(board.state)
    bg = board.createBoard()
    figures = board.setupBoard()
    print(board.state)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(bg, bg.get_rect())
        
        on_board_figures = [screen.blit(fig, (pos[0]*80,pos[1]*80)) for fig, pos in figures]

        pygame.display.flip()    
        
        clock.tick(60)

    pygame.quit()
