from Moe import MOE
from MoeObject import MoeObject

class ListMoeObject(MOE, MoeObject):
    def __init__(self, display=None, x=0, y=0,width=0, height=0, obj=[]):
        MOE.__init__(self, obj=[])
        MoeObject.__init__(self, display=display, x=x, y=y, width=0, height=0)
        self.feelSurvol=False
        self.feelClik=False

    def verifSurvol(self, posX, posY):
        self.updateListSurvoled(posX, posY)
        self.feelSurvol= True in self.survoled
        
    def verifClick(self, posX, posY):
        self.updateListClicked(posX, posY)
        self.feelClik= True in self.clicked

    def onSurvol(self):
        self.survolEffect()       
    
    def onClick(self):
        self.clickEffect()
        
    def place(self):
        for obj in self.obj:
            obj.place()
