import sys
sys.path.append('../../MOE Library')
from ListMoeObject import ListMoeObject
sys.path.append('../object')
from snake import Snake
class ListSnake(ListMoeObject):
    def __init__(self, display, numPlayer, listColor, size, smallSize, padding, direction, allPosition, boardLenght,boxSize=24,key= []):
        ListMoeObject.__init__(self, display)
        self.numPlayer=numPlayer
        self.listColor=listColor
        self.size=size
        self.smallSize=smallSize
        self.padding=padding
        self.direction=direction
        self.boxSize=boxSize
        self.isPlay=True
        self.allPosition=allPosition
        self.key=key
        self.boardLenght=boardLenght
        self.playerCollision=[]
        self.scoreDied=[]
        self.died=[]
        self.surviver=[]
        for i in range(0, numPlayer, 1):
            self.obj.append(Snake(display,listColor[i][0], listColor[i][1], size, smallSize, padding, direction[i], allPosition[i]))
            self.surviver.append(i+1)
            self.scoreDied.append(0)
            
    def between(self, val,pos,lenght):
        if (pos<=val and val<=pos+lenght):
            return True
        return False
        
    def updateDirection(self,keyPressed):
        if (self.isPlay):
            for i in range(0, len(self.obj), 1):
                if (keyPressed==self.key[i][0] and self.obj[i].direction!="down"):
                    self.obj[i].direction="up"
                elif (keyPressed==self.key[i][1] and self.obj[i].direction!="up"):
                    self.obj[i].direction="down"
                elif (keyPressed==self.key[i][2] and self.obj[i].direction!="right"):
                    self.obj[i].direction="left"
                elif (keyPressed==self.key[i][3] and self.obj[i].direction!="left"):    
                    self.obj[i].direction="right"
    
    def updatePositionSnake(self):
        i=0
        while i<len(self.obj):
            self.allPosition[i]=self.obj[i].listPosition
            i+=1
            
    def verifPlayerCollision(self):
        #verifier que la tete du serpent ne rencontre pas un autre serpent ou lui meme
        
        #On recupere toute les entete
        allHead=[]
        for x in range(0, len(self.obj), 1):
            allHead.append(self.obj[x].listPosition[0])
        #Pour chaque serpent
        for i in range(0, len(self.obj), 1):
            #on prend les tete de chaque serpent
            for j in range(0, len(self.obj),1):
                #on verifie alors que aucune tete n'est danns aucun serpent
                for t in range(1, len(self.obj[i].listPosition), 1):
                    if (self.between(allHead[j][0],self.obj[i].listPosition[t][0], 24) and self.between(allHead[j][1],self.obj[i].listPosition[t][1], 24) and i!=j):
                        return (True, i)
                    
        #verifier la sortir hors du plateau de jeu
        for y in range(0, len(self.obj), 1):
            headX=self.obj[y].listPosition[0][0]
            headY=self.obj[y].listPosition[0][1] 
            cond1=not(self.between(headX,self.boardLenght[0] , self.boardLenght[2] ))
            cond2=not(self.between(headY,self.boardLenght[1], self.boardLenght[3] ))
            if  cond1 or cond2 :
                return (True, y)            
        return (False, -1)
        
    #fonction pour supprimer un joueur
    def deletePlayer(self):
        col=self.verifPlayerCollision()
        if(col[0]):
            self.died.append(self.surviver[col[1]])
            self.scoreDied[col[1]]=self.obj[col[1]].score
            del self.obj[col[1]]
            del self.key[col[1]]
            del self.surviver[col[1]]
            
            
    def place(self):
        for obj in self.obj:
            obj.place()
            if self.isPlay:
                obj.move()
        self.deletePlayer()
        self.updatePositionSnake()
