import sys
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
sys.path.append('../object')
from TextSelect import TextSelect

class ListTextSelect(ListMoeObject):
    def __init__(self,display,color, x, y,space,allText, font, underlinePosition, borderWidth, borderOverflow=0, direction="vertical"):    
        ListMoeObject.__init__(self,display=display,x=x,y=y, width=0,height=0,obj = [] )
        self.direction=direction
        if self.direction=="vertical":
            for i in range(0, len(allText), 1) :
                self.obj.append(TextSelect(display, allText[i], color,x, y+i*space, font, underlinePosition, borderWidth, borderOverflow))
        else :
            for i in range(0, len(allText), 1) :
                self.obj.append(TextSelect(display, allText[i], color,x+i*space, y, font, underlinePosition, borderWidth, borderOverflow))
        self.forLauch=5
        
    def onClick(self):
        self.forLauch=self.clicked.index(True)
        self.clickEffect()
        
    
