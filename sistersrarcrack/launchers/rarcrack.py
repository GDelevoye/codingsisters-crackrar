import os
import sys
import argparse
import logging

import sistersrarcrack as src

def rarcrack():
    parser = argparse.ArgumentParser()

    parser.add_argument("rarFile",help="Path to the .rar file")
    parser.add_argument("--combination_length","-l",type=int,required=False,default=4,help="How many times must the attackDicts be combined (DEFAULT: 4)")
    parser.add_argument('--charsets',"-c",
                            nargs='+',
                            help='List of all types of characters among: lowercase, uppercase, digits, special_characters. DEFAULT: contains them all',
                            required=False,
                            choices=["lowercase","uppercase","digits","special_characters"],
                            default=["lowercase","uppercase","digits","special_characters"])

    parser.add_argument('--verbosity',"-v",
                            help='Verbosity among: DEBUG, INFO, WARNING, ERROR, CRITICAL, STDOUT_PSW".\
                                 If set to STDOUT_PASW, passwords tried are printed on stdout [highly deprectaded : Performances issues). DEFAULT: INFO',
                            required=False,
                            default="INFO",
                            choices=["DEBUG", "INFO", "WARNING", "ERROR, CRITICAL", "SHOW_PSW"])
    args = parser.parse_args()

    if args.verbosity == "SHOW_PSW":
        _SRC_SHOW_STDOUT = True
    else:
        _SRC_SHOW_STDOUT = False
        verboselevel = "logging."+str(args.verbosity)
        logging.basicConfig(stream=sys.stdout, level=eval(verboselevel),
                            format='%(asctime)s %(message)s')


    args.rarFile = os.path.realpath(args.rarFile)

    for elt in args.charsets:
        logging.info("[INFO] Using charset --> {}".format(elt))

    brute_strategy = src.Strategy()
    brute_strategy.add_attack_dict(src.bruteAttackDict(charsets=args.charsets),args.combination_length)
    brute_strategy.launch_attack(args.rarFile,SHOW_STDOUT=_SRC_SHOW_STDOUT)

if __name__ == "__main__":
    rarcrack()
