from pygame import SYSTEM_CURSOR_HAND, SYSTEM_CURSOR_ARROW
from pygame.mouse import set_cursor
"""
    Le conteneur des éléments
    ces arguments sont: 
        obj: qui contient tout les objets ou enfant qu'il doit gérer
        clicked: l'etat de tout les élément après un clic sur la page
        survoled: l'etat de tout les élément après un deplacement de la souris 
"""
class MOE(object):
    def __init__(self, obj):
        self.obj=obj
        self.clicked=[]
        self.survoled=[]
        
    
    def updateListClicked(self, mouseX, mouseY):
        self.clicked=[]
        for elt in self.obj:
            elt.verifClick(mouseX, mouseY)
            self.clicked.append(elt.feelClik)
            
    def updateListSurvoled(self, mouseX, mouseY):
        self.survoled=[]
        for elt in self.obj:
            elt.verifSurvol(mouseX, mouseY)
            self.survoled.append(elt.feelSurvol)

    def addOject(self, obj):
        if isinstance(obj,list):
            self.obj=self.obj+obj
        else:
            self.obj.append(obj)
        self.updateListClicked(0,0)
        self.updateListSurvoled(0,0)
    
    #Appliquer tout les élément qui ont été survolé une action predéfinis
    def survolEffect(self):
        if True in self.survoled:
            set_cursor(SYSTEM_CURSOR_HAND)
            elt=self.survoled.index(True)
            self.obj[elt].onSurvol()
        else:
            set_cursor(SYSTEM_CURSOR_ARROW)

    #Appliquer tout les élément qui ont été clické une action predéfinis
    def clickEffect(self):
        if True in self.clicked:
            elt=self.clicked.index(True)
            self.obj[elt].onClick()
    
    def allPlace(self):
        for obj in self.obj:
            obj.place()
        




