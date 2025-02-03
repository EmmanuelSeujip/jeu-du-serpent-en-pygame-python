import pygame
pygame.init()

#Constante de dimension 
X_UNIT=64 #taille d'une unité sur l'axe des abcisse
Y_UNIT=64 #taille d'une unité sur l'axe des ordonné
BORDER_WIDTH=4 #Taille de la bordure du rectantangle
BOX_SIZE=24 #cote d'un carreau

#Constante lie au plateau
FPS=pygame.time.Clock()


# Les constante de couleur en code rgb
WHITE=(255, 255, 255)
BGCOLOR=(50,50, 50)
GREEN=(34, 177, 76)
GREEN2=(21,111, 48)
RED=(255, 0, 0)
RED2=(191, 0, 0)
YELLOW=(255, 255, 51)
YELLOW2=(232, 232, 0)
BLUE=(0, 128, 255)
BLUE2=(0, 68, 136)
MARRON=(139, 69, 19)
GRAY=(220, 220, 220)

#les directions
LEFT="left"
RIGHT="right"
UP="up"
DOWN="down"
#definition de police
JOKERMAN50=pygame.font.SysFont("jokerman", 50)
CAMBRIAMATH30=pygame.font.SysFont("cambria math", 30)
CAMBRIAMATH25=pygame.font.SysFont("cambria math", 25)

#toute les posibilité 
ALLBGCOLOR=[BGCOLOR, WHITE,MARRON,GRAY]
ALLSNAKECOLOR=[[GREEN, GREEN2], [RED, RED2], [YELLOW, YELLOW2], [BLUE, BLUE2]]
ALLCOLORTHEME=[WHITE, BGCOLOR]
