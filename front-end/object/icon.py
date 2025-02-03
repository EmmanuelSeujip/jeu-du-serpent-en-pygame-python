import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject
from pygame import draw

class PlayOrPause(MoeObject):
    def __init__(self, display,color,x, y, width, height,borderWidth=1,  isPlay=True):
        MoeObject.__init__(self,display=display,  x=x, y=y, width=width, height=height)
        self.isPlay=isPlay
        self.color=color
        self.borderWidth=borderWidth
        
    def place(self):
        if (self.isPlay):
            draw.line(self.display, self.color,(self.x, self.y), (self.x, self.y+self.height), self.borderWidth )
            draw.line(self.display, self.color,(self.x+self.width-self.borderWidth, self.y), (self.x+self.width-self.borderWidth, self.y+self.height), self.borderWidth )
        else:
            draw.polygon(self.display,self.color, ((self.x, self.y), (self.x+self.width, self.y+ self.height/2), (self.x, self.y+self.height)))
        
    def onClick(self):
        self.isPlay= not self.isPlay
        self.feelClik=False
        
class Exit(MoeObject):
    def __init__(self, display,color,x, y, size,borderWidth=1):
        MoeObject.__init__(self,display=display,  x=x, y=y, width=size, height=size)
        self.color=color
        self.borderWidth=borderWidth

    def place(self):
        draw.line(self.display, self.color,(self.x, self.y), (self.x+self.width, self.y+self.height), self.borderWidth )
        draw.line(self.display, self.color,(self.x+self.width, self.y), (self.x, self.y+self.height), self.borderWidth )
