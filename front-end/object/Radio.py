from pygame import draw
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject

class Radio(MoeObject):
    def __init__(self,display,  x, y, size, color):
        super().__init__(display=display,  x=x, y=y, width=size, height=size)
        self.color=color
        self.dislay=display
        self.selec=False
        
    def place(self):
        draw.circle(self.display, self.color, (self.x+ self.width/2, self.y+ self.height/2), self.width, 2)
        if self.selec:
            draw.circle(self.display, self.color,(self.x+ self.width/2, self.y+ self.height/2), self.width/2)
    
    def onClick(self):
        self.feelClik=False
        
