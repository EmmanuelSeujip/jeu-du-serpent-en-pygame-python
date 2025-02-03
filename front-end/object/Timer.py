import sys
sys.path.append('../../MOE Library')
from MoeObject import MoeObject
from pygame import time

class Timer(MoeObject):
    def __init__(self, display,x,y ,color,duration, font):
        MoeObject.__init__(self, display, x, y)
        self.duration=duration
        self.remainingTime=duration
        self.minute= self.remainingTime // 60
        self.second=self.remainingTime % 60
        self.text=f"{self.minute:02}:{self.second:02}"
        self.font=font
        self.color=color
        self.startTicks = 0 # temps de départ
        self.start=False
        self.end=False
        self.isPlay=True

    def verifSurvol(self, posX, posY):
        return

    def verifClick(self, posX, posY):
        return
        
    # Calculer le temps écoulé
    def defineRemainingTime(self):
        if not(self.end):
            if self.start:
                seconds = (time.get_ticks() - self.startTicks) // 1000  # Convertir en secondes
                self.remainingTime = self.duration - seconds
            else:
                self.startTicks=time.get_ticks()
                self.start=True
            
    def place(self):
        if self.isPlay:
            self.defineRemainingTime()
        else:
            self.duration=self.remainingTime
            self.startTicks=time.get_ticks()
            
        self.minute = self.remainingTime // 60
        self.second = self.remainingTime % 60
        self.text=f"{self.minute:02}:{self.second:02}"
        self.display.blit(self.font.render(self.text, True, self.color), (self.x, self.y))
        if self.remainingTime == 0:
            self.end=True
        

