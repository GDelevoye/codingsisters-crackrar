# sisters-crackrar

# Quick-start

> Ce README a pour but uniquement de présenter le projet GitHub (l'initiative coding sisters, l'usage du logiciel, la structure du code, l'organisation du dépôt GitHub). 
> Un guide PDF différent est disponible pour les encadrantes ("Guide pour encadrantes") comme pour les participantes ("Guide pour participantes").

# A propos des coding sisters

L'initiative "coding sisters" consiste à accueillir des lycéennes de région parisienne pour les initier au code

L'ensemble des informations relatives à l'initiative codingsisters sont disponibles à la page suivante:

http://codingsisters.fr/


Ce Github consiste à expliquer comment **hacker un mot de passe** en **python**. Il s'agit de l'un des sujets qui sont proposés comme projet au tutorat.

# A propos du projet


Dans ce projet nous verrons plusieurs stratégies pour hacker des mots de passe. 

Nous aborderons un cas concrêt: **Les fichiers .rar cryptés**.

Néanmoins, les concepts sont (en partie) transférables pour d'autres types de cryptages !

Nous allons utiliser un programme fait maison, et y rajouter au fur et à mesure des fonctionnalités pour en faire un vrai logiciel permettant de cracker les mots de passe.

>
> Est-ce qu'on peut vraiment commencer à hacker à partir de si peu ?

Réponse:

>
> **Oui !** En dernière partie, nous vous donnerons quelques notions de cryptographie pour que vous compreniez les limites de ce que vous apprendrez ici. Néanmoins, il s'agit d'un vrai exemple de hacking.


# Prérequis


- Qu'est-ce qu'un **programme** ? Qu'est-ce que la **ligne de commande** ? 

- **Utiliser l'interpréteur python** et sauvegarder un **script**

- Assigner et lire des variables: **Dictionnaires** , **listes**

- Faire des **tests logiques** *(if, else...)* sur les variables

- **Récupérer l'entrée au clavier** de l'utilisateur

- Faire des boucles **while** et **For**

- Savoir faire/utiliser une **fonction**



Et... C'est tout !



***Les "briques" que nous allons créer sont pensées pour pouvoir être réalisées indépendamment les unes des autres selon votre niveau***



# Nous apprendrons au fur et à mesure à:


- **Lire un fichier** ligne par ligne en python

- **installer** et utiliser un **package** pour utiliser ses **fonctions**

- **Faire du brute force en ligne de commande**: brutegen et crackrar

- **Ouvrir un fichier RAR** en python et **tester** le mot de passe

- Utiliser les **générateurs**

- Utiliser le module **strings** pour générer des chaînes de caractères

- Utiliser le module **itertools** pour tester des millions de combinaisons

- Trouver des **heursitiques d'attaque** et les **implémenter**

- **Estimer** le temps que son code va prendre avec le module **time**

- Se familiariser avec des **principes de base de cryptographie**


# Contenu de ce répertoire GitHub


Ce projet contient plusieurs parties pour guider le travail des participantes et servir de support aux encadrantes:


## Une première partie de **guide pour les participantes**, avec plusieurs niveaux de difficulté


Cette partie est située dans le dossier **"Guide pour participantes"**. 


Ce dossier contient des **PDF** pour donner des pistes de résolution pour chacun des sous-problèmes, ou présenter des possibilités d'ajouts utiles pour le projet final ("cracker un mot de passe").

>
> Il ne s'agit que d'un fil rouge, une aide. Toutes les participantes sont vivement encouragées à **suivre leur propre voix !**. Il n'y **aucun ordre à a respecter**: Il y en a pour tous les niveaux !


### Aperçu de la difficulté des différentes briques :


Les étapes sont classées par difficulté de niveau 1 à 4. Il est possible de commencer à n'importe laquelle.

#### [ INTRODUCTION - Avant-propos ] (facultatif - TOUT PUBLIC)


- **La place des femmes** dans le milieu du hacking **- TOUT PUBLIC**


#### [ Niveau 1 - Ligne de commande, boucles, lecture de fichier ]

- Installer un programme/un package avec **pip install** **- NIVEAU 1**

- Utiliser **crackrar** pour cracker un mot de passe en ligne de commande **- NIVEAU1**

- **Tester un mot de passe** .rar en python **- NIVEAU 1**

- Tester tous les **nombres** possibles **- NIVEAU 1**

- Tester tous les mots de passe stockés dans un fichier (attaque par dictionnaire) **- NIVEAU 1**


#### [ Niveau 2 - Créer des itérateurs particuliers ]

- Comprendre, utiliser et créer des **itérateurs** : **- NIVEAU 2**

- Tester toutes les combinaisons de lettres possibles avec **string** et **itertools* : **- NIVEAU 2**

- Tester tous les **codes PIN à 4 chiffres** possibles **- NIVEAU 2**

- **Chronométrer son code** pour estimer le temps d'une attaque **- NIVEAU 2**

- Tester toutes les **dates de naissance** possibles **- NIVEAU 2**

- Tester tous les **digicodes possibles** **- NIVEAU 2**

- Muter les majuscules/minuscules d'une séquence **- NIVEAU 2**

#### [ Niveau 3 - Programmation orientée objet ]

- Utiliser les **objets** du package crackrar pour créer des **mutations()**, **- NIVEAU 3***

- **Combiner** les séquences avec l'objet **strategy()**, **- Niveau 3**

#### [ Niveau 4 - Challenges pour cheffe 4 étoiles ]

- ***Le challenge du kikoO***: cracker un MoTd£p@sS€ **- Niveau 4** ++

- ***Une histoire de tuyaux***: Lire directement des propositions sur l'entrée standard pour les transformer **- Niveau 4**++

- ***Une vraie développeuse:*** Modifier crackrar pour attaquer des fichiers .zip **- Niveau 4** ++

- ***Multiplier, permuter, combiner:*** Modifier crackrar de façon **ergonomique** (en utilisant **argparse** et en modifiant le lanceur **crackrar.py**) pour utiliser un mixte de brute-force et d'attaques dictionnaire (exemple: 2 chiffres, 1 caractère spécial, 1 mot en minuscule d'un dictionnaire où on ajouterait une majuscule au début) **- Niveau super-boss**

