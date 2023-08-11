import pygame

class Figure:

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.name = __class__.__name__.lower()

    def get_color(self):
        return (255,255,255) if self.color == "white" else (0,0,0)

    def draw(self):

        image = pygame.image.load("pieces/piece_" + self.name  + ".png")
        
        img_px_arr = pygame.PixelArray(image)
        img_px_arr.replace((0,0,0), self.get_color())
        del img_px_arr
       
        return [image, self.position] 
        
        
    def vision(self):
        pass

class Pawn(Figure):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.move_num = 0
        self.name = __class__.__name__.lower()

    def vision(self):
        x, y = self.position
        flanks = [(x+1, y+1), (x-1, y+1)]
        if self.move_num == 0:
            return flanks + [(x, y+i) for i in range(1,3)]
        else:
            return flanks + (x, y+1)

"""
    def passantable(self, firstMove=lambda x: True if x == 1 else False, doubleMove, enemyAdjecent):
        return firstMove and doubleMove and enemeyAdjecent
"""
class King(Figure):
    
    def __init__(self, color, position, in_check=False):
        super().__init__(color, position)
        self.in_check = in_check
        self.name = __class__.__name__.lower()

    def vision(self):
        x, y = self.position
        return [(x+ox,y+oy) for ox in range(-1, 2) for oy in range(-1, 2) if (x+ox, y+oy) != self.position]


class Queen(Figure):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()

    def vision(self):
        x, y = self.position
        viz = [(x+ox,y+oy) for ox in range(-1, 2) for oy in range(-1, 2) if (x+ox, y+oy) != self.position]
        viz += [(x+o, y+o)  for o in range(1, 8) if x+o <= 8 and x+o >= 1 and y+o >= 1 and y+o <= 8 and (x+o,y+o) not in viz]
        viz += [(x-o, y-o)  for o in range(1, 8) if x-o <= 8 and x-o >= 1 and y-o >= 1 and y-o <= 8 and (x-o,y-o) not in viz]
        return viz



class Knight(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()

class Bishop(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()

class Rook(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()

if __name__ == "__main__":
    pawn = Pawn((0,0,0), (5,7))
    king = King((0,0,0), (5,5))
    queen = Queen((0,0,0), (4,4))
    print(pawn.vision())
    print(king.vision())
    print(queen.vision())
