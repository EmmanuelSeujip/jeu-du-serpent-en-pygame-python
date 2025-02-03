import pygame, sys
from pygame.locals import *
from constant import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
import os # Importe le module os pour travailler avec les chemins
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../listObject/', '') # Utilise chemin_racine
sys.path.append(chemin)
from ListTextSelect import ListTextSelect

class Home(MoePage):
    def __init__(self):
        MoePage.__init__(self, 0, [])
        self.obj=[
            ListTextSelect(self.display,WHITE, 6*X_UNIT, 2.5*Y_UNIT,Y_UNIT,self.text["HOME"][1:], CAMBRIAMATH30, 5, 2, 10)
        ]
        self.forLauch=5
            
    def drawText(self):
        welcome=JOKERMAN50.render("BIENVENUE", True, WHITE)
        self.display.blit(welcome, (3.5*X_UNIT, 0.5*Y_UNIT))
    
    def play(self):
        mouseX=mouseY=0
        BG_IMAGE = pygame.image.load(chemin_racine+"/background.png").convert()
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        while 1:
            self.display.blit(BG_IMAGE, (0, 0))
            for event in pygame.event.get():
                if event.type== QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)
                    self.clickEffect()
                    self.forLauch=self.obj[0].forLauch
                    if self.forLauch!=5:
                        return
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    
            self.survolEffect()
            self.drawText()
            self.allPlace()
            pygame.display.update()
            FPS.tick(30)

