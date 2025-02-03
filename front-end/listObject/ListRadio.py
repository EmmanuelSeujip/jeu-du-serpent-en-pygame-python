import sys
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
sys.path.append('../object')
from Radio import Radio

class ListRadio(ListMoeObject):
    def __init__(self, display, x, y, size, space, forDB, color, num):
        ListMoeObject.__init__(self,display=display,x=x,y=y, width=size,height=size,obj = []) 
        self.forDB = forDB
        self.space = space
        self.num = num
        self.color=color
        self.listSelect=[]
        for i in range(0, self.num, 1):
            self.obj.append(Radio(display, self.x + i * size +i*space, self.y, size, color))  # Créer et ajouter les objets SquareColor
        for i in range(0, len(self.obj), 1):
            self.listSelect.append(False)
        self.listSelect[self.forDB]=True
        self.obj[self.forDB].selec=self.listSelect[self.forDB]
        
    def updateListSelect(self):
        for i in range(0, len(self.listSelect), 1):
            self.listSelect[i]=False
        self.listSelect[self.forDB]=True
        for i in range(0, len(self.listSelect), 1):
            self.obj[i].selec=self.listSelect[i]

    def onClick(self):
        self.forDB=self.clicked.index(True)
        self.updateListSelect()
        self.clickEffect()
 
