'''
    fichier permettan de récupérrer l'ensemble des données à utiliser

'''

import pickle
import json
import os # Importe le module os pour travailler avec les chemins

chemin_racine = os.path.dirname(os.path.abspath(__file__)) # Chemin de la racine du projet
def pickleDumper(data, road):
  with open(road,'wb') as file:
    pickle.dump(data, file)

def pickleLoader(altData,road):
  try :
    with open(road, 'rb') as file:
      data=pickle.load(file)
  except:
    # Récupérer le type d'erreur
    data=altData
    pickleDumper(data,road)
  return data
 
def jsonDumper(data, road):
  with open(road,'w', encoding='utf-8') as file:
    json.dump(data, file)

    
def jsonLoader(altData,road):
  try :
    with open(road, 'r', encoding='utf-8') as file:
      data=json.load(file)
  except :
    data=altData
    jsonDumper(data,road)
  return data
 
def dumpScore(score):
  pickleDumper(score, os.path.join(chemin_racine,'score', 'score.txt')) # Utilise os.path.join

def loadScore():
    chemin = os.path.join(chemin_racine, 'score', 'score.txt') # Utilise chemin_racine
    return pickleLoader([0, 0, 0], chemin)

def dumpGameScore(score):
  pickleDumper(score, os.path.join(chemin_racine,'score', 'gamescore.txt')) # Utilise os.path.join

def loadGameScore():
    chemin = os.path.join(chemin_racine, 'score', 'gamescore.txt') # Utilise chemin_racine
    return pickleLoader([0, 0, 0,0 ], chemin)
def dumpSetting(setting):
    pickleDumper(setting, os.path.join(chemin_racine,'setting', 'setting.txt')) # Utilise os.path.join

def loadSetting():
    chemin = os.path.join(chemin_racine, 'setting', 'setting.txt') # Utilise chemin_racine
    return pickleLoader([0, 0, 0, 0,0 ], chemin)
    
def dumpMode(mode):
    pickleDumper(mode, os.path.join(chemin_racine,'setting', 'mode.txt')) # Utilise os.path.join

def loadMode():
    chemin = os.path.join(chemin_racine, 'setting', 'mode.txt') # Utilise chemin_racine
    return pickleLoader([1, 0, 0, 0, 1], chemin) 
def dumpListLanguage(liste):
  jsonDumper(liste,'lang/list.json')

def loadListLanguage():
    chemin = os.path.join(chemin_racine, 'lang', 'list.json') # Utilise chemin_racine
    return jsonLoader(["Fr","En"],chemin)

def loadLanguage():
  lang=loadSetting()[3]
  lang=loadListLanguage()[lang]
  chemin = os.path.join(chemin_racine, 'lang', str(lang)+"/"+str(lang)+".json") # Utilise chemin_racine
  return jsonLoader({
    "HOME": [
        "BIENVENUE",
        "Jouer", 
        "Meilleur score",
        "Parametres", 
        "Aide", 
        "Quitter"
    ],
    "BOARD":[
        "Joueur",
        "Difficulte",
        "score"
    ],
    "MODE":[
        "MODE",
        "Joueur",
        "Difficulte",
        "Type",
        "Resolution"
    ],
    "SETTINGS":[
        "PARAMETRE",
        "Plateau",
        "Serpent",
        "Ligne",
        "Langue",
        "clavier"
    ],
    "BEST":[
        "MEILLEUR SCORE",
        "Facile",
        "Moyen",
        "Difficile"
    ],
    "END":[
        "Fin de la partie",
        "Vous êtes le nouveau meilleur score",
        "REJOUER"
    ],
    "GENERAL":[
        "OK",
        "RETOUR"
    ],
    "TYPE":[
        "simple",
        "chronométré"
    ]
    
}
,chemin)

def loadHelpText():
  lang=loadSetting()[3]
  lang=loadListLanguage()[lang]
  chemin = os.path.join(chemin_racine, 'lang', str(lang)+"/help.json") # Utilise chemin_racine
  return jsonLoader({
    "PAGE1":"Le jeu du serpent est un jeu très simple à comprendre. Le but du jeu est de faire en sorte que le serpent mange le plus de fois possible la proie sans sortir du cadre. Plus le serpent mange la proie plus il grandira. Mais contrairement au jeu classique du serpent nous vous proposerons dans cette version un autre mode pour pimenter le jeu",
    "PAGE2":[
        "Il existe 2 principale mode jeu :",
        "    Le jeu simple:",
        "C’est la version classique du jeu serpent que les ancêtres nous ont légué. Donc la seule contrainte ici sera de ne pas sortir du jeu ",
        "    Le jeu chronométré:",
        "Ici vous pouvez pimenter le jeu en ajoutant un minuteur. De ce fait dès que le minuteur sera terminer le jeu s’arrêtera automatiquement",
        "Notez que ces deux modes marchent peu importe le nombre de joueur."
    ],
    "PAGE4":[
        "Touche"
    ],
    "HEAD":"AIDE"

},chemin) 
