from gameboard import GameBoard
import pygame



if __name__ == "__main__":
    
    pygame.init()    
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    board = GameBoard()
    bg = board.createBoard()
    figures = board.setupBoard()
    drag = False
    draw_pos = [(x,y) for x in range(80, 641, 80) for y in  range(80, 641, 80)]
    board_pos = [(x,y) for x in range(1, 9) for y in range(8, 0, -1)]
    draw_translate = {pos:draw_p for pos, draw_p in zip(board_pos, draw_pos)}
    
    while running:
        fig_rects = [fig.get_rect().move(draw_translate[pos]) for fig, pos in figures] 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for chose, rct in enumerate(fig_rects):
                    if rct.collidepoint(event.pos):
                        drag = True
                        select = chose
                         
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False
            if event.type == pygame.MOUSEMOTION and drag:
                
                figures[select][1] = (event.pos[0]//80, event.pos[1]//80)
                

        
        screen.blit(bg, bg.get_rect())
        
        #print(board.state)

        on_board_figures = [screen.blit(fig, draw_translate[pos]) for fig, pos in figures]

        pygame.display.flip()    
        
        clock.tick(60)

    pygame.quit()
