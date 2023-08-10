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
        
        
    #Implement check_legal_move() for all

class Pawn(Figure):

    def __init__(self, color, position, move_num=0):
        super().__init__(color, position)
        self.move_num = move_num
        self.name = __class__.__name__.lower()


"""
    def passantable(self, firstMove=lambda x: True if x == 1 else False, doubleMove, enemyAdjecent):
        return firstMove and doubleMove and enemeyAdjecent
"""
class King(Figure):
    
    def __init__(self, color, position, in_check=False):
        super().__init__(color, position)
        self.in_check = in_check
        self.name = __class__.__name__.lower()


class Queen(Figure):

    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = __class__.__name__.lower()


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
