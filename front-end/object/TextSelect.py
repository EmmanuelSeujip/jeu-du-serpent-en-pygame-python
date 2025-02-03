from pygame import font
from pygame.draw import line
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject
class TextSelect(MoeObject):
    def __init__ (self,display,text,color, x=0, y=0, font=font.SysFont(None, 25),underlinePosition=1,  borderWidth=1,borderOverflow=0):
        self.text=text
        self.font=font
        self.color=color
        self.borderWidth=borderWidth
        self.borderOverflow=borderOverflow
        self.underlinePosition=underlinePosition
        self.textObject=self.font.render(self.text, True, self.color)
        self.rect = self.textObject.get_rect(center=(x,y))
        super().__init__(display=display,  x=self.rect.x, y=self.rect.y, width=self.rect.width, height=self.rect.height)
    
    def onSurvol(self):
        if (self.feelSurvol):
            line(self.display, self.color,(self.rect.x-self.borderOverflow, self.rect.y+self.rect.height+self.underlinePosition), (self.rect.x+self.rect.width+self.borderOverflow, self.rect.y+self.rect.height+self.underlinePosition), self.borderWidth)
            
    def place(self):
        self.display.blit(self.textObject, self.rect )
            


