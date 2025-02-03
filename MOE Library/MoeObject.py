"""
    L'éléments contenus dans le MOE
    ces arguments sont: 
        feelSurvol: Savoir s'il a été survolé c'est à dire True s'il a été survolé
        feelClik: Savoir si on a clicqué sur lui
        x: son abcisse
        y son ordonnée
        width: sa longueur 
        height: sa hauteur
"""

class MoeObject(object):
    def __init__(self,display=None,  x=0, y=0, width=0, height=0):
        self.feelSurvol=False
        self.feelClik=False
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.display=display

        
    def verifSurvol(self, posX, posY):
        if ((self.x <=posX and posX<=(self.x+self.width)) and (self.y<=posY and posY<=(self.y+self.height))):
            self.feelSurvol=True
        else:
            self.feelSurvol=False

    def verifClick(self, posX, posY):
        if ((self.x <=posX and posX<=(self.x+self.width)) and (self.y<=posY and posY<=(self.y+self.height))):
            self.feelClik=True
        else:
            self.feelClik=False
            
            
    def onSurvol(self):
        return       
    
    def onClick(self):
        return
        
    def place(self):
        return
        

            
