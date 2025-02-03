import sys
from ListSnake import ListSnake
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
sys.path.append('../object')
from Food import Food
class ListForGames(ListMoeObject):
    def __init__(self, display, numplayer, listColor, size, smallSize, padding, direction, allPosition,boardLenght,boxsize,  key ):
        ListMoeObject.__init__(self, display )
        self.obj=[
            Food(self.display, 10, allPosition, boardLenght, size), 
            ListSnake(self.display, numplayer,listColor, size, smallSize, padding, direction, allPosition,boardLenght, boxsize, key)
        ]
        self.isPlay=True

    def verifSurvol(self, posX, posY):
        return
        
    def verifClick(self, posX, posY):
        return

    def onSurvol(self):
        return    
    
    def onClick(self):
        return
     
    def direction(self, key):
        if self.isPlay:
            self.obj[1].updateDirection(key)
    
    def place(self):
        if self.isPlay:
            self.obj[0].allPosition=self.obj[1].allPosition.copy()
            if self.obj[0].myEater!=-1:
                self.obj[1].obj[self.obj[0].myEater].upgradeScore()
        self.obj[1].isPlay=self.isPlay
        for obj in self.obj:
            obj.place()
    
