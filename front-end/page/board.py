import pygame, sys, os
from pygame.locals import *
from constant import *
sys.path.append('../../MOE Library')
from MoePage import MoePage
sys.path.append('../object')
from snake import *
from icon import *
from Timer import Timer
sys.path.append('../listObject')
from ListForGames import ListForGames
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../back-end/', '') # Utilise chemin_racine
sys.path.append(chemin)
from database import dumpGameScore

class Board(MoePage):
    def __init__(self):
        MoePage.__init__(self,True, [])
        self.maxX=int(self.width/X_UNIT)
        self.maxY=int(self.height/Y_UNIT)
        self.bgColor=ALLBGCOLOR[self.setting[0]]
        self.colorTheme=ALLCOLORTHEME[self.setting[2]]
        self.snakeColor=ALLSNAKECOLOR[self.setting[1]]
        level=(200, 100, 75)
        self.speed=level[self.mode[1]]
        if self.mode[3]==1:
            self.boarLenght=(X_UNIT-BORDER_WIDTH,1.5*Y_UNIT -BORDER_WIDTH, (self.maxX-1)*X_UNIT-BOX_SIZE , (self.maxY-2.5)*Y_UNIT-1.5*BORDER_WIDTH )
            #A ajouter pour que tout les serpent soient bien positionné
            bonusX=0
            bonusY=2*BORDER_WIDTH
        else:
            self.boarLenght=(X_UNIT-BORDER_WIDTH,1.5*Y_UNIT -BORDER_WIDTH, 8*X_UNIT , 8*Y_UNIT )
            #A ajouter pour que tout les serpent soient bien positionné
            bonusX=2*BORDER_WIDTH
            bonusY=0
        allPos=[
                [
                    [X_UNIT+BOX_SIZE*3,1.5*Y_UNIT, RIGHT],
                    [X_UNIT+BOX_SIZE*2,1.5*Y_UNIT, RIGHT],
                    [X_UNIT+BOX_SIZE*1,1.5*Y_UNIT, RIGHT],
                    [X_UNIT,1.5*Y_UNIT, RIGHT]
                ], 
                 [
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*3+bonusX,1.5*Y_UNIT, LEFT],
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*2+bonusX,1.5*Y_UNIT, LEFT],
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*1+bonusX,1.5*Y_UNIT, LEFT],
                    [(self.maxX-2)*X_UNIT+bonusX,1.5*Y_UNIT, LEFT]
                ], 
                [
                    [X_UNIT+BOX_SIZE*3,(self.maxY-2.5)*Y_UNIT +bonusY, RIGHT],
                    [X_UNIT+BOX_SIZE*2,(self.maxY-2.5)*Y_UNIT+bonusY, RIGHT],
                    [X_UNIT+BOX_SIZE*1,(self.maxY-2.5)*Y_UNIT+bonusY, RIGHT],
                    [X_UNIT,(self.maxY-2.5)*Y_UNIT+bonusY, RIGHT]
                ], 
                [
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*3+bonusX,(self.maxY-2.5)*Y_UNIT+bonusY, LEFT],
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*2+bonusX,(self.maxY-2.5)*Y_UNIT+bonusY, LEFT],
                    [(self.maxX-2)*X_UNIT-BOX_SIZE*1+bonusX,(self.maxY-2.5)*Y_UNIT+bonusY, LEFT],
                    [(self.maxX-2)*X_UNIT+bonusX,(self.maxY-2.5)*Y_UNIT+bonusY, LEFT]
                ]                
        ]
        allDirection=[RIGHT, LEFT, RIGHT, LEFT]
        allColor=[[GREEN, GREEN2], [RED, RED2], [YELLOW, YELLOW2], [BLUE, BLUE2]]
        listDirection=allDirection[:self.mode[0]]
        if self.mode[0]==1:
            listColor=[self.snakeColor]
        else:
            listColor=allColor[:self.mode[0]]
        listPos=allPos[: self.mode[0]]
        self.setting[4]
        allKey=[
            [
                [K_UP, K_DOWN, K_LEFT, K_RIGHT], 
                [K_z,K_s, K_q, K_d], 
                [K_t,K_g, K_f,  K_h], 
                [K_i,K_k, K_j,  K_l]
            ], 
            [
                [K_UP, K_DOWN, K_LEFT, K_RIGHT], 
                [K_w, K_s, K_a, K_d], 
                [K_t,K_g, K_f,  K_h], 
                [K_i,K_k, K_j,  K_l]
            ]        
        ]
        keyration=allKey[self.setting[4]]
        self.obj=[
                        PlayOrPause(self.display, self.colorTheme, (self.maxX-2)*X_UNIT,10, 25, 30, 2), 
                        Exit(self.display, self.colorTheme, (self.maxX-1)*X_UNIT,10, 30, 2), 
                        ListForGames(self.display,self.mode[0],listColor,BOX_SIZE,16, 4, listDirection,listPos,self.boarLenght,BOX_SIZE, keyration)
                    ]
        if self.mode[2]==1:
            self.obj.append(Timer(self.display, 4.5*X_UNIT, 0.8*Y_UNIT, self.colorTheme, self.mode[4]*60, CAMBRIAMATH30 ))
        self.forLauch=7
        
    def headBoard(self):
        if self.mode[0]==1:
            for x in range(1, len(self.text["BOARD"]), 1):
                self.display.blit(CAMBRIAMATH25.render(self.text["BOARD"][x]+" :", True, self.colorTheme), (20+ X_UNIT*4*(x-1), 10))
            self.display.blit(CAMBRIAMATH25.render(self.text["BEST"][self.mode[1]+1], True, self.colorTheme), (5+ X_UNIT*2, 10))
            #On utilise le try except afin de s'assurer que meme s'il n'y a pas d'objet le jeu ne crash pas 
            try:
                self.display.blit(CAMBRIAMATH25.render(str(self.obj[2].obj[1].obj[0].score), True, self.colorTheme), (X_UNIT*5.5, 10))
            except:
                return
        else:
            for x in self.obj[2].obj[1].surviver:
                y=0
                i=(x-1)%2
                j=int(x-3>=0)
                self.display.blit(CAMBRIAMATH25.render(self.text["MODE"][1]+" "+str(x)+":"+str(self.obj[2].obj[1].obj[y].score), True, self.colorTheme), (20+ X_UNIT*3*(i) , 10 +j*(Y_UNIT-10)))
                y+=1
            for x in self.obj[2].obj[1].died:
                i=(x-1)%2
                j=int(x-3>=0)
                self.display.blit(CAMBRIAMATH25.render(self.text["MODE"][1]+" "+str(x)+":"+str(self.obj[2].obj[1].scoreDied[x-1]), True, self.colorTheme), (20+ X_UNIT*3*(i) , 10 +j*(Y_UNIT-10)))
             
    def drawBoard(self):
        self.display.fill(self.bgColor)
        pygame.draw.rect(self.display,self.colorTheme, self.boarLenght, BORDER_WIDTH )
        if self.mode[3]==1:
            for x in range(0, int(self.boarLenght[2]-BOX_SIZE), BOX_SIZE):
                #ligne verticale
                pygame.draw.line(self.display, self.colorTheme, (self.boarLenght[0] +x+BORDER_WIDTH, self.boarLenght[1]), (self.boarLenght[0] +x+BORDER_WIDTH,self.boarLenght[1]+self.boarLenght[3]-BORDER_WIDTH))
            for x in range(0, int(self.boarLenght[3]-2*BOX_SIZE), BOX_SIZE):
                #ligne orizontale
                pygame.draw.line(self.display, self.colorTheme, (self.boarLenght[0] +BORDER_WIDTH,self.boarLenght[1]+BORDER_WIDTH +BOX_SIZE +x), (self.boarLenght[0]+self.boarLenght[2]-BORDER_WIDTH,self.boarLenght[1]+BORDER_WIDTH+BOX_SIZE +x))
        else:
            for x in range(0, 496, BOX_SIZE):
                #ligne verticale
                pygame.draw.line(self.display, self.colorTheme, (X_UNIT+BOX_SIZE +x, 1.5*Y_UNIT -BORDER_WIDTH), (X_UNIT+BOX_SIZE +x,8*Y_UNIT + 1.5*Y_UNIT -2*BORDER_WIDTH ))
                #ligne orizontale
                pygame.draw.line(self.display, self.colorTheme, (X_UNIT, 1.5*Y_UNIT +BOX_SIZE +x), (X_UNIT +X_UNIT*8 -2*BORDER_WIDTH,1.5*Y_UNIT  +BOX_SIZE +x))
        
    def pause(self):
        self.obj[2].isPlay=not self.obj[2].isPlay
        if self.mode[2]==1:
            self.obj[3].isPlay=not self.obj[3].isPlay
        
    def play(self):
        mouseX=mouseY=0
        while 1:
            self.drawBoard()
            self.headBoard()
            self.allPlace()
            
            for event in pygame.event.get():
                if event.type== QUIT:
                    pygame.quit()
                    sys.exit()
                if(event.type==MOUSEBUTTONUP):
                    mouseX, mouseY=event.pos
                    self.updateListClicked(mouseX, mouseY)
                    #Mettre fin au jeu si on clicke sur le bouttton de sortie
                    if self.clicked[1]==True:
                        self.forLauch=5
                        return 
                    if self.clicked[0]==True:
                        self.pause()                        
                    self.clickEffect()
                if (event.type==KEYDOWN):
                    if (event.key==K_SPACE):
                        self.obj[0].isPlay=not self.obj[0].isPlay
                        self.pause()
                    if event.key==K_ESCAPE:
                        self.forLauch=5
                        return                        
                    self.obj[2].direction(event.key)
                if event.type==MOUSEMOTION:
                    mouseX, mouseY=event.pos
                    self.updateListSurvoled(mouseX, mouseY)
                    self.survolEffect()
            # met fin à la partie quand il n'y a plus de serpent
            if len(self.obj[2].obj[1].obj)==0:
                print(self.obj[2].obj[1].scoreDied)
                dumpGameScore(self.obj[2].obj[1].scoreDied)
                return
            #verifier si le minuteur a atteint sa limte
            if self.mode[2]==1:
                if self.obj[3].end:
                    print(self.obj[2].obj[1].scoreDied)
                    dumpGameScore(self.obj[2].obj[1].scoreDied)
                    return
            pygame.display.update()
            pygame.time.wait(self.speed)
            FPS.tick(30)
            

