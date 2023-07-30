import pygame
from figures import *

class GameBoard:
    def __init__(self):
        self.state = {}

    def createBoard(self):
        cellSize = 80
        self.board = pygame.Surface((cellSize * 10, cellSize*10))
        self.board.fill((77, 77, 77))
        cnt = 0
        for x in range(1,9):
            for y in range(1,9):
                pygame.draw.rect(self.board, (233, 237, 204) if cnt%2 == 0 else (119, 153, 84), (x*cellSize, y*cellSize, cellSize, cellSize))
                cnt += 1
            cnt -= 1
        return self.board
    
    def setupBoard(self):
        rows = {val+1:let for val,let in enumerate("abcdefgh")}
        # Work in progress 
        # For now only load king image into game 
        # later create proper state array and return it and use it to record the state of the board and keep track of game
        # pictures also work in progress
        
        blacks = [Rook("black", (1,1)), Knight("black", (2,1)), Bishop("black", (3,1)), Queen("black", (4,1)), King("black", (5,1)), Bishop("black", (6,1)), Knight("black", (7,1)), Rook("black", (8,1))]
        
        blacks.extend([Pawn("black", (x, 2)) for x in range(1, 9)])

        for i in blacks:
            ident = i.name + rows[i.position[1]] + str(i.position[0])
            self.state[ident] = i

        blacks = [fig.draw() for fig in blacks]

        whites = [Rook("white", (1,8)), Knight("white", (2,8)), Bishop("white", (3,8)), Queen("white", (4,8)), King("white", (5,8)), Bishop("white", (6,8)), Knight("white", (7,8)), Rook("white", (8,8))]


        whites.extend([Pawn("white", (x, 7)) for x in range(1, 9)])

        for i in whites:
            ident = i.name + rows[i.position[1]] + str(i.position[0])
            self.state[ident] = i

        whites = [fig.draw() for fig in whites]
        
        return blacks + whites

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
