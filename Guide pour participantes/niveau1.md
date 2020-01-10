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

**python** est un **programme** qui permet de lire des fichiers (ou ce qui est tapé au clavier) pour ensuite **traduire** nos instructions en langage compréhensible par la machine puis **exécuter les actions demandées**. Il est possible d'y ajouter des **extensions** avec tout un tas de choses déjà codées (souvent en python, mais certaines extensions peuvent aussi être codées en C, en Java, etc). Ces extensions sont appelées des **modules** si ce sont des **scripts** sauvegardés sur l'ordinateur avec une extension *".py"* ou sinon des  **packges** si ils sont **installables**. Le programme que nous allons utiliser ici s'appelle **pip**, et il est livré par défaut avec python.


> **pip** est un installateur d'extensions pour python


pip, comme de nombreux programmes, s'utilise en **ligne de commande**. C'est-à-dire que pour l'utiliser vous devez utiliser sous Linux **CTRL+ALT+T"**, et ensuite **taper son nom** et appuyer sur **entrée**


```bash
delevoye@gmcpc04:/export/home1/users/gmc/delevoye$ pip

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don t periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output
```


Dans la plupart des cas, un programme en **ligne de commande** (= Utilisable par la console) affichera une erreur ou une aide si on le tape seul.

> La ligne ***pip <command> [options]***
>
> ...est ici celle qui nous intéresse le plus ici

Ce qui s'affiche ici à l'écran est une **aide**, un **manuel** pour utiliser le programme. COmme on sait que pip est un programme pour **installer** des packages (ce que nous voulons faire ici)


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
