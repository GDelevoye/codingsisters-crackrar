# sisters-rarcrack

## A propos des coding sisters

L'initiative "coding sisters" consiste à accueillir des lycéennes parisiennes pour les initier au code

L'ensemble des informations relatives à l'initiative codingsisters sont disponibles à la page suivante:

http://codingsisters.fr/


Ce Github consiste à expliquer comment cracker un fichier RAR en python. Il s'agit de l'un des sujets qui sont proposés comme projet au tutorat.


## Compétences/connaissances maîisées au fur et à mesure de l'avancée du projet

- Qu'est-ce qu'un **programme** ?

- **Utiliser l'interpréteur** python

- **Utiliser l'interpréteur dans un notebook**

- **Assigner** des variables

- Faire des **tests logiques** sur les variables

- **Récupérer l'entrée au clavier** de l'utilisateur

- Faire des boucles **while**

- Les **listes** et les boucles **For**

- Les **boucles imbriquées**

- **Lire un fichier** ligne par ligne en python

- **installer** et utiliser un **package** pour utiliser ses **fonctions**

- **Ouvrir un fichier RAR** en python avec un package

- Derrière chaque boucle for: les **générateurs**

- Le module **strings**

- Le module **itertools**

- L'affichage à l'écrcan de la **progression d'une boucle avec tqdm**

- **Estimer** le temps que son code va prendre avec le module **time**


## Contenu

Ce projet contient plusieurs parties pour guider le travail des participantes et servir de support aux encadrantes:

### Une première partie de **guide pour les participantes**, avec plusieurs niveaux de difficulté

Cette partie est située dans le dossier **"Guide pour participantes"**. 

Ce dossier contient des **Jupyter notebook** et des **PDF** correspondant à chaque chapitre. 

Les documents y sont **numérotés dans l'ordre à suivre** (et qui reprend chronologiquement les compétences/connaissances cibles évoquées plus haut).


### Une deuxième partie **de correction pour les encadrantes**, avec les corrections détaillées du projet

Cette partie contient là aussi des jupyter notebook et des PDF. Elle est accessible dans le dossier **"Guide pour encadrantes"**.

Ce dossier contient essentiellement des subtilités ou problèmes techniques qui peuvent être rencontrés au cours des TP


### Une troisième partie de **package python** 

Le package "sisters-rarcrack" contient:

- **Une fonction qui permet d'ouvrir un .RAR** facilement en python

- Une fonction qui permette de **tester un mot de passe** facilement sur un fichier RAR ouvert


Ce package est accessible dans le dossier "sisters-rarcrack" sous la forme d'un package python importable et installable par pip (voir "Installation")


## Installation du package sisters-rarcrak


```bash
https://github.com/GDelevoye/sisters-rarcrack.git

pip install sisters-rarcrack
```

## Utilisation du package

### Command-line interface (CLI)

```console
delevoye@gmcpc04://$ rarcrack -h

usage: rarcrack [-h] [--combination_length COMBINATION_LENGTH]

                [--charsets {lowercase,uppercase,digits,special_characters}
                
                [{lowercase,uppercase,digits,special_characters} ...]]
                
                [--verbosity {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}]
                
                rarFile
                


positional arguments:

  rarFile               Path to the .rar file
  


optional arguments:

  -h, --help            show this help message and exit
  
  --combination_length COMBINATION_LENGTH, -l COMBINATION_LENGTH
  
                        How many times must the attackDicts be combined
                        
                        (DEFAULT: 4)
                        
  --charsets {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...], -c {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...]
  
                        List of all types of characters among: lowercase,
                        
                        uppercase, digits, special_characters. DEFAULT:
                        
                        contains them all
                        
  --verbosity {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}, -v {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}
  
                        Verbosity among: DEBUG, INFO, WARNING, ERROR,
                        
                        CRITICAL, STDOUT_PSW". If set to STDOUT_PASW,
                        
                        passwords tried are printed on stdout [highly
                        
                        deprectaded : Performances issues). DEFAULT: INFO
                        
```

L'utilisation des fonctions du package est détaillé dans le jupyter notebook pour les participantes intitulées "Installer et utiliser un package"

