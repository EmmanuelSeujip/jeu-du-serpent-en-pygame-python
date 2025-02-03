"""
     MOEobject qui sont les objets contenus dans des MOE
    C’est ce qu’on verra à l’écran.
    Il a pour a pour attribut propre :
        isFullWindow : qui permet de savoir si la page peut avoir des dimensions dynamique ou fixe 
        text : qui récupère l’ensemble des texte à afficher à l’écran
        setting : pour récupérer les paramètres
        mode : pour récupérer le mode de jeu
        listLang : pour savoir la liste des langues disponible
        forLauch : permet d’avoir l’identifiant de la prochaine page à ouvrir 

"""
from Moe import MOE
import pygame
import sys
import os # Importe le module os pour travailler avec les chemins
chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
chemin = os.path.join(chemin_racine, '../back-end/', '') # Utilise chemin_racine
sys.path.append(chemin)
from database import loadLanguage , loadSetting, loadListLanguage, loadScore, loadMode

class MoePage(MOE):
  def __init__(self, isFullWindow,objet):
    MOE.__init__(self, obj=objet)
    pygame.init()
    pygame.display.set_caption('JEU DU SERPENT')
    self.mode=loadMode()
    if isFullWindow and self.mode[3]==1:
        #On récupère la taille de l'écran
        INFO_DISPLAY=pygame.display.Info()
        self.width=INFO_DISPLAY.current_w #largeur de l'ecran
        self.height=INFO_DISPLAY.current_h -50 #hauteur de l'ecran
    else:
        self.width=640
        self.height=640
    self.display= pygame.display.set_mode((self.width, self.height))
    # Récupère les élément important de la base de donné
    self.text=loadLanguage()
    self.setting=loadSetting()
    self.bestScore=loadScore()
    self.mode=loadMode()
    self.listLang=loadListLanguage()
    self.forLauch=0
    

