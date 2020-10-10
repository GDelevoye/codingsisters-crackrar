import os
from rarfile import RarFile, BadRarFile

""" Ce module contient des fonctions qui permettent de manipuler des fichiers
RAR de manière simplifiée """

# def essayer_mdp(chemin_vers_fichier_RAR,mdp,nom_fichier=None): # FOr debugging purpose
#     if mdp == "a#7H":
#         return True
#     else:
#         return False

def essayer_mdp(chemin_vers_fichier_RAR, mdp, nom_fichier=None):
    """ Permet de tester le mot de passe d'un fichier RAR
    Renvoit True si le mot de passe est bon, et renvoit False si on n'a pas
    pas réussi à ouvrir le fichier RARself.

    Si le nom du fichier (nom_fichier) n'est pas donné en détail, alors par
    défaut la fonction essaye d'ouvrir le premier fichier de la listeself.

    ATTENTION: Si la fonction renvoit False, cela peut également être dû
    à une mauvaise variable nom_fichier"""

    fichierRar = RarFile(os.path.realpath(chemin_vers_fichier_RAR))
    mdp=str(mdp)

    txt_list = {}
    to_return = True
    if not nom_fichier:
        fichier = sorted(fichierRar.namelist())[0]
    else:
        fichier = nom_fichier

    try:
        txt = fichierRar.open(fichier,mdp).read().decode().strip()
        #txt_list[fichier] = txt
    except BadRarFile:
        to_return = False

    return to_return
