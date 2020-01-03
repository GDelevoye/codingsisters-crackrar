# sisters-crackrar

## A propos des coding sisters

L'initiative "coding sisters" consiste à accueillir des lycéennes parisiennes pour les initier au code

L'ensemble des informations relatives à l'initiative codingsisters sont disponibles à la page suivante:

http://codingsisters.fr/


Ce Github consiste à expliquer comment **hacker un mot de passe** en **python**. Notamment, le mot de passe d'un **fichier .rar**. Il s'agit de l'un des sujets qui sont proposés comme projet au tutorat.

## A propos du projet


Dans ce projet nous verrons plusieurs stratégies pour hacker des mots de passe. 

Nous aborderons un cas concrêt: **Les fichiers .rar cryptés**.

Néanmoins, les concepts sont (en partie) transférables pour d'autres types de cryptages !

Nous allons utiliser un programme fait maison, et y rajouter au fur et à mesure des fonctionnalités pour en faire un vrai logiciel permettant de cracker les mots de passe.

```console
Est-ce qu'on peut vraiment commencer à hacker à partir de si peu ?
```

Réponse: **Oui !** En dernière partie, nous vous donnerons quelques notions de cryptographie pour que vous compreniez les limites de ce que vous apprendrez ici. Néanmoins, il s'agit d'un vrai exemple de hacking.


## Prérequis


- Qu'est-ce qu'un **programme** ? Qu'est-ce que la **ligne de commande** ?

- **Utiliser l'interpréteur python** et sauvegarder un **script**

- Assigner et lire des variables: **Dictionnaires** , **listes**

- Faire des **tests logiques** *(if, else...)* sur les variables

- **Récupérer l'entrée au clavier** de l'utilisateur

- Faire des boucles **while** et **For**

- Savoir faire/utiliser une **fonction**



Et... C'est tout !



***Les "briques" que nous allons créer sont pensées pour pouvoir être réalisées indépendamment les unes des autres selon votre niveau***



## Nous apprendrons au fur et à mesure à:


- **Lire un fichier** ligne par ligne en python

- **installer** et utiliser un **package** pour utiliser ses **fonctions**

- **Ouvrir un fichier RAR** en python et **tester** le mot de passe

- Utiliser les **générateurs**

- Utiliser le module **strings** pour générer des chaînes de caractères

- Utiliser le module **itertools** pour tester des millions de combinaisons

- Trouver des **heursitiques d'attaque** et les **implémenter**

- **Estimer** le temps que son code va prendre avec le module **time**

- Se familiariser avec des **principes de base de cryptographie**


## Contenu de ce répertoire GitHub


Ce projet contient plusieurs parties pour guider le travail des participantes et servir de support aux encadrantes:


### Une première partie de **guide pour les participantes**, avec plusieurs niveaux de difficulté


Cette partie est située dans le dossier **"Guide pour participantes"**. 


Ce dossier contient des **Jupyter notebook** et des **PDF** correspondant à chaque chapitre. 

Les documents y sont **numérotés dans l'ordre *indicatif* à suivre / ordre de difficulté**

Nous donnons **quelques clés** aux participantes pour réaliser petit à petit des briques de notre futur programme

Il ne s'agit que d'un fil rouge, une aide. Toutes les participantes sont vivement encouragées à **suivre leur propre voix !**. Il n'y **aucun ordre à a respecter**: Il y en a pour tous les niveaux !


#### Aperçu de la difficulté des différentes briques :


Les étapes sont classées par difficulté de niveau 1 à 4. Il est possible de commencer à n'importe laquelle.

- Utiliser **crackrar** pour cracker un mot de passe en ligne de commande **NIVEAU1**

- Tester un mot de passe .rar en python **NIVEAU 1**

- Tester tous les nombres possibles **NIVEAU 1**

- Tester tous les mots de passe stockés dans un fichier **NIVEAU 1**

- Faire une attaque par dictionnaire **NIVEAU 1**

- Comprendre, utiliser et créer des **itérateurs** : **NIVEAU 2**

- Tester toutes les combinaisons de lettres possibles avec **string** et **itertools* : **NIVEAU 2**

- Tester tous les codes PIN à 4 chiffres possibles **NIVEAU 2**

- Tester toutes les dates de naissance possibles **NIVEAU 2**

- Tester tous les digicodes possibles **NIVEAU 2**

- Muter les majuscules/minuscules d'une séquence **NIVEAU 2**

- Utiliser les **objets** du package crackrar pour créer des **mutations()** **NIVEAU 3***

- Combiner les attaques avec l'objet **strategy()** **Niveau 3**

