import pygame, sys, os, pyautogui
from pygame.locals import *
from constant import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
sys.path.append('../listObject')
from ListRadio import ListRadio
from database import *
sys.path.append('../object')
from TextSelect import TextSelect
from NumberInput import NumberInput
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../../back-end/', '') # Utilise chemin_racine
sys.path.append(chemin)
from database import dumpMode
class Mode(MoePage):
    def __init__(self):
        MoePage.__init__(self,False, [])
        self.obj=[
            ListRadio(self.display, 4.2*X_UNIT, 2.5*Y_UNIT, 12, 1.2*X_UNIT, self.mode[0]-1, WHITE, 4), 
            ListRadio(self.display, 4.2*X_UNIT, 3.5*Y_UNIT, 12,1.5* X_UNIT, self.mode[1], WHITE, 3),
            ListRadio(self.display, 4.2*X_UNIT, 4.5*Y_UNIT, 12,1.7* X_UNIT, self.mode[2], WHITE, 2 ),
            ListRadio(self.display, 4.2*X_UNIT, 5.5*Y_UNIT, 12,2.4* X_UNIT, self.mode[3], WHITE, 2),
            TextSelect(self.display, self.text["GENERAL"][0], WHITE, 8.5*X_UNIT, 7.5*Y_UNIT, CAMBRIAMATH30, 7, 2, 10) , 
            TextSelect(self.display, self.text["GENERAL"][1], WHITE, 6*X_UNIT, 7.5*Y_UNIT, CAMBRIAMATH30, 7, 2, 10), 
            NumberInput(self.display, 8.8*X_UNIT , 4.5*Y_UNIT-25, WHITE, 70, 50, CAMBRIAMATH25, 20, 15, 5, self.mode[4])
        ]
        self.forLauch=6
        
    def drawText(self):
        niv=self.text["BEST"][1:]
        resolution=["640*640",str(pyautogui.size()[0])+"*"+str(pyautogui.size()[1])]
        self.display.blit(JOKERMAN50.render(self.text["MODE"][0], True, WHITE), (4*X_UNIT, 0.5*Y_UNIT))
        for i in range(0, 4, 1):
            self.display.blit(CAMBRIAMATH30.render(str(i+1),True, WHITE),(20+(4.2+i*1.5)*X_UNIT, 2.5*Y_UNIT-14))
        for i in range(0, 3, 1):
            self.display.blit(CAMBRIAMATH25.render(niv[i],True, WHITE),(20+(4.2+i*1.7)*X_UNIT, 3.5*Y_UNIT-10))
        for i in range(0, 2, 1):
            self.display.blit(CAMBRIAMATH25.render(self.text["TYPE"][i],True, WHITE),(20+(4.2+i*2)*X_UNIT, 4.5*Y_UNIT-10))
        for i in range(0, 2, 1):
            self.display.blit(CAMBRIAMATH25.render(resolution[i],True, WHITE),(20+(4.2+i*2.7)*X_UNIT, 5.5*Y_UNIT-10))
        for i in range(1, len(self.text["MODE"]), 1):
            self.display.blit(CAMBRIAMATH30.render(self.text["MODE"][i]+" :",True, WHITE),(1.5*X_UNIT, (1.3+i)*Y_UNIT))
            
    def play(self):
        chemin_racine = os.path.dirname(os.path.abspath(__file__))
        BG_IMAGE = pygame.image.load(chemin_racine+"/background.png").convert()
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        mouseX=mouseY=0
        while 1:
            self.display.blit(BG_IMAGE, (0, 0))
            self.allPlace()
            for event in pygame.event.get():
                if event.type== QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)
                    if self.obj[4].feelClik :
                        dumpMode([self.obj[0].forDB+1, self.obj[1].forDB, self.obj[2].forDB, self.obj[3].forDB, self.obj[6].value])
                        return
                    if self.obj[5].feelClik:
                        self.forLauch=5
                        return
                    self.clickEffect()
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    self.survolEffect()
            self.survolEffect()
            self.drawText()
            pygame.display.update()
            FPS.tick(30)

