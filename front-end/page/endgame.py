import pygame, sys, os
from pygame.locals import *
from constant import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../back-end/', '') # Utilise chemin_racine
sys.path.append(chemin)
from database import loadGameScore, dumpScore
sys.path.append('../listObject')
from ListTextSelect import ListTextSelect
class EndGame(MoePage):
    def __init__(self):
        MoePage.__init__(self,True, [])
        self.maxX=int(self.width/X_UNIT)
        self.playerScore=loadGameScore()
        self.forLauch=5
        self.firework=[0, 0]
        self.bgColor=ALLBGCOLOR[self.setting[0]]
        self.colorTheme=ALLCOLORTHEME[self.setting[2]]
        self.obj=[
                        ListTextSelect(self.display, self.colorTheme, 5*X_UNIT, 8*Y_UNIT, 2*X_UNIT, [self.text["END"][2], self.text["GENERAL"][0]], CAMBRIAMATH30, 2, 2, 2, "horizontal")
                    ]
    def animationForwinner(self):
        pygame.draw.rect(self.display, self.colorTheme, (X_UNIT,7*Y_UNIT, 16, 2*Y_UNIT ))
        pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT,7*Y_UNIT, 16, 2*Y_UNIT ))
        if self.firework[0]<4*X_UNIT:
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6, 7*Y_UNIT-5-self.firework[0], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6, 7*Y_UNIT-5-self.firework[0], 4, 4))
            self.firework[0]+=3
        elif self.firework[1]<50:
        #trajectoire y=x
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6+self.firework[1], 7*Y_UNIT-5-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6-self.firework[1], 7*Y_UNIT-5-self.firework[0] -self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6+self.firework[1], 7*Y_UNIT-5-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6-self.firework[1], 7*Y_UNIT-5-self.firework[0] -self.firework[1], 4, 4))
        #trajectoire y=0 
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6+2*self.firework[1], 7*Y_UNIT-5-self.firework[0] , 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6-2*self.firework[1], 7*Y_UNIT-5-self.firework[0] , 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6+2*self.firework[1], 7*Y_UNIT-5-self.firework[0] , 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6-2*self.firework[1], 7*Y_UNIT-5-self.firework[0] , 4, 4))
        #trajectoire x=0
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6, 7*Y_UNIT+15-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6, 7*Y_UNIT-15-self.firework[0] -self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6, 7*Y_UNIT+15-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6, 7*Y_UNIT-15-self.firework[0] -self.firework[1], 4, 4))
        #trajectoire y=-x
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6-self.firework[1], 7*Y_UNIT-5-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (X_UNIT+6+self.firework[1], 7*Y_UNIT-5-self.firework[0] -self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6-self.firework[1], 7*Y_UNIT-5-self.firework[0] +self.firework[1], 4, 4))
            pygame.draw.rect(self.display, self.colorTheme, (8*X_UNIT+6+self.firework[1], 7*Y_UNIT-5-self.firework[0] -self.firework[1], 4, 4))
        #incrementation
            self.firework[1]+=2
        else:
            self.firework=[0, 0]
            
    def drawText(self):
        headText=JOKERMAN50.render(self.text["END"][0], True, self.colorTheme)
        headTextRect=headText.get_rect(center=(self.width/2, X_UNIT))
        self.display.blit(headText, headTextRect)
        if self.mode[0]==1:
            self.display.blit(CAMBRIAMATH25.render(self.text["BOARD"][1]+" :", True, self.colorTheme), (X_UNIT*3, Y_UNIT*3))
            self.display.blit(CAMBRIAMATH25.render(self.text["BEST"][self.mode[1] +1], True, self.colorTheme), (X_UNIT*5, Y_UNIT*3))
            self.display.blit(CAMBRIAMATH25.render(self.text["BOARD"][2]+" :", True, self.colorTheme), (X_UNIT*3, Y_UNIT*4))
            self.display.blit(CAMBRIAMATH25.render(str(self.playerScore[0]), True, self.colorTheme), (X_UNIT*5, Y_UNIT*4))
        else:
            for i in range(0, self.mode[0], 1):
                self.display.blit(CAMBRIAMATH25.render(self.text["MODE"][1]+" "+str(i+1)+":"+str(self.playerScore[i]), True, self.colorTheme), (X_UNIT*3, Y_UNIT*(3+i)))
    
    # Sauvegarder le scrre au cas où il a eu le meilleur score
    def saveScore(self):
        if self.playerScore[0]>self.bestScore[self.mode[1]] and self.mode[0]==1:
            self.bestScore[self.mode[1]]=self.playerScore[0]
            dumpScore(self.bestScore)
    def play(self):
        while 1:
            self.display.fill(self.bgColor)
            self.drawText()
            self.allPlace()
            for event in pygame.event.get():
                if event.type== QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)
                    if self.obj[0].clicked[0]==True:
                        self.forLauch=6
                        self.saveScore()
                        return 
                    if self.obj[0].clicked[1]==True:
                        self.saveScore()
                        return                        
                    self.clickEffect()
                if (event.type==KEYDOWN):
                    if event.key==K_ESCAPE:
                        self.saveScore()
                        return                             
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    self.survolEffect()
                    
            if self.playerScore[0]>self.bestScore[self.mode[1]] and self.mode[0]==1:
                self.animationForwinner()
            self.survolEffect()
            pygame.display.update()
            FPS.tick(30)
            
