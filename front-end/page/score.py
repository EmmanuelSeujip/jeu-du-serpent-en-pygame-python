import pygame, sys
from pygame.locals import *
from constant import *
sys.path.append('../object')
from TextSelect import TextSelect
sys.path.append('../listObject')
sys.path.append('../../MOE Library')
from MoePage import MoePage
import os # Importe le module os pour travailler avec les chemins
#utilisation de chemin_racine permet de facilement retrouver le chemin lors de l'appel par le main
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
class Score(MoePage):
    def __init__(self):
        MoePage.__init__(self,False, [])
        self.obj=[
            TextSelect(self.display, self.text["GENERAL"][0], WHITE, 7*X_UNIT, 6.5*Y_UNIT, CAMBRIAMATH30, 7, 2, 10)
        ]
        self.forLauch=5
        
    def drawText(self):
        welcome=JOKERMAN50.render(self.text["BEST"][0], True, WHITE)
        self.display.blit(welcome, (2.5*X_UNIT, 0.5*Y_UNIT))
        x=0
        for i in range(1, len(self.text["BEST"]), 1):
            self.display.blit(CAMBRIAMATH30.render(self.text["BEST"][i]+" : "+str(self.bestScore[i-1]), True, WHITE), (4*X_UNIT, 3*Y_UNIT+x))
            x=x+Y_UNIT

    def play(self):
        mouseX=mouseY=0
        BG_IMAGE = pygame.image.load(chemin_racine+"/background.png").convert()
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        while 1:
            self.display.blit(BG_IMAGE, (0, 0))
            self.drawText()
            for event in pygame.event.get():
                if event.type== QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)
                    if self.obj[0].feelClik :
                        return
            self.allPlace()
            self.survolEffect()
            pygame.display.update()
