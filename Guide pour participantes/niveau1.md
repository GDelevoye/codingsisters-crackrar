On entre dans le vif du sujet !

# Contenu Niveau 1

Dans le niveau 1 nous verrons:

[ Niveau 1 - Ligne de commande, boucles, lecture de fichier ]

  - Installer un programme/un package avec pip install - NIVEAU 1

  - Utiliser crackrar pour cracker un mot de passe en ligne de commande - NIVEAU1

  - Tester un mot de passe .rar en python - NIVEAU 1

  - Tester tous les nombres possibles - NIVEAU 1

  - Tester tous les mots de passe stockés dans un fichier (attaque par dictionnaire) - NIVEAU 1


Nous allons installer un programme: **crackrar** et son jumeau **brutegen**

> **brutegen** est un programme d'illustration permettant de générer des combinaisons de mot de passe. **crackrar** est un programme qui repose sur les mêmes principes, mais appliqués à l'ouverture de fichiers .rar cryptés

# Installer un programme/un package avec pip install

**python** est un **programme** qui permet de lire des fichiers (ou ce qui est tapé au clavier) pour ensuite **traduire** nos instructions en langage compréhensible par la machine puis **exécuter les actions demandées**. 

Il est possible d'y ajouter des **extensions** avec tout un tas de choses déjà codées (souvent en python, mais certaines extensions peuvent aussi être codées en C, en Java, etc). 

Ces extensions sont appelées des **modules** si ce sont des **scripts** sauvegardés sur l'ordinateur avec une extension *".py"* ou sinon des  **packges** si ils sont **installables**. 

Pour **installer un package** python on utilise un programme qui s'appelle **pip**, et qui est livré par défaut avec python.


> **pip** est un installateur d'extensions pour python


pip, comme de nombreux programmes, s'utilise en **ligne de commande**. C'est-à-dire que pour l'utiliser vous devez utiliser sous Linux **CTRL+ALT+T"**, et ensuite **taper son nom** et appuyer sur **entrée**


![alt text](https://raw.githubusercontent.com/GDelevoye/codingsisters-crackrar/master/images/Capture%20d%E2%80%99%C3%A9cran%20de%202020-01-10%2017-29-38.png)


Dans la plupart des cas, un programme en **ligne de commande** (= Utilisable par la console) affichera une erreur ou une aide si on le tape seul.

> La ligne ***pip <command> [options]***
>
> ...est ici celle qui nous intéresse le plus ici

Ce qui s'affiche ici à l'écran est une **aide**, un **manuel** pour utiliser le programme. COmme on sait que pip est un programme pour **installer** des packages (ce que nous voulons faire ici)

Certains programmes sont stockés en ligne sur le site [ http://www.PyPI.org ]. Lorsque c'est le cas on peut installer le programme juste en utilisant

```console
user@computer$:pip install NOM_DU_PACKAGE
```

C'est le cas par exemple du package **"numpy"**:

![alt text](https://raw.githubusercontent.com/GDelevoye/codingsisters-crackrar/master/images/Capture%20d%E2%80%99%C3%A9cran%20de%202020-01-10%2017-26-59.png)

> Ici, le package numpy est déjà installé chez moi

----------------


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