> 
> Faire une solution propre est beaucoup plus dur qu'il n'y paraît !

#### [ FIN - Remarques et conclusion ] (facultatif - TOUT PUBLIC) ### A FAIRE

- Sécurité des mots de passe, entre fantasmes et réalités

- Disgression finale: Par où continuer si l'on veut devenir hackeuse ?



## Une deuxième partie **pour les encadrantes**


Cette partie contient là aussi des jupyter notebook et des PDF. Elle est accessible dans le dossier **"Guide pour encadrantes"**.


>
> Ce README fait également partie du support pour les encadrantes !


Ce dossier contient essentiellement **un fichier PDF** qui vient en complément de ce README et qui détaille des subtilités ou problèmes techniques qui peuvent être rencontrés au cours du projet, des propositions de concepts à présenter ou de librairies à utiliser, ainsi que **des exemples de code**. 

>
> Pour des raisons pédagogiques évidentes il ne faut **surtout pas donner les corrections** aux participantes ! Personne n'apprend à coder en recopiant !


## Une troisième partie de **package python** fait maison : crackrar,


Ce répertoire GitHub est en lui-même un **package python fait maison** installable avec **pip** (voir *"Installation"*). est accessible dans le dossier **"crackrar"**.

Il contient deux programmes utilisables en ligne de commande : ***crackrar**** et ***brutegen***. Le permier permet de cracker des fichiers .rar. Le deuxième permet de générer des tas de combinaisons.

- **brutegen** permet d'afficher des mots de passe en brute force

- **crackrar** permet de cracker des fichiers .rar, avec une interface similaire à brutegen


>
> Il s'agit de deux programmes assez rudimentaires. Le but va être de s'en inspirer pour faire des programmes plus "intelligents".


### Autre: Des exemples de dictionnaires

