import pygame, sys
from pygame.locals import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
from constant import *
import os # Importe le module os pour travailler avec les chemins
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../back-end/', '') # Utilise chemin_racine
sys.path.append(chemin)
sys.path.append('../object')
from Chevron import Chevron
from icon import Exit
from database import loadHelpText
class Help(MoePage):
    def __init__(self):
        MoePage.__init__(self, False, [])
        self.currentPage=1
        self.fontText=CAMBRIAMATH30
        self.color=WHITE
        self.helpText=loadHelpText()
        self.squareWidth=40
        self.borderWidth=2
        self.obj=[
            Chevron(self.display,self.color,6.5*X_UNIT-30, 9*Y_UNIT, 30, 30, "left"), 
            Chevron(self.display,self.color,8.5*X_UNIT, 9*Y_UNIT, 30, 30, "right"), 
            Exit(self.display, WHITE, 9*X_UNIT,Y_UNIT, 30, 5)
        ]
        self.indexLeft=-1
        self.indexRight=0
        self.indexExit=1
        self.forLauch=5
        
    def updateIndex(self):
        if self.currentPage==1:
            self.obj=[]
            self.obj.append(Chevron(self.display,self.color,8.5*X_UNIT, 9*Y_UNIT, 30, 30, "right"))
            self.obj.append(Exit(self.display, WHITE, 9*X_UNIT,Y_UNIT/2, 30, 3))
            self.indexLeft=-1
            self.indexRight=0    
            self.indexExit=1
        elif self.currentPage==4:
            self.obj=[]
            self.obj.append(Chevron(self.display,self.color,6.5*X_UNIT-30, 9*Y_UNIT, 30, 30, "left"))
            self.obj.append(Exit(self.display, WHITE, 9*X_UNIT,Y_UNIT/2, 30, 3))
            self.indexLeft=0
            self.indexRight=-1 
            self.indexExit=1
        else:
            self.obj=[]
            self.obj.append(Chevron(self.display,self.color,6.5*X_UNIT-30, 9*Y_UNIT, 30, 30, "left"))
            self.obj.append(Chevron(self.display,self.color,8.5*X_UNIT, 9*Y_UNIT, 30, 30, "right"))
            self.obj.append(Exit(self.display, WHITE, 9*X_UNIT,Y_UNIT/2, 30, 3))
            self.indexLeft=0
            self.indexRight=1 
            self.indexExit=2
            
    def renderParagraph(self,text, position, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            # Vérifier si l'ajout du mot dépasse la largeur maximale
            test_line = current_line + word + ' '
            if self.fontText.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
            

        # Ajouter la dernière ligne
        if current_line:
            lines.append(current_line)

        # Afficher chaque ligne
        y_offset = 0
        for line in lines:
            text_surface = self.fontText.render(line,  True, self.color)
            self.display.blit(text_surface, (position[0], position[1] + y_offset))
            y_offset += self.fontText.get_height()
            
    def drawText(self):
        self.display.blit(JOKERMAN50.render(self.helpText["HEAD"], True, WHITE), (3.5*X_UNIT, 0.5*Y_UNIT))
        self.display.blit(CAMBRIAMATH30.render(str(self.currentPage)+"/4", True, WHITE), (7*X_UNIT, 9*Y_UNIT))
        if self.currentPage==1:
            self.renderParagraph(self.helpText["PAGE1"], (2*X_UNIT, 2*Y_UNIT), X_UNIT*8)
        elif self.currentPage==2:
            self.renderParagraph(self.helpText["PAGE2"][0], (2*X_UNIT, 2*Y_UNIT), X_UNIT*8)
            self.renderParagraph(self.helpText["PAGE2"][1], (2*X_UNIT, 3*Y_UNIT), X_UNIT*8)
            self.renderParagraph(self.helpText["PAGE2"][2], (2*X_UNIT, 4*Y_UNIT), X_UNIT*8)
            self.renderParagraph(self.helpText["PAGE2"][3], (2*X_UNIT, 6.5*Y_UNIT), X_UNIT*8)
        elif self.currentPage==3:
            self.renderParagraph(self.helpText["PAGE2"][4], (2*X_UNIT, 2*Y_UNIT), X_UNIT*8)
            self.renderParagraph(self.helpText["PAGE2"][5], (2*X_UNIT, 5*Y_UNIT), X_UNIT*8)
        elif self.currentPage==4:
            self.renderParagraph(self.helpText["PAGE4"][0], (2*X_UNIT, 2*Y_UNIT), X_UNIT*8) 
            
    def drawTouch(self):
        if self.currentPage==4:
            touchUpCoord=(
                                    (4*X_UNIT-self.squareWidth/2, 3*Y_UNIT), 
                                    (8*X_UNIT-self.squareWidth/2, 3*Y_UNIT), 
                                    (4*X_UNIT-self.squareWidth/2, 5*Y_UNIT), 
                                    (8*X_UNIT-self.squareWidth/2, 5*Y_UNIT)
                                )
            touch=[
                ["up", "dw", "lf", "rg"], 
                ["z","s","q" , "d" ], 
                ["t", "g", "f", "h"], 
                ["i", "k", "j", "l"], 
            ]
            #Permet de distinguer si le clavier est en qwerty ou azety 
            if self.setting[4]==1:
                touch[1][0]="w"
                touch[1][2]="a"
            for i in range(0, 4, 1):
                # affichage des rectangle
                pygame.draw.rect(self.display,WHITE,  (touchUpCoord[i][0], touchUpCoord[i][1], self.squareWidth, self.squareWidth), self.borderWidth) #haut
                pygame.draw.rect(self.display,WHITE, (touchUpCoord[i][0], touchUpCoord[i][1]+self.squareWidth-self.borderWidth, self.squareWidth, self.squareWidth), self.borderWidth) #bas
                pygame.draw.rect(self.display,WHITE, (touchUpCoord[i][0] -self.squareWidth+self.borderWidth,touchUpCoord[i][1]+self.squareWidth-self.borderWidth, self.squareWidth, self.squareWidth), self.borderWidth) #gauche
                pygame.draw.rect(self.display,WHITE, (touchUpCoord[i][0]+self.squareWidth-self.borderWidth, touchUpCoord[i][1]+self.squareWidth-self.borderWidth, self.squareWidth, self.squareWidth), self.borderWidth) #droite
                #affichage du numero du joueur
                textObject=CAMBRIAMATH30.render(self.text["MODE"][1]+" "+str(i+1), True, WHITE)
                rect =textObject.get_rect(center=(touchUpCoord[i][0] +self.squareWidth/2, touchUpCoord[i][1]+2.5*self.squareWidth))
                self.display.blit(textObject,rect ) 
                #affichage des touches
                    #haut
                textObject=CAMBRIAMATH30.render(touch[i][0], True, WHITE)
                rect =textObject.get_rect(center=(touchUpCoord[i][0] +self.squareWidth/2, touchUpCoord[i][1]+0.5*self.squareWidth))
                self.display.blit(textObject,rect ) 
                    #bas
                textObject=CAMBRIAMATH30.render(touch[i][1], True, WHITE)
                rect =textObject.get_rect(center=(touchUpCoord[i][0] +self.squareWidth/2, touchUpCoord[i][1]+1.5*self.squareWidth))
                self.display.blit(textObject,rect ) 
                    #gauche
                textObject=CAMBRIAMATH30.render(touch[i][2], True, WHITE)
                rect =textObject.get_rect(center=(touchUpCoord[i][0] -0.5*self.squareWidth, touchUpCoord[i][1]+1.5*self.squareWidth))
                self.display.blit(textObject,rect ) 
                    #doirte
                textObject=CAMBRIAMATH30.render(touch[i][3], True, WHITE)
                rect =textObject.get_rect(center=(touchUpCoord[i][0] +3*self.squareWidth/2, touchUpCoord[i][1]+1.5*self.squareWidth))
                self.display.blit(textObject,rect ) 
                
    def play(self):
        mouseX=mouseY=0
        BG_IMAGE = pygame.image.load(chemin_racine+"/background.png").convert()
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (self.width, self.height))
        self.updateIndex()
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
                    self.clickEffect()
                    if self.indexLeft!=-1:
                        if self.obj[self.indexLeft].feelClik:
                            self.currentPage-=1
                            self.obj[self.indexLeft].feelClik=False
                            self.updateIndex()
                    if self.indexRight!=-1:
                        if self.obj[self.indexRight].feelClik:
                            self.currentPage+=1
                            self.obj[self.indexRight].feelClik=False
                            self.updateIndex()
                    if self.obj[self.indexExit].feelClik:
                        return
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    self.survolEffect()
            self.drawText()
            self.drawTouch()
            self.survolEffect()
            pygame.display.update()

