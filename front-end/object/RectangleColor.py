from pygame.draw import rect
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject

class RectangleColor(MoeObject):
    def __init__(self,display,  x, y, size, color, offset=10, colorSelector=(255, 255, 51),  widthSelctor=5):
        super().__init__(display=display,  x=x, y=y, width=size, height=size)
        self.color=color
        self.dislay=display
        self.selec=False
        self.offset=offset
    def place(self):
        rect(self.display, self.color,(self.x, self.y, self.width, self.height))
        if self.selec:
            rect(self.display, (255, 255, 51), (self.x-self.offset, self.y-self.offset, self.width+2*self.offset, self.height+2*self.offset), 5)
    
    def onClick(self):
        self.feelClik=False
        

