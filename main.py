import sys 
import pygame
import os # Importe le module os pour travailler avec les chemins
chemin_principale = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet

#On ajoute tout les chemins des sous dossiier afin d'eviter les erreurs lié à des dossiers non trouvé
sys.path.append(os.path.join(chemin_principale, './MOE Library', '') )
sys.path.append(os.path.join(chemin_principale, './front-end/page', ''))
sys.path.append(os.path.join(chemin_principale, './front-end/object', ''))
sys.path.append(os.path.join(chemin_principale, './front-end/listObject', ''))
sys.path.append(os.path.join(chemin_principale,'./back-end', ''))

from MainMoe import MainMoe
from home import Home
from mode import Mode
from setting import Settings
from score import Score
from board import Board
from endgame import EndGame
from help import Help

class Quit():
    def play(self):
        pygame.quit()
        sys.exit()

class Main(MainMoe):
    def __init__(self):
        MainMoe.__init__(self,  [
            Mode(), 
            Score(), 
            Settings(), 
            Help(), 
            Quit(),
            Home(), 
            Board(), 
            EndGame()
        ])
        self.lauch=5


M=Main()
M.mainPlay()
