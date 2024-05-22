import pygame

"""
What the Pieces see (Visions):

X* = Piece can move there 
P* = Piece
oP = other Piece
XoP = Takes other Piece
<X> = Piece can continue in that direction until it hits a border or gets obstructed by oP

Pawn:   
        XfMoPa = Takes First Move other Pawn 

        |X(XoP)|XXXX|X(XoP)|  
        |......|X(P)|XXXXXX|  
        |......|PPPP|XfMoPa|  

King:
        |X(XoP)|X(XoP)|X(XoP)|
        |X(XoP)|PPPPPP|X(XoP)|
        |X(XoP)|X(XoP)|X(XoP)|

Rook:
        |.......|<X>(XoP)|.......|
        <X>(XoP)|PPPPPPPP|<X>(XoP)
        |.......|<X>(XoP)|.......|

Bishop:
        <X>(XoP)|........|<X>(XoP)
        |.......|PPPPPPPP|.......|
        <X>(XoP)|........|<X>(XoP)

Queen:
        <X>(XoP)|<X>(XoP)|<X>(XoP)
        <X>(XoP)|PPPPPPPP|<X>(XoP)
        <X>(XoP)|<X>(XoP)|<X>(XoP)

Knight:
        |X(XoP)|.|X(XoP)|
        |......|.|......|
        |......|P|......|
    
        in every direction
"""


class Figure:

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = __class__.__name__.lower()
        self.ident = ""
        self.move_num = 0

    def get_color(self):
        return (255,255,255) if self.color == "white" else (0,0,0)

    def draw(self):

        image = pygame.image.load("pieces/piece_" + self.name  + ".png")
        
        img_px_arr = pygame.PixelArray(image)
        img_px_arr.replace((0,0,0), self.get_color())
        del img_px_arr
       
        return image 

    
    def draw_highlight(self, board, move_disp):
        for pos in self.vision(board):
            pygame.draw.rect(move_disp, (255, 255, 0, 80), (board.draw_translate[pos][0]*80, board.draw_translate[pos][1]*80, 80, 80))
        
    def vision(self, board):
        pass

    def check_obstruction(self, viz, board):
        temp = list()
        own_color = [board.positions[ofig] for ofig in board.state if self.color in ofig]
        other_color = [board.positions[ofig] for ofig in board.state if self.color not in ofig]

        for pos in viz:
            #Check if we are on the board
            if pos in board.draw_translate.keys():
                #Check if we get obstructed by another figure
                if pos in own_color:
                    continue
                temp.append(pos)

        return temp
    
    def take_piece(self, board):
        other_c = [board.positions[ofig] for ofig in board.state if self.color not in ofig]
        if self.position in other_c:
            return True
        else:
            return False

    def rook_vision(self, x, y, viz, board):
        viz += self.check_obstruction([(x, y+o) for o in range(1, 8) if y+o <= 8 and (x,y+o) not in viz], board)
        viz += self.check_obstruction([(x, y-o) for o in range(1, 8) if y-o >= 1 and (x,y-o) not in viz], board)
        viz += self.check_obstruction([(x-o, y) for o in range(1, 8) if x-o >= 1 and (x-o,y) not in viz], board)
        viz += self.check_obstruction([(x+o, y) for o in range(1, 8) if x+o <= 8 and (x+o,y) not in viz], board)
        return viz
    
    def bishop_vision(self, x, y, viz, board):
        viz += self.check_obstruction([(x+o, y+o) for o in range(1, 8) if x+o <= 8 and y+o <= 8 and (x+o,y+o) not in viz], board)
        viz += self.check_obstruction([(x-o, y-o) for o in range(1, 8) if x-o >= 1 and y-o >= 1 and (x-o,y-o) not in viz], board)
        viz += self.check_obstruction([(x+o, y-o) for o in range(1, 8) if x+o <= 8 and y-o >= 1 and (x+o,y-o) not in viz], board)
        viz += self.check_obstruction([(x-o, y+o) for o in range(1, 8) if x-o >= 1 and y+o <= 8 and (x-o,y+o) not in viz], board)
        return viz

class Pawn(Figure):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()
        self.passantable = False
        self.value = 1

    def vision(self, board):
        x, y = self.position
        if self.color == "white":
            flanks = [flank for flank in [(x+1, y+1), (x-1, y+1)] 
                      if flank in board.draw_translate.keys() and flank in [board.positions[opawn] for opawn in board.state if "black" in opawn]]
            if self.move_num == 0:
                return flanks + [pos for pos in [(x, y+i) for i in range(1,3)] 
                                 if pos in board.draw_translate.keys() and pos not in [board.positions[ofig] for ofig in board.state]]
            else:
                return flanks + [(x, y+1)] if (x, y+1) in board.draw_translate.keys() and (x, y+1) not in [board.positions[ofig] for ofig in board.state] else flanks
        else:
            flanks = [flank for flank in [(x+1, y-1), (x-1, y-1)] 
                      if flank in board.draw_translate.keys() and flank in [board.positions[ofig] for ofig in board.state if "white" in ofig]]
            if self.move_num == 0:
                return flanks + [pos for pos in [(x, y-i) for i in range(1,3)] 
                                 if pos in board.draw_translate.keys() and pos not in [board.positions[ofig] for ofig in board.state]]
            else:
                return flanks + [(x, y-1)] if (x, y-1) in board.draw_translate.keys() and (x, y-1) not in [board.positions[ofig] for ofig in board.state] else flanks
"""
    def passantable(self, firstMove=lambda x: True if x == 1 else False, doubleMove, enemyAdjecent):
        return firstMove and doubleMove and enemeyAdjecent
"""
class King(Figure):
    
    def __init__(self, color, position, in_check=False):
        super().__init__(color, position)
        self.in_check = in_check
        self.name = __class__.__name__.lower()

    def vision(self, board):
        x, y = self.position
        viz = [(x+ox,y+oy) for ox in range(-1, 2) for oy in range(-1, 2) if (x+ox, y+oy) != self.position]
        return [pos for pos in viz if pos in board.draw_translate.keys() and pos not in [board.positions[ofig] for ofig in board.state if self.color in ofig]]


class Queen(Figure):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()
        self.value = 9

    def vision(self, board):
        x, y = self.position

        # King Vision
        viz = self.check_obstruction([(x+ox,y+oy) for ox in range(-1, 2) for oy in range(-1, 2) if (x+ox, y+oy) != self.position], board)
        
        # Bishop Vision
        viz += self.bishop_vision(x, y, viz, board)
        
        # Rook Vision   
        viz += self.rook_vision(x, y, viz, board)

        return viz


class Knight(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()
        self.value = 3

    def vision(self, board):
        x, y = self.position
        viz = [(x+ox,y+oy) for oy in [-2, 2] for ox in [-1, 1]]
        viz += [(x+ox,y+oy) for ox in [-2, 2] for oy in [-1, 1]]
        return self.check_obstruction(viz, board)
    

class Bishop(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()
        self.value = 3

    def vision(self, board):
        x, y = self.position
        viz = list()
        viz = self.bishop_vision(x, y, viz, board)
        return viz



class Rook(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()
        self.value = 5
    
    def vision(self, board):
        x, y = self.position
        viz = list()
        viz = self.rook_vision(x, y, viz, board)
        return viz
