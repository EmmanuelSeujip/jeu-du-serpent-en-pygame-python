import sys
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
from ListTextSelect import ListTextSelect
sys.path.append('../object')
from Chevron import Chevron
from pygame import draw

class Select(ListMoeObject):
    def __init__(self, display,x, y, color, option,font,width, height,chevWidth, chevHeight,choice=0,  borderSize=2, overflow=5):
        ListMoeObject.__init__(self, display,x, y,width, height)
        self.width=width
        self.height=height
        self.option=option
        self.color=color
        self.borderSize=borderSize
        self.choice=choice
        self.overflow=overflow
        self.open=False
        self.font=font
        self.obj=[
            Chevron(display, color, x+width-overflow-chevWidth, y+overflow, chevWidth, chevHeight), 
            ListTextSelect(display,color, x+3*overflow, y+15+overflow,height,option, font, 0,0)
        ]
        self.obj[1].forLauch=self.choice

    def onClick(self):
        self.clickEffect()
        self.open=self.obj[0].isDown
        if self.obj[1].forLauch !=self.choice:
            self.choice=self.obj[1].forLauch
        if self.obj[1].feelClik :
            self.open=self.obj[0].isDown=False
        
    def place(self):
        if self.open:
            self.obj[1].place()
            draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height*len(self.option)), self.borderSize)
        else: 
            self.display.blit(self.font.render(self.option[self.choice], True, self.color), (self.x+self.overflow, self.y+self.overflow))
            draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height), self.borderSize)
        self.obj[0].place()
