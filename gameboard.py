import pygame
from figures import *

class GameBoard:
    def __init__(self):
        self.state = dict()
        self.positions = dict()

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
        
        blacks = [Rook("black", (1,8)), Knight("black", (2,8)), Bishop("black", (3,8)), Queen("black", (4,8)), King("black", (5,8)), Bishop("black", (6,8)), Knight("black", (7,8)), Rook("black", (8,8))]
        
        blacks.extend([Pawn("black", (x, 7)) for x in range(1, 9)])

        for i in blacks:
            ident = i.name + rows[i.position[0]] + str(i.position[1])
            self.state[ident] = i

        blacks = [fig.draw() for fig in blacks]

        whites = [Rook("white", (1,1)), Knight("white", (2,1)), Bishop("white", (3,1)), Queen("white", (4,1)), King("white", (5,1)), Bishop("white", (6,1)), Knight("white", (7,1)), Rook("white", (8,1))]


        whites.extend([Pawn("white", (x, 2)) for x in range(1, 9)])

        for i in whites:
            ident = i.name + rows[i.position[0]] + str(i.position[1])
            self.state[ident] = i

        whites = [fig.draw() for fig in whites]
        
        self.updatePositions()
        
        return blacks + whites
   
    def updatePositions(self):
        self.positions = {pos.position:ident for ident, pos in self.state.items()}


    def getLegalMove(self, figure):
        return [viz for viz in figure.vision() if viz not in self.positions.keys() and 0 not in viz and 9 not in viz]

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard()
    bg = board.createBoard()
    figures = board.setupBoard()
    print(board.positions)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, bg.get_rect())
        
        with open("help.txt", "w") as file:

            for i in figures:
                file.write(str(i))

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
