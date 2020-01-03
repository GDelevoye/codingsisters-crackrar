import time
import logging
import itertools
from crackrar.rar_ouverture import essayer_mdp

import sys

class Strategy(object):
    def __init__(self):
        self.size = 0
        self.attack_dicts = []
        self.found = None
        self.lists_possibles = [] # A list of lists
        # ... Every element i is the list of possibilities for attackDict i
        # self.tried = [] # For dev & debug purposes

    def add_attack_dict(self, newattackdict, fold=1):

        if fold < 1:
            raise RuntimeError("Number of fold cannot be lower than 1")
        for i in range(fold):
            self.attack_dicts.append(newattackdict)
            self.size+=1

    def _compute_attack_dicts(self):

        self.lists_possibles = []

        for attackdict in self.attack_dicts:
            logging.debug("[DEBUG] Computing attackdict {}".format(attackdict))
            list_possibles = []
            for elt in attackdict.generate():
                list_possibles.append(elt)
            self.lists_possibles.append(list_possibles.copy())

    def launch_attack(self,rarfile,SHOW_STDOUT=False):
        """ This fuction try every password in the generator and chronometers it"""
        start = time.time()
        logging.info("[INFO] Attack started at {}".format(start))

        logging.debug("[INFO] Computing and adding the attackdicts to combine them")

        self._compute_attack_dicts()

        logging.debug("[INFO] *** All attackdicts are added. The attack begins **")

        for elt in itertools.product(*[self.lists_possibles[x] for x in range(len(self.attack_dicts))],repeat=1):
            elt = "".join([str(x) for x in elt])

            if SHOW_STDOUT:
                sys.stdout.write(elt+'\n')
            # self.tried.append(elt) # Uncomment to debug

            if essayer_mdp(rarfile, mdp=elt, nom_fichier=None):

                logging.info("[INFO] found password {} for file {}".format(elt,rarfile))
                logging.info("[INFO] Duration : {}".format(time.time() - start))
                self.found = elt

                return elt

        logging.error("[ERROR] Couldn't find password for file {} with strategy {}. Try another strategy".format(rarfile,self))
        logging.info("[INFO] Duration : {} s".format(round(time.time() - start),2))

class bruteGenStrategy(Strategy):
    def __init__(self):
        super().__init__()
    def launch_attack(self): # Overridingthis
        """ This fuction try every password in the generator and chronometers it"""
        self._compute_attack_dicts()

        for elt in itertools.product(*[self.lists_possibles[x] for x in range(len(self.attack_dicts))],repeat=1):
            elt = "".join([str(x) for x in elt])
            sys.stdout.write(elt+'\n')
