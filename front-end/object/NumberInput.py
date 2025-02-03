import sys
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
from Chevron import Chevron
from pygame import draw
class NumberInput(ListMoeObject):
    def __init__(self,display,x,y,color, width,height,font,widthChevron, heightChevron, chevronSpace,value,min=1, max=100, padding=5, borderSize=1 ):
        ListMoeObject.__init__(self,display, x, y)
        self.width=width
        self.height=height
        self.min=min
        self.max=max
        self.padding=padding
        self.borderSize=borderSize
        self.color=color
        self.widthChevron=widthChevron
        self.heightChevron=heightChevron
        self.chevronSpace=chevronSpace
        self.value=value
        self.font=font
        self.obj=[
            Chevron(display, color, x+width-widthChevron, y+self.padding,widthChevron, heightChevron ), 
            Chevron(display, color, x+width-widthChevron, y+padding+heightChevron+chevronSpace,widthChevron, heightChevron, "down" )
        ]
        
            
    def onClick(self):
        #Pour augmenter la valeur
        if self.clicked[0] and self.value<self.max:
            self.value+=1
        #pour reduire la valeur
        if self.clicked[1] and self.value>self.min:
            self.value-=1
        self.clicked[0]=False
        self.clicked[1]=False
        
    def place(self):
        draw.rect(self.display , self.color, (self.x, self.y, self.width, self.height), self.borderSize)
        textObject=self.font.render(str(self.value), True, self.color)
        rectTextObject=textObject.get_rect(center=(self.x+self.padding+(self.width-self.widthChevron)/2, self.y+self.height/2))
        self.display.blit(textObject, rectTextObject)
        self.allPlace()
        
    
        
