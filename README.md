# sisters-rarcrack

## A propos des coding sisters

L'initiative "coding sisters" consiste à accueillir des lycéennes parisiennes pour les initier au code

L'ensemble des informations relatives à l'initiative codingsisters sont disponibles à la page suivante:

http://codingsisters.fr/


Ce Github consiste à expliquer comment cracker un fichier RAR en python. Il s'agit de l'un des sujets qui sont proposés comme projet au tutorat.

## Liste des compétences/connaissances maîtrisées au fur et à mesure de l'avancée du projet

- (facultatif) Quels modèles féminins pour une hackeuse ?


- Qu’y a-t-il dans un **ordinateur** ?


- Qu'est-ce qu'un **programme** ?


- Utiliser la **ligne de commande**


- Utiliser **l'interpréteur python** et afficher des messages


- Assigner des **variables**


- Faire des **tests logiques** sur les variables


- Récupérer **l'entrée au clavier** de l'utilisateur


- (facultatif) Utiliser l'interpréteur dans un **notebook**


- (facultatif) **Enregistrer** son code et **exécuter** le code de quelqu'un d'autre


- Faire des boucles **while**


- Les listes et les boucles **For**


- Les boucles **imbriquées**


- **Lire un fichier** ligne par ligne en python


- **installer** et utiliser un **package** pour utiliser ses fonctions


- **Ouvrir un fichier RAR** en python avec un package


- Derrière chaque boucle for: **les générateurs**


- Le module **strings**


- Le module **itertools**


- L'affichage à l'écrcan de la progression d'une boucle avec **tqdm**


- Estimer le temps que son code va prendre avec le module **time**

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

pip install ./sisters-rarcrack
```

L'import se fait de la façon suivante:

```python
import sistersrarcrack as sr
```

Le package contient essentiellement une fonction

```python
sr.essayer_mdp(chemin_vers_fichier_rar, mot_de_passe, nom_sous_fichier=None)
```

Les autres fonctions sont des corrections pour réaliser le brute force de chiffres, le brute force de lettres, le brute force combiné, l'attaque par dictionnaire ou l'attaque par combinaison de mots



## Credits 

DELEVOYE Guillaume
ROSE France
