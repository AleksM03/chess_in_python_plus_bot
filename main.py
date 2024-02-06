from gameboard import GameBoard
import pygame
        

if __name__ == "__main__":
    # Pygame Setup 
    pygame.init()    
    screen = pygame.display.set_mode((800, 800))
    move_disp = pygame.Surface((800, 800), pygame.SRCALPHA, 32)
    move_disp = move_disp.convert_alpha()
    clock = pygame.time.Clock()
    running = True

    # Game Setup
    turn = 0
    board = GameBoard()
    bg = board.create_board()
    drag = False
    fig_rects = {ident:board.drawn_figs[ident].get_rect().move((board.draw_translate[pos][0]*80, board.draw_translate[pos][1]*80)) 
                 for ident, pos in board.positions.items()}

    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                with open("game_state.txt", "w", encoding="utf-8") as game_state:
                    for ident, position in board.positions.items():
                        game_state.write(f"{ident}: {position}\n")
                
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for chose, rct in fig_rects.items():
                    if turn%2==0:
                        if rct.collidepoint(event.pos) and "white" in chose:
                            drag = True
                            select = chose
                            board.state[chose].draw_highlight(board, move_disp)
                    else:
                         if rct.collidepoint(event.pos) and "black" in chose:
                            drag = True
                            select = chose
                            board.state[chose].draw_highlight(board, move_disp)


            # Changes the position of the figure after being draged            
            if event.type == pygame.MOUSEBUTTONUP and drag:
                drag = False
                move_disp.fill((0,0,0,0))

                fig_rects_updt = {ident:board.drawn_figs[ident].get_rect().move((board.draw_translate[pos][0]*80, board.draw_translate[pos][1]*80)) 
                                  for ident, pos in board.positions.items()}
                
                if fig_rects != fig_rects_updt:
                    fig_rects = fig_rects_updt
                    board.state[select].position = board.positions[select]
                    select = None
                    turn += 1


            # Allows you to drag the figures
            if event.type == pygame.MOUSEMOTION and drag:
                try: 
                    board.positions[select] = board.draw_translate[(event.pos[0]//80, event.pos[1]//80)]
                except (KeyError, TypeError):
                    pass

        
        screen.blit(bg, bg.get_rect())

        on_board_figures = [screen.blit(board.drawn_figs[ident], (board.draw_translate[pos][0]*80, board.draw_translate[pos][1]*80)) 
                            for ident, pos in board.positions.items()]
        
        screen.blit(move_disp, move_disp.get_rect())        
        
        pygame.display.flip()    
        
        clock.tick(60)

    pygame.quit()
