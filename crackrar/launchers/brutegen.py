import os
import sys
import argparse
import logging

import crackrar as cr

def brutegen():
    parser = argparse.ArgumentParser()
    parser.add_argument("--combination_length","-l",type=int,required=True,default=1,help="Length of brute-force. Default: 1")
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
    args = parser.parse_args()

    if "none" in args.charsets:
        args.charsets = []

    if args.combination_length <= 0:
        raise RuntimeError("Choose a combination_length > 0")
    if not args.dictionnary and len(args.charsets) < 1:
        raise RuntimeError("Brutegen cannot generate brute forcing with 0 characters and 0 dictionnaries. Please refer to brutegen --help for more informations.")

    logging.basicConfig(stream=sys.stdout, level="ERROR",
                            format='%(asctime)s %(message)s')

    brute_strategy = cr.brutegenStrategy()

    # Adding the dicts if they are specified
    if args.dictionnary:
        brute_strategy.add_attack_dict(cr.fileAttackDict(path_to_file=args.dictionnary),args.combination_length)
    else:
        brute_strategy.add_attack_dict(cr.bruteAttackDict(charsets=args.charsets),max(0,args.combination_length))

    brute_strategy.launch_attack()

if __name__ == "__main__":
    brutegen()
