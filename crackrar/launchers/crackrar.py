import os
import sys
import argparse
import logging

import crackrar as cr

def crackrar():
    parser = argparse.ArgumentParser()

    parser.add_argument("rarFile",help="Path to the .rar file")

    parser.add_argument("--combination_length","-l",type=int,required=False,default=1,help="Length of brute-force. Default: 1")
    parser.add_argument('--charsets',"-c",
                            nargs='+',
                            help='Choose among: lowercase, uppercase, digits, special_characters. DEFAULT: all of these.',
                            required=False,
                            choices=["lowercase","uppercase","digits","special_characters"],
                            default=["lowercase","uppercase","digits","special_characters"])
    parser.add_argument('--dictionnary',"-d",
                            help='Paths of a file that contains words to use (one word per line). This would override the --charset argument. DEFAULT: [empty]',
                            required=False,
                            default=None)
    parser.add_argument('--verbosity',"-v",
                            help='Verbosity among: DEBUG, INFO, WARNING, ERROR, CRITICAL, STDOUT_PSW".\
                                 If set to STDOUT_PASW, passwords tried are printed on stdout [highly deprectaded : Performances issues). DEFAULT: INFO',
                            required=False,
                            default="INFO",
                            choices=["DEBUG", "INFO", "WARNING", "ERROR, CRITICAL", "SHOW_PSW"])

    #### Checking the arguments

    args = parser.parse_args()
    args.rarFile = os.path.realpath(args.rarFile)

    if args.combination_length <= 0:
        raise RuntimeError("Choose a combination_length > 0")
    if not args.dictionnary and len(args.charsets) < 1:
        raise RuntimeError("Brutegen cannot generate brute forcing with 0 characters and 0 dictionnaries. Please refer to brutegen --help for more informations.")

    if args.verbosity == "SHOW_PSW":
        _cr_SHOW_STDOUT = True
    else:
        _cr_SHOW_STDOUT = False
        verboselevel = "logging."+str(args.verbosity)
        logging.basicConfig(stream=sys.stdout, level=eval(verboselevel),
                            format='%(asctime)s %(message)s')


    ####

    brute_strategy = cr.Strategy()
    # Adding the dict if it is specified

    if args.dictionnary:
        brute_strategy.add_attack_dict(cr.fileAttackDict(path_to_file=args.dictionnary),args.combination_length)
    else:
        brute_strategy.add_attack_dict(cr.bruteAttackDict(charsets=args.charsets),max(0,args.combination_length))

    brute_strategy.launch_attack(args.rarFile,SHOW_STDOUT=_cr_SHOW_STDOUT)

if __name__ == "__main__":
    crackrar()
