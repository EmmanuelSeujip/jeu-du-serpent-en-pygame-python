from pygame import draw
import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject

class Chevron(MoeObject):
    def __init__(self, display,color,x, y, width, height, direction="up"):
        MoeObject.__init__(self,display=display,  x=x, y=y, width=width, height=height)
        self.color=color
        self.direction=direction
        
    def place(self):
        ### Dessiner la fleche pointant vers le haut
        if (self.direction=="up"):
            draw.polygon(self.display,self.color, ((self.x+self.width/2, self.y), (self.x, self.y+ self.height), (self.x+self.width, self.y+self.height)))
        ###Desssiner la fleche pointant le bas
        elif (self.direction=="down"):
            draw.polygon(self.display,self.color, ((self.x, self.y), (self.x+self.width, self.y), (self.x+ self.width/2, self.y+self.height)))
        ###Dessiner la fleche pointant a droite
        elif (self.direction=="right"):
            draw.polygon(self.display,self.color, ((self.x, self.y), (self.x+self.width, self.y+ self.height/2), (self.x, self.y+self.height)))
        ###Dessiner une fleche pointant vers la gauche
        else:
            draw.polygon(self.display,self.color, ((self.x+self.width, self.y), (self.x, self.y+ self.height/2), (self.x+self.width, self.y+self.height)))
