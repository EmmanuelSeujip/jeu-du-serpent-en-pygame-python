import pygame, sys
from pygame.locals import *
from constant import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
sys.path.append('../listObject')
from ListRectangleColor  import ListRectangleColor
from ListRadio import ListRadio
from ListTextSelect import ListTextSelect
sys.path.append('../object')
from database import dumpSetting, loadSetting, loadLanguage
import os # Importe le module os pour travailler avec les chemins
#utilisation de chemin_racine permet de facilement retrouver le chemin lors de l'appel par le main
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
class Settings(MoePage):
    def __init__(self):
        MoePage.__init__(self,False, [])
        self.obj=[
            ListRectangleColor(self.display, 5*X_UNIT, 2*Y_UNIT, 40, 20, self.setting[0], [BGCOLOR, WHITE,MARRON,GRAY]), 
            ListRectangleColor(self.display, 5*X_UNIT, 3*Y_UNIT, 40, 20, self.setting[1], [GREEN, RED, YELLOW, BLUE]), 
            ListRectangleColor(self.display, 5*X_UNIT, 4*Y_UNIT, 40, 20, self.setting[2], ALLCOLORTHEME), 
            ListRadio(self.display, 6*X_UNIT, 5.2*Y_UNIT, 12,X_UNIT, self.setting[3], WHITE, len(self.listLang)), 
            ListRadio(self.display, 6.8*X_UNIT, 6.2*Y_UNIT, 12,2*X_UNIT, self.setting[4], WHITE, len(self.listLang)),
            ListTextSelect(self.display, WHITE, 5*X_UNIT, 7.2*Y_UNIT, 3*X_UNIT, self.text["GENERAL"], CAMBRIAMATH30, 2, 2, 2, "horizontal")
        ]
        self.forLauch=5
        self.originalLang=self.setting[3]
        
    def drawText(self):
        self.display.blit(JOKERMAN50.render(self.text["SETTINGS"][0], True, WHITE), (3.5*X_UNIT, 0.5*Y_UNIT))
        for x in range(1, len(self.text["SETTINGS"]), 1) :
            self.display.blit(CAMBRIAMATH30.render(self.text["SETTINGS"][x]+" :", True, WHITE), (3*X_UNIT, x*Y_UNIT +Y_UNIT))
        
        for i in range(0,len(self.listLang), 1)  :
            self.display.blit(CAMBRIAMATH30.render(self.listLang[i], True, WHITE), (5*X_UNIT+17 +i*(X_UNIT +15) , 5*Y_UNIT ))
        self.display.blit(CAMBRIAMATH30.render("azerty", True, WHITE), (5*X_UNIT+20 , 6*Y_UNIT ))
        self.display.blit(CAMBRIAMATH30.render("qwerty", True, WHITE), (7*X_UNIT+30 , 6*Y_UNIT ))
        
    def play(self):
        self.setting=loadSetting()
        mouseX=mouseY=0
        BG_IMAGE = pygame.image.load(chemin_racine+"/background.png").convert()
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        while 1:
            self.display.blit(BG_IMAGE, (0, 0))
            self.allPlace()
            for event in pygame.event.get():
                if event.type== QUIT:
                    self.setting[3]=self.originalLang
                    dumpSetting(self.setting)
                    pygame.quit()
                    sys.exit()
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)  
                    #lorsqu'on appuie Ok s'a envoie les donnée dans la bd
                    if self.obj[5].obj[0].feelClik:
                        dumpSetting([self.obj[0].forDB,self.obj[1].forDB,self.obj[2].forDB,self.obj[3].forDB, self.obj[4].forDB])
                        return 
                    #lorsqu'on appuie sur annulé
                    if self.obj[5].obj[1].feelClik:
                        self.setting[3]=self.originalLang
                        dumpSetting(self.setting)
                        return 
                    self.clickEffect()
                    #Pour changer directement la langue
                    if self.obj[3].forDB!=self.setting[3]:
                        self.setting[3]=self.obj[3].forDB
                        dumpSetting(self.setting)
                        self.text=loadLanguage()
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    self.survolEffect()
            self.drawText()
            self.survolEffect()
            pygame.display.update()
