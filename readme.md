#Documentation du jeu du serpent

##I-  MOE Library
C'est une collection d'élément permettant de reprendre le Concept de DOM en JavaScript .
Les classes qui composent cette bibliothèque sont : <br>
### 1-	 MOE

MOE qui permet de contenir des objets. Son but principal est de prendre des objets et du placé sur la page et aussi de vérifié les interactions qui se passer sur ces objets. Ces arguments propres sont :

-   `obj`: "qui contient tous les objets ou enfant qu'il doit gérer"
-	`clicked`: l'état de tous les élément après un clic sur la page
-	`survoled`: l'état de tous les élément après un déplacement de la souris

N.B : Lorsqu’on parle d’etat d’un élément c’est généralement un True/False pour savoir si cette élément à recu ou non un clic

### 2-	MoeObject

MOEobject qui sont les objets contenus dans des MOE
ces arguments sont: 

-   `feelSurvol`: Savoir s'il a été survolé c'est à dire True s'il a été survolé
-   `feelClik`: Savoir si on a clicqué sur lui
-   `x`: son abcisse
-   `y` son ordonnée
-   `width`: sa longueur 
-   `height`: sa hauteur

### 3- ListMoeObject

Il permet de gerer plusieurs objets comme s'il es un Moe mais peut aussi etre ajouter a un autre Moe en tant que Moe object

### 4-  MoePage

C’est ce qu’on verra à l’écran.
Il a pour a pour attribut propre :

-   `isFullWindow` : qui permet de savoir si la page peut avoir des dimensions dynamique ou fixe 
-   `text` : qui récupère l’ensemble des texte à afficher à l’écran
-   `setting` : pour récupérer les paramètres
-   `mode` : pour récupérer le mode de jeu
-   `listLang` : pour savoir la liste des langues disponible
-   `forLauch` : permet d’avoir l’identifiant de la prochaine page à ouvrir 

### 5-  MainMoe
Il sert de cadenceur pour afficher les pages suivant leur identifiant. Noté que l'identifiant ici représente la position de la page dans self.obj 

## II- front-end

Le front-end fonctionne principalement avec un modèle que j’ai appelé POLO (Page Objet Liste d’Objet). En gros le fonctionnement est assez simple donc on a : 

### 1-Les pages

Elles permettent d’afficher les éléments à l’écran et aussi de récupérer les éléments dans la base de données. Certes les pages sont toutes différentes les unes des autres mais leur fonctionnement reste les même c’est pour cela qu’on ne va pas expliciter le fonctionnement de chaque page. Mais si le lecteur est perplexe il peut prendre la peine de lire le code source de chaque page

### 2-Les objets
Ils sont des éléments interactifs afficher à l'écran leur imporatance est primordial car c'est sur eux que tout les orincipaux clique sont fait et aussi ils sont les seul élément visuel véritablement afficher

### 3- Liste d'objets
Ce sont eux qui sont responsable de la sauvegarde des préférences de l'utilisateur. Ils permettent de stocké des objets de même type afin de permettre une création dynamique
## Base de données

La base de données est principalement géré par le fichier database.py.<br>
Il contient tout un lot de fonction mais ça sera trop long à tout écrire.Mais les fonction à remarqué sont:

### 1-jsonLoder et pickleLoader

Elles permettent respectivement de récupérer les données dans un fichier json et un fichier txt donc les informations ont été crypté.

### 2-jsonDumper et pickleDumper

Elles permettent respectivement de placé des données dans un fichier json ou txt 

