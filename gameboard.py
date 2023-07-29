import pygame

class GameBoard:
    def __init__(self):
        self.state = []

    def createBoard(self):
        cellSize = 80
        self.board = pygame.Surface((cellSize * 10, cellSize*10))
        self.board.fill((77, 77, 77))
        cnt = 0
        for x in range(1,9):
            for y in range(1,9):
                pygame.draw.rect(self.board, (255,255,255) if cnt%2 == 0 else (0,0,0), (x*cellSize, y*cellSize, cellSize, cellSize))
                cnt += 1
            cnt -= 1
        return self.board
    
    def setupBoard(self):
        # Work in progress 
        # For now only load king image into game 
        # later create proper state array and return it and use it to record the state of the board and keep track of game
        # pictures also work in progress
        king = pygame.image.load("pieces/piece_king.png")
        self.state.append(king)
        return king

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard().createBoard()

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(board, board.get_rect())

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
