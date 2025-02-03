from pygame import draw
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject

class Snake(MoeObject):
    def __init__(self, display, color,colorMiddle, size,smallSize, padding,direction,  listPosition):
        MoeObject.__init__(self, display)
        self.color=color
        self.length=4
        self.collisionValue=[]
        self.listPosition=listPosition
        self.size=size
        self.padding=padding
        self.smallSize=smallSize
        self.direction=direction
        self.colorMiddle=colorMiddle
        self.score=0
        
    #pour faire avancer le serpent
    def updatePosition(self):
        for box in self.listPosition:
            if box[2]=="left":
                box[0]-=self.size
            elif box[2]=="right":
                box[0]+=self.size
            elif box[2]=="down":
                box[1]+=self.size
            else:
                box[1]-=self.size
    
    #pour modifier le sens de déplacement
    def updateDirection(self):
        save=self.listPosition[0][2]
        x=1
        while (x<len(self.listPosition)):
            actual=save
            save=self.listPosition[x][2]
            self.listPosition[x][2]=actual
            x+=1
        self.listPosition[0][2]=self.direction
    
    #deplacer le serpent
    def move(self):
        self.updatePosition()
        self.updateDirection()
    
    #modifier le score et mettre a jour la taille du serpent
    def upgradeScore(self):
        self.score+=1
        lenght=len(self.listPosition)
        last=self.listPosition[lenght-1].copy()
        if last[2]=="left":
            last[0]+=self.size
        elif last[2]=="right":
            last[0]-=self.size
        elif last[2]=="down":
            last[1]-=self.size
        else:
            last[1]+=self.size
        self.listPosition.append(last)
        
    def place(self):
        for box in self.listPosition:
            draw.rect(self.display,self.color, (box[0], box[1],self.size, self.size))
            draw.rect(self.display,self.colorMiddle, (box[0]+self.padding, box[1]+self.padding,self.smallSize, self.smallSize))

