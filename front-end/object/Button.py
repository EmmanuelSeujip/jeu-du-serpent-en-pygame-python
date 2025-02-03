from pygame import font
from pygame.draw import rect
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject

class Button(MoeObject):
    def __init__(self, display, x, y, width, height, text, color, bgColor, font=font.SysFont(None, 25)):
        MoeObject.__init__(self,display, x, y, width, height)
        self.text=text
        self.color=color
        self.bgColor=bgColor
        self.font=font
        self.textObject=self.font.render(self.text, True, self.color)
        self.rectText = self.textObject.get_rect(center=(x+(width/2),y+(height/2)))
        
    def place(self):
        textObject=font.render(self.text, True, self.color)
        rectText = textObject.get_rect(center=(self.x+(self.width/2),self.y+(self.height/2)))
        rect(self.display, self.bgcolor, (self.x,self.y, self.width, self.height))
        self.display.blit(textObject, rectText)
        
        
