import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject
from pygame.draw import circle
from random import randint
class Food(MoeObject):
    def __init__(self, display,size, snakePosition, boardLenght, boxSize):
        MoeObject.__init__(self, display, 0, 0, size, size)
        self.snakePosition=snakePosition
        self.boardLenght=boardLenght
        self.change=True
        self.boxSize=boxSize
        self.myEater= -1
        
    def between(self, val,pos,lenght):
        if (pos<val and val<pos+lenght):
            return True
        return False     
        
    def verifInSnake(self):
        tab=[]
        for posSnake in self.snakePosition:
            cond=False
            x=0
            while cond==False and x<len(posSnake):
                # verifie si le serpent se trouve sur sa proie
                if (self.between(self.x, posSnake[x][0],self.boxSize) and self.between(self.y, posSnake[x][1], self.boxSize)):
                    cond=True    
                x+=1
            tab.append(cond)
        return tab
        
    def whoAreEatMe(self):
        try:
            tab=self.verifInSnake()
            self.myEater=tab.index(True)
        except:
            self.myEater= -1
            
    def changePosition(self):
        while self.change:
            randX=randint(2, int(self.boardLenght[2]/self.boxSize)-1)
            randY=randint(2, int(self.boardLenght[3]/self.boxSize)-1 )
            self.x=self.boardLenght[0]+(self.boxSize*randX)-(self.boxSize/4) -1
            self.y=self.boardLenght[1]+(self.boxSize*randY)-(self.boxSize/4) -1
            tab=self.verifInSnake()
            if not(True in tab):
                self.change=False
                    
    def place(self):
        self.changePosition()
        circle(self.display, (255, 0, 0),(self.x, self.y), self.width)
        self.change= True in self.verifInSnake()
        self.whoAreEatMe()
