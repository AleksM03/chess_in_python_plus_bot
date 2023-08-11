from gameboard import GameBoard
import pygame


if __name__ == "__main__":
    
    pygame.init()    
    screen = pygame.display.set_mode((800, 800))
    move_disp = pygame.Surface((800, 800), pygame.SRCALPHA, 32)
    move_disp = move_disp.convert_alpha()
    clock = pygame.time.Clock()
    turn = 0
    running = True
    board = GameBoard()
    bg = board.createBoard()
    figures = board.setupBoard()
    drag = False
    moved = False
    draw_pos = [(x,y) for x in range(1, 9) for y in  range(1, 9)]
    board_pos = [(x,y) for x in range(1, 9) for y in range(8, 0, -1)]
    draw_translate = {pos:draw_p for pos, draw_p in zip(board_pos, draw_pos)}
    fig_rects = [fig.get_rect().move((draw_translate[pos][0]*80, draw_translate[pos][1]*80)) for fig, pos in figures]

    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for chose, rct in enumerate(fig_rects):
                    if turn%2==0:
                        if rct.collidepoint(event.pos):
                            drag = True
                            if chose >= 16:
                                select = chose
                                chosen = board.state[board.positions[figures[select][1]]]
                                print(chosen)
                                for pos in board.getLegalMove(chosen):
                                    print(pos)
                                    pygame.draw.rect(move_disp, (255, 255, 0, 80), (draw_translate[pos][0]*80, draw_translate[pos][1]*80, 80, 80))
                                    running = False
                    else:
                         if rct.collidepoint(event.pos):
                             drag = True
                             if chose < 16:
                                 select = chose
                         
            if event.type == pygame.MOUSEBUTTONUP and drag:
                drag = False
                move_disp.fill((0,0,0,0))
                if moved:
                    moved = False
                    select = None
                    turn += 1
     

            if event.type == pygame.MOUSEMOTION and drag:
                
                try:
                    figures[select][1] = draw_translate[(event.pos[0]//80, event.pos[1]//80)]
                    fig_rects_updt = [fig.get_rect().move((draw_translate[pos][0]*80, draw_translate[pos][1]*80)) for fig, pos in figures]
                    if fig_rects != fig_rects_updt:
                        moved = True
                        fig_rects = fig_rects_updt
                except (KeyError, TypeError):
                    pass

        
        screen.blit(bg, bg.get_rect())
        
        print(turn)

        on_board_figures = [screen.blit(fig, (draw_translate[pos][0]*80, draw_translate[pos][1]*80)) for fig, pos in figures]
        
        screen.blit(move_disp, move_disp.get_rect())        
        
        pygame.display.flip()    
        
        clock.tick(60)

    pygame.quit()
