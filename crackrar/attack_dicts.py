import os
from string import ascii_lowercase
from string import printable
from datetime import timedelta, date

import itertools
import logging

class attackDict(object):
    def __init__(self,generator,*args_generator,**kwargs_generator):
        self.mutations_list = []
        self.generator = generator
        self.generator_kwargs = kwargs_generator
        self.generator_args = args_generator

    def add_mutation(self,function): # Drops the original
        self.mutations_list.append(function)

    def generate(self):
        for elt in self.generator(*self.generator_args,**self.generator_kwargs):
            if self.mutations_list:
                for mutation in self.mutations_list:
                    mutated_elt = mutation(elt)
                    yield mutated_elt
            else:
                yield elt


class bruteAttackDict(attackDict):
    def __init__(self,charsets):
        super().__init__(custom_brute,charsets=charsets)

class fileAttackDict(attackDict):
    def __init__(self,path_to_file):
        super().__init__(filedictionnary,path_to_file=path_to_file)


########### Now the common generators for brute-forcing

def custom_brute(charsets):
    if "lowercase" in charsets:
        logging.debug("[DEBUG] Using charset --> {}".format("lowercase"))
        for elt in lowercase():
            yield(elt)
    if "uppercase" in charsets:
        logging.debug("[DEBUG] Using charset --> {}".format("uppercase"))
        for elt in uppercase():
            yield(elt)
    if "digits" in charsets:
        logging.debug("[DEBUG] Using charset --> {}".format("digits"))
        for elt in digit():
            yield(elt)
    if "special_characters" in charsets:
        logging.debug("[DEBUG] Using charset --> {}".format("special_characters"))
        for elt in special_char():
            yield(elt)

def full_brute():
    for elt in lowercase():
        yield(elt)
    for elt in uppercase():
        yield(elt)
    for elt in digit():
        yield(elt)
    for elt in special_char():
        yield(elt)

def lowercase():
    for elt in ascii_lowercase:
        yield elt

def uppercase():
    for elt in ascii_lowercase:
        yield elt.upper()

# def special_char():
#     for elt in [x for x in printable if not x.isalnum()]:
#         yield elt

def special_char():
    for elt in "œŒ&é(-è_çà)=^$ù*,;:!\'\"\\~#{}[]|`^@ê²³¿×÷¡ ":
        yield elt

def historical_dates():
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    start_date = date(1, 1, 1)
    end_date = date.today()
    for single_date in daterange(start_date, end_date):
        year = int(single_date.strftime("%Y"))
        month = int(single_date.strftime("%m"))
        day = int(single_date.strftime("%d"))
        yield(str(day)+str(month)+str(year))

def years():
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    start_date = date(1, 1, 1)
    end_date = date.today()
    for single_date in daterange(start_date, end_date):
        year = int(single_date.strftime("%Y"))
        yield(str(day)+str(month)+str(year))

def birth_dates():
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    start_date = date(1, 1, 1900)
    end_date = date.today()
    for single_date in daterange(start_date, end_date):
        year = int("".join(single_date.strftime("%Y")[2:]))
        month = int(single_date.strftime("%m"))
        day = int(single_date.strftime("%d"))
        yield(str(year)) # 91
        yield(str(day)+str(month)) # 0702
        yield(str(day)+str(month)+str(year)) # 070291

def digit():
    for i in range(10):
        yield str(i)

def PIN_2():
    for elt in range(10):
        yield "0"+str(elt)

def PIN_4():
    default_PIN = "0000"
    for i in range(10000):
        yield str(i)
        if i < 1000: # To return 0000 0001 instead of 0, 1...
            yield default_PIN[:-len(str(i))]+str(i)

def digicode():
    list1 = [str(x) for x in [0,1,2,3,4,5,6,7,8,9,"#","*","A","B"]]
    permut_digicode = ["".join(x) for x in list(itertools.product(list1,repeat=4))]
    for elt in permut_digicode:
        yield elt

def filedictionnary(path_to_file):
    filin = open(os.path.realpath(path_to_file), "r")
    for line in filin:
        yield str(line.strip())
    filin.close()