Dans ***~/crackrar/crackrar/data/*** on trouvera plusieurs dictionnaires au format texte (une ligne par mot):

- 10 millions de mots de passe aléatoires

- 1000 mots parmi les plus fréquents en français

- Une liste de 10.000 mots de passe parmi les plus utilisés au monde

- Un dictionnaire de 330.000 mots français

- Les 75 mots de passe les plus fréquets de tous les temps (pas nécessairement dans l'ordre)

- Une liste de prénoms français (en majuscules)

- Un .csv qui reprend ces prénoms mais permet aussi de les classer par abondance


Cela permet de réaliser des attaques par dictionnaire

On trouve aussi: Les mono, bi, tri et quadgrams de la langue française avec leur abondance

Cela permet de générer des mots qui pourront "sonner français" sans pour autant être des mots de français

# Installation du package crackrar


```bash
git clone https://github.com/GDelevoye/codingsisters-crackrar.git
mv ./codingsisters-crackrar crackrar
pip install ./crackrar
```

Et voila !

>
>*Si on veut pouvoir modifier le package pour y ajouter nos propres fonctions on peut l'installer en mode "editable package". Il faut alors utiliser l'argument "-e" dans la dernière ligne (pip install [...]) de la façon suivante:*
>
>

```bash
pip install -e ./crackrar
```

De cette façon, on peut modifier le package tout en continuant à l'utiliser

>
> En cas d'erreur dans la modification, les participantes pourront revenir en arrière car le fichier est gité

```bash
user@computer:$cd crackrar
user@computer:$git checkout master .
```


# Utilisation du package


## Command-line interface (CLI)


Les deux programmes ont une interface d'utilisation similaire, à ceci près que **crackrar** prend en argument un fichier **.rar** et la possibilité d'ajuster la verbosité 

### brutegen

```console
user@computer:$ brutegen -h
usage: brutegen [-h] [--combination_length COMBINATION_LENGTH]
                [--charsets {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...]]
                [--dictionnary DICTIONNARY]

optional arguments:
  -h, --help            show this help message and exit
  --combination_length COMBINATION_LENGTH, -l COMBINATION_LENGTH
                        Length of brute-force. Default: 1
  --charsets {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...], -c {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...]
                        Choose among: lowercase, uppercase, digits,
                        special_characters. DEFAULT: all of these.
  --dictionnary DICTIONNARY, -d DICTIONNARY
                        Paths of a file that contains words to use (one word
                        per line). This would override the --charset argument.
                        DEFAULT: [empty]

```

### crackrar


```console
user@computer:$ crackrar -h
usage: crackrar [-h] [--combination_length COMBINATION_LENGTH]
                [--charsets {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...]]
                [--dictionnary DICTIONNARY]
                [--verbosity {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}]
                rarFile

positional arguments:
  rarFile               Path to the .rar file

optional arguments:
  -h, --help            show this help message and exit
  --combination_length COMBINATION_LENGTH, -l COMBINATION_LENGTH
                        Length of brute-force. Default: 1
  --charsets {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...], -c {lowercase,uppercase,digits,special_characters} [{lowercase,uppercase,digits,special_characters} ...]
                        Choose among: lowercase, uppercase, digits,
                        special_characters. DEFAULT: all of these.
  --dictionnary DICTIONNARY, -d DICTIONNARY
                        Paths of a file that contains words to use (one word
                        per line). This would override the --charset argument.
                        DEFAULT: [empty]
  --verbosity {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}, -v {DEBUG,INFO,WARNING,ERROR, CRITICAL,SHOW_PSW}
                        Verbosity among: DEBUG, INFO, WARNING, ERROR,
                        CRITICAL, STDOUT_PSW". If set to STDOUT_PASW,
                        passwords tried are printed on stdout [highly
                        deprectaded : Performances issues). DEFAULT: INFO
```

## Exemple d'usage

### Crackrar

Cracker un mot de passe en brute force avec une longueur de 4, uniquement des chiffres (digits)

On utilisera donc -l 4 -c digits:


```console
user@computer:~/Github/crackrar/crackrar/test_package/testdata$ crackrar notes.rar -l 4 -c digits
2020-01-05 14:49:44,507 [INFO] Attack started at 05/01/2020 14:49:44
2020-01-05 14:50:21,313 [INFO] found password 1789 for file /export/home1/users/gmc/delevoye/Github/crackrar/crackrar/test_package/testdata/notes.rar
2020-01-05 14:50:21,313 [INFO] Attack ended at 05/01/2020 14:50:21
2020-01-05 14:50:21,313 [INFO] Duration : 36.81 s
2020-01-05 14:50:21,313 [INFO] *** /!\ FOUND PASSWORD /!\ *** : 1789
```

Afficher sur la sortie standard les combinaisons essayées au fur et à mesure:

```console
user@computer:$ crackrar notes.rar -v SHOW_PSW -l 3
aaa
aab
aac
aad
aae
aaf
aag
aah
...
```

>
> L'option -d permet d'utiliser un dictionnaire d'attaque (= un fichier avec un mot par ligne). Les arguments -c et -l sont alors ignorés

### brutegen

Le principe est très similaire


```console
user@computer:~/crackrar/crackrar/test_package/testdata$ brutegen -l 3
aaa
aab
aac
aad
aae
aaf
aag
aah
```

## Remarque sur la performance


Le cassage de mots de passe est **lent**. Ce n'est pas dû au fait que nous utilisons du python, mais au fait que **l'ouverture d'un fichier .rar et la vérification de la clé sont lents**. 

>
> Il est possible de s'en apporter la preuve avec le programme **tqdm** :


```console
user@computer:~/crackrar/crackrar/test_package/testdata$ brutegen -l 4  | python -m tqdm | wc -l
112550881it [01:42, 1095235.63it/s]
112550881
```

C'est-à-dire que le CPU peut générer un peu plus de **1 million de combinaisons par secondes avec brutegen** (en python !)

Cependant si on regarde le temps que met **crackrar** pour attaquer un fichier, on s'aperçoit que sur une machine moyenne on est **plutôt entre ~30 à 50 essais par seconde**:

```console
user@computer:~/crackrar/crackrar/test_package/testdata$ crackrar notes.rar -l 4 -c digits -v SHOW_PSW | python -m tqdm | wc -l
1790it [00:59, 29.96it/s]
```

A quoi cela est-t-il dû ?


>
>Le temps de calcul en python est **négligeable** par rapport au temps d'ouverture du fichier .rar / la vérification de la clé. 

Lorsque l'on travaille avec **brutegen**, la taille des mots de passe à générer impacte les performances. Si on passe la taille du mot de passe de **n=4** à **n=12**, on **diminue de 50%** les performances. Par contre si on travaille avec **crackrar**, cette perte reste totalement négligeable !


La relative lenteur de python par rapport à d'autres langages réputés plus rapides (comme le langage C par exemple) n'est donc absolument pas handicapante ici: Le problème c'est l'ouverture du fichier .RAR !

>
> On ne peut donc pas tester rapidement les combinaisons sur un fichier .RAR. Les mots de passe sont donc plus durs à trouver: IL faut idéalement utiliser d'autres stratégies que le brute-force (exemple: attaque par dictionnaire)



## Usage en python du package crackrar


A partir du niveau 3, on propose aux participantes d'utiliser des concepts de POO en reprenant les objets du package. Le but ici est de vous donner un aperçu du fonctionnement de ces objets pour que les participantes puissent les utiliser voir les modifier.


### Vue d'ensemble


Le package est fait de telle sorte qu'on peut soit faire du brute force total (option 1), soit faire des attaques par dictionnaire (option 2), soit combiner différents types d'approches. Pour pouvoir faire du **brute force** ou **enrichir** les **attaques par dictionnaires**, nous utiliserons trois concepts: 

- Le **dictionnaire d'attaque**

- La **mutation**

- La **stratégie d'attaque**


### L'objet "dictionnaire d'attaque" (attackDict)


L'objet attackDict se crée à partir d'un générateur

Exemple: La fonction suivante est un générateur des lettres de A à Z

```python
def my_generator_letters():
    for i in "abcdefghijklmnopqrstuvwxyz":
        yield i
```

On peut alors créer un objet "attackDict" à partir de ce générateur

```python
import crackrar as cr

mydict = cr.attackDict(my_generator_letters)
```

Ce dictionnaire permettra donc de faire des attaques avec des lettres en minuscules de A à Z


### L'objet "mutation"

Si maintenant on voudrait faire des lettres majuscules, on peut soit faire un nouveau générateur comme suit:

```python
def my_generator_letters():
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        yield i
```

Mais on pourrait aussi utiliser l'objet **mutation** !

En effet, on pourrait imaginer une fonction génératrice qui prend une lettre en entrée, et qui renvoie la majuscule correspondante. Par exemple:

```python
def from_small_to_large_letter(letter):
    yield letter.lower()
    yield letter.upper()
```

Puis utiliser cette fonction génératrice pour faire un objet "mutation"

```
mutation_small_to_large = cr.mutation(from_small_to_large_letter)
```

Il sera ainsi facile de combiner les mutations pour transformer nos chaînes d'entrée

Par exemple, si on attaque avec un dictionnaire qui contient le mot "test", on pourra facilement tester les mots de la façon suivante:

- test

- Test

- TeSt

- tEsT

- TEST

Ceci est d'ailleurs l'objet d'une brique à construire.


[ Quel est l'intérêt ? ]

>
> **Intérêt**: *L'intérêt de créer ces modifications est que si le propriétaire du mot de passe a légèrement modifé un mot du dictionnaire mais en utilisant des tactiques courantes (exemple: Faire démarrer par une majuscule, utiliser alternativement des majuscules ou minuscules...) alors on pourra quand même trouver son mot de passe, sans ajouter beaucoup de temps de calcul, et de manière très modulaire.*


### L'objet "Stratégie" (strategy)


L'objet stratégie va nous permettre de choisir comment nous allons planifier et exécuter l'attaque

```python
# On possède nos fonctions qui permettent de générer des lettres de l'alphabet minuscule

def my_generator_letters(): # L'objet attackDict sera crée à partir de ce générateur
    for i in "abcdefghijklmnopqrstuvwxyz":
        yield i
        
# ... Et de les transformer en majuscules

def from_small_to_large_letter(letter):
    yield letter.lower()
    yield letter.upper()
```

```python    
# On importe alors le package
import crackrar as cr

# On va crée un dictionnaire d'attaque ("attackDict"): il générera les lettres de l'alphabet
# On crée l'objet attackDict à partir de l'itérateur de la façon suivante:
my_attack_dict = cr.attackDict(my_generator_letters)

# On va rajouter à notre itérateur la possibilité de faire les majuscules
my_attack_dict.add_mutation(from_small_to_large_letter) 
# Désormais, notre dictionnaire d'attaque générera des majuscules ET des minuscules !

# Et à partir de ce dictionnaire d'attaque "muté" on crée une stratégie 
# Avec cet objet "strategy" on va pouvoir tester toutes les possibilités de combinaisons
# Dans cet exemple, on testera les possibilités de taille 5 (5 lettres majuscules ou minuscules)

my_strategy = cr.Strategy()
my_strategy.add_attack_dict(my_attack_dict,fold=5) 
# "fold" précise le nombre de fois qu'on ajoute l'attackDict
# "5" signifie donc ici qu'on utilisera 5 fois cet attackDict

# Puis ensuite on attaque un fichier RAR: Le brute force commence !
my_strategy.launch_attack(rarfile,SHOW_STDOUT=True)

```

>
> L'option "SHOW_STDOUT" de la méthode "launch_attack" permet d'afficher (ou non) les combinaisons essayées sur la sortie standard (l'écran)


## Combiner les stratégies


Nous avons vu que les objets attackDict (mutés ou non) sont crées à partir d'itérables.


Nous avons vu que les stratégies sont crées à partir des objets attackDict


L'une des pistes d'amélioration du package que les participantes peuvent coder (NIveau 4 - Challenge) pourrait être de rendre les stratégies itérables en implémentant la fonction __iter__

>
> C'est à dire qu'à partir d'une stratégie, on pourra la combiner avec une autre. On pourra créer de nouveaux dictionnaires à partir de dictionnaires (c'est le principe des mutations). On pourra par exemple, faire une recherche de mot de passe de la façon suivante:  ***"un caractère spécial, une 1 mot du dictionnaire en changeant les majuscules/minuscules, 1 date, trois chiffres"*** etc.

>
> De nombreux tutoriels expliquent comment rendre un objet itérable en ligne. Ex:
> [ https://www.programiz.com/python-programming/iterator ]


