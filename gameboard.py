import pygame
from figures import *

class GameBoard:
    def __init__(self):
        self.state = dict()
        self.positions = dict()
        self.drawn_figs = dict()
        draw_pos = [(x,y) for x in range(1, 9) for y in  range(1, 9)]
        board_pos = [(x,y) for x in range(1, 9) for y in range(8, 0, -1)]
        self.draw_translate = {pos:draw_p for pos, draw_p in zip(board_pos, draw_pos)}

    def create_board(self):
        self.drawn_figs = self.setup_board()
        return self.draw_bg_board()

    def draw_bg_board(self):
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

    
    def setup_board(self):
        
        blacks = [Rook("black", (1,8)), Knight("black", (2,8)), Bishop("black", (3,8)), Queen("black", (4,8)), 
                  King("black", (5,8)), Bishop("black", (6,8)), Knight("black", (7,8)), Rook("black", (8,8))]
        
        blacks.extend([Pawn("black", (x, 7)) for x in range(1, 9)])

        whites = [Rook("white", (1,1)), Knight("white", (2,1)), Bishop("white", (3,1)), Queen("white", (4,1)), 
                  King("white", (5,1)), Bishop("white", (6,1)), Knight("white", (7,1)), Rook("white", (8,1))]


        whites.extend([Pawn("white", (x, 2)) for x in range(1, 9)])

        for fig, id in zip(blacks+whites, list(range(1, 17))+list(range(1, 17))):
            ident = fig.name + fig.color + str(id)
            fig.ident = ident
            self.state[ident] = fig
        
        self.update_positions()
        
        return {ident:fig.draw() for ident, fig in self.state.items()}
   
    def update_positions(self):
        self.positions = {ident:fig.position for ident, fig in self.state.items()}

    def remove_figure(self, ident):
        del self.state[ident]
        self.update_positions()


"""
Testing Only
"""

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard()
    bg = board.create_board()
    print(board.positions)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, bg.get_rect())
        
        with open("help.txt", "w") as file:

            for i in board.state.items():
                file.write(str(i))

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