- Le challenge du kikoO: cracker un MoTd£p@sS€ **Niveau 4**

- Modifier crackrar pour attaquer des fichiers .zip **Niveau 4**

- REMARQUE : Sécurité des mots de passe, entre fantasmes et réalités **Niveau 0**

- Disgression finale: Par où continuer si l'on veut devenir hackeuse ?



### Une deuxième partie **pour les encadrantes**


Cette partie contient là aussi des jupyter notebook et des PDF. Elle est accessible dans le dossier **"Guide pour encadrantes"**.


Ce dossier contient essentiellement des subtilités ou problèmes techniques qui peuvent être rencontrés au cours du projet, ainsi que **des exemples de code**. Pour des raisons évidentes il ne faut **surtout pas donner les corrections** aux participantes ! On n'apprend pas à coder en recopiant !


### Une troisième partie de **package python** fait maison : crackrar


Ce répertoire GitHub est en lui-même un **package python fait maison** installable avec **pip** (voir *"Installation"*). est accessible dans le dossier **"crackrar"**.


## Installation du package crackrar


```bash
https://github.com/GDelevoye/crackrar.git

pip install ./crackrar
```

## Utilisation du package


### Command-line interface (CLI)

```console
user@computer:$ crackrar -h
usage: crackrar [-h] [--combination_length COMBINATION_LENGTH]
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

### Exemple d'usage

Cracker un mot de passe composé de [par défaut] 4 chiffres

```console
user@computer:$ rarcrack notes.rar --charset digits
2020-01-03 10:11:52,730 [INFO] Using charset --> digits
2020-01-03 10:11:52,730 [INFO] Attack started at 1578042712.7302287
2020-01-03 10:12:52,293 [INFO] found password 1789 for file /export/home1/users/gmc/delevoye/Github/sisters-rarcrack/sistersrarcrack/test_package/testdata/notes.rar
2020-01-03 10:12:52,293 [INFO] Duration : 59 s
```

Afficher sur la sortie standard les combinaisons essayées:

```console
user@computer:$ rarcrack notes.rar -v SHOW_PSW -l 3
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

### Remarque sur la performance


Le cassage de mots de passe est **lent**. Ce n'est pas dû au fait que nous utilisons du python, mais au fait que **l'ouverture d'un fichier .rar et la vérification de la clé sont lents**. 


### Principes python du package crackrar


#### Vue d'ensemble


Le package est fait de telle sorte qu'on peut soit faire du brute force total (option 1), soit faire des attaques par dictionnaire (option 2), soit combiner différents types d'approches.

Pour combiner les attaques, nous utiliserons trois concepts: 

- Le **dictionnaire d'attaque**

- La **mutation**

- La **stratégie d'attaque**


#### L'objet "dictionnaire d'attaque" (attackDict)


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


#### L'objet "mutation"

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

**Intérêt**: *L'intérêt de créer ces modifications est que si le propriétaire du mot de passe a légèrement modifé un mot du dictionnaire mais en utilisant des tactiques courantes (exemple: Faire démarrer par une majuscule, utiliser alternativement des majuscules ou minuscules...) alors on pourra quand même trouver son mot de passe, sans ajouter beaucoup de temps de calcul, et de manière très modulaire.*

#### L'objet "Stratégie" (strategy)

L'objet stratégie va nous permettre de choisir des "stratégies" globales d'attaque pour restreindre l'attaque

Par exemple: 8 caractères avec au moins un chiffre, une majuscule et un caractère spécial

Pour résumer avec un exemple, on utilise la stratégie de la façon suivante

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

# On va crée un dictionnaire d'attaque ("attackDict"): les lettres de l'alphabet
# On crée l'objet attackDict à partir de l'itérateur
my_attack_dict = cr.attackDict(my_generator_letters)

# On va rajouter à notre itérateur la possibilité de faire les majuscules
my_attack_dict.add_mutation(from_small_to_large_letter)

# Et à partir de ce dictionnaire "muté" on crée une stratégie où on va tester toutes les possibilités de combinaisons
# Ici, on testera les possibilités de taille 5 (5 lettres majuscules ou minuscules)

my_strategy = cr.Strategy()
my_strategy.add_attack_dict(my_attack_dict,fold=5) 
# "fold" précise le nombre de fois qu'on ajoute l'attackDict
# "4" signifie donc ici qu'on utilisera 5 fois cet attackDict

# Puis ensuite on attaque un fichier RAR
my_strategy.launch_attack(rarfile,SHOW_STDOUT=True)

```

L'option "SHOW_STDOUT" de la méthode "launch_attack" permet d'afficher (ou non) les combinaisons essayées sur la sortie standard (l'écran)
