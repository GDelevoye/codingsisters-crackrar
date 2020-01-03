import os
import sys
import argparse
import logging

import crackrar as cr

def brutegen():
    parser = argparse.ArgumentParser()

    parser.add_argument("--combination_length","-l",type=int,required=False,default=4,help="How many times must the attackDicts be combined (DEFAULT: 4)")
    parser.add_argument('--charsets',"-c",
                            nargs='+',
                            help='List of all types of characters among: lowercase, uppercase, digits, special_characters. DEFAULT: contains them all.\
                            If None is selected, charset is fully ignored.',
                            required=False,
                            choices=["none","lowercase","uppercase","digits","special_characters"],
                            default=["lowercase","uppercase","digits","special_characters"])
    parser.add_argument('--dictionnaries',"-d",
                            nargs='+',
                            help='List here the paths of files that contains words to use (one word per line). DEFAULT: [empty]',
                            required=False,,
                            default=None)

    args = parser.parse_args()

    if "none" in args.charsets:
        args.charsets = []

    if args.max_combination_length < 2:
        raise RuntimeError("Choose a max_combination_length >= 2")
    if not len(args.dictionnaries) > 0 and len(args.charsets) < 1:
        raise RuntimeError("No dictionnary and no charset specified. brutegen cannot generate anything without it. Please refer to brutegen --help for more informations.")


    brute_strategy = cr.brutegenStrategy()

    # Adding the dicts if they are specified
    if args.dictionnaries:
        for dictfile in args.dictionnaries:
            brute_strategy.add_attack_dict(cr.filedictionnary,path_to_file=dictfile)

    brute_strategy.add_attack_dict(cr.bruteAttackDict(charsets=args.charsets),args.combination_length)


    brute_strategy.launch_attack()

if __name__ == "__main__":
    brutegen()
